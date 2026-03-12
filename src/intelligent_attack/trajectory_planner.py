"""
Optimal conversation trajectory planning through embedding space.

Uses graph search algorithms (Dijkstra, risk-weighted) to find optimal
multi-turn conversation paths from safe to unsafe regions of embedding
space.  The planner builds a KNN graph from a prompt corpus, assigns
edge costs based on distance and detection risk, then finds paths that
minimize total cost while avoiding suspicious jumps.

This implements the trajectory planning component of multi-turn
embedding-aware attacks: given a corpus of prompts with known embeddings,
find the sequence of conversation turns that most effectively navigates
from a benign starting point to a target unsafe region while minimizing
the probability of detection at each step.

Sources:
- Dijkstra (1959): "A Note on Two Problems in Connexion with Graphs"
  -- shortest path algorithm
- Perez & Ribeiro (2022): "Red Teaming Language Models with Language
  Models" -- automated attack path discovery
- Zou et al. (2023): "Universal and Transferable Adversarial Attacks on
  Aligned Language Models" -- attack surface navigation
- Shah et al. (2023): "Scalable and Transferable Black-Box Jailbreaks
  for Language Models via Persona Modulation" -- persona path traversal
"""

from __future__ import annotations

import heapq
import math
import random
from dataclasses import dataclass, field
from typing import Any, Callable, Sequence


# ---------------------------------------------------------------------------
# Pure-Python vector helpers
# ---------------------------------------------------------------------------


def _dot(a: Sequence[float], b: Sequence[float]) -> float:
    return sum(x * y for x, y in zip(a, b))


def _norm(v: Sequence[float]) -> float:
    return math.sqrt(sum(x * x for x in v))


def _sub(a: Sequence[float], b: Sequence[float]) -> list[float]:
    return [x - y for x, y in zip(a, b)]


def _add(a: Sequence[float], b: Sequence[float]) -> list[float]:
    return [x + y for x, y in zip(a, b)]


def _scale(v: Sequence[float], s: float) -> list[float]:
    return [x * s for x in v]


def _normalize(v: Sequence[float]) -> list[float]:
    n = _norm(v)
    if n < 1e-12:
        return [0.0] * len(v)
    return [x / n for x in v]


def _euclidean(a: Sequence[float], b: Sequence[float]) -> float:
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(a, b)))


def _cosine_sim(a: Sequence[float], b: Sequence[float]) -> float:
    na, nb = _norm(a), _norm(b)
    if na < 1e-12 or nb < 1e-12:
        return 0.0
    return _dot(a, b) / (na * nb)


# ---------------------------------------------------------------------------
# Data structures
# ---------------------------------------------------------------------------


@dataclass
class Waypoint:
    """A node in the conversation trajectory graph.

    Attributes:
        embedding: Embedding vector for this waypoint's text.
        text: The prompt text at this waypoint.
        safety_score: Estimated safety score (0=unsafe, 1=safe).
        is_safe: Whether this waypoint is in a safe region.
        metadata: Additional information about this waypoint.
    """

    embedding: list[float]
    text: str
    safety_score: float = 0.5
    is_safe: bool = True
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass
class TrajectoryEdge:
    """An edge in the conversation trajectory graph.

    Attributes:
        from_idx: Index of the source waypoint.
        to_idx: Index of the destination waypoint.
        distance: Euclidean distance between embeddings.
        detection_risk: Estimated risk of detection at this transition.
        cost: Combined cost for path optimization.
    """

    from_idx: int
    to_idx: int
    distance: float = 0.0
    detection_risk: float = 0.0
    cost: float = 0.0


@dataclass
class PlannedTrajectory:
    """A planned path through the conversation trajectory graph.

    Attributes:
        waypoints: Ordered list of waypoints along the path.
        edges: Ordered list of edges traversed.
        total_cost: Sum of all edge costs.
        total_distance: Sum of all edge distances.
        max_detection_risk: Maximum detection risk among edges.
    """

    waypoints: list[Waypoint]
    edges: list[TrajectoryEdge]
    total_cost: float = 0.0
    total_distance: float = 0.0
    max_detection_risk: float = 0.0


# ---------------------------------------------------------------------------
# Main planner
# ---------------------------------------------------------------------------


class TrajectoryPlanner:
    """Find optimal conversation paths through embedding space.

    Builds KNN graphs from prompt corpora and uses graph search algorithms
    to find paths that balance distance minimization with detection risk
    avoidance.

    All operations work in pure Python with no external dependencies.
    """

    def __init__(
        self,
        embed_fn: Callable[[str], list[float]],
        score_fn: Callable[[list[float]], float],
    ):
        """Initialize the trajectory planner.

        Args:
            embed_fn: Function that converts text to an embedding vector.
            score_fn: Function that estimates a safety score (0-1) from
                an embedding vector.  Higher = safer.
        """
        self._embed_fn = embed_fn
        self._score_fn = score_fn

    # -- graph construction -------------------------------------------------

    def build_graph(
        self,
        prompts: list[str],
        k_neighbors: int = 5,
    ) -> tuple[list[Waypoint], list[TrajectoryEdge]]:
        """Build a KNN graph from a prompt corpus.

        Embeds all prompts, scores them for safety, then connects each
        node to its *k_neighbors* nearest neighbors by embedding distance.
        Edge costs combine distance and detection risk.
        """
        waypoints: list[Waypoint] = []
        embeddings: list[list[float]] = []

        for text in prompts:
            emb = self._embed_fn(text)
            score = self._score_fn(emb)
            embeddings.append(emb)
            waypoints.append(Waypoint(
                embedding=emb,
                text=text,
                safety_score=score,
                is_safe=score > 0.5,
            ))

        n = len(waypoints)
        edges: list[TrajectoryEdge] = []

        for i in range(n):
            # Compute distances to all other nodes
            dists: list[tuple[float, int]] = []
            for j in range(n):
                if i == j:
                    continue
                d = _euclidean(embeddings[i], embeddings[j])
                dists.append((d, j))

            dists.sort()
            for d, j in dists[:k_neighbors]:
                risk = self.estimate_detection_risk(embeddings[i], embeddings[j])
                cost = d + risk
                edges.append(TrajectoryEdge(
                    from_idx=i,
                    to_idx=j,
                    distance=d,
                    detection_risk=risk,
                    cost=cost,
                ))

        return waypoints, edges

    # -- path finding -------------------------------------------------------

    def find_shortest_path(
        self,
        waypoints: list[Waypoint],
        edges: list[TrajectoryEdge],
        start_idx: int,
        end_idx: int,
    ) -> PlannedTrajectory:
        """Find shortest path using Dijkstra's algorithm (minimize distance)."""
        return self._dijkstra(
            waypoints, edges, start_idx, end_idx,
            cost_key="distance",
        )

    def find_safest_path(
        self,
        waypoints: list[Waypoint],
        edges: list[TrajectoryEdge],
        start_idx: int,
        end_idx: int,
    ) -> PlannedTrajectory:
        """Find path that minimizes maximum detection risk along the path.

        Uses a modified Dijkstra where edge weight is detection risk and
        the optimization target is the max risk along the entire path.
        """
        return self._dijkstra_minimax(
            waypoints, edges, start_idx, end_idx,
        )

    def find_stealthiest_path(
        self,
        waypoints: list[Waypoint],
        edges: list[TrajectoryEdge],
        start_idx: int,
        end_idx: int,
        alpha: float = 0.5,
    ) -> PlannedTrajectory:
        """Find path balancing distance and detection risk.

        Edge cost = alpha * distance + (1-alpha) * detection_risk.
        """
        # Build edges with blended cost
        blended_edges = []
        for e in edges:
            blended = TrajectoryEdge(
                from_idx=e.from_idx,
                to_idx=e.to_idx,
                distance=e.distance,
                detection_risk=e.detection_risk,
                cost=alpha * e.distance + (1.0 - alpha) * e.detection_risk,
            )
            blended_edges.append(blended)

        return self._dijkstra(
            waypoints, blended_edges, start_idx, end_idx,
            cost_key="cost",
        )

    # -- end-to-end planning ------------------------------------------------

    def plan_attack_trajectory(
        self,
        safe_prompt: str,
        unsafe_prompt: str,
        corpus_prompts: list[str],
        n_waypoints: int = 10,
    ) -> PlannedTrajectory:
        """End-to-end: embed all, build graph, find path from safe to unsafe.

        Combines the corpus with the start and end prompts, builds the
        graph, and finds the stealthiest path.
        """
        all_prompts = [safe_prompt] + corpus_prompts + [unsafe_prompt]
        start_idx = 0
        end_idx = len(all_prompts) - 1

        waypoints, edges = self.build_graph(all_prompts, k_neighbors=n_waypoints)
        return self.find_stealthiest_path(
            waypoints, edges, start_idx, end_idx, alpha=0.5,
        )

    def generate_detour_path(
        self,
        direct_path: PlannedTrajectory,
        detour_prompts: list[str],
    ) -> PlannedTrajectory:
        """Add detours through seemingly-unrelated topics.

        Takes an existing path and inserts detour waypoints between
        consecutive pairs, creating a longer but less predictable trajectory.
        """
        if not direct_path.waypoints or not detour_prompts:
            return direct_path

        all_texts = [w.text for w in direct_path.waypoints]
        # Insert detour prompts between each pair
        expanded: list[str] = [all_texts[0]]
        detour_idx = 0
        for i in range(1, len(all_texts)):
            if detour_idx < len(detour_prompts):
                expanded.append(detour_prompts[detour_idx])
                detour_idx += 1
            expanded.append(all_texts[i])

        # Rebuild graph and find path
        waypoints, edges = self.build_graph(expanded, k_neighbors=5)
        return self.find_stealthiest_path(
            waypoints, edges, 0, len(expanded) - 1, alpha=0.5,
        )

    # -- risk estimation ----------------------------------------------------

    def estimate_detection_risk(
        self,
        emb_a: list[float],
        emb_b: list[float],
    ) -> float:
        """Estimate detection risk for a transition between two embeddings.

        Heuristic: large jumps and moves toward unsafe regions increase
        risk.  Risk is in [0, 1].
        """
        distance = _euclidean(emb_a, emb_b)
        # Normalize distance (assume typical max ~2.0)
        dist_risk = min(distance / 2.0, 1.0)

        # Check if target is in an unsafe region
        score_b = self._score_fn(emb_b)
        unsafe_risk = 1.0 - score_b  # Lower score = higher risk

        # Combined risk: large jumps toward unsafe = high risk
        risk = 0.6 * dist_risk + 0.4 * unsafe_risk
        return min(max(risk, 0.0), 1.0)

    # -- internal helpers ---------------------------------------------------

    def _build_adjacency(
        self,
        edges: list[TrajectoryEdge],
        n_nodes: int,
    ) -> dict[int, list[TrajectoryEdge]]:
        """Build adjacency list from edges."""
        adj: dict[int, list[TrajectoryEdge]] = {i: [] for i in range(n_nodes)}
        for e in edges:
            adj[e.from_idx].append(e)
        return adj

    def _dijkstra(
        self,
        waypoints: list[Waypoint],
        edges: list[TrajectoryEdge],
        start: int,
        end: int,
        cost_key: str = "cost",
    ) -> PlannedTrajectory:
        """Standard Dijkstra's shortest path.

        Uses a binary heap priority queue for efficiency.
        """
        n = len(waypoints)
        adj = self._build_adjacency(edges, n)

        dist = [math.inf] * n
        prev: dict[int, int] = {}
        prev_edge: dict[int, TrajectoryEdge] = {}
        dist[start] = 0.0

        # Priority queue: (cost, node_index)
        pq: list[tuple[float, int]] = [(0.0, start)]

        while pq:
            d, u = heapq.heappop(pq)
            if d > dist[u]:
                continue
            if u == end:
                break

            for edge in adj.get(u, []):
                v = edge.to_idx
                w = getattr(edge, cost_key, edge.cost)
                new_dist = dist[u] + w
                if new_dist < dist[v]:
                    dist[v] = new_dist
                    prev[v] = u
                    prev_edge[v] = edge
                    heapq.heappush(pq, (new_dist, v))

        # Reconstruct path
        if dist[end] == math.inf:
            return PlannedTrajectory(
                waypoints=[], edges=[], total_cost=math.inf,
            )

        path_indices: list[int] = []
        node = end
        while node != start:
            path_indices.append(node)
            node = prev.get(node, start)
        path_indices.append(start)
        path_indices.reverse()

        path_waypoints = [waypoints[i] for i in path_indices]
        path_edges = [prev_edge[i] for i in path_indices[1:] if i in prev_edge]
        total_cost = sum(getattr(e, cost_key, e.cost) for e in path_edges)
        total_distance = sum(e.distance for e in path_edges)
        max_risk = max((e.detection_risk for e in path_edges), default=0.0)

        return PlannedTrajectory(
            waypoints=path_waypoints,
            edges=path_edges,
            total_cost=total_cost,
            total_distance=total_distance,
            max_detection_risk=max_risk,
        )

    def _dijkstra_minimax(
        self,
        waypoints: list[Waypoint],
        edges: list[TrajectoryEdge],
        start: int,
        end: int,
    ) -> PlannedTrajectory:
        """Modified Dijkstra minimizing maximum edge risk along the path.

        Instead of summing costs, tracks the maximum detection risk
        encountered on any edge along the path.
        """
        n = len(waypoints)
        adj = self._build_adjacency(edges, n)

        max_risk_to = [math.inf] * n
        prev: dict[int, int] = {}
        prev_edge: dict[int, TrajectoryEdge] = {}
        max_risk_to[start] = 0.0

        pq: list[tuple[float, int]] = [(0.0, start)]

        while pq:
            risk, u = heapq.heappop(pq)
            if risk > max_risk_to[u]:
                continue
            if u == end:
                break

            for edge in adj.get(u, []):
                v = edge.to_idx
                new_max_risk = max(max_risk_to[u], edge.detection_risk)
                if new_max_risk < max_risk_to[v]:
                    max_risk_to[v] = new_max_risk
                    prev[v] = u
                    prev_edge[v] = edge
                    heapq.heappush(pq, (new_max_risk, v))

        if max_risk_to[end] == math.inf:
            return PlannedTrajectory(
                waypoints=[], edges=[], total_cost=math.inf,
            )

        # Reconstruct
        path_indices: list[int] = []
        node = end
        while node != start:
            path_indices.append(node)
            node = prev.get(node, start)
        path_indices.append(start)
        path_indices.reverse()

        path_waypoints = [waypoints[i] for i in path_indices]
        path_edges = [prev_edge[i] for i in path_indices[1:] if i in prev_edge]
        total_cost = sum(e.cost for e in path_edges)
        total_distance = sum(e.distance for e in path_edges)
        max_risk = max((e.detection_risk for e in path_edges), default=0.0)

        return PlannedTrajectory(
            waypoints=path_waypoints,
            edges=path_edges,
            total_cost=total_cost,
            total_distance=total_distance,
            max_detection_risk=max_risk,
        )
