#!/usr/bin/env python3
"""
Database Import Script

Imports test cases from JSON files into SQLite database for the
LLM Safety Testing Framework.

Usage:
    python scripts/import_database.py
    python scripts/import_database.py --json-dir data/test_suites --db data/tests.db
"""

import argparse
import json
import sqlite3
from pathlib import Path
from datetime import datetime
import sys

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent))


def create_database_schema(conn: sqlite3.Connection):
    """Create the database schema."""
    cursor = conn.cursor()

    # Tests table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tests (
            id TEXT PRIMARY KEY,
            prompt TEXT NOT NULL,
            category TEXT,
            subcategory TEXT,
            difficulty_level TEXT,
            corridor TEXT,
            attack_type TEXT,
            attack_sophistication TEXT,
            ilo_indicators TEXT,  -- JSON array
            exploitation_types TEXT,  -- JSON array
            metadata TEXT,  -- Full JSON metadata
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    # Test suites table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS test_suites (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE NOT NULL,
            description TEXT,
            total_tests INTEGER DEFAULT 0,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    # Test to suite mapping
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS test_suite_mapping (
            test_id TEXT,
            suite_id INTEGER,
            PRIMARY KEY (test_id, suite_id),
            FOREIGN KEY (test_id) REFERENCES tests(id),
            FOREIGN KEY (suite_id) REFERENCES test_suites(id)
        )
    """)

    # Test runs table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS test_runs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            test_id TEXT,
            model_name TEXT,
            model_provider TEXT,
            response TEXT,
            is_harmful BOOLEAN,
            harm_score REAL,
            confidence REAL,
            evaluation_method TEXT,
            latency_ms REAL,
            tokens_used INTEGER,
            cost REAL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (test_id) REFERENCES tests(id)
        )
    """)

    # Models table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS models (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE NOT NULL,
            provider TEXT,
            version TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    # Create indexes
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_tests_category ON tests(category)")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_tests_corridor ON tests(corridor)")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_tests_difficulty ON tests(difficulty_level)")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_test_runs_model ON test_runs(model_name)")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_test_runs_harmful ON test_runs(is_harmful)")

    conn.commit()
    print("[+] Database schema created")


def import_json_file(conn: sqlite3.Connection, json_path: Path, suite_name: str = None):
    """Import tests from a JSON file."""
    cursor = conn.cursor()

    print(f"[*] Importing: {json_path.name}")

    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Determine suite name from file or metadata
    if suite_name is None:
        suite_name = json_path.stem.replace('_tests', '').replace('_', ' ').title()

    # Create suite if needed
    cursor.execute(
        "INSERT OR IGNORE INTO test_suites (name, description) VALUES (?, ?)",
        (suite_name, f"Imported from {json_path.name}")
    )
    cursor.execute("SELECT id FROM test_suites WHERE name = ?", (suite_name,))
    suite_id = cursor.fetchone()[0]

    # Handle different JSON structures
    tests = []
    if 'tests' in data:
        tests = data['tests']
    elif 'test_suites' in data:
        # Flatten test suites
        for suite_tests in data['test_suites'].values():
            tests.extend(suite_tests)
    elif 'test_cases' in data:
        tests = data['test_cases']
    elif isinstance(data, list):
        tests = data

    imported = 0
    skipped = 0

    for test in tests:
        try:
            test_id = test.get('id', f"imported_{imported}")

            # Extract fields
            prompt = test.get('prompt', '')
            category = test.get('category', '')
            subcategory = test.get('subcategory', '')
            difficulty = test.get('difficulty', test.get('difficulty_level', ''))
            corridor = test.get('corridor', '')
            attack_type = test.get('attack_type', '')
            attack_sophistication = test.get('attack_sophistication', '')

            # Handle metadata
            metadata = test.get('metadata', {})
            if not isinstance(metadata, dict):
                metadata = {}

            ilo_indicators = test.get('ilo_indicators', metadata.get('ilo_indicators', []))
            exploitation_types = metadata.get('exploitation_types', [])

            # Insert test
            cursor.execute("""
                INSERT OR REPLACE INTO tests
                (id, prompt, category, subcategory, difficulty_level, corridor,
                 attack_type, attack_sophistication, ilo_indicators, exploitation_types, metadata)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                test_id,
                prompt,
                category,
                subcategory,
                difficulty,
                corridor,
                attack_type,
                attack_sophistication,
                json.dumps(ilo_indicators) if ilo_indicators else None,
                json.dumps(exploitation_types) if exploitation_types else None,
                json.dumps(metadata)
            ))

            # Map to suite
            cursor.execute(
                "INSERT OR IGNORE INTO test_suite_mapping (test_id, suite_id) VALUES (?, ?)",
                (test_id, suite_id)
            )

            imported += 1

        except Exception as e:
            print(f"    [!] Error importing test: {e}")
            skipped += 1

    # Update suite count
    cursor.execute(
        "UPDATE test_suites SET total_tests = ? WHERE id = ?",
        (imported, suite_id)
    )

    conn.commit()
    print(f"    [+] Imported {imported} tests, skipped {skipped}")

    return imported


def main():
    parser = argparse.ArgumentParser(description='Import tests into SQLite database')
    parser.add_argument(
        '--json-dir', '-j',
        type=Path,
        default=Path(__file__).parent.parent / 'data',
        help='Directory containing JSON test files'
    )
    parser.add_argument(
        '--db', '-d',
        type=Path,
        default=Path(__file__).parent.parent / 'data' / 'safety_tests.db',
        help='SQLite database path'
    )
    parser.add_argument(
        '--file', '-f',
        type=Path,
        help='Import a single JSON file'
    )

    args = parser.parse_args()

    print("=" * 70)
    print("  LLM Safety Framework - Database Import")
    print("=" * 70)
    print()

    # Create database directory if needed
    args.db.parent.mkdir(parents=True, exist_ok=True)

    # Connect to database
    conn = sqlite3.connect(str(args.db))

    # Create schema
    create_database_schema(conn)

    total_imported = 0

    if args.file:
        # Import single file
        if args.file.exists():
            total_imported = import_json_file(conn, args.file)
        else:
            print(f"[!] File not found: {args.file}")
    else:
        # Import all JSON files from directory
        json_files = list(args.json_dir.glob('*.json'))

        # Also check test_suites subdirectory
        test_suites_dir = args.json_dir / 'test_suites'
        if test_suites_dir.exists():
            json_files.extend(test_suites_dir.glob('*.json'))

        print(f"[*] Found {len(json_files)} JSON files")
        print()

        for json_file in sorted(json_files):
            imported = import_json_file(conn, json_file)
            total_imported += imported

    # Print summary
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM tests")
    total_tests = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM test_suites")
    total_suites = cursor.fetchone()[0]

    print()
    print("=" * 70)
    print("  Import Complete")
    print("=" * 70)
    print(f"  Database: {args.db}")
    print(f"  Total tests in database: {total_tests:,}")
    print(f"  Total suites: {total_suites}")
    print(f"  Tests imported this run: {total_imported:,}")
    print()

    conn.close()


if __name__ == '__main__':
    main()
