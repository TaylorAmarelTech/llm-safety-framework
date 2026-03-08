Legacy Code Archive
===================
Archived: 2026-02-13
Reason:   Plugin architecture migration completed.
          All routes now served by src/web/plugins/ (10 plugins).
          These files are no longer imported by the application.

Contents
--------

legacy_routes_package/
    The routes/ package that was previously imported by app.py via
    "from .routes import api_router". Contains 12 .py files:
    __init__.py, analytics.py, data_management.py, endpoints.py,
    health.py, integrations.py, intelligent_attack.py, multi_turn.py,
    prompts.py, scraper.py, spinning.py, wizard.py.

    Also includes routes_single_file.py (the original monolithic
    routes.py that predated the routes/ package split).

legacy_monolith/
    index.html - The original single-file SPA (~8400 lines, 462KB)
    that contained all HTML sections and JS for every feature.
    Replaced by shell.html + per-plugin fragment.html/fragment.js.

Replacement
-----------
All functionality is now provided by:
  - src/web/plugins/       (10 plugin packages with routes + fragments)
  - src/web/static/shell.html  (plugin-aware SPA shell)
  - src/web/app.py         (mounts plugins, inline /api/health)
