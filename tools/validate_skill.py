#!/usr/bin/env python3
"""
validate_skill.py — integrity checks for Genesis Protocol.

READ-ONLY. Never modifies SKILL.md. This is a single-file cognitive OS, so the
guarantees live entirely in the markdown; the checks below hold the file to the
contract it advertises.

Run:  python tools/validate_skill.py
Exit: 0 pass · 1 fail
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:  # pragma: no cover
    pass

try:
    import yaml
except ImportError:
    print("Missing dependency: pyyaml. Install with: pip install pyyaml")
    sys.exit(1)

ROOT = Path(__file__).resolve().parent.parent
SKILL = ROOT / "SKILL.md"
REQUIRED = ["name", "description"]
RECOMMENDED = ["license", "version"]

results: list[tuple[str, bool]] = []


def check(name: str, cond) -> None:
    results.append((name, bool(cond)))
    print(f"  {'PASS' if cond else 'FAIL'}  {name}")


def main() -> int:
    if not SKILL.exists():
        print(f"FATAL: SKILL.md not found at {SKILL}")
        return 1
    text = SKILL.read_text(encoding="utf-8")

    print("\nINSTALLABILITY")
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    check("frontmatter present and delimited", m is not None)
    if not m:
        return 1
    try:
        fm = yaml.safe_load(m.group(1))
        check("frontmatter is valid YAML", isinstance(fm, dict))
    except yaml.YAMLError:
        check("frontmatter is valid YAML", False)
        return 1

    for f in REQUIRED:
        check(f"frontmatter has '{f}'", f in fm)
    check("name is slug-safe (a-z0-9-)",
          bool(re.fullmatch(r"[a-z0-9][a-z0-9-]*", str(fm.get("name", "")))))
    for f in RECOMMENDED:
        check(f"frontmatter declares '{f}'", f in fm)
    check("license is Apache-2.0 (matches LICENSE file)",
          str(fm.get("license", "")).lower().replace(" ", "-") == "apache-2.0")
    check("canonical filename is SKILL.md", SKILL.name == "SKILL.md")

    meta = fm.get("metadata", {}) if isinstance(fm.get("metadata"), dict) else {}
    check("metadata.compatibility declared", bool(meta.get("compatibility")))
    check("metadata.not_for bounds the scope", bool(meta.get("not_for")))

    body = text[m.end():]
    print("\nINTEGRITY")
    check("Known / Inferred / Unknown separation is specified",
          all(w in body for w in ("Known", "Inferred", "Unknown")))
    check("output states confidence",
          re.search(r"confidence", body, re.I) is not None)
    check("a Skeptic / shadow gate exists",
          re.search(r"skeptic|shadow gate", body, re.I) is not None)
    check("scenarios, not a single prediction",
          re.search(r"scenarios not predictions|≥\s*2 scenarios", body, re.I) is not None)
    check("abstain-over-fabricate is a stated law",
          re.search(r"abstain|unverified", body, re.I) is not None)
    check("human decides (no autonomous commands)",
          re.search(r"human decides", body, re.I) is not None)

    print("\nREPOSITORY")
    check("LICENSE exists", (ROOT / "LICENSE").exists())
    check("NOTICE exists", (ROOT / "NOTICE").exists())

    passed = sum(1 for _, ok in results if ok)
    total = len(results)
    print(f"\n{'=' * 52}\nVALIDATION: {passed}/{total} passed")
    if passed != total:
        print("FAILED:", [n for n, ok in results if not ok])
        return 1
    print(f"{SKILL.name} is installable and structurally intact.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
