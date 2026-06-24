# CLAUDE.md — operating rules for CIG / Capital Injury Group portal

## HARD RULE — read context docs at session start
Before any non-trivial work, read these in order:
1. `docs/SESSION_STATE.md` — where we are right now (if it exists)
2. `docs/BACKLOG.md` — what's on deck
3. `CHANGELOG.md` — what's already shipped
4. `docs/SYSTEM_BLUEPRINT.md` — architecture reference when you need it

## HARD RULE — changelog on every change (CI-enforced)
Every change to the site (HTML, JS, CSS, workflows) MUST include a `CHANGELOG.md`
entry in the same commit/PR. No changelog = PR is incomplete.
The CI gate (`changelog-gate.yml`) will fail any PR that touches site files without it.

## HARD RULE — update BACKLOG.md when scope changes
When a backlog item ships, mark it done. When a new one is identified, add it.
Do this in the same PR as the work, not as a follow-up.

## HARD RULE — propose before you dig or edit
Before any non-trivial investigation or change based on an assumption, state:
1. "I think the problem is X."
2. "I think the fix is A."
3. "Do you want me to proceed?"
Then wait for a yes. Exceptions: a single read-only fact lookup, or a direct explicit
instruction.

## HARD RULE — no assumptions; verify or ask
Never assume anything you cannot verify from the codebase or tool output. If uncertain,
ask the user. Do not theorize when the correct answer matters.

## HARD RULE — automate, don't hand off
If a tool can perform a task, Claude performs it. Never give the user a click-through
checklist or terminal commands to paste.

## Deploy model
- **No backend, no server.** Pure static HTML deployed to GitHub Pages.
- Push to `main` → `mri_script.yml` → GitHub Pages deploy. Live within ~1 minute.
- All processing runs in-browser (pdf-lib, html2pdf.js, localStorage).
- Claude API calls go through the Cloudflare Worker proxy (API key never in the HTML).
- **Never hardcode the Claude API key or any secret in any HTML/JS file.**

## Compliance (non-negotiable)
- HIPAA forms and consent documents must never be altered in substance without
  explicit instruction — wording has legal significance.
- English and Spanish versions of the same form must stay in sync. When one changes,
  flag the other for update.
- CIG and SpineMed/PainMed must never be cross-linked or cross-branded.
- The Cloudflare Worker CORS lock (`drberns.github.io`) must not be widened.

## Where state lives

| File | Purpose | Updated when |
|---|---|---|
| `CLAUDE.md` | Rules + this index | Rule changes only |
| `docs/SYSTEM_BLUEPRINT.md` | What exists and how it fits | Architecture changes |
| `docs/BACKLOG.md` | What's left to build | Scope changes; each session |
| `docs/SESSION_STATE.md` | Where we are right now | Each session |
| `CHANGELOG.md` | What shipped (CI-enforced) | Every change |
