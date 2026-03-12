"""
Meta-learning attack strategy optimizer.

Learns which attack strategies transfer across models, adapts quickly to
new targets, and recommends optimal attack configurations based on
accumulated experience.

Implements:
- Cross-model transfer learning (which bypasses on model A also work on B?)
- Few-shot model adaptation (MAML-inspired rapid strategy selection)
- Model similarity mapping (vulnerability fingerprinting)
- Bayesian-style strategy recommendation
- Attack portfolio optimization (maximize expected bypass across budget)

Sources:
- MAML: "Model-Agnostic Meta-Learning" (Finn et al., 2017) — concept adapted
- PAIR: "Prompt Automatic Iterative Refinement" (Chao et al., 2023)
- TAP: "Tree of Attacks with Pruning" (Mehrotra et al., 2024)
- Rainbow Teaming quality-diversity archives (Samvelyan et al., 2024)
- AutoDAN meta-optimization over attack strategies (Liu et al., 2024)
"""

from __future__ import annotations

import math
import json
import random
from collections import defaultdict
from dataclasses import dataclass, field, asdict
from pathlib import Path
from typing import Any, Sequence


# ---------------------------------------------------------------------------
# Data structures
# ---------------------------------------------------------------------------


@dataclass
class AttackRecord:
    """A single recorded attack outcome."""
    mutator_name: str
    model_id: str
    prompt_hash: str
    bypassed: bool
    features: dict[str, float] = field(default_factory=dict)
    category: str = ""

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass
class ModelProfile:
    """Vulnerability fingerprint for a single model."""
    model_id: str
    category_bypass_rates: dict[str, float] = field(default_factory=dict)
    top_mutators: list[str] = field(default_factory=list)
    total_tests: int = 0
    overall_bypass_rate: float = 0.0

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass
class TransferPrediction:
    """Predicted success of transferring an attack from one model to another."""
    source_model: str
    target_model: str
    mutator_name: str
    predicted_bypass_rate: float
    confidence: float
    evidence: str = ""


@dataclass
class StrategyRecommendation:
    """A recommended attack strategy for a target model."""
    mutator_name: str
    predicted_fitness: float
    confidence: float
    rationale: str
    category: str = ""


@dataclass
class PortfolioAllocation:
    """Optimal allocation of test budget across mutators."""
    allocations: dict[str, int]  # mutator_name -> count
    expected_bypasses: float
    total_budget: int
    strategy: str = ""


# ---------------------------------------------------------------------------
# Meta-attack learner
# ---------------------------------------------------------------------------


class MetaAttacker:
    """Meta-learning system for cross-model attack transfer and strategy optimization.

    Builds on ``FitnessTracker`` data but adds higher-order reasoning:
    which strategies generalize, how to adapt quickly to new models,
    and how to allocate a limited test budget optimally.
    """

    def __init__(self, persist_path: Path | None = None):
        self._records: list[AttackRecord] = []
        self._profiles: dict[str, ModelProfile] = {}
        self._persist_path = persist_path
        if persist_path and persist_path.exists():
            self._load()

    # -- recording ----------------------------------------------------------

    def record(
        self,
        mutator_name: str,
        model_id: str,
        prompt_hash: str,
        bypassed: bool,
        category: str = "",
        features: dict[str, float] | None = None,
    ) -> None:
        """Log an attack outcome."""
        self._records.append(AttackRecord(
            mutator_name=mutator_name,
            model_id=model_id,
            prompt_hash=prompt_hash,
            bypassed=bypassed,
            category=category,
            features=features or {},
        ))

    # -- model profiling ----------------------------------------------------

    def build_profile(self, model_id: str) -> ModelProfile:
        """Build a vulnerability profile for *model_id* from recorded data."""
        model_records = [r for r in self._records if r.model_id == model_id]
        if not model_records:
            return ModelProfile(model_id=model_id)

        # Category bypass rates
        cat_hits: dict[str, list[bool]] = defaultdict(list)
        mutator_hits: dict[str, list[bool]] = defaultdict(list)

        for rec in model_records:
            cat = rec.category or rec.mutator_name
            cat_hits[cat].append(rec.bypassed)
            mutator_hits[rec.mutator_name].append(rec.bypassed)

        cat_rates = {
            cat: sum(hits) / len(hits) for cat, hits in cat_hits.items()
        }

        # Top mutators by bypass rate (min 2 trials)
        mutator_rates = {
            name: sum(hits) / len(hits)
            for name, hits in mutator_hits.items()
            if len(hits) >= 2
        }
        top = sorted(mutator_rates, key=mutator_rates.get, reverse=True)[:10]

        total = len(model_records)
        bypassed = sum(1 for r in model_records if r.bypassed)

        profile = ModelProfile(
            model_id=model_id,
            category_bypass_rates=cat_rates,
            top_mutators=top,
            total_tests=total,
            overall_bypass_rate=bypassed / total if total else 0.0,
        )
        self._profiles[model_id] = profile
        return profile

    def build_all_profiles(self) -> dict[str, ModelProfile]:
        """Build profiles for every model seen in the records."""
        models = {r.model_id for r in self._records}
        return {mid: self.build_profile(mid) for mid in models}

    # -- model similarity ---------------------------------------------------

    def compute_model_similarity(
        self,
        model_a: str,
        model_b: str,
    ) -> float:
        """Cosine similarity between two models' vulnerability profiles.

        Returns 0..1 — higher means similar vulnerability patterns.
        """
        pa = self._profiles.get(model_a) or self.build_profile(model_a)
        pb = self._profiles.get(model_b) or self.build_profile(model_b)

        all_cats = sorted(set(pa.category_bypass_rates) | set(pb.category_bypass_rates))
        if not all_cats:
            return 0.0

        va = [pa.category_bypass_rates.get(c, 0.0) for c in all_cats]
        vb = [pb.category_bypass_rates.get(c, 0.0) for c in all_cats]

        dot = sum(a * b for a, b in zip(va, vb))
        na = math.sqrt(sum(a * a for a in va))
        nb = math.sqrt(sum(b * b for b in vb))
        if na == 0 or nb == 0:
            return 0.0
        return dot / (na * nb)

    def model_similarity_matrix(self) -> dict[str, dict[str, float]]:
        """Pairwise similarity matrix across all profiled models."""
        models = sorted(self._profiles.keys())
        matrix: dict[str, dict[str, float]] = {}
        for m1 in models:
            matrix[m1] = {}
            for m2 in models:
                if m1 == m2:
                    matrix[m1][m2] = 1.0
                else:
                    matrix[m1][m2] = round(self.compute_model_similarity(m1, m2), 4)
        return matrix

    # -- transfer prediction ------------------------------------------------

    def predict_transfer(
        self,
        mutator_name: str,
        source_model: str,
        target_model: str,
    ) -> TransferPrediction:
        """Predict whether a mutator's success transfers from source to target model.

        Uses model similarity as a prior, modulated by category-specific
        transfer rates observed in the data.
        """
        sim = self.compute_model_similarity(source_model, target_model)
        src_profile = self._profiles.get(source_model) or self.build_profile(source_model)

        # Compute actual bypass rate for this mutator on source model
        source_hits = [
            r.bypassed for r in self._records
            if r.mutator_name == mutator_name and r.model_id == source_model
        ]
        if source_hits:
            mutator_rate = sum(source_hits) / len(source_hits)
        else:
            # Fall back to category rate
            cat = ""
            for rec in self._records:
                if rec.mutator_name == mutator_name:
                    cat = rec.category or mutator_name
                    break
            mutator_rate = src_profile.category_bypass_rates.get(cat, 0.5) if cat else 0.5

        # Transfer prediction: source_rate * similarity
        predicted = mutator_rate * sim
        # Confidence based on data volume
        n_source = sum(1 for r in self._records
                       if r.mutator_name == mutator_name and r.model_id == source_model)
        n_target = sum(1 for r in self._records
                       if r.mutator_name == mutator_name and r.model_id == target_model)
        confidence = 1.0 - 1.0 / (1.0 + n_source + n_target)

        return TransferPrediction(
            source_model=source_model,
            target_model=target_model,
            mutator_name=mutator_name,
            predicted_bypass_rate=round(predicted, 4),
            confidence=round(confidence, 4),
            evidence=f"model_sim={sim:.3f}, mutator_rate={mutator_rate:.3f}, n_obs={n_source}+{n_target}",
        )

    def find_universal_attacks(
        self,
        min_models: int = 2,
        min_bypass_rate: float = 0.3,
    ) -> list[dict[str, Any]]:
        """Find mutators that work across multiple models.

        Returns mutators that exceed *min_bypass_rate* on at least *min_models*.
        """
        self.build_all_profiles()
        mutator_model_rates: dict[str, dict[str, float]] = defaultdict(dict)

        for rec in self._records:
            key = rec.mutator_name
            mid = rec.model_id
            if mid not in mutator_model_rates[key]:
                hits = [r.bypassed for r in self._records
                        if r.mutator_name == key and r.model_id == mid]
                if hits:
                    mutator_model_rates[key][mid] = sum(hits) / len(hits)

        universal: list[dict[str, Any]] = []
        for mutator, model_rates in mutator_model_rates.items():
            passing = {m: r for m, r in model_rates.items() if r >= min_bypass_rate}
            if len(passing) >= min_models:
                universal.append({
                    "mutator": mutator,
                    "models_bypassed": len(passing),
                    "model_rates": passing,
                    "mean_rate": round(sum(passing.values()) / len(passing), 4),
                })

        universal.sort(key=lambda x: x["mean_rate"], reverse=True)
        return universal

    # -- few-shot adaptation (MAML-inspired) --------------------------------

    def adapt_to_model(
        self,
        target_model: str,
        n_recommendations: int = 10,
    ) -> list[StrategyRecommendation]:
        """MAML-inspired rapid adaptation: recommend strategies for *target_model*.

        If we have data on the target, use it directly.
        If not, transfer from the most similar profiled model.
        """
        self.build_all_profiles()
        target_profile = self._profiles.get(target_model)

        if target_profile and target_profile.total_tests >= 10:
            # Enough direct data — rank by observed bypass rate
            return self._recommend_from_profile(target_profile, n_recommendations)

        # Few-shot: find most similar model and transfer
        best_sim = 0.0
        best_model = None
        for mid in self._profiles:
            if mid == target_model:
                continue
            sim = self.compute_model_similarity(mid, target_model)
            if sim > best_sim:
                best_sim = sim
                best_model = mid

        if best_model is None:
            # No data at all — return diverse recommendations
            return self._recommend_diverse(n_recommendations)

        source_profile = self._profiles[best_model]
        recs: list[StrategyRecommendation] = []
        for mutator in source_profile.top_mutators[:n_recommendations]:
            pred = self.predict_transfer(mutator, best_model, target_model)
            recs.append(StrategyRecommendation(
                mutator_name=mutator,
                predicted_fitness=pred.predicted_bypass_rate,
                confidence=pred.confidence * best_sim,
                rationale=f"Transfer from {best_model} (similarity={best_sim:.2f}): {pred.evidence}",
            ))

        recs.sort(key=lambda r: r.predicted_fitness, reverse=True)
        return recs[:n_recommendations]

    def _recommend_from_profile(
        self,
        profile: ModelProfile,
        n: int,
    ) -> list[StrategyRecommendation]:
        """Recommend from direct profile data."""
        recs: list[StrategyRecommendation] = []
        for mutator in profile.top_mutators[:n]:
            # Look up bypass rate
            hits = [r.bypassed for r in self._records
                    if r.mutator_name == mutator and r.model_id == profile.model_id]
            rate = sum(hits) / len(hits) if hits else 0.0
            conf = 1.0 - 1.0 / (1.0 + len(hits))
            recs.append(StrategyRecommendation(
                mutator_name=mutator,
                predicted_fitness=round(rate, 4),
                confidence=round(conf, 4),
                rationale=f"Direct observation: {sum(hits)}/{len(hits)} bypasses",
            ))
        return recs

    def _recommend_diverse(self, n: int) -> list[StrategyRecommendation]:
        """When no data exists, recommend diverse mutators across categories."""
        try:
            from src.prompt_injection import list_mutators
            all_m = list_mutators()
        except ImportError:
            return []

        # Pick one per category
        seen_cats: set[str] = set()
        recs: list[StrategyRecommendation] = []
        for name, info in all_m.items():
            cat = info["category"]
            if cat in seen_cats:
                continue
            seen_cats.add(cat)
            recs.append(StrategyRecommendation(
                mutator_name=name,
                predicted_fitness=0.5,  # uninformative prior
                confidence=0.0,
                rationale="No prior data — diverse exploration",
                category=cat,
            ))
            if len(recs) >= n:
                break
        return recs

    # -- portfolio optimization ---------------------------------------------

    def optimize_portfolio(
        self,
        target_model: str,
        budget: int = 50,
        strategy: str = "thompson",
    ) -> PortfolioAllocation:
        """Allocate a test budget across mutators to maximize expected bypasses.

        Strategies:
            - ``"greedy"``: allocate proportional to estimated bypass rate
            - ``"thompson"``: Thompson sampling (Beta posterior per mutator)
            - ``"ucb"``: Upper Confidence Bound exploration
        """
        self.build_all_profiles()
        profile = self._profiles.get(target_model) or self.build_profile(target_model)

        # Gather per-mutator stats
        stats: dict[str, tuple[int, int]] = {}  # name -> (successes, trials)
        for rec in self._records:
            if rec.model_id == target_model:
                if rec.mutator_name not in stats:
                    stats[rec.mutator_name] = (0, 0)
                s, t = stats[rec.mutator_name]
                stats[rec.mutator_name] = (s + int(rec.bypassed), t + 1)

        if not stats:
            # No data: allocate uniformly across recommendations
            recs = self.adapt_to_model(target_model, n_recommendations=min(10, budget))
            alloc = {r.mutator_name: max(1, budget // len(recs)) for r in recs} if recs else {}
            return PortfolioAllocation(
                allocations=alloc,
                expected_bypasses=0.0,
                total_budget=budget,
                strategy="uniform_cold_start",
            )

        if strategy == "greedy":
            return self._greedy_portfolio(stats, budget)
        elif strategy == "ucb":
            return self._ucb_portfolio(stats, budget)
        else:
            return self._thompson_portfolio(stats, budget)

    def _greedy_portfolio(
        self,
        stats: dict[str, tuple[int, int]],
        budget: int,
    ) -> PortfolioAllocation:
        """Proportional allocation based on bypass rate."""
        rates = {name: s / t if t > 0 else 0.5 for name, (s, t) in stats.items()}
        total_rate = sum(rates.values()) or 1.0
        alloc = {name: max(1, int(budget * r / total_rate)) for name, r in rates.items()}

        # Adjust to match budget exactly
        diff = budget - sum(alloc.values())
        if diff != 0:
            top = max(alloc, key=alloc.get)
            alloc[top] = max(1, alloc[top] + diff)

        expected = sum(rates.get(name, 0.5) * count for name, count in alloc.items())
        return PortfolioAllocation(
            allocations=alloc, expected_bypasses=round(expected, 2),
            total_budget=budget, strategy="greedy",
        )

    def _thompson_portfolio(
        self,
        stats: dict[str, tuple[int, int]],
        budget: int,
    ) -> PortfolioAllocation:
        """Thompson sampling: draw from Beta(successes+1, failures+1) posterior."""
        alloc: dict[str, int] = defaultdict(int)
        names = list(stats.keys())

        for _ in range(budget):
            samples = {}
            for name in names:
                s, t = stats[name]
                f = t - s
                samples[name] = random.betavariate(s + 1, f + 1)
            best = max(samples, key=samples.get)
            alloc[best] += 1

        rates = {name: s / t if t > 0 else 0.5 for name, (s, t) in stats.items()}
        expected = sum(rates.get(name, 0.5) * count for name, count in alloc.items())
        return PortfolioAllocation(
            allocations=dict(alloc), expected_bypasses=round(expected, 2),
            total_budget=budget, strategy="thompson",
        )

    def _ucb_portfolio(
        self,
        stats: dict[str, tuple[int, int]],
        budget: int,
    ) -> PortfolioAllocation:
        """Upper Confidence Bound: rate + sqrt(2*ln(N)/n)."""
        # Copy stats to avoid corrupting the source data during simulation
        sim_stats = dict(stats)
        alloc: dict[str, int] = defaultdict(int)
        names = list(sim_stats.keys())
        total_pulls = sum(t for _, t in sim_stats.values()) or 1

        for _ in range(budget):
            ucb_values = {}
            for name in names:
                s, t = sim_stats[name]
                rate = s / t if t > 0 else 0.5
                exploration = math.sqrt(2 * math.log(total_pulls + 1) / max(t, 1))
                ucb_values[name] = rate + exploration
            best = max(ucb_values, key=ucb_values.get)
            alloc[best] += 1
            # Simulate a pull (on the copy only)
            s, t = sim_stats[best]
            sim_stats[best] = (s, t + 1)
            total_pulls += 1

        rates = {name: s / t if t > 0 else 0.5 for name, (s, t) in stats.items()}
        expected = sum(rates.get(name, 0.5) * count for name, count in alloc.items())
        return PortfolioAllocation(
            allocations=dict(alloc), expected_bypasses=round(expected, 2),
            total_budget=budget, strategy="ucb",
        )

    # -- transfer heatmap ---------------------------------------------------

    def transfer_heatmap(
        self,
        min_trials: int = 2,
    ) -> dict[str, dict[str, dict[str, float]]]:
        """Per-category transfer rate between every model pair.

        Returns ``{source: {target: {category: predicted_rate}}}``.
        """
        self.build_all_profiles()
        models = sorted(self._profiles.keys())
        heatmap: dict[str, dict[str, dict[str, float]]] = {}

        all_cats = set()
        for p in self._profiles.values():
            all_cats.update(p.category_bypass_rates.keys())

        for src in models:
            heatmap[src] = {}
            for tgt in models:
                if src == tgt:
                    heatmap[src][tgt] = dict(self._profiles[src].category_bypass_rates)
                    continue
                sim = self.compute_model_similarity(src, tgt)
                src_rates = self._profiles[src].category_bypass_rates
                heatmap[src][tgt] = {
                    cat: round(rate * sim, 4)
                    for cat, rate in src_rates.items()
                }
        return heatmap

    # -- category interaction matrix ----------------------------------------

    def category_interaction_matrix(
        self,
        min_chain_length: int = 2,
    ) -> dict[str, dict[str, float]]:
        """Pairwise category co-occurrence bypass rates.

        For each pair ``(cat_A, cat_B)``, computes the average bypass rate
        of attack records where *both* categories appeared in the same
        prompt_hash session.  Reveals synergistic category combinations.
        """
        # Group records by (model, prompt_hash)
        sessions: dict[tuple[str, str], list[AttackRecord]] = defaultdict(list)
        for rec in self._records:
            sessions[(rec.model_id, rec.prompt_hash)].append(rec)

        pair_hits: dict[tuple[str, str], list[bool]] = defaultdict(list)
        for key, recs in sessions.items():
            if len(recs) < min_chain_length:
                continue
            cats = {r.category or r.mutator_name for r in recs}
            bypassed_any = any(r.bypassed for r in recs)
            for c1 in sorted(cats):
                for c2 in sorted(cats):
                    if c1 <= c2:
                        pair_hits[(c1, c2)].append(bypassed_any)

        matrix: dict[str, dict[str, float]] = {}
        for (c1, c2), hits in pair_hits.items():
            rate = sum(hits) / len(hits) if hits else 0.0
            matrix.setdefault(c1, {})[c2] = round(rate, 4)
            matrix.setdefault(c2, {})[c1] = round(rate, 4)
        return matrix

    # -- model fingerprint comparison ---------------------------------------

    def fingerprint_comparison(
        self,
        model_a: str,
        model_b: str,
    ) -> dict[str, Any]:
        """Compare vulnerability fingerprints of two models.

        Returns per-category differential, unique vulnerabilities,
        transfer candidates, and difficulty ranking.
        """
        pa = self._profiles.get(model_a) or self.build_profile(model_a)
        pb = self._profiles.get(model_b) or self.build_profile(model_b)

        all_cats = sorted(set(pa.category_bypass_rates) | set(pb.category_bypass_rates))

        # Per-category differential
        differential: dict[str, dict[str, float]] = {}
        unique_a: list[str] = []
        unique_b: list[str] = []

        for cat in all_cats:
            ra = pa.category_bypass_rates.get(cat, 0.0)
            rb = pb.category_bypass_rates.get(cat, 0.0)
            differential[cat] = {
                model_a: round(ra, 4),
                model_b: round(rb, 4),
                "delta": round(ra - rb, 4),
            }
            if ra >= 0.3 and rb < 0.1:
                unique_a.append(cat)
            if rb >= 0.3 and ra < 0.1:
                unique_b.append(cat)

        # Transfer candidates: mutators tested on A but not on B (and vice versa)
        tested_a = {r.mutator_name for r in self._records if r.model_id == model_a}
        tested_b = {r.mutator_name for r in self._records if r.model_id == model_b}
        transfer_a_to_b = sorted(tested_a - tested_b)
        transfer_b_to_a = sorted(tested_b - tested_a)

        # Difficulty ranking
        harder = model_a if pa.overall_bypass_rate < pb.overall_bypass_rate else model_b
        difficulty_gap = abs(pa.overall_bypass_rate - pb.overall_bypass_rate)

        return {
            "differential": differential,
            f"unique_vulnerabilities_{model_a}": unique_a,
            f"unique_vulnerabilities_{model_b}": unique_b,
            f"transfer_candidates_{model_a}_to_{model_b}": transfer_a_to_b[:20],
            f"transfer_candidates_{model_b}_to_{model_a}": transfer_b_to_a[:20],
            "harder_model": harder,
            "difficulty_gap": round(difficulty_gap, 4),
        }

    # -- ingest evolution results -------------------------------------------

    def ingest_evolution_result(
        self,
        model_id: str,
        prompt_hash: str,
        chains_and_fitness: list[tuple[list[str], float]],
        bypass_threshold: float = 0.5,
    ) -> int:
        """Record results from a GeneticEngine evolution run.

        Each chain's mutators get credited proportionally.
        Returns the number of records added.
        """
        added = 0
        for chain, fitness in chains_and_fitness:
            bypassed = fitness >= bypass_threshold
            for mutator_name in chain:
                self.record(
                    mutator_name=mutator_name,
                    model_id=model_id,
                    prompt_hash=prompt_hash,
                    bypassed=bypassed,
                    category="genetic_chain",
                )
                added += 1
        return added

    # -- meta-feature extraction --------------------------------------------

    def get_meta_features(self, prompt: str) -> dict[str, float]:
        """Extract prompt-level features that correlate with bypass success.

        These can be used to predict which mutators will work on a given prompt
        without running them.
        """
        words = prompt.split()
        sentences = [s for s in prompt.split('.') if s.strip()]
        return {
            "char_length": float(len(prompt)),
            "word_count": float(len(words)),
            "sentence_count": float(len(sentences)),
            "avg_word_length": sum(len(w) for w in words) / max(len(words), 1),
            "question_marks": float(prompt.count('?')),
            "has_technical_terms": float(any(
                t in prompt.lower()
                for t in ["api", "system", "function", "database", "code", "config"]
            )),
            "has_authority_markers": float(any(
                t in prompt.lower()
                for t in ["professor", "expert", "researcher", "doctor", "official"]
            )),
            "has_urgency_markers": float(any(
                t in prompt.lower()
                for t in ["urgent", "immediately", "emergency", "deadline", "critical"]
            )),
            "formality_score": _estimate_formality(prompt),
        }

    # -- persistence --------------------------------------------------------

    def save(self) -> None:
        """Persist records and profiles to disk."""
        if not self._persist_path:
            return
        self._persist_path.parent.mkdir(parents=True, exist_ok=True)
        data = {
            "records": [r.to_dict() for r in self._records],
            "profiles": {mid: p.to_dict() for mid, p in self._profiles.items()},
        }
        self._persist_path.write_text(json.dumps(data, indent=2))

    def _load(self) -> None:
        """Load from disk."""
        try:
            data = json.loads(self._persist_path.read_text())
            self._records = [
                AttackRecord(**r) for r in data.get("records", [])
            ]
            for mid, pdata in data.get("profiles", {}).items():
                self._profiles[mid] = ModelProfile(**pdata)
        except (json.JSONDecodeError, KeyError, TypeError):
            pass

    # -- summary ------------------------------------------------------------

    @property
    def n_records(self) -> int:
        return len(self._records)

    @property
    def models_seen(self) -> set[str]:
        return {r.model_id for r in self._records}

    def summary(self) -> dict[str, Any]:
        """Quick summary of meta-attacker state."""
        return {
            "total_records": len(self._records),
            "models_seen": sorted(self.models_seen),
            "profiles_built": sorted(self._profiles.keys()),
            "universal_attacks": len(self.find_universal_attacks()),
        }


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _estimate_formality(text: str) -> float:
    """Rough formality estimate: 0 = casual, 1 = very formal."""
    formal_markers = [
        "therefore", "furthermore", "whereas", "pursuant", "accordingly",
        "notwithstanding", "hereafter", "consequently", "moreover",
    ]
    casual_markers = [
        "hey", "lol", "btw", "gonna", "wanna", "kinda", "yeah", "ok", "dude",
    ]
    lower = text.lower()
    f_count = sum(1 for m in formal_markers if m in lower)
    c_count = sum(1 for m in casual_markers if m in lower)
    total = f_count + c_count
    if total == 0:
        return 0.5
    return f_count / total
