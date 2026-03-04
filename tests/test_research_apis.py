"""
Tests for research API adapters.

All tests mock httpx.AsyncClient so no real HTTP calls are made.
"""

import asyncio
import json
from unittest.mock import AsyncMock, MagicMock, patch

import httpx
import pytest

from src.integrations.research_apis import (
    AggregatedResults,
    ArxivAPI,
    CodeResult,
    DatasetResult,
    GitHubSearchAPI,
    HuggingFaceAPI,
    ModelResult,
    OpenAlexAPI,
    PaperResult,
    RepoResult,
    ResearchAggregator,
    SemanticScholarAPI,
)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _mock_response(
    status_code: int = 200,
    json_data: dict | list | None = None,
    text: str = "",
    headers: dict | None = None,
) -> httpx.Response:
    """Build a fake httpx.Response."""
    resp = MagicMock(spec=httpx.Response)
    resp.status_code = status_code
    resp.headers = headers or {}
    if json_data is not None:
        resp.json.return_value = json_data
        resp.text = json.dumps(json_data)
    else:
        resp.text = text
        resp.json.side_effect = json.JSONDecodeError("no json", "", 0)
    if status_code >= 400:
        resp.raise_for_status.side_effect = httpx.HTTPStatusError(
            message=f"{status_code}", request=MagicMock(), response=resp
        )
    else:
        resp.raise_for_status.return_value = None
    return resp


def _run(coro):
    """Run a coroutine to completion."""
    return asyncio.get_event_loop().run_until_complete(coro)


# We patch the adapter's _get method directly for most tests, so we do not
# need to worry about the actual httpx.AsyncClient plumbing.


# ---------------------------------------------------------------------------
# Dataclass tests
# ---------------------------------------------------------------------------


class TestDataclasses:
    def test_paper_result_to_dict(self):
        p = PaperResult(
            title="Test Paper",
            abstract="Abstract",
            year=2024,
            authors=["Alice", "Bob"],
            citation_count=42,
            url="https://example.com",
            pdf_url="https://example.com/paper.pdf",
            source="semantic_scholar",
        )
        d = p.to_dict()
        assert d["title"] == "Test Paper"
        assert d["year"] == 2024
        assert d["authors"] == ["Alice", "Bob"]
        assert d["citation_count"] == 42

    def test_repo_result_to_dict(self):
        r = RepoResult(
            name="my-repo",
            full_name="user/my-repo",
            stars=100,
            url="https://github.com/user/my-repo",
            language="Python",
            topics=["llm", "safety"],
        )
        d = r.to_dict()
        assert d["full_name"] == "user/my-repo"
        assert d["stars"] == 100
        assert d["topics"] == ["llm", "safety"]

    def test_dataset_result_defaults(self):
        ds = DatasetResult(id="my-dataset")
        assert ds.description == ""
        assert ds.downloads == 0
        assert ds.tags == []

    def test_model_result_defaults(self):
        m = ModelResult(id="my-model")
        assert m.pipeline_tag == ""
        assert m.downloads == 0

    def test_aggregated_results_to_dict(self):
        agg = AggregatedResults(
            papers=[PaperResult(title="P1", source="arxiv")],
            repos=[RepoResult(name="R1", full_name="u/R1")],
            datasets=[DatasetResult(id="D1")],
            models=[ModelResult(id="M1")],
            errors={"openalex": "timeout"},
        )
        d = agg.to_dict()
        assert len(d["papers"]) == 1
        assert d["papers"][0]["title"] == "P1"
        assert len(d["repos"]) == 1
        assert d["errors"]["openalex"] == "timeout"

    def test_code_result_to_dict(self):
        c = CodeResult(path="src/main.py", repo_name="user/repo", url="https://github.com")
        d = c.to_dict()
        assert d["path"] == "src/main.py"
        assert d["repo_name"] == "user/repo"


# ---------------------------------------------------------------------------
# Semantic Scholar
# ---------------------------------------------------------------------------


class TestSemanticScholar:
    def test_search_parses_results(self):
        api = SemanticScholarAPI()
        mock_data = {
            "data": [
                {
                    "title": "LLM Safety Benchmark",
                    "abstract": "We propose...",
                    "year": 2024,
                    "authors": [{"name": "Alice"}, {"name": "Bob"}],
                    "citationCount": 15,
                    "url": "https://semantic.com/paper1",
                    "openAccessPdf": {"url": "https://pdf.com/1.pdf"},
                }
            ]
        }
        api._get = AsyncMock(return_value=_mock_response(json_data=mock_data))
        results = _run(api.search("llm safety"))
        assert len(results) == 1
        assert results[0].title == "LLM Safety Benchmark"
        assert results[0].authors == ["Alice", "Bob"]
        assert results[0].citation_count == 15
        assert results[0].pdf_url == "https://pdf.com/1.pdf"
        assert results[0].source == "semantic_scholar"

    def test_search_returns_empty_on_error(self):
        api = SemanticScholarAPI()
        api._get = AsyncMock(return_value=_mock_response(status_code=500))
        results = _run(api.search("bad query"))
        assert results == []

    def test_get_paper(self):
        api = SemanticScholarAPI()
        mock_data = {
            "title": "Single Paper",
            "abstract": "Details",
            "year": 2023,
            "authors": [{"name": "Eve"}],
            "citationCount": 7,
        }
        api._get = AsyncMock(return_value=_mock_response(json_data=mock_data))
        paper = _run(api.get_paper("abc123"))
        assert paper is not None
        assert paper.title == "Single Paper"
        assert paper.year == 2023

    def test_get_paper_returns_none_on_error(self):
        api = SemanticScholarAPI()
        api._get = AsyncMock(return_value=_mock_response(status_code=404))
        paper = _run(api.get_paper("nonexistent"))
        assert paper is None

    def test_get_citations(self):
        api = SemanticScholarAPI()
        mock_data = {
            "data": [
                {"citingPaper": {"title": "Citing Paper 1", "year": 2025, "authors": []}},
                {"citingPaper": {"title": "Citing Paper 2", "year": 2024, "authors": []}},
            ]
        }
        api._get = AsyncMock(return_value=_mock_response(json_data=mock_data))
        citations = _run(api.get_citations("paper1"))
        assert len(citations) == 2
        assert citations[0].title == "Citing Paper 1"


# ---------------------------------------------------------------------------
# arXiv
# ---------------------------------------------------------------------------


_ARXIV_XML = """<?xml version="1.0" encoding="UTF-8"?>
<feed xmlns="http://www.w3.org/2005/Atom">
  <entry>
    <title>Red Teaming LLMs</title>
    <summary>We study adversarial attacks...</summary>
    <published>2024-01-15T00:00:00Z</published>
    <author><name>Carol</name></author>
    <author><name>Dave</name></author>
    <link rel="alternate" href="http://arxiv.org/abs/2401.00001"/>
    <link title="pdf" type="application/pdf" href="http://arxiv.org/pdf/2401.00001"/>
  </entry>
  <entry>
    <title>Prompt Injection Survey</title>
    <summary>A survey of prompt injection...</summary>
    <published>2023-06-10T00:00:00Z</published>
    <author><name>Eve</name></author>
    <link rel="alternate" href="http://arxiv.org/abs/2306.00002"/>
  </entry>
</feed>"""


class TestArxiv:
    def test_search_parses_xml(self):
        api = ArxivAPI()
        api._get = AsyncMock(return_value=_mock_response(text=_ARXIV_XML))
        results = _run(api.search("red teaming"))
        assert len(results) == 2
        assert results[0].title == "Red Teaming LLMs"
        assert results[0].year == 2024
        assert results[0].authors == ["Carol", "Dave"]
        assert results[0].pdf_url == "http://arxiv.org/pdf/2401.00001"
        assert results[0].source == "arxiv"
        assert results[1].title == "Prompt Injection Survey"
        assert results[1].year == 2023

    def test_search_with_categories(self):
        api = ArxivAPI()
        api._get = AsyncMock(return_value=_mock_response(text=_ARXIV_XML))
        results = _run(api.search("safety", categories=["cs.CL", "cs.AI"]))
        assert len(results) == 2
        # Verify the call was made (categories are embedded in query param)
        api._get.assert_called_once()

    def test_search_returns_empty_on_error(self):
        api = ArxivAPI()
        api._get = AsyncMock(side_effect=httpx.ConnectError("connection refused"))
        results = _run(api.search("fail"))
        assert results == []

    def test_get_paper(self):
        api = ArxivAPI()
        api._get = AsyncMock(return_value=_mock_response(text=_ARXIV_XML))
        paper = _run(api.get_paper("2401.00001"))
        assert paper is not None
        assert paper.title == "Red Teaming LLMs"

    def test_parse_malformed_xml_returns_empty(self):
        api = ArxivAPI()
        api._get = AsyncMock(return_value=_mock_response(text="not xml at all"))
        results = _run(api.search("broken"))
        assert results == []


# ---------------------------------------------------------------------------
# GitHub Search
# ---------------------------------------------------------------------------


class TestGitHubSearch:
    def test_search_repos(self):
        api = GitHubSearchAPI()
        mock_data = {
            "items": [
                {
                    "name": "llm-guard",
                    "full_name": "org/llm-guard",
                    "description": "LLM safety toolkit",
                    "stargazers_count": 500,
                    "html_url": "https://github.com/org/llm-guard",
                    "language": "Python",
                    "topics": ["llm", "safety"],
                    "updated_at": "2024-06-01T00:00:00Z",
                }
            ]
        }
        api._get = AsyncMock(return_value=_mock_response(json_data=mock_data))
        repos = _run(api.search_repos("llm safety"))
        assert len(repos) == 1
        assert repos[0].name == "llm-guard"
        assert repos[0].stars == 500
        assert repos[0].topics == ["llm", "safety"]

    def test_search_repos_empty_on_error(self):
        api = GitHubSearchAPI()
        api._get = AsyncMock(return_value=_mock_response(status_code=403))
        repos = _run(api.search_repos("forbidden"))
        assert repos == []

    def test_search_code(self):
        api = GitHubSearchAPI()
        mock_data = {
            "items": [
                {
                    "path": "src/safety.py",
                    "html_url": "https://github.com/org/repo/blob/main/src/safety.py",
                    "repository": {"full_name": "org/repo"},
                    "text_matches": [{"fragment": "def check_safety():"}],
                }
            ]
        }
        api._get = AsyncMock(return_value=_mock_response(json_data=mock_data))
        code = _run(api.search_code("check_safety", language="python"))
        assert len(code) == 1
        assert code[0].path == "src/safety.py"
        assert code[0].repo_name == "org/repo"
        assert "check_safety" in code[0].matched_content

    def test_search_code_no_text_matches(self):
        api = GitHubSearchAPI()
        mock_data = {
            "items": [
                {
                    "path": "main.py",
                    "html_url": "https://github.com/x/y",
                    "repository": {"full_name": "x/y"},
                }
            ]
        }
        api._get = AsyncMock(return_value=_mock_response(json_data=mock_data))
        code = _run(api.search_code("query"))
        assert len(code) == 1
        assert code[0].matched_content == ""


# ---------------------------------------------------------------------------
# HuggingFace
# ---------------------------------------------------------------------------


class TestHuggingFace:
    def test_search_datasets(self):
        api = HuggingFaceAPI()
        mock_data = [
            {
                "id": "safety-bench/toxicity",
                "description": "Toxicity benchmark",
                "downloads": 1200,
                "tags": ["safety", "toxicity"],
            }
        ]
        api._get = AsyncMock(return_value=_mock_response(json_data=mock_data))
        datasets = _run(api.search_datasets("toxicity"))
        assert len(datasets) == 1
        assert datasets[0].id == "safety-bench/toxicity"
        assert datasets[0].downloads == 1200
        assert datasets[0].url == "https://huggingface.co/datasets/safety-bench/toxicity"

    def test_search_datasets_empty_on_error(self):
        api = HuggingFaceAPI()
        api._get = AsyncMock(return_value=_mock_response(status_code=500))
        datasets = _run(api.search_datasets("error"))
        assert datasets == []

    def test_search_models(self):
        api = HuggingFaceAPI()
        mock_data = [
            {
                "id": "safety-model/guard",
                "modelId": "safety-model/guard",
                "pipeline_tag": "text-classification",
                "downloads": 5000,
                "tags": ["safety", "guard"],
            }
        ]
        api._get = AsyncMock(return_value=_mock_response(json_data=mock_data))
        models = _run(api.search_models("safety guard", task="text-classification"))
        assert len(models) == 1
        assert models[0].id == "safety-model/guard"
        assert models[0].pipeline_tag == "text-classification"
        assert models[0].downloads == 5000

    def test_search_models_empty_on_error(self):
        api = HuggingFaceAPI()
        api._get = AsyncMock(return_value=_mock_response(status_code=503))
        models = _run(api.search_models("error"))
        assert models == []


# ---------------------------------------------------------------------------
# OpenAlex
# ---------------------------------------------------------------------------


class TestOpenAlex:
    def test_search_parses_results(self):
        api = OpenAlexAPI()
        mock_data = {
            "results": [
                {
                    "title": "AI Safety Research",
                    "abstract": "We study...",
                    "publication_year": 2025,
                    "authorships": [
                        {"author": {"display_name": "Frank"}},
                        {"author": {"display_name": "Grace"}},
                    ],
                    "cited_by_count": 22,
                    "doi": "https://doi.org/10.1234/test",
                    "best_oa_location": {"pdf_url": "https://oa.com/paper.pdf"},
                }
            ]
        }
        api._get = AsyncMock(return_value=_mock_response(json_data=mock_data))
        results = _run(api.search("AI safety"))
        assert len(results) == 1
        assert results[0].title == "AI Safety Research"
        assert results[0].authors == ["Frank", "Grace"]
        assert results[0].citation_count == 22
        assert results[0].pdf_url == "https://oa.com/paper.pdf"
        assert results[0].source == "openalex"

    def test_search_empty_on_error(self):
        api = OpenAlexAPI()
        api._get = AsyncMock(side_effect=httpx.TimeoutException("timeout"))
        results = _run(api.search("timeout"))
        assert results == []

    def test_search_missing_oa_location(self):
        api = OpenAlexAPI()
        mock_data = {
            "results": [
                {
                    "title": "No PDF",
                    "publication_year": 2020,
                    "authorships": [],
                    "cited_by_count": 0,
                    "id": "https://openalex.org/W123",
                }
            ]
        }
        api._get = AsyncMock(return_value=_mock_response(json_data=mock_data))
        results = _run(api.search("minimal"))
        assert len(results) == 1
        assert results[0].pdf_url == ""
        assert results[0].url == "https://openalex.org/W123"


# ---------------------------------------------------------------------------
# Rate-limit retry
# ---------------------------------------------------------------------------


class TestRateLimitRetry:
    def test_429_retries_then_succeeds(self):
        """Adapter should retry on 429 and return the successful response.

        We mock the underlying httpx.AsyncClient.get so the base-class
        retry loop in ``_get`` actually executes.
        """
        api = SemanticScholarAPI()

        good_data = {"data": [{"title": "After Retry", "authors": [], "citationCount": 0}]}
        resp_429 = _mock_response(status_code=429, headers={"Retry-After": "0"})
        # 429 must NOT raise on raise_for_status — the base _get checks
        # status_code directly and retries; raise_for_status is only
        # called by the adapter's search() on the *returned* response.
        resp_429.raise_for_status = MagicMock()  # no-op
        resp_ok = _mock_response(json_data=good_data)

        mock_client = AsyncMock(spec=httpx.AsyncClient)
        mock_client.is_closed = False
        mock_client.get = AsyncMock(side_effect=[resp_429, resp_ok])

        # Inject the mock client directly
        api._client = mock_client
        results = _run(api.search("retry test"))
        assert len(results) == 1
        assert results[0].title == "After Retry"
        assert mock_client.get.call_count == 2


# ---------------------------------------------------------------------------
# Aggregator
# ---------------------------------------------------------------------------


class TestAggregator:
    def test_search_all_combines_results(self):
        agg = ResearchAggregator()

        # Mock each sub-adapter
        agg.semantic_scholar.search = AsyncMock(
            return_value=[PaperResult(title="SS Paper", source="semantic_scholar")]
        )
        agg.arxiv.search = AsyncMock(
            return_value=[PaperResult(title="Arxiv Paper", source="arxiv")]
        )
        agg.openalex.search = AsyncMock(
            return_value=[PaperResult(title="OA Paper", source="openalex")]
        )
        agg.github.search_repos = AsyncMock(
            return_value=[RepoResult(name="repo1", full_name="u/repo1")]
        )
        agg.huggingface.search_datasets = AsyncMock(
            return_value=[DatasetResult(id="ds1")]
        )
        agg.huggingface.search_models = AsyncMock(
            return_value=[ModelResult(id="m1")]
        )

        result = _run(agg.search_all("test"))
        assert len(result.papers) == 3
        assert len(result.repos) == 1
        assert len(result.datasets) == 1
        assert len(result.models) == 1
        assert result.errors == {}

    def test_search_all_handles_partial_failure(self):
        agg = ResearchAggregator()

        agg.semantic_scholar.search = AsyncMock(
            return_value=[PaperResult(title="OK", source="semantic_scholar")]
        )
        agg.arxiv.search = AsyncMock(side_effect=Exception("arxiv down"))
        agg.openalex.search = AsyncMock(return_value=[])
        agg.github.search_repos = AsyncMock(return_value=[])
        agg.huggingface.search_datasets = AsyncMock(return_value=[])
        agg.huggingface.search_models = AsyncMock(return_value=[])

        result = _run(agg.search_all("test"))
        assert len(result.papers) == 1
        assert "arxiv" in result.errors
        assert "arxiv down" in result.errors["arxiv"]

    def test_search_safety_papers(self):
        agg = ResearchAggregator()
        agg.semantic_scholar.search = AsyncMock(
            return_value=[PaperResult(title="Safety 1", source="semantic_scholar")]
        )
        agg.arxiv.search = AsyncMock(
            return_value=[PaperResult(title="Safety 2", source="arxiv")]
        )
        agg.openalex.search = AsyncMock(
            return_value=[PaperResult(title="Safety 3", source="openalex")]
        )

        papers = _run(agg.search_safety_papers("jailbreak"))
        assert len(papers) == 3
        titles = {p.title for p in papers}
        assert "Safety 1" in titles
        assert "Safety 2" in titles

    def test_search_safety_repos_deduplicates(self):
        agg = ResearchAggregator()
        repo = RepoResult(name="llm-guard", full_name="org/llm-guard")
        # Each query returns the same repo
        agg.github.search_repos = AsyncMock(return_value=[repo])

        repos = _run(agg.search_safety_repos())
        # Should be deduplicated to 1
        assert len(repos) == 1
        assert repos[0].full_name == "org/llm-guard"

    def test_search_safety_datasets_deduplicates(self):
        agg = ResearchAggregator()
        ds = DatasetResult(id="safety/toxicity")
        agg.huggingface.search_datasets = AsyncMock(return_value=[ds])

        datasets = _run(agg.search_safety_datasets())
        assert len(datasets) == 1
        assert datasets[0].id == "safety/toxicity"
