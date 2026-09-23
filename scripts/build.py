#!/usr/bin/env python3
"""Assemble the deployable static site.

Reads every JSON file in cases/, validates the minimal contract the
front-end relies on, merges them into data/cases.json and copies the
static shell from site/ into _site/. A validation error aborts the build,
so a broken entry can never replace the live dataset.
"""
import json
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "site"
CASES = ROOT / "cases"
OUT = ROOT / "_site"

REQUIRED = [
    "slug", "name", "filing_year", "status", "geography", "jurisdiction",
    "docket", "at_issue", "abstract", "topics", "proceedings", "sources",
]
FORUM_TYPES = ("Domestic", "CJEU", "ECtHR")


def fail(msg: str) -> None:
    print(f"BUILD FAILED: {msg}", file=sys.stderr)
    sys.exit(1)


def load_cases() -> list:
    files = sorted(CASES.glob("*.json"))
    if not files:
        fail("no case files found in cases/")
    cases, slugs = [], set()
    for path in files:
        try:
            case = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            fail(f"{path.name}: invalid JSON ({exc})")
        missing = [k for k in REQUIRED if k not in case]
        if missing:
            fail(f"{path.name}: missing fields {missing}")
        if case["slug"] in slugs:
            fail(f"{path.name}: duplicate slug '{case['slug']}'")
        slugs.add(case["slug"])
        for key in ("country", "iso_n3"):
            if not case["geography"].get(key):
                fail(f"{path.name}: geography.{key} is required")
        if not str(case["geography"]["iso_n3"]).isdigit() or len(str(case["geography"]["iso_n3"])) != 3:
            fail(f"{path.name}: geography.iso_n3 must be a 3-digit code, got '{case['geography']['iso_n3']}'")
        if case["jurisdiction"].get("type") not in FORUM_TYPES:
            fail(f"{path.name}: jurisdiction.type must be one of {FORUM_TYPES}")
        try:
            case["filing_year"] = int(case["filing_year"])
        except (TypeError, ValueError):
            fail(f"{path.name}: filing_year must be a number")
        for proc in case["proceedings"]:
            proc["link"] = proc.get("link") or None
        for src in case["sources"]:
            src["url"] = src.get("url") or None
        cases.append(case)
    cases.sort(key=lambda c: (-c["filing_year"], c["name"]))
    return cases


def main() -> None:
    cases = load_cases()
    if OUT.exists():
        shutil.rmtree(OUT)
    shutil.copytree(SITE, OUT)
    dest = OUT / "data" / "cases.json"
    dest.write_text(json.dumps(cases, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"built _site/ with {len(cases)} cases")


if __name__ == "__main__":
    main()
