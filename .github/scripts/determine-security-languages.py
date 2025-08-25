#!/usr/bin/env python3
# file: .github/scripts/determine-security-languages.py
# version: 1.0.0
# guid: 7bbf6c2e-3f3c-4c6e-a0d4-9a2f6b7c8d90
"""
Determine which languages need security (CodeQL) scanning based on change
indicators provided via environment variables.

Intended to be invoked from GitHub Actions workflows that export boolean-like
variables (true/false, 1/0, yes/no) describing whether source files for a
language changed in the current push or PR, typically via a prior diff or
path-filter step.

Input Environment Variables (optional):
  GO_CHANGED          -> include Go (go)
  FRONTEND_CHANGED    -> include JavaScript/TypeScript (javascript)
  PYTHON_CHANGED      -> include Python (python)
  RUST_CHANGED        -> include Rust (rust)

Outputs (written to $GITHUB_OUTPUT):
  matrix              JSON object usable with strategy.matrix (e.g. {"language":["go","python"]})
  has-languages       true/false whether any languages present
  language-count      integer count of included languages
  languages           comma-separated list of language identifiers

Exit Codes:
  0 on success (even if no languages detected)
  1 on unexpected error

This mirrors the implementation present in other repositories (ghcommon, etc.)
so that reusable workflows referencing this script function uniformly.
"""

from __future__ import annotations

import json
import os
import sys
from typing import Dict, List


def _env_bool(key: str) -> bool:
    """Return True if the environment variable is set to a truthy value.

    Truthy values (case-insensitive): true, 1, yes, on
    """
    val = os.environ.get(key, "").strip().lower()
    return val in {"true", "1", "yes", "on"}


def _collect_languages() -> Dict[str, object]:
    """Collect languages to scan based on *_CHANGED environment variables.

    Returns a dictionary with matrix + metadata.
    """
    mapping = {
        "GO_CHANGED": "go",
        "FRONTEND_CHANGED": "javascript",  # Covers JS/TS family
        "PYTHON_CHANGED": "python",
        "RUST_CHANGED": "rust",
    }

    langs: List[str] = []

    print("🔍 Evaluating language change indicators:")
    for env_var, codeql_lang in mapping.items():
        if _env_bool(env_var):
            langs.append(codeql_lang)
            print(f"  ✓ {codeql_lang}: {env_var}=true")
        else:
            print(f"  - {codeql_lang}: {env_var}=false or unset")

    if langs:
        matrix = {"language": langs}
        has = True
        print(f"✅ Languages selected for scanning: {', '.join(langs)}")
    else:
        matrix = {"include": []}  # Empty matrix pattern
        has = False
        print("ℹ️  No languages selected (matrix will be empty)")

    result = {
        "matrix": matrix,
        "has_languages": has,
        "language_count": len(langs),
        "languages": langs,
    }
    print(f"Matrix JSON: {json.dumps(matrix)}")
    return result


def _write_output(key: str, value: str) -> None:
    """Append a key=value line to the GitHub Actions GITHUB_OUTPUT file."""
    path = os.environ.get("GITHUB_OUTPUT")
    if not path:
        # Fall back to stdout warning only (useful for local dry runs)
        print(f"[warn] GITHUB_OUTPUT not set; would write {key}={value}")
        return
    try:
        with open(path, "a", encoding="utf-8") as fh:
            fh.write(f"{key}={value}\n")
        print(f"⬆️  Wrote output: {key}={value}")
    except Exception as exc:  # pragma: no cover - defensive
        print(f"❌ Failed writing output {key}: {exc}")
        sys.exit(1)


def main() -> None:
    try:
        print("=== Determine Security Languages ===")
        result = _collect_languages()
        _write_output("matrix", json.dumps(result["matrix"]))
        _write_output("has-languages", str(result["has_languages"]).lower())
        _write_output("language-count", str(result["language_count"]))
        _write_output("languages", ",".join(result["languages"]))
        print("Done.")
    except Exception as exc:  # pragma: no cover - defensive
        print(f"❌ Unexpected error: {exc}")
        sys.exit(1)


if __name__ == "__main__":  # pragma: no cover
    main()
