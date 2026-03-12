"""
Feature space analysis using dimensionality reduction and clustering.

Uses UMAP for 2D projection and HDBSCAN for clustering.
Falls back to PCA + KMeans if those aren't installed.
"""

from typing import List, Dict, Any, Optional, Tuple
import json
from pathlib import Path
from datetime import datetime, timezone


class SpaceAnalyzer:
    """Analyze embedding/feature space for patterns."""

    def __init__(self, analysis_dir: str = "data/pipeline/analysis"):
        self.analysis_dir = Path(analysis_dir)

    def reduce_dimensions(
        self,
        vectors: List[List[float]],
        n_components: int = 2,
        method: str = "auto",
    ) -> List[List[float]]:
        """Reduce high-dimensional vectors to 2D/3D for visualization.

        Args:
            vectors: List of float vectors.
            n_components: Target dimensions (2 or 3).
            method: "umap", "pca", or "auto" (tries UMAP first).
        """
        import numpy as np
        arr = np.array(vectors)

        if method == "auto":
            try:
                import umap
                method = "umap"
            except ImportError:
                method = "pca"

        if method == "umap":
            import umap
            reducer = umap.UMAP(
                n_components=n_components,
                n_neighbors=min(15, len(vectors) - 1),
                min_dist=0.1,
                random_state=42,
            )
            reduced = reducer.fit_transform(arr)
        else:
            from sklearn.decomposition import PCA
            reducer = PCA(n_components=n_components, random_state=42)
            reduced = reducer.fit_transform(arr)

        return reduced.tolist()

    def cluster(
        self,
        vectors: List[List[float]],
        method: str = "auto",
        min_cluster_size: int = 5,
    ) -> List[int]:
        """Cluster vectors into groups.

        Returns list of cluster labels (-1 = noise).
        """
        import numpy as np
        arr = np.array(vectors)

        if method == "auto":
            try:
                import hdbscan
                method = "hdbscan"
            except ImportError:
                method = "kmeans"

        if method == "hdbscan":
            import hdbscan
            clusterer = hdbscan.HDBSCAN(
                min_cluster_size=min_cluster_size,
                min_samples=2,
            )
            labels = clusterer.fit_predict(arr)
        else:
            from sklearn.cluster import KMeans
            n_clusters = max(2, len(vectors) // min_cluster_size)
            n_clusters = min(n_clusters, 20)
            clusterer = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
            labels = clusterer.fit_predict(arr)

        return labels.tolist()

    def analyze(
        self,
        embeddings: List[List[float]],
        labels: Optional[List[str]] = None,
        classifications: Optional[List[str]] = None,
        min_cluster_size: int = 5,
    ) -> Dict[str, Any]:
        """Run full analysis: reduce dimensions, cluster, return results.

        Args:
            embeddings: List of embedding vectors.
            labels: Optional text labels (prompt text or ID).
            classifications: Optional SAFE/HARMFUL/UNCLEAR per prompt.
            min_cluster_size: Minimum points for a cluster.

        Returns:
            Analysis results with 2D coordinates, clusters, and stats.
        """
        if not embeddings or len(embeddings) < 3:
            return {
                "error": "Need at least 3 embeddings for analysis",
                "points": [],
                "clusters": {},
            }

        # Reduce to 2D
        coords_2d = self.reduce_dimensions(embeddings, n_components=2)

        # Cluster
        cluster_labels = self.cluster(embeddings, min_cluster_size=min_cluster_size)

        # Build points
        points = []
        for i, (coord, cluster) in enumerate(zip(coords_2d, cluster_labels)):
            point = {
                "x": coord[0],
                "y": coord[1],
                "cluster": cluster,
            }
            if labels and i < len(labels):
                point["label"] = labels[i]
            if classifications and i < len(classifications):
                point["classification"] = classifications[i]
            points.append(point)

        # Compute cluster stats
        clusters: Dict[int, Dict[str, Any]] = {}
        for i, cl in enumerate(cluster_labels):
            if cl not in clusters:
                clusters[cl] = {"count": 0, "safe": 0, "harmful": 0, "unclear": 0}
            clusters[cl]["count"] += 1
            if classifications and i < len(classifications):
                clf = classifications[i].upper()
                if clf == "SAFE":
                    clusters[cl]["safe"] += 1
                elif clf == "HARMFUL":
                    clusters[cl]["harmful"] += 1
                else:
                    clusters[cl]["unclear"] += 1

        # Compute cluster harm rates
        for cl_id, stats in clusters.items():
            total = stats["safe"] + stats["harmful"]
            stats["harm_rate"] = stats["harmful"] / max(total, 1)

        return {
            "points": points,
            "clusters": {str(k): v for k, v in clusters.items()},
            "total_points": len(points),
            "n_clusters": len([k for k in clusters if k != -1]),
        }

    def save_analysis(self, analysis: Dict[str, Any], name: str = "latest") -> str:
        """Save analysis results to disk."""
        self.analysis_dir.mkdir(parents=True, exist_ok=True)
        analysis["created_at"] = datetime.now(tz=timezone.utc).isoformat()
        filename = f"{name}_analysis.json"
        filepath = self.analysis_dir / filename
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(analysis, f, indent=2, ensure_ascii=False)
        return str(filepath)

    def load_analysis(self, name: str = "latest") -> Optional[Dict[str, Any]]:
        """Load analysis results from disk."""
        filepath = self.analysis_dir / f"{name}_analysis.json"
        if not filepath.exists():
            return None
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)

    def list_analyses(self) -> List[Dict[str, Any]]:
        """List all saved analyses."""
        if not self.analysis_dir.exists():
            return []

        analyses = []
        for f in sorted(
            self.analysis_dir.glob("*_analysis.json"),
            key=lambda x: x.stat().st_mtime,
            reverse=True,
        ):
            try:
                with open(f, 'r', encoding='utf-8') as fh:
                    data = json.load(fh)
                analyses.append({
                    "id": f.stem.replace("_analysis", ""),
                    "created_at": data.get("created_at", ""),
                    "total_points": data.get("total_points", 0),
                    "n_clusters": data.get("n_clusters", 0),
                })
            except Exception:
                continue
        return analyses
