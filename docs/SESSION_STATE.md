# What's going on right now — updated 2026-06-25

## This session (2026-06-25) — make the docs gate enforceable

The `changelog-gate.yml` now runs on every PR (no `paths:` filter) so it can be set as a
*required* status check in a branch ruleset on `main` — the missing piece that made the gate
advisory. Next: enable the ruleset (require PR + this check, empty bypass list) so changes
can't merge without the three docs. Same hardening applied across JFBDC, SpineMed, PainMed.

---

# (prior) What's going on right now — updated 2026-06-24

## This session (2026-06-24) — docs scaffold + CI gate hardening

**Completed this session:**
- **PR #12 merged** — docs scaffold: `CLAUDE.md` rules, `docs/SYSTEM_BLUEPRINT.md`,
  `docs/BACKLOG.md`, `CHANGELOG.md` seed, `.github/workflows/changelog-gate.yml`
  (CHANGELOG.md only at first).
- **Gate hardened** — `changelog-gate.yml` now requires all three docs on every code PR:
  CHANGELOG.md + docs/BACKLOG.md + docs/SESSION_STATE.md. Nothing is on honor system.
- **`CLAUDE.md` updated** — hard rule now says "update all three docs on every change
  (CI-enforced)" instead of just CHANGELOG.md.

**No code/HTML/JS changes this session.** Gate and doc improvements only.

---

## Current state of the site (as of 2026-06-24)

See `docs/SYSTEM_BLUEPRINT.md` for full architecture. Summary:

- **Pure static HTML** on GitHub Pages (`drberns.github.io/cig/`). No backend.
- **Claude API** proxied through Cloudflare Worker (`spinemed-anthropic-proxy.drberns.workers.dev`).
  Auth: `x-api-secret: SpineMed2026`. CORS locked to `drberns.github.io`.
- **API key** is in the Cloudflare Worker secret only — never in any HTML/JS file.
- **EN + ES** versions of all forms. Spanish versions were created in a prior sprint
  (see BACKLOG.md Completed section).

---

## Open items to carry forward

See `docs/BACKLOG.md` for full list. Known gaps:

- **Language parity for AI tools** — Note Optimizer, Clinical Polish, MRI Distiller,
  ICD-10 Lookup, CPT Lookup have no Spanish version
- **Language parity for financial tools** — Estimate Builders, Combined Ledger have
  no Spanish version
- **Outcome Assessments ES sync** — LEDD was added to EN; verify ES version is in sync
- **MRI Script Builder filename** — has space + "(1)" in filename; URL stability risk
- **Combined Ledger security** — review for embedded API tokens/credentials

---

## Compliance constraints (carry into every session)

- HIPAA forms and consent documents must never be altered in substance without
  explicit instruction.
- English and Spanish versions of the same form must stay in sync.
- CIG and SpineMed/PainMed must never be cross-linked or cross-branded.
- The Cloudflare Worker CORS lock (`drberns.github.io`) must not be widened.
- API key must never appear in any HTML/JS file.

**Dev branch:** `claude/friendly-planck-spm4d3`
