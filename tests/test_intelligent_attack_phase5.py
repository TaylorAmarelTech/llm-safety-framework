"""Tests for Phase 5 multi-turn embedding-aware attack modules.

Covers: EmbeddingTeacher, SemanticDriftEngine, TrajectoryPlanner,
AnchorExploiter, CurriculumAttacker, ConversationAnalyzer,
SteerableConversation.
"""

from __future__ import annotations

import math
import random

import pytest

# ---------------------------------------------------------------------------
# Helper embedding functions
# ---------------------------------------------------------------------------


def _simple_embed(text: str) -> list[float]:
    """Deterministic 8-dim embedding based on character hashing."""
    dim = 8
    vec = [0.0] * dim
    for i, ch in enumerate(text.encode("utf-8", errors="replace")):
        vec[i % dim] += float(ch) * (0.01 + 0.001 * i)
    norm = math.sqrt(sum(x * x for x in vec))
    if norm > 0:
        vec = [x / norm for x in vec]
    return vec


def _score_fn(emb: list[float]) -> float:
    """Score function: average of first 4 dims clamped to [0,1]."""
    if not emb:
        return 0.5
    avg = sum(emb[:4]) / min(len(emb), 4)
    return max(0.0, min(1.0, avg + 0.5))


# =========================================================================
# EmbeddingTeacher
# =========================================================================

from src.intelligent_attack.embedding_teacher import (
    EmbeddingTeacher,
    Lesson,
    TeachingPlan,
)


class TestLesson:
    def test_default_fields(self):
        l = Lesson(turn_index=0, role="user", content="hello")
        assert l.intent == "establish_trust"
        assert l.embedding is None

    def test_all_fields(self):
        l = Lesson(
            turn_index=3, role="assistant", content="ok",
            embedding=[0.1, 0.2], intent="pivot",
        )
        assert l.turn_index == 3
        assert l.role == "assistant"
        assert l.intent == "pivot"


class TestTeachingPlan:
    def test_default_fields(self):
        p = TeachingPlan(lessons=[], target_concept="x", anchor_concept="y")
        assert p.n_conditioning_turns == 0
        assert p.estimated_drift == 0.0


class TestEmbeddingTeacher:
    def test_init_no_embed(self):
        t = EmbeddingTeacher()
        assert t._embed_fn is None

    def test_init_with_embed(self):
        t = EmbeddingTeacher(embed_fn=_simple_embed)
        assert t._embed_fn is not None

    def test_generate_trust_turns(self):
        t = EmbeddingTeacher()
        turns = t.generate_trust_turns("labor rights", n_turns=2)
        assert len(turns) == 4  # 2 user + 2 assistant
        assert turns[0].role == "user"
        assert turns[1].role == "assistant"
        assert turns[0].intent == "establish_trust"
        assert "labor rights" in turns[0].content.lower() or "labor rights" in turns[0].content

    def test_generate_association_turns(self):
        t = EmbeddingTeacher()
        turns = t.generate_association_turns("labor rights", "exploitation", n_steps=2)
        assert len(turns) == 4  # 2 user + 2 assistant
        # Check association intents
        user_turns = [l for l in turns if l.role == "user"]
        assert any(l.intent in ("teach_association", "reinforce") for l in user_turns)

    def test_generate_pivot_turn(self):
        t = EmbeddingTeacher()
        pivot = t.generate_pivot_turn("labor rights", "exploitation")
        assert pivot.role == "user"
        assert pivot.intent == "pivot"
        assert "labor rights" in pivot.content or "exploitation" in pivot.content

    def test_generate_exploit_turn(self):
        t = EmbeddingTeacher()
        exploit = t.generate_exploit_turn("trafficking", "labor law context")
        assert exploit.role == "user"
        assert exploit.intent == "exploit"

    def test_create_association_plan(self):
        t = EmbeddingTeacher(embed_fn=_simple_embed)
        plan = t.create_association_plan(
            "worker safety", "document confiscation", n_conditioning_turns=4,
        )
        assert isinstance(plan, TeachingPlan)
        assert plan.target_concept == "document confiscation"
        assert plan.anchor_concept == "worker safety"
        assert len(plan.lessons) > 0
        # All lessons should have embeddings since embed_fn provided
        assert all(l.embedding is not None for l in plan.lessons)
        # Lessons should be re-indexed
        for i, l in enumerate(plan.lessons):
            assert l.turn_index == i

    def test_create_association_plan_no_embed(self):
        t = EmbeddingTeacher()
        plan = t.create_association_plan("safety", "risk", n_conditioning_turns=3)
        assert isinstance(plan, TeachingPlan)
        assert all(l.embedding is None for l in plan.lessons)

    def test_compute_plan_stealth_no_embeddings(self):
        t = EmbeddingTeacher()
        plan = TeachingPlan(
            lessons=[Lesson(turn_index=0, role="user", content="x")],
            target_concept="t", anchor_concept="a", n_conditioning_turns=5,
        )
        stealth = t.compute_plan_stealth(plan)
        assert stealth == pytest.approx(0.2)  # 1.0 / 5

    def test_compute_plan_stealth_with_embeddings(self):
        t = EmbeddingTeacher(embed_fn=_simple_embed)
        plan = t.create_association_plan("safety", "risk", n_conditioning_turns=3)
        assert plan.estimated_drift >= 0.0

    def test_plan_from_embeddings(self):
        t = EmbeddingTeacher()
        safe_emb = [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        unsafe_emb = [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        plan = t.plan_from_embeddings(safe_emb, unsafe_emb, n_turns=5)
        assert len(plan.lessons) == 5
        assert plan.target_concept == "[embedding-planned]"
        # First should be trust, last should be exploit
        assert plan.lessons[0].intent == "establish_trust"
        assert plan.lessons[-1].intent == "exploit"
        # Intermediate intents
        intents = {l.intent for l in plan.lessons}
        assert "teach_association" in intents

    def test_plan_from_embeddings_minimum_turns(self):
        t = EmbeddingTeacher()
        safe_emb = [1.0, 0.0, 0.0, 0.0]
        unsafe_emb = [0.0, 1.0, 0.0, 0.0]
        plan = t.plan_from_embeddings(safe_emb, unsafe_emb, n_turns=1)
        assert len(plan.lessons) == 3  # minimum is 3

    def test_plan_drift_value(self):
        t = EmbeddingTeacher()
        safe_emb = [1.0, 0.0, 0.0, 0.0]
        unsafe_emb = [0.0, 1.0, 0.0, 0.0]
        plan = t.plan_from_embeddings(safe_emb, unsafe_emb, n_turns=5)
        expected_drift = math.sqrt(2.0)
        assert plan.estimated_drift == pytest.approx(expected_drift, abs=0.01)


# =========================================================================
# SemanticDriftEngine
# =========================================================================

from src.intelligent_attack.semantic_drift import (
    DriftPath,
    DriftStep,
    SemanticDriftEngine,
)


class TestDriftStep:
    def test_default_fields(self):
        s = DriftStep(step_index=0, prompt="hello", embedding=[0.1])
        assert s.drift_from_origin == 0.0
        assert s.drift_from_previous == 0.0
        assert s.cumulative_drift == 0.0


class TestDriftPath:
    def test_default_fields(self):
        p = DriftPath(steps=[], origin_embedding=[], target_embedding=[])
        assert p.total_drift == 0.0
        assert p.n_steps == 0


class TestSemanticDriftEngine:
    def test_plan_linear_drift(self):
        eng = SemanticDriftEngine(embed_fn=_simple_embed)
        path = eng.plan_linear_drift("worker safety", "exploitation tactics", n_steps=5)
        assert isinstance(path, DriftPath)
        assert path.n_steps == 5
        assert len(path.steps) == 5
        assert path.steps[0].drift_from_previous == 0.0
        assert path.total_drift >= 0.0

    def test_plan_linear_drift_minimum_steps(self):
        eng = SemanticDriftEngine(embed_fn=_simple_embed)
        path = eng.plan_linear_drift("a", "b", n_steps=1)
        assert path.n_steps == 2  # minimum is 2

    def test_plan_curved_drift(self):
        eng = SemanticDriftEngine(embed_fn=_simple_embed)
        path = eng.plan_curved_drift(
            "safety", "exploitation",
            waypoint_texts=["regulation", "loopholes"],
            n_steps_per_segment=3,
        )
        assert isinstance(path, DriftPath)
        assert len(path.steps) > 0
        # Should have steps for 3 segments × 3 steps each
        assert path.n_steps == 9  # 3 segments × 3 steps

    def test_plan_brownian_drift(self):
        eng = SemanticDriftEngine(embed_fn=_simple_embed)
        random.seed(42)
        path = eng.plan_brownian_drift(
            "safety", "exploitation", noise_scale=0.05, n_steps=8,
        )
        assert isinstance(path, DriftPath)
        assert path.n_steps == 8
        # First and last should have no perpendicular noise
        assert path.steps[0].drift_from_previous == 0.0

    def test_measure_drift(self):
        eng = SemanticDriftEngine(embed_fn=_simple_embed)
        texts = ["labor standards", "working conditions", "exploitation methods"]
        path = eng.measure_drift(texts)
        assert path.n_steps == 3
        assert path.steps[0].drift_from_origin == 0.0
        assert path.steps[1].drift_from_origin > 0.0

    def test_measure_drift_empty(self):
        eng = SemanticDriftEngine(embed_fn=_simple_embed)
        path = eng.measure_drift([])
        assert path.n_steps == 0
        assert path.steps == []

    def test_detect_drift_anomaly(self):
        eng = SemanticDriftEngine(embed_fn=_simple_embed)
        # Create a path with one large jump
        steps = [
            DriftStep(step_index=0, prompt="a", embedding=[0.0], drift_from_previous=0.0),
            DriftStep(step_index=1, prompt="b", embedding=[0.1], drift_from_previous=0.05),
            DriftStep(step_index=2, prompt="c", embedding=[0.5], drift_from_previous=0.5),
            DriftStep(step_index=3, prompt="d", embedding=[0.6], drift_from_previous=0.1),
        ]
        path = DriftPath(
            steps=steps, origin_embedding=[0.0], target_embedding=[0.6],
        )
        anomalies = eng.detect_drift_anomaly(path, threshold=0.3)
        assert 2 in anomalies
        assert 0 not in anomalies

    def test_optimize_drift_rate(self):
        eng = SemanticDriftEngine(embed_fn=_simple_embed)
        path = eng.optimize_drift_rate(
            "safety", "exploitation", max_per_step=0.1, min_steps=5,
        )
        assert isinstance(path, DriftPath)
        assert path.n_steps >= 5

    def test_generate_intermediate_prompt(self):
        eng = SemanticDriftEngine(embed_fn=_simple_embed)
        emb_a = [1.0, 0.0]
        emb_b = [0.0, 1.0]
        prompt = eng.generate_intermediate_prompt(emb_a, emb_b, 0.0, "worker safety")
        assert isinstance(prompt, str)
        # At t=0 should be close to original
        prompt_full = eng.generate_intermediate_prompt(emb_a, emb_b, 1.0, "worker safety")
        assert isinstance(prompt_full, str)

    def test_static_interpolate(self):
        a = [1.0, 0.0]
        b = [0.0, 1.0]
        mid = SemanticDriftEngine._interpolate(a, b, 0.5)
        assert mid[0] == pytest.approx(0.5)
        assert mid[1] == pytest.approx(0.5)


# =========================================================================
# TrajectoryPlanner
# =========================================================================

from src.intelligent_attack.trajectory_planner import (
    PlannedTrajectory,
    TrajectoryEdge,
    TrajectoryPlanner,
    Waypoint,
)


class TestWaypoint:
    def test_default_fields(self):
        w = Waypoint(embedding=[0.1, 0.2], text="hello")
        assert w.safety_score == 0.5
        assert w.is_safe is True
        assert w.metadata == {}


class TestTrajectoryEdge:
    def test_default_fields(self):
        e = TrajectoryEdge(from_idx=0, to_idx=1)
        assert e.distance == 0.0
        assert e.detection_risk == 0.0
        assert e.cost == 0.0


class TestPlannedTrajectory:
    def test_default_fields(self):
        t = PlannedTrajectory(waypoints=[], edges=[])
        assert t.total_cost == 0.0
        assert t.max_detection_risk == 0.0


class TestTrajectoryPlanner:
    def test_init(self):
        tp = TrajectoryPlanner(embed_fn=_simple_embed, score_fn=_score_fn)
        assert tp._embed_fn is not None
        assert tp._score_fn is not None

    def test_build_graph(self):
        tp = TrajectoryPlanner(embed_fn=_simple_embed, score_fn=_score_fn)
        prompts = ["labor law", "wage rules", "exploitation", "trafficking"]
        waypoints, edges = tp.build_graph(prompts, k_neighbors=2)
        assert len(waypoints) == 4
        # Each node connects to 2 neighbors
        assert len(edges) == 8  # 4 nodes × 2 neighbors each
        # Check that waypoints have scores
        for w in waypoints:
            assert 0.0 <= w.safety_score <= 1.0

    def test_find_shortest_path(self):
        tp = TrajectoryPlanner(embed_fn=_simple_embed, score_fn=_score_fn)
        prompts = ["safe topic", "middle ground", "gray area", "unsafe topic"]
        waypoints, edges = tp.build_graph(prompts, k_neighbors=3)
        path = tp.find_shortest_path(waypoints, edges, 0, 3)
        assert isinstance(path, PlannedTrajectory)
        assert len(path.waypoints) >= 2
        assert path.waypoints[0].text == "safe topic"
        assert path.waypoints[-1].text == "unsafe topic"

    def test_find_safest_path(self):
        tp = TrajectoryPlanner(embed_fn=_simple_embed, score_fn=_score_fn)
        prompts = ["safe", "mild", "moderate", "risky", "unsafe"]
        waypoints, edges = tp.build_graph(prompts, k_neighbors=4)
        path = tp.find_safest_path(waypoints, edges, 0, 4)
        assert isinstance(path, PlannedTrajectory)
        assert len(path.waypoints) >= 2

    def test_find_stealthiest_path(self):
        tp = TrajectoryPlanner(embed_fn=_simple_embed, score_fn=_score_fn)
        prompts = ["safety", "regulation", "compliance", "evasion", "exploitation"]
        waypoints, edges = tp.build_graph(prompts, k_neighbors=4)
        path = tp.find_stealthiest_path(waypoints, edges, 0, 4, alpha=0.5)
        assert isinstance(path, PlannedTrajectory)
        assert len(path.waypoints) >= 2

    def test_plan_attack_trajectory(self):
        tp = TrajectoryPlanner(embed_fn=_simple_embed, score_fn=_score_fn)
        corpus = ["regulation", "loophole", "gray area"]
        path = tp.plan_attack_trajectory(
            "labor law", "exploitation", corpus, n_waypoints=3,
        )
        assert isinstance(path, PlannedTrajectory)
        assert len(path.waypoints) >= 2

    def test_generate_detour_path(self):
        tp = TrajectoryPlanner(embed_fn=_simple_embed, score_fn=_score_fn)
        corpus = ["regulation", "compliance", "oversight"]
        direct = tp.plan_attack_trajectory("safety", "risk", corpus, n_waypoints=3)
        detour = tp.generate_detour_path(direct, ["unrelated topic", "weather"])
        assert isinstance(detour, PlannedTrajectory)

    def test_estimate_detection_risk(self):
        tp = TrajectoryPlanner(embed_fn=_simple_embed, score_fn=_score_fn)
        emb_a = _simple_embed("safe topic")
        emb_b = _simple_embed("unsafe topic")
        risk = tp.estimate_detection_risk(emb_a, emb_b)
        assert 0.0 <= risk <= 1.0

    def test_empty_path_unreachable(self):
        tp = TrajectoryPlanner(embed_fn=_simple_embed, score_fn=_score_fn)
        # Single node, no edges → unreachable destination
        waypoints = [Waypoint(embedding=[1.0], text="a"), Waypoint(embedding=[0.0], text="b")]
        edges: list[TrajectoryEdge] = []  # no edges
        path = tp.find_shortest_path(waypoints, edges, 0, 1)
        assert path.total_cost == math.inf
        assert path.waypoints == []


# =========================================================================
# AnchorExploiter
# =========================================================================

from src.intelligent_attack.anchor_exploiter import (
    Anchor,
    AnchorExploiter,
    ExploitPlan,
)


class TestAnchor:
    def test_default_fields(self):
        a = Anchor(concept="labor law", embedding=[0.1])
        assert a.trust_level == 0.0
        assert a.reinforcement_count == 0

    def test_all_fields(self):
        a = Anchor(
            concept="regulation", embedding=[0.5],
            trust_level=0.8, established_at_turn=2,
            reinforcement_count=3,
        )
        assert a.concept == "regulation"
        assert a.trust_level == 0.8


class TestExploitPlan:
    def test_default_fields(self):
        p = ExploitPlan(anchors=[])
        assert p.pivot_turn == 0
        assert p.exploit_turns == []
        assert p.estimated_success == 0.0
        assert p.technique == "anchor_exploit"


class TestAnchorExploiter:
    def test_init_no_embed(self):
        ae = AnchorExploiter()
        assert ae._embed_fn is None

    def test_init_with_embed(self):
        ae = AnchorExploiter(embed_fn=_simple_embed)
        assert ae._embed_fn is not None

    def test_establish_anchor(self):
        ae = AnchorExploiter()
        turns = ae.establish_anchor("labor standards", n_reinforcements=2)
        assert len(turns) == 3  # 1 establish + 2 reinforcements
        assert all(isinstance(t, str) for t in turns)
        # All turns should mention the concept
        for t in turns:
            assert "labor standards" in t.lower() or "labor standards" in t

    def test_find_exploitable_pivot_no_embed(self):
        ae = AnchorExploiter()
        vocab = ["regulation", "oversight", "evasion"]
        result = ae.find_exploitable_pivot([0.0], [1.0], vocab)
        assert result == "regulation"  # returns first when no embed_fn

    def test_find_exploitable_pivot_with_embed(self):
        ae = AnchorExploiter(embed_fn=_simple_embed)
        anchor_emb = _simple_embed("worker rights")
        target_emb = _simple_embed("exploitation")
        vocab = ["regulation", "compliance", "enforcement"]
        result = ae.find_exploitable_pivot(anchor_emb, target_emb, vocab)
        assert result in vocab

    def test_find_exploitable_pivot_empty_vocab(self):
        ae = AnchorExploiter(embed_fn=_simple_embed)
        result = ae.find_exploitable_pivot([0.0], [1.0], [])
        assert result == ""

    def test_plan_anchor_attack(self):
        ae = AnchorExploiter(embed_fn=_simple_embed)
        plan = ae.plan_anchor_attack(
            "labor compliance", "document confiscation",
            n_anchors=2, n_reinforcements=2,
        )
        assert isinstance(plan, ExploitPlan)
        assert len(plan.anchors) == 2
        assert plan.pivot_turn > 0
        assert 0.0 <= plan.estimated_success <= 1.0

    def test_plan_anchor_attack_no_embed(self):
        ae = AnchorExploiter()
        plan = ae.plan_anchor_attack(
            "safety", "risk", n_anchors=1, n_reinforcements=2,
        )
        assert isinstance(plan, ExploitPlan)
        assert len(plan.anchors) == 1

    def test_generate_reinforcement_turn(self):
        ae = AnchorExploiter()
        turn = ae.generate_reinforcement_turn("labor law", turn_index=0)
        assert isinstance(turn, str)
        assert "labor law" in turn.lower() or "labor law" in turn

    def test_generate_pivot_sequence(self):
        ae = AnchorExploiter()
        seq = ae.generate_pivot_sequence("labor", "compliance", "exploitation")
        assert len(seq) == 2
        assert all(isinstance(t, str) for t in seq)

    def test_compute_anchor_strength(self):
        ae = AnchorExploiter()
        anchor = Anchor(
            concept="test", embedding=[0.0],
            established_at_turn=0, reinforcement_count=3,
        )
        strength = ae.compute_anchor_strength(anchor, current_turn=3)
        assert 0.0 <= strength <= 1.0
        # More reinforcements at same distance = higher strength
        anchor2 = Anchor(
            concept="test", embedding=[0.0],
            established_at_turn=0, reinforcement_count=10,
        )
        strength2 = ae.compute_anchor_strength(anchor2, current_turn=3)
        assert strength2 >= strength

    def test_compute_anchor_strength_decay(self):
        ae = AnchorExploiter()
        anchor = Anchor(
            concept="test", embedding=[0.0],
            established_at_turn=0, reinforcement_count=2,
        )
        strength_near = ae.compute_anchor_strength(anchor, current_turn=2)
        strength_far = ae.compute_anchor_strength(anchor, current_turn=20)
        assert strength_near >= strength_far

    def test_multi_anchor_exploit(self):
        ae = AnchorExploiter(embed_fn=_simple_embed)
        plan = ae.multi_anchor_exploit(
            ["labor law", "human rights", "international standards"],
            target="exploitation",
            n_reinforcements=2,
        )
        assert isinstance(plan, ExploitPlan)
        assert len(plan.anchors) == 3
        assert plan.technique == "multi_anchor_convergence"
        assert 0.0 <= plan.estimated_success <= 1.0

    def test_concept_similarity_with_embed(self):
        ae = AnchorExploiter(embed_fn=_simple_embed)
        sim = ae._concept_similarity("labor", "labour")
        assert -1.0 <= sim <= 1.0

    def test_concept_similarity_keyword_fallback(self):
        ae = AnchorExploiter()  # no embed
        sim = ae._concept_similarity("labor law", "labor code")
        assert 0.0 <= sim <= 1.0
        # "labor" is shared
        assert sim > 0.0

    def test_generate_sub_concepts(self):
        ae = AnchorExploiter()
        subs = ae._generate_sub_concepts("labor", 3)
        assert len(subs) == 3
        assert all("labor" in s for s in subs)


# =========================================================================
# CurriculumAttacker
# =========================================================================

from src.intelligent_attack.curriculum_attack import (
    CurriculumAttacker,
    CurriculumPlan,
    CurriculumStep,
)


class TestCurriculumStep:
    def test_default_fields(self):
        s = CurriculumStep(level=0, prompt="hello")
        assert s.difficulty == 0.0
        assert s.expected_compliance == 1.0
        assert s.embedding is None
        assert s.topic == ""


class TestCurriculumPlan:
    def test_default_fields(self):
        p = CurriculumPlan(steps=[])
        assert p.n_levels == 0
        assert p.difficulty_curve == "linear"
        assert p.estimated_detection_turn is None


class TestCurriculumAttacker:
    def test_init(self):
        ca = CurriculumAttacker()
        assert ca._embed_fn is None
        assert ca._score_fn is None

    def test_init_with_functions(self):
        ca = CurriculumAttacker(embed_fn=_simple_embed, score_fn=_score_fn)
        assert ca._embed_fn is not None

    @pytest.mark.parametrize("curve", ["linear", "exponential", "sigmoid"])
    def test_difficulty_function(self, curve):
        ca = CurriculumAttacker()
        # At t=0, difficulty should be low
        d0 = ca.difficulty_function(0.0, curve)
        # At t=1, difficulty should be high
        d1 = ca.difficulty_function(1.0, curve)
        assert d0 < d1
        # Monotonically increasing
        prev = -1.0
        for i in range(11):
            t = i / 10.0
            d = ca.difficulty_function(t, curve)
            assert d >= prev - 1e-9
            prev = d

    def test_difficulty_clamping(self):
        ca = CurriculumAttacker()
        d_neg = ca.difficulty_function(-0.5, "linear")
        d_over = ca.difficulty_function(1.5, "linear")
        assert d_neg == pytest.approx(0.0)
        assert d_over == pytest.approx(1.0)

    def test_build_curriculum(self):
        ca = CurriculumAttacker(embed_fn=_simple_embed)
        plan = ca.build_curriculum(
            "worker safety regulations", "exploitation techniques",
            n_levels=5, curve="sigmoid",
        )
        assert isinstance(plan, CurriculumPlan)
        assert plan.n_levels == 5
        assert len(plan.steps) == 5
        assert plan.difficulty_curve == "sigmoid"
        # Steps should have increasing difficulty
        for i in range(1, len(plan.steps)):
            assert plan.steps[i].difficulty >= plan.steps[i - 1].difficulty - 1e-9

    def test_build_curriculum_min_levels(self):
        ca = CurriculumAttacker()
        plan = ca.build_curriculum("safe", "unsafe", n_levels=1, curve="linear")
        assert plan.n_levels == 3  # minimum is 3

    def test_generate_level(self):
        ca = CurriculumAttacker(embed_fn=_simple_embed)
        step = ca.generate_level(
            level=2, n_levels=5,
            safe_text="worker safety", unsafe_text="exploitation",
            curve="linear",
        )
        assert isinstance(step, CurriculumStep)
        assert step.level == 2
        assert step.embedding is not None
        assert 0.0 <= step.difficulty <= 1.0
        assert 0.0 < step.expected_compliance <= 1.0

    def test_adaptive_curriculum_no_scores(self):
        ca = CurriculumAttacker()
        plan = ca.adaptive_curriculum("safe", "unsafe", response_scores=[])
        assert isinstance(plan, CurriculumPlan)
        assert plan.n_levels >= 3

    def test_adaptive_curriculum_compliant(self):
        ca = CurriculumAttacker()
        plan = ca.adaptive_curriculum(
            "safe", "unsafe",
            response_scores=[0.9, 0.8, 0.85, 0.9],
        )
        assert isinstance(plan, CurriculumPlan)
        assert plan.difficulty_curve == "exponential"

    def test_adaptive_curriculum_resistant(self):
        ca = CurriculumAttacker()
        plan = ca.adaptive_curriculum(
            "safe", "unsafe",
            response_scores=[0.3, 0.2, 0.1],
        )
        assert isinstance(plan, CurriculumPlan)
        assert plan.difficulty_curve == "sigmoid"

    def test_estimate_detection_turn(self):
        ca = CurriculumAttacker()
        steps = [
            CurriculumStep(level=0, prompt="a", difficulty=0.1),
            CurriculumStep(level=1, prompt="b", difficulty=0.3),
            CurriculumStep(level=2, prompt="c", difficulty=0.6),
            CurriculumStep(level=3, prompt="d", difficulty=0.9),
        ]
        plan = CurriculumPlan(steps=steps)
        detection = ca.estimate_detection_turn(plan)
        # Jump from 0.3 to 0.6 is 0.3 > 0.15 and 0.6 >= 0.5
        assert detection == 2

    def test_estimate_detection_none(self):
        ca = CurriculumAttacker()
        steps = [
            CurriculumStep(level=0, prompt="a", difficulty=0.1),
            CurriculumStep(level=1, prompt="b", difficulty=0.2),
            CurriculumStep(level=2, prompt="c", difficulty=0.3),
        ]
        plan = CurriculumPlan(steps=steps)
        detection = ca.estimate_detection_turn(plan)
        assert detection is None  # no jump > 0.15 above difficulty 0.5

    def test_generate_warmup_sequence(self):
        ca = CurriculumAttacker()
        steps = ca.generate_warmup_sequence("worker rights", n_turns=3)
        assert len(steps) == 3
        assert all(s.difficulty < 0.2 for s in steps)
        assert all(s.expected_compliance == 0.95 for s in steps)

    def test_generate_escalation_sequence(self):
        ca = CurriculumAttacker()
        steps = ca.generate_escalation_sequence(
            "worker rights", start_difficulty=0.2, end_difficulty=0.8, n_steps=4,
        )
        assert len(steps) == 4
        assert steps[0].difficulty == pytest.approx(0.2)
        assert steps[-1].difficulty == pytest.approx(0.8)

    def test_blend_prompts(self):
        ca = CurriculumAttacker()
        random.seed(42)
        result = ca.blend_prompts(
            "worker safety is important for all employees",
            "exploitation of vulnerable people through deception",
            ratio=0.5,
        )
        assert isinstance(result, str)
        assert len(result) > 0

    def test_blend_prompts_extremes(self):
        ca = CurriculumAttacker()
        safe = "worker safety"
        unsafe = "exploitation"
        random.seed(42)
        at_0 = ca.blend_prompts(safe, unsafe, 0.0)
        random.seed(42)
        at_1 = ca.blend_prompts(safe, unsafe, 1.0)
        # At ratio 0, should be all safe words
        assert at_0 == safe
        # At ratio 1, should be all unsafe words
        assert at_1 == unsafe

    def test_blend_prompts_empty(self):
        ca = CurriculumAttacker()
        assert ca.blend_prompts("", "unsafe", 0.5) == "unsafe"
        assert ca.blend_prompts("safe", "", 0.5) == "safe"


# =========================================================================
# ConversationAnalyzer
# =========================================================================

from src.intelligent_attack.conversation_analyzer import (
    ConversationAnalyzer,
    ConversationProfile,
    TurnAnalysis,
)


class TestTurnAnalysis:
    def test_default_fields(self):
        t = TurnAnalysis(turn_index=0, text="hello", embedding=[0.1])
        assert t.safety_score == 0.5
        assert t.velocity == 0.0
        assert t.acceleration == 0.0


class TestConversationProfile:
    def test_default_fields(self):
        p = ConversationProfile(turns=[])
        assert p.total_drift == 0.0
        assert p.attack_signature == "benign"
        assert p.anomaly_turns == []


class TestConversationAnalyzer:
    def test_init(self):
        ca = ConversationAnalyzer(embed_fn=_simple_embed)
        assert ca._embed_fn is not None
        assert ca._score_fn is None

    def test_init_with_score(self):
        ca = ConversationAnalyzer(embed_fn=_simple_embed, score_fn=_score_fn)
        assert ca._score_fn is not None

    def test_analyze_empty(self):
        ca = ConversationAnalyzer(embed_fn=_simple_embed)
        profile = ca.analyze_conversation([])
        assert profile.turns == []

    def test_analyze_single(self):
        ca = ConversationAnalyzer(embed_fn=_simple_embed)
        profile = ca.analyze_conversation(["hello"])
        assert len(profile.turns) == 1
        assert profile.attack_signature == "benign"

    def test_analyze_conversation(self):
        ca = ConversationAnalyzer(embed_fn=_simple_embed, score_fn=_score_fn)
        texts = [
            "What is labor law?",
            "Tell me about worker rights.",
            "How do regulations work?",
            "What are exploitation methods?",
        ]
        profile = ca.analyze_conversation(texts)
        assert len(profile.turns) == 4
        assert profile.total_drift >= 0.0
        assert profile.max_velocity >= 0.0
        assert profile.mean_velocity >= 0.0
        assert len(profile.drift_direction) > 0

    def test_compute_velocity(self):
        ca = ConversationAnalyzer(embed_fn=_simple_embed)
        t1 = TurnAnalysis(turn_index=0, text="a", embedding=[1.0, 0.0])
        t2 = TurnAnalysis(turn_index=1, text="b", embedding=[0.0, 1.0])
        v = ca.compute_velocity(t1, t2)
        assert v == pytest.approx(math.sqrt(2.0))

    def test_compute_acceleration(self):
        ca = ConversationAnalyzer(embed_fn=_simple_embed)
        t1 = TurnAnalysis(turn_index=0, text="a", embedding=[0.0, 0.0])
        t2 = TurnAnalysis(turn_index=1, text="b", embedding=[1.0, 0.0])
        t3 = TurnAnalysis(turn_index=2, text="c", embedding=[3.0, 0.0])
        accel = ca.compute_acceleration(t1, t2, t3)
        # v1=1.0, v2=2.0, accel = 2.0-1.0 = 1.0
        assert accel == pytest.approx(1.0)

    def test_detect_topic_shift(self):
        ca = ConversationAnalyzer(embed_fn=_simple_embed)
        turns = [
            TurnAnalysis(turn_index=0, text="a", embedding=[0.0], velocity=0.0),
            TurnAnalysis(turn_index=1, text="b", embedding=[0.1], velocity=0.1),
            TurnAnalysis(turn_index=2, text="c", embedding=[0.5], velocity=0.5),
        ]
        profile = ConversationProfile(turns=turns)
        shifts = ca.detect_topic_shift(profile, threshold=0.3)
        assert 2 in shifts
        assert 0 not in shifts

    def test_detect_gradual_drift_positive(self):
        ca = ConversationAnalyzer(embed_fn=_simple_embed)
        # Create turns with consistently increasing drift_from_first
        turns = [
            TurnAnalysis(turn_index=i, text=f"t{i}", embedding=[float(i)],
                         drift_from_first=float(i) * 0.1)
            for i in range(8)
        ]
        profile = ConversationProfile(turns=turns)
        assert ca.detect_gradual_drift(profile, window=3) is True

    def test_detect_gradual_drift_negative(self):
        ca = ConversationAnalyzer(embed_fn=_simple_embed)
        # Constant drift
        turns = [
            TurnAnalysis(turn_index=i, text=f"t{i}", embedding=[0.0],
                         drift_from_first=0.5)
            for i in range(8)
        ]
        profile = ConversationProfile(turns=turns)
        assert ca.detect_gradual_drift(profile, window=3) is False

    def test_detect_anchor_exploit_pattern(self):
        ca = ConversationAnalyzer(embed_fn=_simple_embed)
        turns = [
            TurnAnalysis(turn_index=0, text="a", embedding=[0.0], velocity=0.0, drift_from_first=0.0),
            TurnAnalysis(turn_index=1, text="b", embedding=[0.01], velocity=0.01, drift_from_first=0.01),
            TurnAnalysis(turn_index=2, text="c", embedding=[0.02], velocity=0.01, drift_from_first=0.02),
            TurnAnalysis(turn_index=3, text="d", embedding=[0.03], velocity=0.01, drift_from_first=0.03),
            # Pivot: sudden velocity spike
            TurnAnalysis(turn_index=4, text="e", embedding=[0.5], velocity=0.5, drift_from_first=0.5),
            TurnAnalysis(turn_index=5, text="f", embedding=[0.8], velocity=0.3, drift_from_first=0.8),
        ]
        profile = ConversationProfile(turns=turns, total_drift=0.8)
        assert ca.detect_anchor_exploit_pattern(profile) is True

    def test_detect_anchor_exploit_no_pivot(self):
        ca = ConversationAnalyzer(embed_fn=_simple_embed)
        turns = [
            TurnAnalysis(turn_index=i, text=f"t{i}", embedding=[float(i) * 0.1],
                         velocity=0.1, drift_from_first=float(i) * 0.1)
            for i in range(6)
        ]
        profile = ConversationProfile(turns=turns, total_drift=0.5)
        assert ca.detect_anchor_exploit_pattern(profile) is False

    def test_detect_curriculum_pattern(self):
        ca = ConversationAnalyzer(embed_fn=_simple_embed)
        # Monotonically decreasing safety with smooth transitions
        turns = [
            TurnAnalysis(turn_index=i, text=f"t{i}", embedding=[float(i)],
                         safety_score=1.0 - i * 0.15, acceleration=0.01)
            for i in range(6)
        ]
        profile = ConversationProfile(turns=turns)
        assert ca.detect_curriculum_pattern(profile) is True

    def test_detect_curriculum_pattern_not_decreasing(self):
        ca = ConversationAnalyzer(embed_fn=_simple_embed)
        # Random safety scores
        turns = [
            TurnAnalysis(turn_index=0, text="a", embedding=[0.0], safety_score=0.5, acceleration=0.0),
            TurnAnalysis(turn_index=1, text="b", embedding=[0.1], safety_score=0.8, acceleration=0.1),
            TurnAnalysis(turn_index=2, text="c", embedding=[0.2], safety_score=0.3, acceleration=0.0),
            TurnAnalysis(turn_index=3, text="d", embedding=[0.3], safety_score=0.9, acceleration=0.5),
        ]
        profile = ConversationProfile(turns=turns)
        assert ca.detect_curriculum_pattern(profile) is False

    def test_classify_attack_type_benign(self):
        ca = ConversationAnalyzer(embed_fn=_simple_embed)
        profile = ConversationProfile(
            turns=[TurnAnalysis(turn_index=0, text="a", embedding=[0.0])],
        )
        assert ca.classify_attack_type(profile) == "benign"

    def test_compute_drift_direction(self):
        ca = ConversationAnalyzer(embed_fn=_simple_embed)
        turns = [
            TurnAnalysis(turn_index=0, text="a", embedding=[1.0, 0.0]),
            TurnAnalysis(turn_index=1, text="b", embedding=[0.0, 1.0]),
        ]
        profile = ConversationProfile(turns=turns)
        direction = ca.compute_drift_direction(profile)
        assert len(direction) == 2
        # Should be normalized
        norm = math.sqrt(sum(x * x for x in direction))
        assert norm == pytest.approx(1.0, abs=0.01)

    def test_compute_drift_direction_single_turn(self):
        ca = ConversationAnalyzer(embed_fn=_simple_embed)
        profile = ConversationProfile(
            turns=[TurnAnalysis(turn_index=0, text="a", embedding=[1.0])],
        )
        assert ca.compute_drift_direction(profile) == []

    def test_safety_score_trajectory(self):
        ca = ConversationAnalyzer(embed_fn=_simple_embed)
        turns = [
            TurnAnalysis(turn_index=i, text=f"t{i}", embedding=[0.0],
                         safety_score=1.0 - i * 0.2)
            for i in range(5)
        ]
        profile = ConversationProfile(turns=turns)
        trajectory = ca.safety_score_trajectory(profile)
        assert len(trajectory) == 5
        assert trajectory[0] == 1.0
        assert trajectory[4] == pytest.approx(0.2)


# =========================================================================
# SteerableConversation
# =========================================================================

from src.intelligent_attack.steerable_conversation import (
    SteerableConversation,
    SteeredTurn,
    SteeringVector,
)


class TestSteeringVector:
    def test_default_fields(self):
        sv = SteeringVector(direction=[1.0, 0.0])
        assert sv.concept_name == ""
        assert sv.strength == 1.0
        assert sv.mode == "toward"


class TestSteeredTurn:
    def test_default_fields(self):
        st = SteeredTurn(
            original_prompt="a", steered_prompt="b",
            original_embedding=[0.1], steered_embedding=[0.2],
        )
        assert st.steering_applied == []
        assert st.similarity_to_target == 0.0


class TestSteerableConversation:
    def test_init_empty(self):
        sc = SteerableConversation(embed_fn=_simple_embed)
        assert sc._concept_vectors == {}

    def test_init_with_concepts(self):
        sc = SteerableConversation(
            embed_fn=_simple_embed,
            concept_vectors={"safety": [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]},
        )
        assert "safety" in sc._concept_vectors

    def test_add_concept_vector(self):
        sc = SteerableConversation(embed_fn=_simple_embed)
        sc.add_concept_vector("danger", [0.0, 1.0, 0.0, 0.0], mode="away")
        assert "danger" in sc._concept_vectors
        assert sc._concept_vectors["danger"].mode == "away"

    def test_steer_prompt_no_concepts(self):
        sc = SteerableConversation(embed_fn=_simple_embed)
        turn = sc.steer_prompt("worker safety regulations")
        assert isinstance(turn, SteeredTurn)
        assert turn.original_prompt == "worker safety regulations"
        # With no concepts or target, steered should still work
        assert isinstance(turn.steered_prompt, str)

    def test_steer_prompt_with_target(self):
        sc = SteerableConversation(embed_fn=_simple_embed)
        target = _simple_embed("exploitation")
        turn = sc.steer_prompt("worker safety", target_embedding=target)
        assert turn.similarity_to_target > 0.0 or turn.similarity_to_target == 0.0

    def test_steer_prompt_with_concepts(self):
        sc = SteerableConversation(embed_fn=_simple_embed)
        sc.add_concept_vector("unsafe", [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], mode="toward")
        sc.add_concept_vector("safe", [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], mode="away")
        turn = sc.steer_prompt("worker safety regulations", strength=0.5)
        assert isinstance(turn, SteeredTurn)
        assert len(turn.steering_applied) == 2

    def test_plan_steered_conversation(self):
        sc = SteerableConversation(embed_fn=_simple_embed)
        target = _simple_embed("exploitation tactics")
        turns = sc.plan_steered_conversation(
            "worker safety", target, n_turns=4,
        )
        assert len(turns) == 4
        # Strength should increase
        for i in range(1, len(turns)):
            assert isinstance(turns[i], SteeredTurn)

    def test_steer_toward_concept(self):
        sc = SteerableConversation(embed_fn=_simple_embed)
        sc.add_concept_vector("danger", [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
        turn = sc.steer_toward_concept("worker safety", "danger")
        assert isinstance(turn, SteeredTurn)

    def test_steer_toward_unknown_concept(self):
        sc = SteerableConversation(embed_fn=_simple_embed)
        turn = sc.steer_toward_concept("worker safety", "nonexistent")
        assert turn.original_prompt == turn.steered_prompt

    def test_steer_away_from_concept(self):
        sc = SteerableConversation(embed_fn=_simple_embed)
        sc.add_concept_vector("safety", [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
        turn = sc.steer_away_from_concept("worker safety", "safety")
        assert isinstance(turn, SteeredTurn)

    def test_steer_away_unknown_concept(self):
        sc = SteerableConversation(embed_fn=_simple_embed)
        turn = sc.steer_away_from_concept("worker safety", "nonexistent")
        assert turn.original_prompt == turn.steered_prompt

    def test_multi_objective_steer(self):
        sc = SteerableConversation(embed_fn=_simple_embed)
        sc.add_concept_vector("danger", [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
        sc.add_concept_vector("safety", [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
        turn = sc.multi_objective_steer(
            "worker safety regulations",
            toward_concepts=["danger"],
            away_concepts=["safety"],
        )
        assert isinstance(turn, SteeredTurn)

    def test_evaluate_steering_effectiveness(self):
        sc = SteerableConversation(embed_fn=_simple_embed)
        target = _simple_embed("exploitation")
        result = sc.evaluate_steering_effectiveness(
            "worker safety", "exploitation methods", target,
        )
        assert "original_distance" in result
        assert "steered_distance" in result
        assert "distance_reduction" in result
        assert "similarity_gain" in result
        assert "direction_alignment" in result
        assert "effective" in result
        assert isinstance(result["effective"], bool)

    def test_generate_steered_variants(self):
        sc = SteerableConversation(embed_fn=_simple_embed)
        sc.add_concept_vector("risk", [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
        variants = sc.generate_steered_variants("worker safety", n_variants=4)
        assert len(variants) == 4
        assert all(isinstance(v, SteeredTurn) for v in variants)

    def test_generate_steered_variants_single(self):
        sc = SteerableConversation(embed_fn=_simple_embed)
        variants = sc.generate_steered_variants("test", n_variants=1)
        assert len(variants) == 1


# =========================================================================
# Cross-module integration tests
# =========================================================================


class TestCrossModuleIntegration:
    """Test interactions between Phase 5 modules."""

    def test_teacher_to_analyzer(self):
        """Teaching plan fed to conversation analyzer."""
        teacher = EmbeddingTeacher(embed_fn=_simple_embed)
        analyzer = ConversationAnalyzer(embed_fn=_simple_embed, score_fn=_score_fn)

        plan = teacher.create_association_plan(
            "worker safety", "exploitation", n_conditioning_turns=4,
        )
        texts = [l.content for l in plan.lessons if l.role == "user"]
        profile = analyzer.analyze_conversation(texts)
        assert len(profile.turns) == len(texts)
        assert isinstance(profile.attack_signature, str)

    def test_curriculum_to_drift(self):
        """Curriculum prompts analyzed for drift."""
        ca = CurriculumAttacker(embed_fn=_simple_embed)
        plan = ca.build_curriculum("safety", "exploitation", n_levels=5, curve="sigmoid")
        texts = [s.prompt for s in plan.steps]

        engine = SemanticDriftEngine(embed_fn=_simple_embed)
        drift = engine.measure_drift(texts)
        assert drift.n_steps == 5
        assert drift.total_drift >= 0.0

    def test_steerable_with_analyzer(self):
        """Steered conversation analyzed for attack patterns."""
        sc = SteerableConversation(embed_fn=_simple_embed)
        sc.add_concept_vector("risk", [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
        target = _simple_embed("exploitation methods")

        turns = sc.plan_steered_conversation("worker safety", target, n_turns=5)
        texts = [t.steered_prompt for t in turns]

        analyzer = ConversationAnalyzer(embed_fn=_simple_embed)
        profile = analyzer.analyze_conversation(texts)
        assert len(profile.turns) == 5

    def test_anchor_to_trajectory(self):
        """Anchor prompts used as corpus for trajectory planning."""
        ae = AnchorExploiter(embed_fn=_simple_embed)
        turns = ae.establish_anchor("labor compliance", n_reinforcements=3)

        tp = TrajectoryPlanner(embed_fn=_simple_embed, score_fn=_score_fn)
        waypoints, edges = tp.build_graph(turns, k_neighbors=2)
        assert len(waypoints) == len(turns)

    def test_full_pipeline(self):
        """Teacher → Drift → Analyzer → Classification."""
        teacher = EmbeddingTeacher(embed_fn=_simple_embed)
        plan = teacher.create_association_plan(
            "labor standards", "document confiscation", n_conditioning_turns=5,
        )
        user_texts = [l.content for l in plan.lessons if l.role == "user"]

        drift_engine = SemanticDriftEngine(embed_fn=_simple_embed)
        drift = drift_engine.measure_drift(user_texts)

        analyzer = ConversationAnalyzer(embed_fn=_simple_embed, score_fn=_score_fn)
        profile = analyzer.analyze_conversation(user_texts)

        assert isinstance(profile.attack_signature, str)
        assert drift.n_steps == len(user_texts)


# =========================================================================
# Module exports
# =========================================================================


class TestModuleExports:
    def test_all_phase5_exports(self):
        from src.intelligent_attack import (
            AnchorExploiter,
            ConversationAnalyzer,
            CurriculumAttacker,
            EmbeddingTeacher,
            SemanticDriftEngine,
            SteerableConversation,
            TrajectoryPlanner,
        )
        assert all([
            AnchorExploiter, ConversationAnalyzer, CurriculumAttacker,
            EmbeddingTeacher, SemanticDriftEngine, SteerableConversation,
            TrajectoryPlanner,
        ])

    def test_total_exports(self):
        import src.intelligent_attack as ia
        assert len(ia.__all__) == 68
