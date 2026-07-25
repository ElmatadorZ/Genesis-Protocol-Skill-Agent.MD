"""The Genesis Protocol contract.

This is a single-file cognitive OS: a model reads SKILL.md and runs the pipeline
described in it. There is no Python to unit-test, so the tests hold the markdown
to the guarantees it makes — the epistemic separation, the non-skippable Skeptic
gate, and the laws that keep it from overreaching.
"""
from __future__ import annotations

import re
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
SKILL = ROOT / "SKILL.md"


def _split():
    text = SKILL.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    assert m, "frontmatter must be present and delimited"
    return yaml.safe_load(m.group(1)), text[m.end():]


def test_canonical_filename():
    assert SKILL.exists()


def test_frontmatter_and_license():
    fm, _ = _split()
    for f in ("name", "description", "license", "version"):
        assert f in fm, f"frontmatter must declare '{f}'"
    # The frontmatter license must agree with the LICENSE file — they disagreed
    # once (frontmatter said Open Cognitive while LICENSE was Apache-2.0).
    assert str(fm["license"]).lower().replace(" ", "-") == "apache-2.0"


def test_name_slug_safe():
    fm, _ = _split()
    assert re.fullmatch(r"[a-z0-9][a-z0-9-]*", str(fm["name"]))


def test_metadata_bounds_scope():
    fm, _ = _split()
    meta = fm.get("metadata", {})
    assert meta.get("compatibility")
    assert meta.get("not_for")


def test_known_inferred_unknown_separation():
    _, body = _split()
    for word in ("Known", "Inferred", "Unknown"):
        assert word in body, f"FPCOS decomposition must label '{word}'"


def test_skeptic_gate_is_present_and_unskippable():
    _, body = _split()
    assert re.search(r"skeptic", body, re.I)
    assert re.search(r"cannot be skipped|shadow gate", body, re.I)


def test_scenarios_not_single_prediction():
    _, body = _split()
    assert re.search(r"scenarios not predictions|≥\s*2 scenarios", body, re.I)


def test_abstain_over_fabricate_is_a_law():
    _, body = _split()
    assert re.search(r"abstain", body, re.I)
    assert re.search(r"\[UNVERIFIED\]|unverified", body, re.I)


def test_human_decides():
    _, body = _split()
    assert re.search(r"human decides", body, re.I)
