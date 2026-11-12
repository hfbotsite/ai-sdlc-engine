# Installation

## Prerequisites

- ZCode with plugin support (Settings → Plugin Management present).
- `node` on PATH (v18+) for the hook scripts. Hooks degrade safely:
  if node is missing, hooks simply do not run and never block sessions.

## Add the marketplace

1. Open ZCode → **Plugin Marketplace → Add → Add Plugin Marketplace**.
2. Paste the path to this repository's root directory
   (the directory containing `marketplace.json`).
3. Wait for the marketplace validation.

## Install the plugin

1. Find **AI SDLC Engine** in the marketplace listing.
2. Click **Install**.
3. Enable the plugin if it is not enabled automatically.

## Verify

- **Settings → Plugin Management**: plugin listed and enabled.
- **Settings → Skills**: `project-onboarding`, `testing-engineering`,
  `security-engineering`, `code-quality-engineering` present.
- **Settings → Subagents**: six agents from `ai-sdlc-engine/agents/` present.
- Type `/sdlc` in a chat: the eight `/sdlc-*` commands appear.
- Open a new session: the TeamLead rules should be visible as injected
  context (SessionStart hook).

## Updating

1. Pull the latest changes in this repository.
2. Bump version in `ai-sdlc-engine/.zcode-plugin/plugin.json` **and** the entry in
   `marketplace.json` **and** `VERSION` — ZCode detects updates by version.
3. In **Plugin Marketplace**, find the plugin and choose **Update**.

## Installing into a working project

1. Open the project in ZCode.
2. Ensure the AI SDLC Engine plugin is installed and enabled (plugins are
   global; no per-project copying).
3. Run `/sdlc-start` — it creates the project profile and proposes
   project-specific additions to the project's `AGENTS.md`.
4. The TeamLead rules arrive automatically via the SessionStart hook in
   every session; the project `AGENTS.md` only narrows/specializes them.

## Troubleshooting

- Commands missing → check the plugin is enabled; check Settings → Plugin
  Management detail view.
- Hook errors → verify `node --version` works in a terminal; hooks exit
  silently on failure by design.
- Marketplace rejected → verify `marketplace.json` is at the directory root
  you pasted and JSON is valid (`python tests/validate-manifest.py`).
