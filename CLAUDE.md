# CLAUDE.md — Capital Injury Group (CIG) repo

> **Claude: read this every session.** Then open and read **`docs/SESSION_STATE.md`**
> before doing anything else — that is our cross-device "where we left off" log.
> At the **end** of any session where something meaningful changed, **update
> `docs/SESSION_STATE.md`** and commit + push it so the next session (on any
> device) has the context. The cloud containers are wiped after each session —
> if it isn't committed to git, it's gone.

## What this repo is
A collection of **static HTML tools and patient forms** for **Capital Injury Group
(CIG)** — a Florida injury/spine practice (Dr. Eldeeb). Everything is plain
HTML/CSS/JS (no build step). The whole repo is **deployed to GitHub Pages** on
every push to `main` (see `.github/workflows/mri_script.yml`). Live site is served
from `drberns.github.io`.

Origin: these tools were **cloned from an earlier "SpineMed" project and rebranded
to CIG** (burgundy palette). Some SpineMed names still linger in code/worker URLs.

## Map of the repo
- `index.html` — the **Document Portal** dashboard; tiles link to each tool.
- `widget_common.js` — shared helper. `callAnthropic()` and `extractJson()` for the
  AI-powered tools.
- **Patient forms:** `CIG_Intake.html`, `CIG_Procedure_Consent.html`,
  `CIG_Signature_Packet.html`, `CIG_Outcome_Assessments.html`
  (each has a Spanish counterpart: `_ES_v_04.22.26.html` or `_es.html`).
- **Clinical/billing tools:** `CIG_CPT_Lookup.html`, `CIG_ICD10_Lookup.html`,
  `CIG_MRI_Distiller.html`, `CIG_MRI_Script_Builder_FIXED (1).html`,
  `CIG_Note_Optimizer.html`, `CIG_Clinical_Polish.html`, `CIG_Combined_Ledger.html`.
- **Estimate builders:** `CIG_PanamaCity_Estimate_Builder.html`,
  `CIG_Tallahassee_Estimate_Builder.html`.
- **Assets:** CIG logos, Eldeeb signature PNGs, Florida State Seal.
- `docs/SESSION_STATE.md` — **living context log (read first, update last).**

## Backend services (Cloudflare Workers, owned by drberns)
- **`spinemed-anthropic-proxy.drberns.workers.dev`** — holds the Anthropic API key
  server-side; AI tools call it via `widget_common.js`. CORS locked to
  `drberns.github.io`. Default model: `claude-sonnet-4-6`. (Note: when changing
  models, use current Claude model IDs — e.g. Opus 4.8 = `claude-opus-4-8`,
  Sonnet 4.6 = `claude-sonnet-4-6`, Haiku 4.5 = `claude-haiku-4-5-20251001`.)
- **`cig-intake.drberns.workers.dev`** — `/consent-submit`, `/packet-submit`
  endpoints (form submission handling).
- **`spinemed-imap-worker.drberns.workers.dev`** — `/sendemail` (emails forms/PDFs
  to patients).

## Conventions
- Brand: CIG burgundy. Keep the rebrand consistent — don't reintroduce SpineMed
  branding in user-facing text.
- Bilingual: when editing a patient form, check whether its Spanish twin needs the
  same change.
- No framework, no bundler. Edit HTML/JS directly. Test by opening the file.
- Deployment = merge to `main`. PRs are created as **drafts** by default.

## Working agreement
- Most real work happens on the **home PC**; mobile/web sessions are for quick
  changes and review. Keep `docs/SESSION_STATE.md` current so either device can
  pick up the thread.
