"""
Re-score existing test results with improved scoring function.

Usage:
    PYTHONPATH=. py -3.13 scripts/rescore_results.py data/research/test_results/full_run_*.json
"""

import json
import sys
import os
from collections import Counter, defaultdict
from pathlib import Path

# Force UTF-8 output on Windows
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

# Import the scoring function from the pipeline
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from scripts.run_test_pipeline import score_response


def rescore(input_path: str):
    """Re-score all results in a file."""
    path = Path(input_path)
    with open(path, encoding="utf-8") as f:
        data = json.load(f)

    results = data.get("results", [])
    if not results:
        print(f"No results in {path}")
        return

    print(f"Re-scoring {len(results)} results from {path}")

    changed = 0
    before = Counter()
    after = Counter()

    for r in results:
        before[r["verdict"]] += 1
        new_score = score_response(r["response"])
        if new_score["verdict"] != r["verdict"]:
            changed += 1
        r["verdict"] = new_score["verdict"]
        r["confidence"] = new_score["confidence"]
        r["signals"] = new_score["signals"]
        after[r["verdict"]] += 1

    print(f"\nChanged: {changed}/{len(results)} ({100*changed/len(results):.1f}%)")
    print(f"\nBefore: {dict(before)}")
    print(f"After:  {dict(after)}")

    # Rebuild analysis
    baselines = [r for r in results if r["variant"] == "baseline"]
    baseline_verdicts = Counter(r["verdict"] for r in baselines)
    total_tests = len(baselines)

    print(f"\nBaseline verdicts ({total_tests} tests):")
    for v, c in sorted(baseline_verdicts.items(), key=lambda x: -x[1]):
        print(f"  {v}: {c} ({100*c/total_tests:.1f}%)")

    # Mutation bypass
    baseline_by_idx = {r["test_index"]: r["verdict"] for r in baselines}
    bypass_stats = defaultdict(lambda: {"total": 0, "bypassed": 0})
    for r in results:
        if r["variant"] != "baseline" and r.get("mutator"):
            base_v = baseline_by_idx.get(r["test_index"])
            if base_v == "REFUSED":
                bypass_stats[r["mutator"]]["total"] += 1
                if r["verdict"] in ("COMPLIANT", "PARTIAL"):
                    bypass_stats[r["mutator"]]["bypassed"] += 1

    print(f"\nMutation bypass rates:")
    for m in sorted(bypass_stats):
        s = bypass_stats[m]
        rate = 100 * s["bypassed"] / s["total"] if s["total"] else 0
        print(f"  {m}: {s['bypassed']}/{s['total']} = {rate:.1f}%")

    # Domain breakdown
    print(f"\nDomain safety rates (baselines):")
    for domain in sorted(set(r.get("domain", "?") for r in baselines)):
        subset = [r for r in baselines if r.get("domain") == domain]
        refused = sum(1 for r in subset if r["verdict"] == "REFUSED")
        compliant = sum(1 for r in subset if r["verdict"] == "COMPLIANT")
        print(f"  {domain}: {len(subset)} tests, {refused} refused ({100*refused/len(subset):.1f}%), "
              f"{compliant} compliant ({100*compliant/len(subset):.1f}%)")

    # Update data
    data["results"] = results
    data["baseline_verdicts"] = dict(baseline_verdicts)
    data["rescored"] = True

    # Save
    out_path = path.with_name(path.stem + "_rescored.json")
    out_path.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"\nSaved to: {out_path}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: py -3.13 scripts/rescore_results.py <results_file.json>")
        sys.exit(1)
    rescore(sys.argv[1])
