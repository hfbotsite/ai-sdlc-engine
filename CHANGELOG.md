# Changelog

All notable changes to the AI SDLC Engine are documented here.
Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/); versioning is SemVer.

## [0.1.0] - 2026-11-11

### Added
- TeamLead orchestration rules (`AGENTS.md`).
- Plugin manifest and local marketplace catalog.
- 8 subagents: requirements-analyst, architect, developer, qa-engineer, code-reviewer, security-auditor, performance-engineer, devops-release.
- 10 skills: teamlead-orchestration, project-onboarding, requirements-engineering, architecture-engineering, implementation-engineering, testing-engineering, code-quality-engineering, security-engineering, performance-engineering, devops-release-engineering.
- 10 commands: sdlc-start, sdlc-analyze, sdlc-plan, sdlc-implement, sdlc-review, sdlc-test, sdlc-security, sdlc-audit, sdlc-release, sdlc-status.
- Hooks: SessionStart, PostToolUseFailure, Stop.
- Policies: quality-gates, git-policy, security-policy, release-policy.
- Documentation set and structural validators.

### Notes
- First version deliberately ships defensive, non-blocking hooks. Hard access control (production config, secrets, critical files) is planned for 0.2.x after the base system is validated in real projects.
