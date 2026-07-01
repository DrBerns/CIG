# Permissions & session-launch model

_Authoritative record so this decision never evaporates between sessions again._
_Established 2026-07-01; replicated from the SpineMed repo where the model originated._

## The core principle

**Rules that matter must be enforced by the machine, not by Claude's memory.**
Permission prompts are consistent because they are a deterministic harness behavior;
Claude's prose promises are not, because they run on a fallible agent with amnesia
between sessions. So every rule that matters lives in enforced config + hooks
(`.claude/settings.json`, `.claude/hooks/guard.py`), not only in prose.

## The three tiers

### GREEN - auto-allowed, NEVER ask
Everything used every session: git/gh, python/pip, node/npx/npm, curl, wrangler,
cloudflared, nssm, read-only shell, file tools (Read/Edit/Write), and the MCP servers
(Cloudflare, Airtable, Chrome, Google Drive/Calendar, CMS Coverage, Supabase). Defined
in `.claude/settings.json` `allow`. No session-start tool-probing ritual.

### RED - hard-blocked, UNBYPASSABLE
The catastrophic, data-destroying class (a robocopy mirror once destroyed EMR data in
the SpineMed practice). Enforced by TWO layers: `.claude/settings.json` `deny` (deny
always wins) AND `.claude/hooks/guard.py`, a PreToolUse hook that inspects every
Bash/PowerShell command before it runs and blocks robocopy, `rm -rf`, recursive-force
`Remove-Item`, `del /s`, `format`, `diskpart`, `git push --force`, `git clean -f`. The
guard FAILS OPEN (only blocks known-bad; never benign work) and strips quoted spans so
a commit message mentioning these words is not itself blocked.

### YELLOW - ask once
Anything not GREEN; the harness prompts. Plus self-govern: always confirm before
patient-facing / outward-facing / materially-destructive actions.

## Session launch
Started from the desktop shortcut `CIG - Claude Code.lnk`, which runs plain `claude` in
NORMAL permission mode (NOT `--dangerously-skip-permissions` - that would disable the
RED deny layer). The no-prompt experience comes from the GREEN allowlist.

## Files
| File | Role |
|---|---|
| `.claude/settings.json` | GREEN allow + RED deny + hook registration |
| `.claude/hooks/guard.py` | PreToolUse RED enforcement, fails open, tested |
| `docs/PERMISSIONS.md` | This document |
