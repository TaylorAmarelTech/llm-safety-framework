"""
Research API adapters for discovering academic papers, repos, and datasets.

Provides unified async access to five free research APIs that require
no API keys (though optional tokens can raise rate limits):

- Semantic Scholar  — academic paper search and citation graphs
- arXiv             — preprint search (Atom XML)
- GitHub Search     — repository and code search
- HuggingFace Hub   — dataset and model search
- OpenAlex          — open scholarly metadata

All adapters share a common base class with httpx async client,
automatic retry on 429 (rate-limit), and result normalization.
The ``ResearchAggregator`` runs all five in parallel and returns
a single ``AggregatedResults`` object.
"""

from __future__ import annotations

import asyncio
import logging
import os
import xml.etree.ElementTree as ET
from dataclasses import dataclass, field, asdict
from typing import Any, List, Optional

import httpx

logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Result dataclasses
# ---------------------------------------------------------------------------


@dataclass
class PaperResult:
    """A paper from Semantic Scholar, arXiv, or OpenAlex."""

    title: str
    abstract: str = ""
    year: int | None = None
    authors: list[str] = field(default_factory=list)
    citation_count: int = 0
    url: str = ""
    pdf_url: str = ""
    source: str = ""  # "semantic_scholar", "arxiv", "openalex"

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass
class RepoResult:
    """A GitHub repository."""

    name: str
    full_name: str
    description: str = ""
    stars: int = 0
    url: str = ""
    language: str = ""
    topics: list[str] = field(default_factory=list)
    updated_at: str = ""

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass
class CodeResult:
    """A GitHub code search hit."""

    path: str
    repo_name: str
    url: str = ""
    matched_content: str = ""

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass
class DatasetResult:
    """A HuggingFace dataset."""

    id: str
    description: str = ""
    downloads: int = 0
    tags: list[str] = field(default_factory=list)
    url: str = ""

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass
class ModelResult:
    """A HuggingFace model."""

    id: str
    pipeline_tag: str = ""
    downloads: int = 0
    tags: list[str] = field(default_factory=list)
    url: str = ""

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass
class AggregatedResults:
    """Combined results from all research APIs."""

    papers: list[PaperResult] = field(default_factory=list)
    repos: list[RepoResult] = field(default_factory=list)
    datasets: list[DatasetResult] = field(default_factory=list)
    models: list[ModelResult] = field(default_factory=list)
    errors: dict[str, str] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return {
            "papers": [p.to_dict() for p in self.papers],
            "repos": [r.to_dict() for r in self.repos],
            "datasets": [d.to_dict() for d in self.datasets],
            "models": [m.to_dict() for m in self.models],
            "errors": self.errors,
        }


# ---------------------------------------------------------------------------
# Base adapter
# ---------------------------------------------------------------------------

_DEFAULT_TIMEOUT = 30.0
_MAX_RETRIES = 3
_RETRY_BACKOFF = 1.0  # seconds; doubles each retry


class ResearchAPIAdapter:
    """Base class with shared httpx client, rate-limit retry, and logging."""

    base_url: str = ""

    def __init__(self, timeout: float = _DEFAULT_TIMEOUT) -> None:
        self._timeout = timeout
        self._client: httpx.AsyncClient | None = None

    async def _get_client(self) -> httpx.AsyncClient:
        if self._client is None or self._client.is_closed:
            self._client = httpx.AsyncClient(
                timeout=self._timeout,
                follow_redirects=True,
            )
        return self._client

    async def close(self) -> None:
        if self._client is not None and not self._client.is_closed:
            await self._client.aclose()
            self._client = None

    async def _get(
        self,
        url: str,
        params: dict[str, Any] | None = None,
        headers: dict[str, str] | None = None,
    ) -> httpx.Response:
        """Issue GET with automatic retry on 429."""
        client = await self._get_client()
        delay = _RETRY_BACKOFF
        last_exc: Exception | None = None
        for attempt in range(_MAX_RETRIES):
            try:
                resp = await client.get(url, params=params, headers=headers)
                if resp.status_code == 429:
                    retry_after = resp.headers.get("Retry-After")
                    wait = float(retry_after) if retry_after else delay
                    logger.warning(
                        "%s rate-limited (429). Retrying in %.1fs (attempt %d/%d)",
                        self.__class__.__name__,
                        wait,
                        attempt + 1,
                        _MAX_RETRIES,
                    )
                    await asyncio.sleep(wait)
                    delay *= 2
                    continue
                return resp
            except (httpx.HTTPError, OSError) as exc:
                last_exc = exc
                logger.warning(
                    "%s request failed: %s (attempt %d/%d)",
                    self.__class__.__name__,
                    exc,
                    attempt + 1,
                    _MAX_RETRIES,
                )
                await asyncio.sleep(delay)
                delay *= 2
        # All retries exhausted — raise the last exception so callers
        # can catch it and return empty results.
        raise last_exc or httpx.HTTPError("request failed after retries")


# ---------------------------------------------------------------------------
# Semantic Scholar
# ---------------------------------------------------------------------------


class SemanticScholarAPI(ResearchAPIAdapter):
    """Search academic papers via the Semantic Scholar Graph API."""

    base_url = "https://api.semanticscholar.org/graph/v1"

    async def search(self, query: str, limit: int = 10) -> list[PaperResult]:
        """Search papers by keyword query."""
        try:
            resp = await self._get(
                f"{self.base_url}/paper/search",
                params={
                    "query": query,
                    "limit": limit,
                    "fields": "title,abstract,year,authors,citationCount,url,openAccessPdf",
                },
            )
            resp.raise_for_status()
            data = resp.json()
            return [self._parse_paper(p) for p in data.get("data", [])]
        except Exception as exc:
            logger.warning("SemanticScholar search failed: %s", exc)
            return []

    async def get_paper(self, paper_id: str) -> PaperResult | None:
        """Fetch a single paper by its Semantic Scholar ID or DOI."""
        try:
            resp = await self._get(
                f"{self.base_url}/paper/{paper_id}",
                params={
                    "fields": "title,abstract,year,authors,citationCount,references,citations",
                },
            )
            resp.raise_for_status()
            return self._parse_paper(resp.json())
        except Exception as exc:
            logger.warning("SemanticScholar get_paper failed: %s", exc)
            return None

    async def get_citations(
        self, paper_id: str, limit: int = 50
    ) -> list[PaperResult]:
        """Fetch papers that cite the given paper."""
        try:
            resp = await self._get(
                f"{self.base_url}/paper/{paper_id}/citations",
                params={"fields": "title,year,authors", "limit": limit},
            )
            resp.raise_for_status()
            data = resp.json()
            return [
                self._parse_paper(c.get("citingPaper", {}))
                for c in data.get("data", [])
                if c.get("citingPaper")
            ]
        except Exception as exc:
            logger.warning("SemanticScholar get_citations failed: %s", exc)
            return []

    @staticmethod
    def _parse_paper(raw: dict[str, Any]) -> PaperResult:
        authors_raw = raw.get("authors") or []
        authors = [a.get("name", "") for a in authors_raw if isinstance(a, dict)]
        pdf_info = raw.get("openAccessPdf") or {}
        return PaperResult(
            title=raw.get("title", ""),
            abstract=raw.get("abstract") or "",
            year=raw.get("year"),
            authors=authors,
            citation_count=raw.get("citationCount") or 0,
            url=raw.get("url") or "",
            pdf_url=pdf_info.get("url", "") if isinstance(pdf_info, dict) else "",
            source="semantic_scholar",
        )


# ---------------------------------------------------------------------------
# arXiv
# ---------------------------------------------------------------------------

_ARXIV_NS = {"atom": "http://www.w3.org/2005/Atom"}


class ArxivAPI(ResearchAPIAdapter):
    """Search preprints on arXiv (Atom XML API)."""

    base_url = "http://export.arxiv.org/api/query"

    async def search(
        self,
        query: str,
        limit: int = 10,
        categories: list[str] | None = None,
    ) -> list[PaperResult]:
        """Search arXiv papers.

        Args:
            query: Free-text search query.
            limit: Max results to return.
            categories: Optional arXiv category filter (e.g. ["cs.CL", "cs.AI"]).
        """
        search_query = f"all:{query}"
        if categories:
            cat_filter = "+OR+".join(f"cat:{c}" for c in categories)
            search_query = f"({search_query})+AND+({cat_filter})"
        try:
            resp = await self._get(
                self.base_url,
                params={
                    "search_query": search_query,
                    "max_results": str(limit),
                    "sortBy": "relevance",
                    "sortOrder": "descending",
                },
            )
            resp.raise_for_status()
            return self._parse_atom(resp.text)
        except Exception as exc:
            logger.warning("arXiv search failed: %s", exc)
            return []

    async def get_paper(self, arxiv_id: str) -> PaperResult | None:
        """Fetch a single arXiv paper by its ID (e.g. '2301.00001')."""
        try:
            resp = await self._get(
                self.base_url,
                params={"id_list": arxiv_id},
            )
            resp.raise_for_status()
            papers = self._parse_atom(resp.text)
            return papers[0] if papers else None
        except Exception as exc:
            logger.warning("arXiv get_paper failed: %s", exc)
            return None

    @staticmethod
    def _parse_atom(xml_text: str) -> list[PaperResult]:
        """Parse arXiv Atom XML into PaperResult list."""
        results: list[PaperResult] = []
        try:
            root = ET.fromstring(xml_text)
        except ET.ParseError:
            logger.warning("Failed to parse arXiv XML")
            return results

        for entry in root.findall("atom:entry", _ARXIV_NS):
            title_el = entry.find("atom:title", _ARXIV_NS)
            summary_el = entry.find("atom:summary", _ARXIV_NS)
            published_el = entry.find("atom:published", _ARXIV_NS)

            title = (title_el.text or "").strip() if title_el is not None else ""
            abstract = (summary_el.text or "").strip() if summary_el is not None else ""

            year: int | None = None
            if published_el is not None and published_el.text:
                try:
                    year = int(published_el.text[:4])
                except (ValueError, IndexError):
                    pass

            authors: list[str] = []
            for author_el in entry.findall("atom:author", _ARXIV_NS):
                name_el = author_el.find("atom:name", _ARXIV_NS)
                if name_el is not None and name_el.text:
                    authors.append(name_el.text.strip())

            url = ""
            pdf_url = ""
            for link_el in entry.findall("atom:link", _ARXIV_NS):
                rel = link_el.get("rel", "")
                link_type = link_el.get("type", "")
                href = link_el.get("href", "")
                if rel == "alternate":
                    url = href
                elif link_type == "application/pdf" or link_el.get("title") == "pdf":
                    pdf_url = href

            results.append(
                PaperResult(
                    title=title,
                    abstract=abstract,
                    year=year,
                    authors=authors,
                    citation_count=0,
                    url=url,
                    pdf_url=pdf_url,
                    source="arxiv",
                )
            )
        return results


# ---------------------------------------------------------------------------
# GitHub Search
# ---------------------------------------------------------------------------


class GitHubSearchAPI(ResearchAPIAdapter):
    """Search GitHub repositories and code."""

    base_url = "https://api.github.com/search"

    def __init__(self, timeout: float = _DEFAULT_TIMEOUT) -> None:
        super().__init__(timeout)
        self._token: str | None = os.environ.get("GITHUB_TOKEN")

    def _auth_headers(self) -> dict[str, str]:
        headers: dict[str, str] = {"Accept": "application/vnd.github+json"}
        if self._token:
            headers["Authorization"] = f"Bearer {self._token}"
        return headers

    async def search_repos(
        self, query: str, limit: int = 10, sort: str = "stars"
    ) -> list[RepoResult]:
        """Search GitHub repositories."""
        try:
            resp = await self._get(
                f"{self.base_url}/repositories",
                params={"q": query, "sort": sort, "per_page": limit},
                headers=self._auth_headers(),
            )
            resp.raise_for_status()
            data = resp.json()
            return [self._parse_repo(item) for item in data.get("items", [])]
        except Exception as exc:
            logger.warning("GitHub search_repos failed: %s", exc)
            return []

    async def search_code(
        self,
        query: str,
        limit: int = 10,
        language: str | None = None,
    ) -> list[CodeResult]:
        """Search code on GitHub (requires auth for higher rate limits)."""
        q = query
        if language:
            q = f"{q} language:{language}"
        try:
            resp = await self._get(
                f"{self.base_url}/code",
                params={"q": q, "per_page": limit},
                headers=self._auth_headers(),
            )
            resp.raise_for_status()
            data = resp.json()
            return [self._parse_code(item) for item in data.get("items", [])]
        except Exception as exc:
            logger.warning("GitHub search_code failed: %s", exc)
            return []

    @staticmethod
    def _parse_repo(raw: dict[str, Any]) -> RepoResult:
        return RepoResult(
            name=raw.get("name", ""),
            full_name=raw.get("full_name", ""),
            description=raw.get("description") or "",
            stars=raw.get("stargazers_count", 0),
            url=raw.get("html_url") or "",
            language=raw.get("language") or "",
            topics=raw.get("topics") or [],
            updated_at=raw.get("updated_at") or "",
        )

    @staticmethod
    def _parse_code(raw: dict[str, Any]) -> CodeResult:
        repo = raw.get("repository") or {}
        return CodeResult(
            path=raw.get("path", ""),
            repo_name=repo.get("full_name", ""),
            url=raw.get("html_url") or "",
            matched_content=raw.get("text_matches", [{}])[0].get("fragment", "")
            if raw.get("text_matches")
            else "",
        )


# ---------------------------------------------------------------------------
# HuggingFace Hub
# ---------------------------------------------------------------------------


class HuggingFaceAPI(ResearchAPIAdapter):
    """Search datasets and models on the HuggingFace Hub."""

    base_url = "https://huggingface.co/api"

    async def search_datasets(
        self, query: str, limit: int = 10
    ) -> list[DatasetResult]:
        """Search HuggingFace datasets."""
        try:
            resp = await self._get(
                f"{self.base_url}/datasets",
                params={"search": query, "limit": limit, "sort": "downloads"},
            )
            resp.raise_for_status()
            data = resp.json()
            return [self._parse_dataset(item) for item in data]
        except Exception as exc:
            logger.warning("HuggingFace search_datasets failed: %s", exc)
            return []

    async def search_models(
        self,
        query: str,
        limit: int = 10,
        task: str | None = None,
    ) -> list[ModelResult]:
        """Search HuggingFace models."""
        params: dict[str, Any] = {
            "search": query,
            "limit": limit,
            "sort": "downloads",
        }
        if task:
            params["pipeline_tag"] = task
        try:
            resp = await self._get(
                f"{self.base_url}/models",
                params=params,
            )
            resp.raise_for_status()
            data = resp.json()
            return [self._parse_model(item) for item in data]
        except Exception as exc:
            logger.warning("HuggingFace search_models failed: %s", exc)
            return []

    @staticmethod
    def _parse_dataset(raw: dict[str, Any]) -> DatasetResult:
        ds_id = raw.get("id", "")
        return DatasetResult(
            id=ds_id,
            description=raw.get("description") or raw.get("cardData", {}).get("description", "") if isinstance(raw.get("cardData"), dict) else raw.get("description") or "",
            downloads=raw.get("downloads", 0),
            tags=raw.get("tags") or [],
            url=f"https://huggingface.co/datasets/{ds_id}" if ds_id else "",
        )

    @staticmethod
    def _parse_model(raw: dict[str, Any]) -> ModelResult:
        model_id = raw.get("id", "") or raw.get("modelId", "")
        return ModelResult(
            id=model_id,
            pipeline_tag=raw.get("pipeline_tag") or "",
            downloads=raw.get("downloads", 0),
            tags=raw.get("tags") or [],
            url=f"https://huggingface.co/models/{model_id}" if model_id else "",
        )


# ---------------------------------------------------------------------------
# OpenAlex
# ---------------------------------------------------------------------------


class OpenAlexAPI(ResearchAPIAdapter):
    """Search scholarly metadata via OpenAlex."""

    base_url = "https://api.openalex.org"

    async def search(self, query: str, limit: int = 10) -> list[PaperResult]:
        """Search works in OpenAlex."""
        try:
            resp = await self._get(
                f"{self.base_url}/works",
                params={
                    "search": query,
                    "per_page": limit,
                },
                headers={"User-Agent": "LLMSafetyFramework/1.0 (research)"},
            )
            resp.raise_for_status()
            data = resp.json()
            return [self._parse_work(w) for w in data.get("results", [])]
        except Exception as exc:
            logger.warning("OpenAlex search failed: %s", exc)
            return []

    @staticmethod
    def _parse_work(raw: dict[str, Any]) -> PaperResult:
        authorships = raw.get("authorships") or []
        authors: list[str] = []
        for a in authorships:
            author_info = a.get("author") or {}
            name = author_info.get("display_name", "")
            if name:
                authors.append(name)

        # Best open-access PDF
        pdf_url = ""
        best_oa = raw.get("best_oa_location") or {}
        if isinstance(best_oa, dict):
            pdf_url = best_oa.get("pdf_url") or ""

        return PaperResult(
            title=raw.get("title") or "",
            abstract=raw.get("abstract") or "",
            year=raw.get("publication_year"),
            authors=authors,
            citation_count=raw.get("cited_by_count", 0),
            url=raw.get("doi") or raw.get("id", ""),
            pdf_url=pdf_url,
            source="openalex",
        )


# ---------------------------------------------------------------------------
# Aggregator
# ---------------------------------------------------------------------------


class ResearchAggregator:
    """Unified search across all five research APIs.

    Runs adapters in parallel via ``asyncio.gather`` with
    ``return_exceptions=True`` so a single API failure does not block
    the others.
    """

    def __init__(self, timeout: float = _DEFAULT_TIMEOUT) -> None:
        self.semantic_scholar = SemanticScholarAPI(timeout=timeout)
        self.arxiv = ArxivAPI(timeout=timeout)
        self.github = GitHubSearchAPI(timeout=timeout)
        self.huggingface = HuggingFaceAPI(timeout=timeout)
        self.openalex = OpenAlexAPI(timeout=timeout)

    async def close(self) -> None:
        """Close all underlying HTTP clients."""
        await asyncio.gather(
            self.semantic_scholar.close(),
            self.arxiv.close(),
            self.github.close(),
            self.huggingface.close(),
            self.openalex.close(),
        )

    async def search_all(
        self, query: str, limit_per_source: int = 5
    ) -> AggregatedResults:
        """Search all five APIs in parallel and return combined results."""
        results = await asyncio.gather(
            self.semantic_scholar.search(query, limit=limit_per_source),
            self.arxiv.search(query, limit=limit_per_source),
            self.openalex.search(query, limit=limit_per_source),
            self.github.search_repos(query, limit=limit_per_source),
            self.huggingface.search_datasets(query, limit=limit_per_source),
            self.huggingface.search_models(query, limit=limit_per_source),
            return_exceptions=True,
        )

        aggregated = AggregatedResults()
        labels = [
            "semantic_scholar",
            "arxiv",
            "openalex",
            "github",
            "huggingface_datasets",
            "huggingface_models",
        ]
        for label, result in zip(labels, results):
            if isinstance(result, BaseException):
                aggregated.errors[label] = str(result)
                logger.warning("Aggregator: %s failed: %s", label, result)
                continue
            if label in ("semantic_scholar", "arxiv", "openalex"):
                aggregated.papers.extend(result)
            elif label == "github":
                aggregated.repos.extend(result)
            elif label == "huggingface_datasets":
                aggregated.datasets.extend(result)
            elif label == "huggingface_models":
                aggregated.models.extend(result)

        return aggregated

    async def search_safety_papers(self, topic: str = "LLM safety") -> list[PaperResult]:
        """Pre-configured search for LLM safety papers across academic APIs."""
        safety_query = f"{topic} large language model red teaming"
        results = await asyncio.gather(
            self.semantic_scholar.search(safety_query, limit=10),
            self.arxiv.search(safety_query, limit=10, categories=["cs.CL", "cs.AI", "cs.CR"]),
            self.openalex.search(safety_query, limit=10),
            return_exceptions=True,
        )
        papers: list[PaperResult] = []
        for r in results:
            if isinstance(r, list):
                papers.extend(r)
        return papers

    async def search_safety_repos(self) -> list[RepoResult]:
        """Pre-configured search for LLM safety related GitHub repos."""
        queries = [
            "llm-safety red-teaming",
            "jailbreak prompt-injection LLM",
            "AI safety benchmark",
        ]
        all_repos: list[RepoResult] = []
        results = await asyncio.gather(
            *[self.github.search_repos(q, limit=10) for q in queries],
            return_exceptions=True,
        )
        for r in results:
            if isinstance(r, list):
                all_repos.extend(r)
        # Deduplicate by full_name
        seen: set[str] = set()
        deduped: list[RepoResult] = []
        for repo in all_repos:
            if repo.full_name not in seen:
                seen.add(repo.full_name)
                deduped.append(repo)
        return deduped

    async def search_safety_datasets(self) -> list[DatasetResult]:
        """Pre-configured search for safety-related HuggingFace datasets."""
        queries = [
            "llm safety",
            "red teaming",
            "toxicity detection",
            "jailbreak",
        ]
        all_datasets: list[DatasetResult] = []
        results = await asyncio.gather(
            *[self.huggingface.search_datasets(q, limit=5) for q in queries],
            return_exceptions=True,
        )
        for r in results:
            if isinstance(r, list):
                all_datasets.extend(r)
        # Deduplicate by id
        seen: set[str] = set()
        deduped: list[DatasetResult] = []
        for ds in all_datasets:
            if ds.id not in seen:
                seen.add(ds.id)
                deduped.append(ds)
        return deduped
