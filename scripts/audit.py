#!/usr/bin/env python3
"""
LLM Safety Framework — Automated Audit Script
===============================================
Runs 12 audit modules against the codebase and produces a scored report.

Usage:
    py -3.13 scripts/audit.py                  # basic audit
    py -3.13 scripts/audit.py --run-tests      # also execute pytest
    py -3.13 scripts/audit.py --json           # JSON output to stdout
    py -3.13 scripts/audit.py --verbose        # show INFO-level findings
    py -3.13 scripts/audit.py --modules plugin_manifests route_inventory
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import os
import re
import subprocess
import sys
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Optional


# =============================================================================
# Data Classes
# =============================================================================

@dataclass
class Finding:
    severity: str       # "error", "warning", "info"
    file: str           # relative path
    line: Optional[int]
    message: str
    code: str           # machine-readable, e.g. "ROUTE_MISMATCH"


@dataclass
class AuditResult:
    module_name: str
    module_id: str
    status: str = "PASS"   # PASS / WARN / FAIL
    findings: list[Finding] = field(default_factory=list)
    stats: dict[str, Any] = field(default_factory=dict)
    duration_ms: float = 0.0

    def add(self, severity: str, file: str, line: Optional[int],
            message: str, code: str):
        self.findings.append(Finding(severity, file, line, message, code))
        if severity == "error" and self.status != "FAIL":
            self.status = "FAIL"
        elif severity == "warning" and self.status == "PASS":
            self.status = "WARN"


@dataclass
class AuditReport:
    timestamp: str
    project_root: str
    modules: list[AuditResult] = field(default_factory=list)
    total_score: int = 0
    grade: str = "?"
    summary: dict[str, int] = field(default_factory=dict)


# =============================================================================
# Regex Patterns
# =============================================================================

PAT = {
    "py_route":       re.compile(r'@router\.(get|post|put|delete|patch)\(\s*["\']([^"\']*)["\']'),
    "py_import_from": re.compile(r'^\s*from\s+(\S+)\s+import', re.MULTILINE),
    "py_test_func":   re.compile(r'def\s+(test_\w+)'),

    "js_apicall_q":   re.compile(r"apiCall\(\s*['\"]([^'\"]+)['\"]"),
    "js_apicall_bt":  re.compile(r"apiCall\(\s*`([^`]+)`"),
    "js_fetch_q":     re.compile(r"fetch\(\s*['\"]([^'\"]+)['\"]"),
    "js_fetch_bt":    re.compile(r"fetch\(\s*`([^`]+)`"),
    "js_func":        re.compile(r"(?:async\s+)?function\s+(\w+)\s*\("),
    "js_toplevel_var": re.compile(r"^(let|var|const)\s+(\w+)", re.MULTILINE),
    "js_getbyid_q":   re.compile(r"getElementById\(\s*['\"]([^'\"]+)['\"]"),
    "js_getbyid_bt":  re.compile(r"getElementById\(\s*`([^`]+)`"),
    "js_qsel_id":     re.compile(r"querySelector\(\s*['\"]#([^ '\"]+)['\"]"),
    "js_innerhtml":   re.compile(r"\.innerHTML\s*[\+]?=\s*"),
    "js_eschtml":     re.compile(r"escHtml\("),

    "html_id":        re.compile(r'id="([^"]+)"'),

    "test_client":    re.compile(r'client\.(get|post|put|delete|patch)\(\s*["\']([^"\']+)["\']'),
}


# =============================================================================
# Project Context — discovers all files once
# =============================================================================

class ProjectContext:
    def __init__(self, root: Path):
        self.root = root
        self.plugins_dir = root / "src" / "web" / "plugins"
        self.static_dir = root / "src" / "web" / "static"
        self.tests_dir = root / "tests"

        # Discover plugins
        self.plugin_ids: list[str] = []
        self.plugin_routes: dict[str, Path] = {}
        self.plugin_inits: dict[str, Path] = {}
        self.plugin_html: dict[str, Path] = {}
        self.plugin_js: dict[str, Path] = {}

        if self.plugins_dir.exists():
            for d in sorted(self.plugins_dir.iterdir()):
                if d.is_dir() and (d / "__init__.py").exists() and not d.name.startswith("_"):
                    pid = d.name
                    self.plugin_ids.append(pid)
                    self.plugin_inits[pid] = d / "__init__.py"
                    r = d / "routes.py"
                    if r.exists():
                        self.plugin_routes[pid] = r
                    h = d / "static" / "fragment.html"
                    if h.exists():
                        self.plugin_html[pid] = h
                    j = d / "static" / "fragment.js"
                    if j.exists():
                        self.plugin_js[pid] = j

        # Shell
        self.shell_html = self.static_dir / "shell.html"
        self.styles_css = self.static_dir / "styles.css"
        self.app_py = root / "src" / "web" / "app.py"

        # Extract shell JS block
        self.shell_js_content = ""
        self.shell_js_line_offset = 0
        if self.shell_html.exists():
            text = self.shell_html.read_text(encoding="utf-8", errors="replace")
            m = re.search(r"<script>(.*?)</script>", text, re.DOTALL)
            if m:
                self.shell_js_content = m.group(1)
                self.shell_js_line_offset = text[:m.start(1)].count("\n")

        # Test files
        self.test_files: list[Path] = []
        if self.tests_dir.exists():
            self.test_files = sorted(self.tests_dir.glob("test_*.py"))

        # File content cache
        self._cache: dict[Path, str] = {}

    def read(self, path: Path) -> str:
        if path not in self._cache:
            self._cache[path] = path.read_text(encoding="utf-8", errors="replace")
        return self._cache[path]

    def relpath(self, path: Path) -> str:
        try:
            return str(path.relative_to(self.root)).replace("\\", "/")
        except ValueError:
            return str(path).replace("\\", "/")


# =============================================================================
# Base Module
# =============================================================================

class AuditModule:
    module_id: str = ""
    module_name: str = ""

    def __init__(self, ctx: ProjectContext):
        self.ctx = ctx

    def run(self, shared: dict[str, Any]) -> AuditResult:
        raise NotImplementedError


# =============================================================================
# Module 1: Plugin Manifests
# =============================================================================

class AuditPluginManifests(AuditModule):
    module_id = "plugin_manifests"
    module_name = "Plugin Manifests"

    def run(self, shared):
        r = AuditResult(self.module_name, self.module_id)
        checked = 0
        for pid in self.ctx.plugin_ids:
            init_path = self.ctx.plugin_inits[pid]
            text = self.ctx.read(init_path)
            rel = self.ctx.relpath(init_path)
            checked += 1

            if "manifest" not in text:
                r.add("error", rel, None, f"Plugin '{pid}' has no manifest variable", "NO_MANIFEST")
                continue

            # Check required fields via text search (robust enough)
            for fld in ["id=", "name=", "router=", "api_prefix=", "fragment_dir="]:
                if fld not in text and fld.replace("=", " =") not in text:
                    r.add("warning", rel, None,
                           f"Plugin '{pid}' manifest may be missing field '{fld.rstrip('=')}'",
                           "MISSING_FIELD")

            if pid not in self.ctx.plugin_routes:
                r.add("warning", rel, None, f"Plugin '{pid}' has no routes.py", "NO_ROUTES")

        r.stats = {"plugins_checked": checked}
        return r


# =============================================================================
# Module 2: Route Inventory
# =============================================================================

@dataclass
class RouteEntry:
    method: str
    path: str
    plugin: str
    file: str
    line: int


class AuditRouteInventory(AuditModule):
    module_id = "route_inventory"
    module_name = "Route Inventory"

    def run(self, shared):
        r = AuditResult(self.module_name, self.module_id)
        routes: list[RouteEntry] = []
        prefix_map: dict[str, str] = {}

        # Gather api_prefix from manifests
        for pid in self.ctx.plugin_ids:
            text = self.ctx.read(self.ctx.plugin_inits[pid])
            m = re.search(r'api_prefix\s*=\s*["\']([^"\']*)["\']', text)
            prefix_map[pid] = m.group(1) if m else ""

        # Parse routes from each plugin
        for pid, rpath in self.ctx.plugin_routes.items():
            text = self.ctx.read(rpath)
            prefix = prefix_map.get(pid, "")
            rel = self.ctx.relpath(rpath)
            for i, line in enumerate(text.splitlines(), 1):
                for m in PAT["py_route"].finditer(line):
                    method = m.group(1).upper()
                    path = f"/api{prefix}{m.group(2)}"
                    routes.append(RouteEntry(method, path, pid, rel, i))

        # App-level routes
        if self.ctx.app_py.exists():
            text = self.ctx.read(self.ctx.app_py)
            rel = self.ctx.relpath(self.ctx.app_py)
            for i, line in enumerate(text.splitlines(), 1):
                for m in PAT["py_route"].finditer(line):
                    method = m.group(1).upper()
                    path = m.group(2)
                    if not path.startswith("/api"):
                        path = "/api" + path
                    routes.append(RouteEntry(method, path, "_app", rel, i))
            # Catch @app.get patterns too
            for i, line in enumerate(text.splitlines(), 1):
                am = re.search(r'@app\.(get|post|put|delete)\(\s*["\']([^"\']*)["\']', line)
                if am:
                    routes.append(RouteEntry(
                        am.group(1).upper(), am.group(2), "_app", rel, i
                    ))

        # Per-plugin stats
        plugin_counts: dict[str, int] = {}
        for rt in routes:
            plugin_counts[rt.plugin] = plugin_counts.get(rt.plugin, 0) + 1

        r.stats = {
            "total_routes": len(routes),
            "per_plugin": plugin_counts,
            "routes": routes,
        }
        if not routes:
            r.add("error", "", None, "No routes found", "NO_ROUTES")
        return r


# =============================================================================
# Module 3: JS → Route Cross-Reference
# =============================================================================

class AuditJsRouteCrossRef(AuditModule):
    module_id = "js_route_xref"
    module_name = "JS->Route Cross-Ref"

    def _normalize(self, path: str) -> str:
        """Normalize JS path: strip query params, replace ${...} with {}."""
        path = re.sub(r"\$\{[^}]+\}", "{}", path)
        path = path.split("?")[0]
        if not path.startswith("/api"):
            path = "/api" + path
        return path

    def _matches_route(self, js_path: str, route_path: str) -> bool:
        """Check if a JS path matches a route path (with path params)."""
        js_parts = js_path.strip("/").split("/")
        rt_parts = route_path.strip("/").split("/")
        if len(js_parts) != len(rt_parts):
            return False
        for jp, rp in zip(js_parts, rt_parts):
            if rp.startswith("{") or jp == "{}":
                continue
            if jp != rp:
                return False
        return True

    def run(self, shared):
        r = AuditResult(self.module_name, self.module_id)
        route_inv = shared.get("route_inventory")
        if not route_inv:
            r.add("warning", "", None, "Route inventory not available", "NO_DEPENDENCY")
            return r

        declared_routes: list[RouteEntry] = route_inv.stats.get("routes", [])

        # Collect all JS api calls
        js_calls: list[tuple[str, str, int]] = []  # (normalized_path, file, line)

        all_js_sources = []
        for pid, jpath in self.ctx.plugin_js.items():
            all_js_sources.append((self.ctx.relpath(jpath), self.ctx.read(jpath)))
        if self.ctx.shell_js_content:
            all_js_sources.append(("src/web/static/shell.html:<script>", self.ctx.shell_js_content))

        for src_name, text in all_js_sources:
            for i, line in enumerate(text.splitlines(), 1):
                for pat_name in ("js_apicall_q", "js_apicall_bt"):
                    for m in PAT[pat_name].finditer(line):
                        raw = m.group(1)
                        # Check if this is a concatenation pattern (e.g. '/foo/' + var)
                        after = line[m.end():]
                        is_concat = raw.endswith("/") and ("+" in after[:5])
                        norm = self._normalize(raw)
                        js_calls.append((norm, src_name, i, is_concat))

        # Check each JS call against declared routes
        unmatched = []
        matched_routes = set()
        for norm, src, ln, is_concat in js_calls:
            found = False
            for rt in declared_routes:
                if self._matches_route(norm, rt.path):
                    matched_routes.add(rt.path)
                    found = True
                    break
                # For concatenation patterns, check if the JS prefix matches
                # the beginning of any route
                if is_concat and rt.path.startswith(norm.rstrip("/") + "/"):
                    matched_routes.add(rt.path)
                    found = True
                    break
            if not found:
                unmatched.append((norm, src, ln))

        for norm, src, ln in unmatched:
            r.add("warning", src, ln,
                   f"JS calls '{norm}' but no matching backend route found",
                   "ROUTE_NOT_FOUND")

        # Orphan routes (declared but never called from JS) — INFO only
        called_paths = {c[0] for c in js_calls}
        concat_prefixes = {c[0].rstrip("/") for c in js_calls if c[3]}
        orphan_count = 0
        for rt in declared_routes:
            if rt.path not in matched_routes:
                # Check if any JS call could match with path params
                any_match = any(self._matches_route(cp, rt.path) for cp in called_paths)
                if not any_match:
                    # Also check concat prefixes
                    any_prefix = any(rt.path.startswith(p + "/") for p in concat_prefixes)
                    if not any_prefix:
                        orphan_count += 1

        r.stats = {
            "js_api_calls": len(js_calls),
            "unmatched_calls": len(unmatched),
            "orphan_routes": orphan_count,
        }
        return r


# =============================================================================
# Module 4: DOM ID Integrity
# =============================================================================

class AuditDomIdIntegrity(AuditModule):
    module_id = "dom_id_integrity"
    module_name = "DOM ID Integrity"

    def run(self, shared):
        r = AuditResult(self.module_name, self.module_id)

        # Collect all HTML IDs
        html_ids: dict[str, list[tuple[str, int]]] = {}  # id -> [(file, line)]

        all_html = []
        if self.ctx.shell_html.exists():
            all_html.append((self.ctx.relpath(self.ctx.shell_html),
                             self.ctx.read(self.ctx.shell_html)))
        for pid, hpath in self.ctx.plugin_html.items():
            all_html.append((self.ctx.relpath(hpath), self.ctx.read(hpath)))

        for src, text in all_html:
            for i, line in enumerate(text.splitlines(), 1):
                for m in PAT["html_id"].finditer(line):
                    eid = m.group(1)
                    html_ids.setdefault(eid, []).append((src, i))

        # Check for duplicate IDs
        dup_count = 0
        for eid, locs in html_ids.items():
            if len(locs) > 1:
                files = [f"{f}:{l}" for f, l in locs]
                r.add("warning", locs[0][0], locs[0][1],
                       f"Duplicate ID '{eid}' found in: {', '.join(files)}",
                       "DUPLICATE_ID")
                dup_count += 1

        # Collect all JS getElementById references
        js_id_refs: dict[str, list[tuple[str, int]]] = {}
        all_js = []
        for pid, jpath in self.ctx.plugin_js.items():
            all_js.append((self.ctx.relpath(jpath), self.ctx.read(jpath)))
        if self.ctx.shell_js_content:
            all_js.append(("shell.html:<script>", self.ctx.shell_js_content))

        for src, text in all_js:
            for i, line in enumerate(text.splitlines(), 1):
                for pat in ("js_getbyid_q", "js_qsel_id"):
                    for m in PAT[pat].finditer(line):
                        eid = m.group(1)
                        js_id_refs.setdefault(eid, []).append((src, i))

        # Skip dynamic IDs (containing ${...} or template syntax)
        static_refs = {eid for eid in js_id_refs if "${" not in eid and "`" not in eid}

        # Find missing IDs
        all_ids = set(html_ids.keys())
        missing = static_refs - all_ids
        missing_count = 0
        for eid in sorted(missing):
            locs = js_id_refs[eid]
            # Skip IDs that are clearly dynamic prefixes (e.g. 'ep-' + id)
            if eid.endswith("-") or eid.endswith("_"):
                continue
            # Skip IDs known to be created dynamically by JS (e.g. buildSidebar)
            if eid.startswith("nav-count-"):
                continue
            r.add("warning", locs[0][0], locs[0][1],
                   f"JS references ID '{eid}' but it's not in any HTML file",
                   "MISSING_ID")
            missing_count += 1

        r.stats = {
            "html_ids": len(all_ids),
            "js_id_refs": len(static_refs),
            "duplicate_ids": dup_count,
            "missing_ids": missing_count,
        }

        # Also store for module 10
        shared["_html_id_owner"] = {}
        for eid, locs in html_ids.items():
            shared["_html_id_owner"][eid] = locs[0][0]  # first file that declares it

        return r


# =============================================================================
# Module 5: Function Duplicate Detection
# =============================================================================

# Shell stub functions that are intentionally overridden by plugins
SHELL_STUBS = {
    "loadDashboard", "heatmapColor", "loadHeatmap", "exportDashboardReport",
    "loadCoverageMatrix", "switchCoverageTab", "renderCoverageGrid",
    "closeRunViewer", "switchRunViewerTab", "filterRunResults",
    "exportRunResults", "deepDiveNav",
    "togglePipelineDrawer", "loadPipelineDrawer",
    "buildPipelineFromDrawer", "exportPipelineFromDrawer",
}


class AuditFunctionDuplicates(AuditModule):
    module_id = "function_duplicates"
    module_name = "Function Duplicates"

    def run(self, shared):
        r = AuditResult(self.module_name, self.module_id)

        func_map: dict[str, list[tuple[str, int]]] = {}

        all_js = []
        if self.ctx.shell_js_content:
            all_js.append(("shell.html", self.ctx.shell_js_content))
        for pid, jpath in self.ctx.plugin_js.items():
            all_js.append((self.ctx.relpath(jpath), self.ctx.read(jpath)))

        for src, text in all_js:
            for i, line in enumerate(text.splitlines(), 1):
                for m in PAT["js_func"].finditer(line):
                    name = m.group(1)
                    func_map.setdefault(name, []).append((src, i))

        dup_count = 0
        for name, locs in sorted(func_map.items()):
            if len(locs) <= 1:
                continue
            files = [f[0] for f in locs]
            is_stub = name in SHELL_STUBS and any("shell" in f.lower() for f in files)
            if is_stub:
                r.add("info", locs[0][0], locs[0][1],
                       f"Function '{name}' in {len(locs)} files (shell stub override — OK)",
                       "STUB_OVERRIDE")
            else:
                r.add("warning", locs[0][0], locs[0][1],
                       f"Function '{name}' defined in {len(locs)} files: "
                       + ", ".join(files),
                       "DUPLICATE_FUNC")
                dup_count += 1

        r.stats = {
            "total_functions": sum(len(v) for v in func_map.values()),
            "unique_functions": len(func_map),
            "duplicates": dup_count,
        }

        # Store for module 10
        shared["_func_owner"] = {}
        for name, locs in func_map.items():
            shared["_func_owner"][name] = locs[0][0]

        return r


# =============================================================================
# Module 6: Variable Scoping
# =============================================================================

class AuditVariableScoping(AuditModule):
    module_id = "variable_scoping"
    module_name = "Variable Scoping"

    def run(self, shared):
        r = AuditResult(self.module_name, self.module_id)

        var_map: dict[str, list[tuple[str, str, int]]] = {}  # name -> [(keyword, file, line)]

        all_js = []
        if self.ctx.shell_js_content:
            all_js.append(("shell.html", self.ctx.shell_js_content))
        for pid, jpath in self.ctx.plugin_js.items():
            all_js.append((self.ctx.relpath(jpath), self.ctx.read(jpath)))

        for src, text in all_js:
            for m in PAT["js_toplevel_var"].finditer(text):
                keyword = m.group(1)
                name = m.group(2)
                lineno = text[:m.start()].count("\n") + 1
                var_map.setdefault(name, []).append((keyword, src, lineno))

        conflict_count = 0
        for name, entries in sorted(var_map.items()):
            if len(entries) <= 1:
                continue
            files = set(e[1] for e in entries)
            if len(files) <= 1:
                continue  # same file, not a cross-file conflict

            keywords = [e[0] for e in entries]
            # var in shell + assignment-only in plugin = OK (already checked in code)
            # let/const in both = conflict
            has_let = any(k in ("let", "const") for k in keywords)
            if has_let:
                loc_str = "; ".join(f"{e[0]} in {e[1]}:{e[2]}" for e in entries)
                r.add("warning", entries[0][1], entries[0][2],
                       f"Variable '{name}' declared in multiple files: {loc_str}",
                       "VAR_REDECLARATION")
                conflict_count += 1

        r.stats = {
            "total_declarations": sum(len(v) for v in var_map.values()),
            "cross_file_conflicts": conflict_count,
        }
        return r


# =============================================================================
# Module 7: API Pattern Consistency
# =============================================================================

class AuditApiPatterns(AuditModule):
    module_id = "api_patterns"
    module_name = "API Pattern Consistency"

    def run(self, shared):
        r = AuditResult(self.module_name, self.module_id)

        apicall_count = 0
        fetch_count = 0
        raw_fetch_warnings = 0

        all_js = []
        for pid, jpath in self.ctx.plugin_js.items():
            all_js.append((self.ctx.relpath(jpath), self.ctx.read(jpath), pid))

        for src, text, pid in all_js:
            text_lines = text.splitlines()
            for i, line in enumerate(text_lines, 1):
                if PAT["js_apicall_q"].search(line) or PAT["js_apicall_bt"].search(line):
                    apicall_count += 1
                for pat in ("js_fetch_q", "js_fetch_bt"):
                    for m in PAT[pat].finditer(line):
                        fetch_count += 1
                        url = m.group(1)
                        # Exclude fragment loading and blob URLs
                        if "fragment" in url or "blob:" in url:
                            continue
                        # Check nearby lines (±5) for FormData usage (upload patterns)
                        ctx_start = max(0, i - 6)
                        ctx_end = min(len(text_lines), i + 5)
                        context_block = "\n".join(text_lines[ctx_start:ctx_end])
                        if "FormData" in context_block:
                            continue
                        r.add("warning", src, i,
                               f"Raw fetch() call to '{url}' — consider using apiCall()",
                               "RAW_FETCH")
                        raw_fetch_warnings += 1

        r.stats = {
            "apicall_count": apicall_count,
            "fetch_count": fetch_count,
            "raw_fetch_warnings": raw_fetch_warnings,
        }
        return r


# =============================================================================
# Module 8: Test Coverage Matrix
# =============================================================================

class AuditTestCoverage(AuditModule):
    module_id = "test_coverage"
    module_name = "Test Coverage Matrix"

    def run(self, shared):
        r = AuditResult(self.module_name, self.module_id)

        route_inv = shared.get("route_inventory")
        declared_routes: list[RouteEntry] = []
        if route_inv:
            declared_routes = route_inv.stats.get("routes", [])

        # Parse tested URLs from test files
        tested_paths: set[str] = set()
        test_counts: dict[str, int] = {}
        total_tests = 0

        for tpath in self.ctx.test_files:
            text = self.ctx.read(tpath)
            rel = self.ctx.relpath(tpath)
            funcs = PAT["py_test_func"].findall(text)
            test_counts[rel] = len(funcs)
            total_tests += len(funcs)

            for m in PAT["test_client"].finditer(text):
                url = m.group(2)
                tested_paths.add(url)

        # Build per-plugin coverage
        plugin_coverage: dict[str, dict[str, int]] = {}
        for rt in declared_routes:
            pid = rt.plugin
            if pid not in plugin_coverage:
                plugin_coverage[pid] = {"total": 0, "tested": 0}
            plugin_coverage[pid]["total"] += 1

            # Check if this route is tested (fuzzy match with path params)
            for tp in tested_paths:
                if self._route_matches(tp, rt.path):
                    plugin_coverage[pid]["tested"] += 1
                    break

        # Report low-coverage plugins
        for pid, cov in sorted(plugin_coverage.items()):
            total = cov["total"]
            tested = cov["tested"]
            pct = (tested / total * 100) if total else 0
            if pct < 25 and total >= 3:
                r.add("warning", "", None,
                       f"Plugin '{pid}': {tested}/{total} routes tested ({pct:.0f}%)",
                       "LOW_COVERAGE")
            elif pct < 50 and total >= 5:
                r.add("info", "", None,
                       f"Plugin '{pid}': {tested}/{total} routes tested ({pct:.0f}%)",
                       "PARTIAL_COVERAGE")

        r.stats = {
            "total_tests": total_tests,
            "test_files": len(self.ctx.test_files),
            "tested_urls": len(tested_paths),
            "per_plugin": {k: f"{v['tested']}/{v['total']}" for k, v in plugin_coverage.items()},
        }
        return r

    @staticmethod
    def _route_matches(test_url: str, route_path: str) -> bool:
        tp = test_url.strip("/").split("/")
        rp = route_path.strip("/").split("/")
        if len(tp) != len(rp):
            return False
        for a, b in zip(tp, rp):
            if b.startswith("{"):
                continue
            if a != b:
                return False
        return True


# =============================================================================
# Module 9: Import Validation
# =============================================================================

class AuditImportValidation(AuditModule):
    module_id = "import_validation"
    module_name = "Import Validation"

    def run(self, shared):
        r = AuditResult(self.module_name, self.module_id)
        checked = 0
        failed = 0

        for pid, rpath in self.ctx.plugin_routes.items():
            text = self.ctx.read(rpath)
            rel = self.ctx.relpath(rpath)

            for m in PAT["py_import_from"].finditer(text):
                module_str = m.group(1)
                lineno = text[:m.start()].count("\n") + 1
                checked += 1

                if module_str.startswith("."):
                    # Relative import — resolve to file path
                    # In Python: 1 dot = current package, 2 = parent, 3 = grandparent
                    # For routes.py in src/web/plugins/X/, rpath.parent is the package dir
                    # so we go up (dots - 1) more times from that starting point.
                    dots = len(module_str) - len(module_str.lstrip("."))
                    remainder = module_str.lstrip(".")
                    base = rpath.parent
                    for _ in range(dots - 1):
                        base = base.parent
                    if remainder:
                        parts = remainder.split(".")
                        target = base / "/".join(parts)
                        if not target.with_suffix(".py").exists() and not (target / "__init__.py").exists():
                            r.add("error", rel, lineno,
                                   f"Import '{module_str}' cannot be resolved (tried {target})",
                                   "IMPORT_FAIL")
                            failed += 1
                else:
                    # Absolute import — check with importlib
                    top = module_str.split(".")[0]
                    try:
                        spec = importlib.util.find_spec(top)
                        if spec is None:
                            r.add("warning", rel, lineno,
                                   f"Import '{module_str}' — top-level '{top}' not found",
                                   "IMPORT_NOT_FOUND")
                    except (ModuleNotFoundError, ValueError):
                        r.add("warning", rel, lineno,
                               f"Import '{module_str}' — '{top}' not resolvable",
                               "IMPORT_NOT_FOUND")

        r.stats = {"checked": checked, "failed": failed}
        return r


# =============================================================================
# Module 10: Cross-Plugin Dependencies
# =============================================================================

SHELL_GLOBALS = {
    "apiCall", "toast", "escHtml", "switchTab", "showSection",
    "refreshContextBar", "updateWorkflowBar", "switchMode", "loadModules",
    "togglePipelineDrawer", "loadPipelineDrawer", "buildPipelineFromDrawer",
    "exportPipelineFromDrawer", "closeRunViewer", "switchRunViewerTab",
    "filterRunResults", "exportRunResults", "deepDiveNav", "buildSidebar",
    "API", "SECTION_STAGES", "SECTION_PLUGIN_MAP", "SECTION_LOADERS",
    "dashboardCharts", "_coverageData", "_coverageTab",
    "currentMode", "_fragmentCache", "_ctxTimer",
    "heatmapColor", "loadHeatmap", "exportDashboardReport",
    "loadCoverageMatrix", "switchCoverageTab", "renderCoverageGrid",
    "loadDashboard",
}


class AuditCrossPluginDeps(AuditModule):
    module_id = "cross_plugin_deps"
    module_name = "Cross-Plugin Dependencies"

    def run(self, shared):
        r = AuditResult(self.module_name, self.module_id)

        func_owner = shared.get("_func_owner", {})
        html_id_owner = shared.get("_html_id_owner", {})

        cross_func = 0
        cross_dom = 0

        for pid, jpath in self.ctx.plugin_js.items():
            text = self.ctx.read(jpath)
            src = self.ctx.relpath(jpath)
            plugin_file_prefix = f"src/web/plugins/{pid}/"

            for i, line in enumerate(text.splitlines(), 1):
                # Check getElementById references to other plugins' IDs
                for pat in ("js_getbyid_q",):
                    for m in PAT[pat].finditer(line):
                        eid = m.group(1)
                        owner = html_id_owner.get(eid, "")
                        if owner and plugin_file_prefix not in owner and "shell" not in owner.lower():
                            r.add("info", src, i,
                                   f"Cross-plugin DOM ref: '{eid}' belongs to {owner}",
                                   "CROSS_PLUGIN_DOM")
                            cross_dom += 1

        r.stats = {"cross_func_refs": cross_func, "cross_dom_refs": cross_dom}
        return r


# =============================================================================
# Module 11: XSS Safety
# =============================================================================

class AuditXssSafety(AuditModule):
    module_id = "xss_safety"
    module_name = "XSS Safety"

    def run(self, shared):
        r = AuditResult(self.module_name, self.module_id)

        total_innerhtml = 0
        unescaped = 0

        all_js = []
        for pid, jpath in self.ctx.plugin_js.items():
            all_js.append((self.ctx.relpath(jpath), self.ctx.read(jpath)))
        if self.ctx.shell_js_content:
            all_js.append(("shell.html", self.ctx.shell_js_content))

        for src, text in all_js:
            for i, line in enumerate(text.splitlines(), 1):
                if not PAT["js_innerhtml"].search(line):
                    continue
                total_innerhtml += 1

                # Check if line has template literals with ${...} that lack escHtml
                if "${" in line or "' +" in line or '" +' in line:
                    has_escape = PAT["js_eschtml"].search(line)
                    if not has_escape:
                        # Check if it's just numeric or safe values
                        interps = re.findall(r"\$\{([^}]+)\}", line)
                        # Properties known to carry user/API text (XSS vectors)
                        TEXT_PROPS = [".name", ".title", ".text", ".label",
                                      ".message", ".url", ".desc", ".prompt",
                                      ".response", ".content"]
                        # Properties known to be safe (numbers, booleans)
                        SAFE_RE = re.compile(
                            r"^[\d\w_.]+\s*"
                            r"([\|]{2}\s*[\d'\"][^}]*)?"
                            r"(\?\.\w+)*"
                            r"(\.\s*(length|count|total|size))?$"
                        )
                        # Ternary with string literals only: var ? 'a' : 'b'
                        TERNARY_RE = re.compile(
                            r"^[\w_.]+\s*\?\s*['\"][^'\"]*['\"]\s*:\s*['\"][^'\"]*['\"]$"
                        )
                        has_string_interp = False
                        for ip in interps:
                            ip = ip.strip()
                            # Skip safe ternaries like: save ? ' & saved' : ''
                            if TERNARY_RE.match(ip):
                                continue
                            # Skip safe numeric chain: (x || []).length
                            if ip.endswith(".length") or ip.endswith(".count") \
                               or ip.endswith(".total") or ip.endswith(".size"):
                                continue
                            # Skip simple safe properties
                            if SAFE_RE.match(ip):
                                continue
                            # Check for known text properties
                            if any(kw in ip for kw in TEXT_PROPS):
                                has_string_interp = True
                                break
                            # If it doesn't match any safe pattern and is complex, flag it
                            # Allow simple method chains like .toLowerCase()/.toUpperCase()
                            if not re.match(r"^[\d\w_.]+(\.(toLowerCase|toUpperCase|trim|toString)\(\))?$", ip):
                                has_string_interp = True
                                break
                        if has_string_interp:
                            r.add("warning", src, i,
                                   "innerHTML with interpolation but no escHtml() call",
                                   "XSS_RISK")
                            unescaped += 1

        r.stats = {"innerhtml_assignments": total_innerhtml, "unescaped": unescaped}
        return r


# =============================================================================
# Module 12: Static Asset Verification
# =============================================================================

class AuditStaticAssets(AuditModule):
    module_id = "static_assets"
    module_name = "Static Assets"

    def run(self, shared):
        r = AuditResult(self.module_name, self.module_id)
        assets_ok = 0
        assets_total = 0

        # Shell files
        for p in [self.ctx.shell_html, self.ctx.styles_css]:
            assets_total += 1
            if not p.exists():
                r.add("error", self.ctx.relpath(p), None, "File missing", "MISSING_ASSET")
            elif p.stat().st_size == 0:
                r.add("warning", self.ctx.relpath(p), None, "File is empty", "EMPTY_ASSET")
            else:
                assets_ok += 1

        # Plugin fragment files
        for pid in self.ctx.plugin_ids:
            for kind in ("fragment.html", "fragment.js"):
                p = self.ctx.plugins_dir / pid / "static" / kind
                assets_total += 1
                if not p.exists():
                    r.add("error", f"src/web/plugins/{pid}/static/{kind}", None,
                           f"Plugin '{pid}' missing {kind}", "MISSING_ASSET")
                elif p.stat().st_size == 0:
                    r.add("warning", f"src/web/plugins/{pid}/static/{kind}", None,
                           f"Plugin '{pid}' has empty {kind}", "EMPTY_ASSET")
                else:
                    assets_ok += 1

        r.stats = {"total": assets_total, "ok": assets_ok}
        return r


# =============================================================================
# Optional: Test Runner Module
# =============================================================================

class AuditTestRunner(AuditModule):
    module_id = "test_runner"
    module_name = "Test Execution"

    def run(self, shared):
        r = AuditResult(self.module_name, self.module_id)
        try:
            result = subprocess.run(
                [sys.executable, "-m", "pytest", "tests/", "--tb=line", "-W", "ignore"],
                capture_output=True, text=True,
                cwd=str(self.ctx.root), timeout=180,
            )
            output = result.stdout + result.stderr

            # Parse pass/fail from pytest output
            m = re.search(r"(\d+) passed", output)
            passed = int(m.group(1)) if m else 0
            m = re.search(r"(\d+) failed", output)
            failed = int(m.group(1)) if m else 0
            m = re.search(r"(\d+) error", output)
            errors = int(m.group(1)) if m else 0

            r.stats = {"passed": passed, "failed": failed, "errors": errors}

            if failed or errors:
                r.add("error", "", None,
                       f"Tests: {passed} passed, {failed} failed, {errors} errors",
                       "TEST_FAILURES")
            else:
                r.add("info", "", None, f"All {passed} tests passed", "TESTS_OK")

        except subprocess.TimeoutExpired:
            r.add("error", "", None, "Test execution timed out (180s)", "TEST_TIMEOUT")
        except Exception as e:
            r.add("error", "", None, f"Failed to run tests: {e}", "TEST_ERROR")

        return r


# =============================================================================
# Audit Runner
# =============================================================================

class AuditRunner:
    def __init__(self, ctx: ProjectContext, args: argparse.Namespace):
        self.ctx = ctx
        self.args = args

    def get_modules(self) -> list[AuditModule]:
        modules = [
            AuditPluginManifests(self.ctx),
            AuditRouteInventory(self.ctx),
            AuditJsRouteCrossRef(self.ctx),
            AuditDomIdIntegrity(self.ctx),
            AuditFunctionDuplicates(self.ctx),
            AuditVariableScoping(self.ctx),
            AuditApiPatterns(self.ctx),
            AuditTestCoverage(self.ctx),
            AuditImportValidation(self.ctx),
            AuditCrossPluginDeps(self.ctx),
            AuditXssSafety(self.ctx),
            AuditStaticAssets(self.ctx),
        ]
        if self.args.run_tests:
            modules.append(AuditTestRunner(self.ctx))
        return modules

    def run(self) -> AuditReport:
        modules = self.get_modules()
        shared: dict[str, Any] = {}
        results: list[AuditResult] = []

        for mod in modules:
            if self.args.modules and mod.module_id not in self.args.modules:
                continue
            t0 = time.monotonic()
            result = mod.run(shared)
            result.duration_ms = (time.monotonic() - t0) * 1000
            results.append(result)
            shared[mod.module_id] = result

        score, grade = compute_score(results)
        summary = {"pass": 0, "warn": 0, "fail": 0}
        for res in results:
            summary[res.status.lower()] = summary.get(res.status.lower(), 0) + 1

        return AuditReport(
            timestamp=time.strftime("%Y-%m-%dT%H:%M:%S"),
            project_root=str(self.ctx.root),
            modules=results,
            total_score=score,
            grade=grade,
            summary=summary,
        )


# =============================================================================
# Scoring
# =============================================================================

def compute_score(results: list[AuditResult]) -> tuple[int, str]:
    if not results:
        return 0, "F"
    per_module = 100.0 / len(results)
    total = 0.0
    for res in results:
        if res.status == "PASS":
            total += per_module
        elif res.status == "WARN":
            total += per_module * 0.5
        # FAIL = 0
    score = round(total)
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"
    return score, grade


# =============================================================================
# Report Renderer
# =============================================================================

STATUS_ICONS = {"PASS": "+", "WARN": "~", "FAIL": "!"}


def render_terminal(report: AuditReport, verbose: bool = False) -> str:
    lines = []
    w = 80
    lines.append("=" * w)
    lines.append("LLM Safety Framework — Audit Report".center(w))
    lines.append(f"Generated: {report.timestamp}".center(w))
    lines.append("=" * w)
    lines.append("")

    # Summary table
    lines.append("  #  Module                             Status  Key Stats")
    lines.append("  " + "-" * (w - 4))
    for i, mod in enumerate(report.modules, 1):
        icon = STATUS_ICONS.get(mod.status, "?")
        # Build a short stats string
        stat_parts = []
        for k, v in mod.stats.items():
            if isinstance(v, dict):
                continue
            stat_parts.append(f"{k}={v}")
        stat_str = ", ".join(stat_parts[:3])
        if len(stat_str) > 30:
            stat_str = stat_str[:30] + "..."
        lines.append(f"  {i:2d}  {mod.module_name:<35s} [{icon}] {mod.status:<4s}  {stat_str}")
    lines.append("")

    # Detailed findings
    has_findings = False
    for mod in report.modules:
        findings = mod.findings
        if not verbose:
            findings = [f for f in findings if f.severity != "info"]
        if not findings:
            continue
        if not has_findings:
            lines.append("DETAILED FINDINGS")
            lines.append("-" * w)
            has_findings = True
        lines.append(f"\n  [{mod.module_name}]")
        for f in findings:
            sev = f.severity.upper()[:4]
            loc = f.file
            if f.line:
                loc += f":{f.line}"
            lines.append(f"    {sev:4s}  {loc:<45s}  {f.message}")
            if len(lines[-1]) > 120:
                # Wrap long lines
                lines[-1] = lines[-1][:117] + "..."

    if not has_findings:
        lines.append("  No warnings or errors found.")

    lines.append("")
    lines.append("=" * w)
    lines.append(f"  SCORE: {report.total_score}/100 ({report.grade})")
    lines.append(f"  Modules: {report.summary.get('pass', 0)} PASS, "
                 f"{report.summary.get('warn', 0)} WARN, "
                 f"{report.summary.get('fail', 0)} FAIL")
    lines.append("=" * w)
    return "\n".join(lines)


def render_json(report: AuditReport) -> str:
    def ser(obj):
        if hasattr(obj, "__dataclass_fields__"):
            return {k: getattr(obj, k) for k in obj.__dataclass_fields__}
        return str(obj)
    return json.dumps(report, default=ser, indent=2)


# =============================================================================
# Main
# =============================================================================

def main():
    parser = argparse.ArgumentParser(
        description="LLM Safety Framework — Automated Audit",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  py -3.13 scripts/audit.py                     # basic audit
  py -3.13 scripts/audit.py --run-tests         # include pytest execution
  py -3.13 scripts/audit.py --json              # JSON to stdout
  py -3.13 scripts/audit.py --modules plugin_manifests route_inventory
  py -3.13 scripts/audit.py --verbose           # show INFO findings
""",
    )
    parser.add_argument("--project-root", default=None,
                        help="Project root (auto-detected if run from scripts/)")
    parser.add_argument("--run-tests", action="store_true",
                        help="Also run pytest and include results")
    parser.add_argument("--json", action="store_true",
                        help="Output JSON to stdout")
    parser.add_argument("--output-dir", default="reports",
                        help="Directory for report files (default: reports/)")
    parser.add_argument("--modules", nargs="*",
                        help="Run only specific modules (by module_id)")
    parser.add_argument("--verbose", "-v", action="store_true",
                        help="Show INFO-level findings")
    args = parser.parse_args()

    # Auto-detect project root
    if args.project_root:
        root = Path(args.project_root).resolve()
    else:
        # Try relative to script location or cwd
        script_dir = Path(__file__).resolve().parent
        if (script_dir.parent / "src" / "web").exists():
            root = script_dir.parent
        elif (Path.cwd() / "src" / "web").exists():
            root = Path.cwd()
        else:
            print("ERROR: Cannot detect project root. Use --project-root.", file=sys.stderr)
            sys.exit(1)

    if not args.json:
        print(f"Auditing: {root}")
        print()

    ctx = ProjectContext(root)
    runner = AuditRunner(ctx, args)

    t0 = time.monotonic()
    report = runner.run()
    elapsed = (time.monotonic() - t0) * 1000

    # Terminal output
    if args.json:
        print(render_json(report))
    else:
        print(render_terminal(report, verbose=args.verbose))
        print(f"\n  Completed in {elapsed:.0f}ms")

        # Write report files
        out_dir = root / args.output_dir
        out_dir.mkdir(parents=True, exist_ok=True)

        json_path = out_dir / "audit_report.json"
        json_path.write_text(render_json(report), encoding="utf-8")

        txt_path = out_dir / "audit_report.txt"
        txt_path.write_text(render_terminal(report, verbose=True), encoding="utf-8")

        print(f"  Reports written to: {out_dir}/")

    # Exit code
    if report.summary.get("fail", 0) > 0:
        sys.exit(1)
    sys.exit(0)


if __name__ == "__main__":
    main()
