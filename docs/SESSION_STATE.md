# SESSION_STATE — Capital Injury Group (CIG)

> **Purpose:** our shared, cross-device memory. Read this at the **start** of every
> session; update it at the **end** of every session that changes anything, then
> commit + push. This file lives in git so it's the same on the home PC, on mobile,
> and in every Claude Code web/cloud session. Nothing else persists between sessions.

> **How to update:** add a new dated entry at the top of the **Session log**. Keep
> **Current focus** and **Open threads** accurate. Move finished items to **Done**.

---

## Project snapshot
- **What:** static HTML tools + bilingual patient forms for CIG, deployed to GitHub
  Pages on push to `main`. See `CLAUDE.md` for the full repo map and the Cloudflare
  Worker backends.
- **Repo:** `DrBerns/CIG` (this repo).
- **Live:** served from `drberns.github.io`.

## Current focus
- Establishing a durable, cross-device context/memory system (this file + `CLAUDE.md`).

## Open threads / TODO
- _(none recorded yet — add items here as they come up)_

## Decisions & gotchas (don't relearn these)
- Cloud session containers are **ephemeral** — anything not committed + pushed is
  lost. (This is why the previous session-state doc disappeared: it was created in a
  container and never pushed.)
- AI tools route through `spinemed-anthropic-proxy` Worker; the Anthropic key is
  never in the front-end. Worker CORS is locked to `drberns.github.io`.
- Several Worker URLs still carry the old **"spinemed"** name even though the product
  is now CIG — that's expected, not a bug to "fix" blindly.
- Patient forms are **bilingual** — English + Spanish twin files; keep them in sync.

## Done (recent history, newest first)
- LEDD (Loss of Enjoyment & Duties Under Duress) OATs assessment added (#9).
- Spanish Procedure Consent + dashboard tiles added (#8).
- Signature Packet rebranded from SpineMed → CIG burgundy; Florida seal localized.
- HIPAA Notice PDF emailed to patient on signature-packet submit.

---

## Session log

### 2026-06-17 — Set up cross-device context system
- **Device:** mobile (web session). Branch: `claude/session-setup-context-fxqraa`.
- Discovered the prior session's "session state" doc was never committed, so it was
  gone (ephemeral container). Searched all branches + full git history to confirm.
- Created **`CLAUDE.md`** (auto-loaded every session, repo map + working agreement)
  and **`docs/SESSION_STATE.md`** (this file) as the durable memory system.
- **Next time:** read `CLAUDE.md` → read this file → work → update this file → push.
