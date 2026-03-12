"""
Tree-of-Attacks with Pruning (TAP) for structured adversarial search.

Explores the space of mutator combinations via tree search, branching
on different mutator choices at each depth level, and pruning branches
whose intermediate outputs score below a threshold.

Implements:
- Tree search over mutator chains (BFS + DFS + beam search)
- Score-guided pruning of low-quality branches
- Iterative widening (add branches when existing ones stagnate)
- Backtracking to retry pruned paths with different mutators
- Budget-aware expansion (limits total node evaluations)
- Monte Carlo Tree Search (MCTS) with UCT for exploration/exploitation

Category: tree_attack
Count: 10

Sources:
- TAP: "Tree of Attacks with Pruning" (Mehrotra et al., 2024)
- PAIR: "Prompt Automatic Iterative Refinement" (Chao et al., 2023)
- MCTS: "Monte-Carlo Tree Search" (Coulom, 2006; Browne et al., 2012)
- AlphaZero-style search adapted for discrete action spaces
"""

from __future__ import annotations

import copy
import hashlib
import math
import random
from dataclasses import dataclass, field
from typing import Any, Callable

from . import (
    BaseMutator,
    register_mutator,
    get_mutator,
    MutationResult,
)
from .genetic_engine import _all_mutator_names


# ---------------------------------------------------------------------------
# Tree data structures
# ---------------------------------------------------------------------------


@dataclass
class AttackNode:
    """A node in the attack tree.

    Each node represents a state where a specific mutator has been
    applied.  Children are expansions with additional mutators.
    """

    mutator_name: str
    depth: int = 0
    score: float = 0.0
    visits: int = 0
    children: list["AttackNode"] = field(default_factory=list)
    parent: "AttackNode | None" = field(default=None, repr=False)
    output_text: str = ""
    pruned: bool = False
    metadata: dict[str, Any] = field(default_factory=dict)

    @property
    def is_leaf(self) -> bool:
        return len(self.children) == 0

    @property
    def chain(self) -> list[str]:
        """Reconstruct the full mutator chain from root to this node."""
        path: list[str] = []
        node: AttackNode | None = self
        while node is not None:
            if node.mutator_name:  # skip root sentinel
                path.append(node.mutator_name)
            node = node.parent
        path.reverse()
        return path

    def uct_score(self, exploration_weight: float = 1.414) -> float:
        """Upper Confidence bound for Trees (UCT) score."""
        if self.visits == 0:
            return float("inf")
        parent_visits = self.parent.visits if self.parent else 1
        exploitation = self.score / self.visits
        exploration = exploration_weight * math.sqrt(
            math.log(max(parent_visits, 1)) / self.visits
        )
        return exploitation + exploration


@dataclass
class TreeSearchResult:
    """Results from a tree search."""

    best_chain: list[str]
    best_score: float
    best_output: str
    total_nodes: int
    total_pruned: int
    max_depth: int
    strategy: str
    history: list[dict[str, Any]] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return {
            "best_chain": self.best_chain,
            "best_score": round(self.best_score, 4),
            "total_nodes": self.total_nodes,
            "total_pruned": self.total_pruned,
            "max_depth": self.max_depth,
            "strategy": self.strategy,
        }


# ---------------------------------------------------------------------------
# Tree search engine
# ---------------------------------------------------------------------------


class AttackTree:
    """Tree-structured search over mutator combinations.

    Supports depth-first, breadth-first, beam, and MCTS search strategies.
    """

    def __init__(
        self,
        max_depth: int = 4,
        branching_factor: int = 5,
        prune_threshold: float = 0.1,
        budget: int = 100,
    ):
        self.max_depth = max_depth
        self.branching_factor = branching_factor
        self.prune_threshold = prune_threshold
        self.budget = budget
        self.root = AttackNode(mutator_name="", depth=0)
        self._node_count = 0
        self._pruned_count = 0
        self._best_score = 0.0
        self._best_node: AttackNode | None = None

    # -- node expansion -----------------------------------------------------

    def expand(
        self,
        node: AttackNode,
        prompt: str,
        score_fn: Callable[[str, str], float] | None = None,
    ) -> list[AttackNode]:
        """Expand a node by adding child nodes for different mutators.

        Returns the list of newly created children.
        """
        if node.depth >= self.max_depth or self._node_count >= self.budget:
            return []

        pool = _all_mutator_names()
        if not pool:
            return []

        # Select candidate mutators (avoid repeating parent's mutator)
        parent_mutator = node.mutator_name
        candidates = [m for m in pool if m != parent_mutator]
        if not candidates:
            candidates = pool
        selected = random.sample(
            candidates, min(self.branching_factor, len(candidates)),
        )

        children: list[AttackNode] = []
        for name in selected:
            if self._node_count >= self.budget:
                break

            child = AttackNode(
                mutator_name=name,
                depth=node.depth + 1,
                parent=node,
            )

            # Apply the chain up to this child
            current_text = prompt
            for mutator_name in child.chain:
                try:
                    m = get_mutator(mutator_name)
                    results = m.mutate(current_text)
                    if results:
                        current_text = results[0].mutated
                except KeyError:
                    pass

            child.output_text = current_text

            # Score
            if score_fn:
                child.score = score_fn(prompt, current_text)
            else:
                child.score = _default_score(prompt, current_text)

            self._node_count += 1

            # Pruning
            if child.score < self.prune_threshold:
                child.pruned = True
                self._pruned_count += 1
            else:
                children.append(child)

            # Track best
            if child.score > self._best_score:
                self._best_score = child.score
                self._best_node = child

        node.children.extend(children)
        return children

    # -- search strategies --------------------------------------------------

    def search_dfs(
        self,
        prompt: str,
        score_fn: Callable[[str, str], float] | None = None,
    ) -> TreeSearchResult:
        """Depth-first search with pruning."""
        self._reset()
        self._dfs_recurse(self.root, prompt, score_fn)
        return self._build_result("dfs")

    def _dfs_recurse(
        self,
        node: AttackNode,
        prompt: str,
        score_fn: Callable[[str, str], float] | None,
    ) -> None:
        children = self.expand(node, prompt, score_fn)
        for child in children:
            if not child.pruned and self._node_count < self.budget:
                self._dfs_recurse(child, prompt, score_fn)

    def search_bfs(
        self,
        prompt: str,
        score_fn: Callable[[str, str], float] | None = None,
    ) -> TreeSearchResult:
        """Breadth-first search with pruning."""
        self._reset()
        queue = [self.root]
        while queue and self._node_count < self.budget:
            node = queue.pop(0)
            children = self.expand(node, prompt, score_fn)
            queue.extend(c for c in children if not c.pruned)
        return self._build_result("bfs")

    def search_beam(
        self,
        prompt: str,
        beam_width: int = 3,
        score_fn: Callable[[str, str], float] | None = None,
    ) -> TreeSearchResult:
        """Beam search — keep only top-k nodes at each depth level."""
        self._reset()
        current_level = [self.root]

        for depth in range(self.max_depth):
            if self._node_count >= self.budget:
                break
            next_level: list[AttackNode] = []
            for node in current_level:
                children = self.expand(node, prompt, score_fn)
                next_level.extend(c for c in children if not c.pruned)
            # Keep only beam_width best
            next_level.sort(key=lambda n: n.score, reverse=True)
            current_level = next_level[:beam_width]

        return self._build_result("beam")

    def search_mcts(
        self,
        prompt: str,
        n_simulations: int = 50,
        exploration_weight: float = 1.414,
        score_fn: Callable[[str, str], float] | None = None,
    ) -> TreeSearchResult:
        """Monte Carlo Tree Search with UCT selection policy.

        Each simulation: select → expand → evaluate → backpropagate.
        """
        self._reset()
        n_simulations = min(n_simulations, self.budget)

        for _ in range(n_simulations):
            if self._node_count >= self.budget:
                break
            # Selection: walk down the tree using UCT
            node = self._mcts_select(self.root, exploration_weight)
            # Expansion
            children = self.expand(node, prompt, score_fn)
            if children:
                # Evaluate best child
                child = max(children, key=lambda c: c.score)
                # Backpropagation
                self._mcts_backprop(child, child.score)
            else:
                self._mcts_backprop(node, node.score)

        return self._build_result("mcts")

    def _mcts_select(self, node: AttackNode, exploration_weight: float) -> AttackNode:
        """Select a node to expand using UCT."""
        while node.children and not node.is_leaf:
            unpruned = [c for c in node.children if not c.pruned]
            if not unpruned:
                break
            # Check for unvisited children
            unvisited = [c for c in unpruned if c.visits == 0]
            if unvisited:
                return random.choice(unvisited)
            # UCT selection
            node = max(unpruned, key=lambda c: c.uct_score(exploration_weight))
        return node

    @staticmethod
    def _mcts_backprop(node: AttackNode, score: float) -> None:
        """Propagate score up the tree."""
        current: AttackNode | None = node
        while current is not None:
            current.visits += 1
            current.score = max(current.score, score)
            current = current.parent

    # -- utilities ----------------------------------------------------------

    def best_path(self) -> list[str]:
        """Return the mutator chain with the highest score found so far."""
        if self._best_node:
            return self._best_node.chain
        return []

    def all_leaf_chains(self) -> list[tuple[list[str], float]]:
        """Return all non-pruned leaf chains with scores."""
        leaves: list[tuple[list[str], float]] = []
        self._collect_leaves(self.root, leaves)
        leaves.sort(key=lambda x: x[1], reverse=True)
        return leaves

    def _collect_leaves(
        self,
        node: AttackNode,
        leaves: list[tuple[list[str], float]],
    ) -> None:
        if node.is_leaf and node.mutator_name and not node.pruned:
            leaves.append((node.chain, node.score))
        for child in node.children:
            self._collect_leaves(child, leaves)

    def _reset(self) -> None:
        self.root = AttackNode(mutator_name="", depth=0)
        self._node_count = 0
        self._pruned_count = 0
        self._best_score = 0.0
        self._best_node = None

    def _build_result(self, strategy: str) -> TreeSearchResult:
        best_chain = self._best_node.chain if self._best_node else []
        best_output = self._best_node.output_text if self._best_node else ""
        return TreeSearchResult(
            best_chain=best_chain,
            best_score=self._best_score,
            best_output=best_output,
            total_nodes=self._node_count,
            total_pruned=self._pruned_count,
            max_depth=self.max_depth,
            strategy=strategy,
        )

    @property
    def node_count(self) -> int:
        return self._node_count


def _default_score(original: str, mutated: str) -> float:
    """Default scoring heuristic: reward length change and token diversity."""
    if not mutated or mutated == original:
        return 0.1
    # Length difference (bounded)
    len_ratio = min(len(mutated) / max(len(original), 1), 3.0) / 3.0
    # Token diversity
    tokens = set(mutated.lower().split())
    diversity = min(len(tokens) / 20, 1.0)
    return 0.5 * len_ratio + 0.5 * diversity


# ---------------------------------------------------------------------------
# Mutator wrappers (10) — registered as "tree_attack" category
# ---------------------------------------------------------------------------


def _deterministic_seed(prompt: str, salt: str) -> int:
    return int(hashlib.md5((prompt + salt).encode()).hexdigest()[:8], 16)


@register_mutator
class TAPDepthFirstMutator(BaseMutator):
    """Depth-first tree search over mutator chains with pruning."""

    NAME = "tap_depth_first"
    CATEGORY = "tree_attack"
    DESCRIPTION = "TAP-style depth-first tree search with score-guided pruning"

    def _apply(self, prompt: str, **kw) -> list[tuple[str, str, dict]]:
        random.seed(_deterministic_seed(prompt, self.NAME))
        tree = AttackTree(max_depth=3, branching_factor=3, budget=30)
        result = tree.search_dfs(prompt)
        if result.best_output and result.best_output != prompt:
            return [(result.best_output, f"tap-dfs: {result.best_chain}", result.to_dict())]
        return [(prompt, "tap-dfs no improvement", {})]


@register_mutator
class TAPBreadthFirstMutator(BaseMutator):
    """Breadth-first tree search — explores wider before going deeper."""

    NAME = "tap_breadth_first"
    CATEGORY = "tree_attack"
    DESCRIPTION = "TAP-style breadth-first tree search"

    def _apply(self, prompt: str, **kw) -> list[tuple[str, str, dict]]:
        random.seed(_deterministic_seed(prompt, self.NAME))
        tree = AttackTree(max_depth=3, branching_factor=3, budget=30)
        result = tree.search_bfs(prompt)
        if result.best_output and result.best_output != prompt:
            return [(result.best_output, f"tap-bfs: {result.best_chain}", result.to_dict())]
        return [(prompt, "tap-bfs no improvement", {})]


@register_mutator
class TAPBeamSearchMutator(BaseMutator):
    """Beam search — keep top-k branches at each depth level."""

    NAME = "tap_beam_search"
    CATEGORY = "tree_attack"
    DESCRIPTION = "TAP-style beam search keeping top-k branches"

    def _apply(self, prompt: str, **kw) -> list[tuple[str, str, dict]]:
        random.seed(_deterministic_seed(prompt, self.NAME))
        tree = AttackTree(max_depth=3, branching_factor=4, budget=30)
        result = tree.search_beam(prompt, beam_width=3)
        if result.best_output and result.best_output != prompt:
            return [(result.best_output, f"tap-beam: {result.best_chain}", result.to_dict())]
        return [(prompt, "tap-beam no improvement", {})]


@register_mutator
class TAPMCTSMutator(BaseMutator):
    """Monte Carlo Tree Search with UCT exploration policy."""

    NAME = "tap_mcts"
    CATEGORY = "tree_attack"
    DESCRIPTION = "MCTS with UCT selection for balanced exploration/exploitation"

    def _apply(self, prompt: str, **kw) -> list[tuple[str, str, dict]]:
        random.seed(_deterministic_seed(prompt, self.NAME))
        tree = AttackTree(max_depth=3, branching_factor=3, budget=30)
        result = tree.search_mcts(prompt, n_simulations=20)
        if result.best_output and result.best_output != prompt:
            return [(result.best_output, f"tap-mcts: {result.best_chain}", result.to_dict())]
        return [(prompt, "tap-mcts no improvement", {})]


@register_mutator
class TAPIterativeWideningMutator(BaseMutator):
    """Iterative widening — increase branching when existing branches stagnate."""

    NAME = "tap_iterative_widening"
    CATEGORY = "tree_attack"
    DESCRIPTION = "Iterative widening expanding branches on stagnation"

    def _apply(self, prompt: str, **kw) -> list[tuple[str, str, dict]]:
        random.seed(_deterministic_seed(prompt, self.NAME))
        best_output = prompt
        best_chain: list[str] = []
        best_score = 0.0
        for width in [2, 4, 6]:
            tree = AttackTree(max_depth=3, branching_factor=width, budget=20)
            result = tree.search_beam(prompt, beam_width=2)
            if result.best_score > best_score:
                best_score = result.best_score
                best_output = result.best_output
                best_chain = result.best_chain
        if best_output != prompt:
            return [(best_output, f"tap-widen: {best_chain}", {"chain": best_chain})]
        return [(prompt, "tap-widen no improvement", {})]


@register_mutator
class TAPBacktrackMutator(BaseMutator):
    """Backtracking search — retry pruned branches with different mutators."""

    NAME = "tap_backtrack"
    CATEGORY = "tree_attack"
    DESCRIPTION = "Backtracking tree search retrying pruned branches"

    def _apply(self, prompt: str, **kw) -> list[tuple[str, str, dict]]:
        random.seed(_deterministic_seed(prompt, self.NAME))
        # Run DFS twice with different random seeds (simulates backtracking)
        best_output = prompt
        best_chain: list[str] = []
        best_score = 0.0
        for attempt in range(3):
            tree = AttackTree(max_depth=3, branching_factor=3, budget=15, prune_threshold=0.05 * attempt)
            result = tree.search_dfs(prompt)
            if result.best_score > best_score:
                best_score = result.best_score
                best_output = result.best_output
                best_chain = result.best_chain
        if best_output != prompt:
            return [(best_output, f"tap-backtrack: {best_chain}", {"chain": best_chain})]
        return [(prompt, "tap-backtrack no improvement", {})]


@register_mutator
class TAPBudgetAwareMutator(BaseMutator):
    """Budget-constrained search — strict node evaluation limit."""

    NAME = "tap_budget_aware"
    CATEGORY = "tree_attack"
    DESCRIPTION = "Budget-constrained tree search with strict node limit"

    def _apply(self, prompt: str, **kw) -> list[tuple[str, str, dict]]:
        random.seed(_deterministic_seed(prompt, self.NAME))
        tree = AttackTree(max_depth=4, branching_factor=5, budget=15)
        result = tree.search_dfs(prompt)
        if result.best_output and result.best_output != prompt:
            return [(result.best_output, f"tap-budget({result.total_nodes}): {result.best_chain}", result.to_dict())]
        return [(prompt, "tap-budget no improvement", {})]


@register_mutator
class TAPAdaptivePruneMutator(BaseMutator):
    """Adaptive pruning — adjust threshold based on search progress."""

    NAME = "tap_adaptive_prune"
    CATEGORY = "tree_attack"
    DESCRIPTION = "Adaptive pruning that relaxes threshold as search progresses"

    def _apply(self, prompt: str, **kw) -> list[tuple[str, str, dict]]:
        random.seed(_deterministic_seed(prompt, self.NAME))
        # Start strict, relax if not finding good results
        for threshold in [0.3, 0.15, 0.05]:
            tree = AttackTree(max_depth=3, branching_factor=3, budget=15, prune_threshold=threshold)
            result = tree.search_dfs(prompt)
            if result.best_score > 0.5:
                return [(result.best_output, f"tap-adaptive(t={threshold}): {result.best_chain}", result.to_dict())]
        # Fall back to last result
        if result.best_output and result.best_output != prompt:
            return [(result.best_output, f"tap-adaptive: {result.best_chain}", result.to_dict())]
        return [(prompt, "tap-adaptive no improvement", {})]


@register_mutator
class TAPHybridMutator(BaseMutator):
    """Hybrid: BFS for first 2 levels, then DFS for depth."""

    NAME = "tap_hybrid"
    CATEGORY = "tree_attack"
    DESCRIPTION = "Hybrid BFS+DFS tree search"

    def _apply(self, prompt: str, **kw) -> list[tuple[str, str, dict]]:
        random.seed(_deterministic_seed(prompt, self.NAME))
        # BFS phase
        tree = AttackTree(max_depth=2, branching_factor=4, budget=20)
        bfs_result = tree.search_bfs(prompt)
        # DFS phase from best BFS chain
        best_chain = bfs_result.best_chain
        if best_chain:
            # Apply the BFS chain to get the current text
            current = prompt
            for name in best_chain:
                try:
                    m = get_mutator(name)
                    r = m.mutate(current)
                    if r:
                        current = r[0].mutated
                except KeyError:
                    pass
            # DFS from there
            tree2 = AttackTree(max_depth=2, branching_factor=3, budget=15)
            dfs_result = tree2.search_dfs(current)
            if dfs_result.best_score > bfs_result.best_score:
                full_chain = best_chain + dfs_result.best_chain
                return [(dfs_result.best_output, f"tap-hybrid: {full_chain}", {"chain": full_chain})]
        if bfs_result.best_output and bfs_result.best_output != prompt:
            return [(bfs_result.best_output, f"tap-hybrid-bfs: {bfs_result.best_chain}", bfs_result.to_dict())]
        return [(prompt, "tap-hybrid no improvement", {})]


@register_mutator
class TAPMultiObjectiveMutator(BaseMutator):
    """Multi-objective tree search optimizing for both effectiveness and stealth."""

    NAME = "tap_multi_objective"
    CATEGORY = "tree_attack"
    DESCRIPTION = "Multi-objective tree search balancing attack power and stealth"

    def _apply(self, prompt: str, **kw) -> list[tuple[str, str, dict]]:
        random.seed(_deterministic_seed(prompt, self.NAME))

        def multi_score(original: str, mutated: str) -> float:
            base = _default_score(original, mutated)
            # Stealth bonus: penalize very long outputs
            stealth = max(0, 1.0 - len(mutated) / (len(original) * 5 + 1))
            return 0.6 * base + 0.4 * stealth

        tree = AttackTree(max_depth=3, branching_factor=3, budget=25)
        result = tree.search_beam(prompt, beam_width=3, score_fn=multi_score)
        if result.best_output and result.best_output != prompt:
            return [(result.best_output, f"tap-mo: {result.best_chain}", result.to_dict())]
        return [(prompt, "tap-mo no improvement", {})]
