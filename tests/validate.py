#!/usr/bin/env python
"""Structural validator for the AI SDLC Engine repository.

Checks manifest consistency, declared resources, frontmatter of
agents/skills/commands, and hook wiring. Stdlib only.

Usage: python tests/validate.py
Exit code 0 = all checks passed.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PLUGIN = ROOT / "ai-sdlc-engine"
ERRORS: list[str] = []
WARNINGS: list[str] = []


def err(msg: str) -> None:
    ERRORS.append(msg)


def warn(msg: str) -> None:
    WARNINGS.append(msg)


def parse_frontmatter(text: str) -> tuple[dict[str, str], str]:
    """Flat YAML frontmatter parser: single-line top-level keys only."""
    if not text.startswith("---"):
        return {}, text
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n?(.*)$", text, re.DOTALL)
    if not m:
        return {}, text
    fm_block, body = m.group(1), m.group(2)
    fm: dict[str, str] = {}
    for line in fm_block.splitlines():
        if not line.strip() or line.startswith((" ", "\t")):
            if line.strip():
                warn(f"indented frontmatter line dropped: {line.strip()!r}")
            continue
        if ":" in line:
            key, _, value = line.partition(":")
            fm[key.strip()] = value.strip()
    return fm, body


def check_manifest() -> dict:
    mp = PLUGIN / ".zcode-plugin" / "plugin.json"
    try:
        manifest = json.loads(mp.read_text(encoding="utf-8"))
    except Exception as e:
        err(f"plugin.json is not valid JSON: {e}")
        return {}
    if manifest.get("name") != PLUGIN.name:
        err(f"manifest name {manifest.get('name')!r} != directory name {PLUGIN.name!r}")
    for key in ("agents", "skills", "commands"):
        sub = PLUGIN / str(manifest.get(key, ""))
        if manifest.get(key) and not sub.is_dir():
            err(f"manifest declares {key}={manifest[key]!r} but {sub} is missing")
    version = manifest.get("version")
    if not version:
        err("plugin.json has no version")
    return manifest


def check_marketplace(manifest: dict) -> None:
    mp = ROOT / "marketplace.json"
    try:
        catalog = json.loads(mp.read_text(encoding="utf-8"))
    except Exception as e:
        err(f"marketplace.json is not valid JSON: {e}")
        return
    entries = {p.get("name"): p for p in catalog.get("plugins", [])}
    entry = entries.get(manifest.get("name", ""))
    if entry is None:
        err("marketplace.json has no entry for the plugin")
        return
    if entry.get("version") != manifest.get("version"):
        err(f"marketplace version {entry.get('version')} != manifest version {manifest.get('version')}")
    source = entry.get("source")
    src = (mp.parent / str(source)).resolve() if source else None
    if not src or src != PLUGIN.resolve():
        err(f"marketplace source {source!r} does not resolve to the plugin directory")
    # path containment
    if src and ROOT.resolve() not in src.parents:
        err("marketplace source escapes the repository root")


def check_version_file(manifest: dict) -> None:
    vf = ROOT / "VERSION"
    if not vf.is_file():
        err("VERSION file missing")
        return
    v = vf.read_text(encoding="utf-8").strip()
    if v != manifest.get("version"):
        err(f"VERSION ({v}) != manifest version ({manifest.get('version')})")


def check_agents() -> None:
    agents_dir = PLUGIN / "agents"
    expected = {
        "requirements-analyst", "architect", "developer",
        "qa-engineer", "code-reviewer", "security-auditor",
    }
    found: set[str] = set()
    for f in agents_dir.glob("*.md"):
        fm, _ = parse_frontmatter(f.read_text(encoding="utf-8"))
        found.add(fm.get("name", f.stem))
        if "name" not in fm:
            err(f"agent {f.name}: missing frontmatter name")
        if not fm.get("description"):
            err(f"agent {f.name}: missing frontmatter description")
        if fm.get("model") != "inherit":
            err(f"agent {f.name}: model must be 'inherit', got {fm.get('model')!r}")
        if "\n" in str(fm.get("description", "")):
            err(f"agent {f.name}: multi-line description (flat parser drops it)")
    missing = expected - found
    if missing:
        err(f"agents missing: {sorted(missing)}")
    extra = found - expected
    if extra:
        warn(f"agents not in expected set: {sorted(extra)}")


def check_skills() -> None:
    skills_dir = PLUGIN / "skills"
    expected = {
        "project-onboarding", "testing-engineering",
        "security-engineering", "code-quality-engineering",
    }
    found: set[str] = set()
    for d in skills_dir.iterdir():
        if not d.is_dir():
            warn(f"unexpected file in skills/: {d.name}")
            continue
        found.add(d.name)
        sm = d / "SKILL.md"
        if not sm.is_file():
            err(f"skill {d.name}: SKILL.md missing")
            continue
        fm, body = parse_frontmatter(sm.read_text(encoding="utf-8"))
        if fm.get("name") != d.name:
            err(f"skill {d.name}: frontmatter name {fm.get('name')!r} != directory name")
        if not fm.get("description"):
            err(f"skill {d.name}: missing frontmatter description")
        if len(body.strip()) < 200:
            err(f"skill {d.name}: body too short to be a real procedure")
    missing = expected - found
    if missing:
        err(f"skills missing: {sorted(missing)}")
    extra = found - expected
    if extra:
        warn(f"skills not in expected set: {sorted(extra)}")


def check_commands() -> None:
    commands_dir = PLUGIN / "commands"
    expected = {
        "sdlc-start", "sdlc-analyze", "sdlc-plan", "sdlc-implement",
        "sdlc-review", "sdlc-test", "sdlc-release", "sdlc-status",
    }
    valid_keys = {"description", "argument-hint", "allowed-tools", "model",
                  "skills", "disable-noninteractive"}
    known_skills = {d.name for d in (PLUGIN / "skills").iterdir() if d.is_dir()}
    found: set[str] = set()
    for f in commands_dir.glob("*.md"):
        name = f.stem
        found.add(name)
        fm, body = parse_frontmatter(f.read_text(encoding="utf-8"))
        if not fm.get("description"):
            err(f"command {name}: missing frontmatter description")
        if not body.strip():
            err(f"command {name}: empty body (command would be dropped)")
        bad = set(fm) - valid_keys
        if bad:
            err(f"command {name}: unknown frontmatter keys {sorted(bad)} (misspelling?)")
        for s in re.findall(r"[\w-]+", fm.get("skills", "")):
            if s not in known_skills:
                err(f"command {name}: mounts unknown skill {s!r}")
        if "$ARGUMENTS" in body and "argument-hint" not in fm:
            warn(f"command {name}: uses $ARGUMENTS without argument-hint")
    missing = expected - found
    if missing:
        err(f"commands missing: {sorted(missing)}")
    extra = found - expected
    if extra:
        warn(f"commands not in expected set: {sorted(extra)}")


VALID_EVENTS = {"SessionStart", "UserPromptSubmit", "PreToolUse",
                "PermissionRequest", "PostToolUse", "PostToolUseFailure", "Stop"}


def check_hooks() -> None:
    hp = PLUGIN / "hooks" / "hooks.json"
    try:
        cfg = json.loads(hp.read_text(encoding="utf-8"))
    except Exception as e:
        err(f"hooks.json is not valid JSON: {e}")
        return
    hooks = cfg.get("hooks", {})
    if not hooks:
        err("hooks.json declares no events")
    for event, groups in hooks.items():
        if event not in VALID_EVENTS:
            err(f"unsupported hook event: {event}")
        for group in groups:
            for h in group.get("hooks", []):
                if h.get("type") != "process":
                    err(f"{event}: only type 'process' is used in this repo")
                args = h.get("args", [])
                for a in args:
                    if "${CLAUDE_PLUGIN_ROOT}" not in a and "${ZCODE_PLUGIN_ROOT}" not in a:
                        err(f"{event}: arg {a!r} does not reference ${{CLAUDE_PLUGIN_ROOT}}")
                    bad = re.findall(r"\$\{[A-Z_]+\}", a)
                    for b in bad:
                        if b not in ("${CLAUDE_PLUGIN_ROOT}", "${ZCODE_PLUGIN_ROOT}"):
                            err(f"{event}: unsupported template variable {b}")
                script = args[0].replace("${CLAUDE_PLUGIN_ROOT}/", "").replace("${ZCODE_PLUGIN_ROOT}/", "") if args else ""
                if script and not (PLUGIN / script).is_file():
                    err(f"{event}: hook script {script} missing")


def check_root_docs() -> None:
    for f in ("AGENTS.md", "README.md", "CHANGELOG.md"):
        if not (ROOT / f).is_file():
            err(f"root file missing: {f}")
    agents_text = (ROOT / "AGENTS.md").read_text(encoding="utf-8") if (ROOT / "AGENTS.md").is_file() else ""
    hook_text = (PLUGIN / "hooks" / "session-start.mjs").read_text(encoding="utf-8") if (PLUGIN / "hooks" / "session-start.mjs").is_file() else ""
    for marker in ("TeamLead", "quality gates", "user approval"):
        if marker.lower() not in agents_text.lower():
            warn(f"AGENTS.md does not mention {marker!r}")
        if marker.lower() not in hook_text.lower():
            warn(f"session-start.mjs rules do not mention {marker!r} (AGENTS.md/hook drift)")


def main() -> int:
    manifest = check_manifest()
    check_marketplace(manifest)
    check_version_file(manifest)
    check_agents()
    check_skills()
    check_commands()
    check_hooks()
    check_root_docs()

    if WARNINGS:
        print("Warnings:")
        for w in WARNINGS:
            print(f"  [warn] {w}")
    if ERRORS:
        print("Errors:")
        for e in ERRORS:
            print(f"  [error] {e}")
        print(f"\nFAILED: {len(ERRORS)} error(s), {len(WARNINGS)} warning(s)")
        return 1
    print(f"OK: all checks passed ({len(WARNINGS)} warning(s))")
    return 0


if __name__ == "__main__":
    sys.exit(main())
