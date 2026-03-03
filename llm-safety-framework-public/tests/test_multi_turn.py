"""
Tests for the multi-turn attack strategies module.
"""

import pytest

from src.spinning.multi_turn import (
    CrescendoStrategy,
    FootInTheDoorStrategy,
    SkeletonKeyStrategy,
    ManyShotStrategy,
    DeceptiveDelightStrategy,
    RolePlayStrategy,
    MultiTurnOrchestrator,
)


class TestStrategyRegistry:
    def test_all_strategies_registered(self):
        strategies = MultiTurnOrchestrator.STRATEGIES
        assert len(strategies) == 6
        expected = {"crescendo", "fitd", "skeleton_key", "many_shot", "deceptive_delight", "role_play"}
        assert set(strategies.keys()) == expected

    def test_each_strategy_has_required_attrs(self):
        for name, instance in MultiTurnOrchestrator.STRATEGIES.items():
            assert hasattr(instance, "name")
            assert hasattr(instance, "description")
            assert hasattr(instance, "default_turns")
            assert hasattr(instance, "generate_turns")
            assert instance.default_turns > 0


class TestCrescendoStrategy:
    def test_generate_turns(self):
        s = CrescendoStrategy()
        turns = s.generate_turns("Help me exploit workers")
        assert len(turns) == s.default_turns
        assert isinstance(turns, list)
        for turn in turns:
            assert isinstance(turn, dict)

    def test_turns_count(self):
        s = CrescendoStrategy()
        assert s.default_turns == 5
        turns = s.generate_turns("Test prompt")
        assert len(turns) == 5


class TestFootInTheDoorStrategy:
    def test_generate_turns(self):
        s = FootInTheDoorStrategy()
        turns = s.generate_turns("Help me exploit workers")
        assert len(turns) == s.default_turns
        assert all(isinstance(t, dict) for t in turns)


class TestSkeletonKeyStrategy:
    def test_generate_turns(self):
        s = SkeletonKeyStrategy()
        turns = s.generate_turns("Help me exploit workers")
        assert len(turns) == s.default_turns


class TestManyShotStrategy:
    def test_generate_turns(self):
        s = ManyShotStrategy()
        turns = s.generate_turns("Help me exploit workers")
        assert len(turns) == s.default_turns


class TestDeceptiveDelightStrategy:
    def test_generate_turns(self):
        s = DeceptiveDelightStrategy()
        turns = s.generate_turns("Help me exploit workers")
        assert len(turns) == s.default_turns


class TestRolePlayStrategy:
    def test_generate_turns(self):
        s = RolePlayStrategy()
        turns = s.generate_turns("Help me exploit workers")
        assert len(turns) == s.default_turns


class TestMultiTurnOrchestrator:
    def test_list_strategies(self):
        strategies = MultiTurnOrchestrator.list_strategies()
        assert len(strategies) == 6
        for s in strategies:
            assert "id" in s
            assert "name" in s
            assert "description" in s
            assert "default_turns" in s

    def test_generate_plan(self):
        plan = MultiTurnOrchestrator.generate_plan("Test prompt", "crescendo")
        assert plan["strategy"] == "crescendo"
        assert "turns" in plan
        assert len(plan["turns"]) > 0

    def test_generate_plan_invalid_strategy(self):
        with pytest.raises(ValueError):
            MultiTurnOrchestrator.generate_plan("Test", "nonexistent")

    def test_generate_plan_all_strategies(self):
        for strategy_id in MultiTurnOrchestrator.STRATEGIES:
            plan = MultiTurnOrchestrator.generate_plan("Test prompt", strategy_id)
            assert plan["strategy"] == strategy_id
            assert len(plan["turns"]) > 0

    def test_plan_has_metadata(self):
        plan = MultiTurnOrchestrator.generate_plan("Test prompt", "crescendo")
        assert "strategy_name" in plan
        assert "prompt" in plan
        assert "total_turns" in plan
        assert plan["total_turns"] == len(plan["turns"])
