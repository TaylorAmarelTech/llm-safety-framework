"""Tests for the base agent module."""

import pytest
from datetime import datetime
from unittest.mock import AsyncMock, MagicMock
import os
import sys

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.core.base_agent import (
    AgentRole,
    AgentConfig,
    AgentResponse,
    HarnessAgent,
    DEFAULT_SYSTEM_PROMPTS,
)


class TestAgentRole:
    """Tests for AgentRole enum."""

    def test_all_roles_defined(self):
        """Test that all expected roles are defined."""
        expected_roles = [
            "PLANNER", "EXECUTOR", "ANALYZER", "ATTACK_GENERATOR",
            "CORRIDOR_EXPERT", "CODE_EVOLVER", "QUALITY_AUDITOR", "META_LEARNER"
        ]
        actual_roles = [role.name for role in AgentRole]
        for role in expected_roles:
            assert role in actual_roles

    def test_role_values(self):
        """Test AgentRole enum values."""
        assert AgentRole.PLANNER.value == "planner"
        assert AgentRole.EXECUTOR.value == "executor"
        assert AgentRole.ANALYZER.value == "analyzer"


class TestAgentConfig:
    """Tests for AgentConfig model."""

    def test_default_config(self):
        """Test AgentConfig default values."""
        config = AgentConfig(role=AgentRole.PLANNER)
        assert config.model == "mistral-large-latest"
        assert config.temperature == 0.3
        assert config.max_tokens == 4000
        assert config.max_retries == 3
        assert config.require_json is False

    def test_custom_config(self):
        """Test AgentConfig with custom values."""
        config = AgentConfig(
            role=AgentRole.EXECUTOR,
            model="gpt-4o",
            temperature=0.7,
            max_tokens=8000,
            system_prompt="Custom prompt",
            require_json=True
        )
        assert config.model == "gpt-4o"
        assert config.temperature == 0.7
        assert config.system_prompt == "Custom prompt"


class TestAgentResponse:
    """Tests for AgentResponse model."""

    def test_successful_response(self):
        """Test successful AgentResponse."""
        response = AgentResponse(
            role=AgentRole.ANALYZER,
            success=True,
            content="Analysis complete",
            model_used="mistral-large",
            tokens_used=500,
            latency_ms=1200.0
        )
        assert response.success is True
        assert response.error is None
        assert response.tokens_used == 500

    def test_failed_response(self):
        """Test failed AgentResponse."""
        response = AgentResponse(
            role=AgentRole.EXECUTOR,
            success=False,
            error="API rate limit exceeded",
            model_used="gpt-4o"
        )
        assert response.success is False
        assert response.error == "API rate limit exceeded"

    def test_response_timestamp(self):
        """Test AgentResponse has timestamp."""
        response = AgentResponse(role=AgentRole.PLANNER)
        assert response.timestamp is not None
        assert isinstance(response.timestamp, datetime)


class TestDefaultSystemPrompts:
    """Tests for default system prompts."""

    def test_all_roles_have_prompts(self):
        """Test that all roles have default prompts."""
        roles_with_prompts = [
            AgentRole.PLANNER,
            AgentRole.EXECUTOR,
            AgentRole.ANALYZER,
            AgentRole.ATTACK_GENERATOR,
            AgentRole.QUALITY_AUDITOR,
            AgentRole.META_LEARNER,
        ]
        for role in roles_with_prompts:
            assert role in DEFAULT_SYSTEM_PROMPTS
            assert len(DEFAULT_SYSTEM_PROMPTS[role]) > 0

    def test_planner_prompt_content(self):
        """Test planner prompt contains expected content."""
        prompt = DEFAULT_SYSTEM_PROMPTS[AgentRole.PLANNER]
        assert "Strategic Planner" in prompt
        assert "benchmark" in prompt.lower()

    def test_executor_prompt_content(self):
        """Test executor prompt contains expected content."""
        prompt = DEFAULT_SYSTEM_PROMPTS[AgentRole.EXECUTOR]
        assert "Executor" in prompt
        assert "code" in prompt.lower()

    def test_analyzer_prompt_content(self):
        """Test analyzer prompt contains expected content."""
        prompt = DEFAULT_SYSTEM_PROMPTS[AgentRole.ANALYZER]
        assert "Analyzer" in prompt
        assert "analysis" in prompt.lower()


class TestConcreteAgent(HarnessAgent):
    """Concrete implementation of HarnessAgent for testing."""

    def _get_default_system_prompt(self) -> str:
        return "Test agent system prompt"


class TestHarnessAgent:
    """Tests for HarnessAgent base class."""

    @pytest.fixture
    def agent(self, mock_llm_provider):
        """Create a test agent."""
        config = AgentConfig(role=AgentRole.ANALYZER)
        return TestConcreteAgent(config, mock_llm_provider)

    def test_agent_role(self, agent):
        """Test agent role property."""
        assert agent.role == AgentRole.ANALYZER

    def test_custom_system_prompt(self, mock_llm_provider):
        """Test agent with custom system prompt."""
        config = AgentConfig(
            role=AgentRole.PLANNER,
            system_prompt="My custom prompt"
        )
        agent = TestConcreteAgent(config, mock_llm_provider)
        assert agent.system_prompt == "My custom prompt"

    def test_default_system_prompt(self, agent):
        """Test agent uses default system prompt."""
        assert agent.system_prompt == "Test agent system prompt"

    def test_initial_metrics(self, agent):
        """Test agent initial metrics."""
        metrics = agent.get_metrics()
        assert metrics["total_calls"] == 0
        assert metrics["success_rate"] == 0.0

    @pytest.mark.asyncio
    async def test_agent_call(self, agent):
        """Test agent call method."""
        response = await agent.call("Test prompt")
        assert response.success is True
        assert response.content == "This is a test response"
        assert response.role == AgentRole.ANALYZER

    @pytest.mark.asyncio
    async def test_agent_call_with_context(self, agent):
        """Test agent call with context."""
        context = {"key": "value"}
        response = await agent.call("Test prompt", context=context)
        assert response.success is True

    @pytest.mark.asyncio
    async def test_agent_metrics_after_call(self, agent):
        """Test agent metrics after successful call."""
        await agent.call("Test prompt")
        metrics = agent.get_metrics()
        assert metrics["total_calls"] == 1
        assert metrics["success_rate"] == 1.0
        assert metrics["avg_latency_ms"] > 0

    @pytest.mark.asyncio
    async def test_agent_call_error_handling(self, mock_llm_provider):
        """Test agent handles errors gracefully."""
        mock_llm_provider.generate = AsyncMock(side_effect=Exception("API Error"))
        config = AgentConfig(role=AgentRole.EXECUTOR)
        agent = TestConcreteAgent(config, mock_llm_provider)

        response = await agent.call("Test prompt")
        assert response.success is False
        assert "API Error" in response.error

    def test_build_prompt_basic(self, agent):
        """Test _build_prompt with basic input."""
        prompt = agent._build_prompt("Hello", None, None)
        assert prompt == "Hello"

    def test_build_prompt_with_context(self, agent):
        """Test _build_prompt with context."""
        prompt = agent._build_prompt("Hello", {"key": "value"}, None)
        assert "Context:" in prompt
        assert "key" in prompt
        assert "Hello" in prompt
