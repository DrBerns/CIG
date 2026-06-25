# CIG Backlog
_Last updated: 2026-06-24 (seeded at project kickoff — fill in as work begins)_

Format: grouped by epic. Update this file in the same PR as the work.

---

## Known gaps (identified from architecture review)

- [ ] **Language parity for AI tools** — Note Optimizer, Clinical Polish, MRI Distiller,
      ICD-10 Lookup, CPT Lookup have no Spanish version
- [ ] **Language parity for financial tools** — Estimate Builders, Combined Ledger have
      no Spanish version
- [ ] **Outcome Assessments ES sync** — LEDD instrument was recently added to EN version;
      verify it was added to the ES version as well
- [ ] **MRI Script Builder filename** — `CIG_MRI_Script_Builder_FIXED (1).html` has a
      space and "(1)" in the filename; should be cleaned up for URL stability
- [ ] **Combined Ledger security** — review whether any API tokens or credentials are
      embedded in the HTML (flagged as a known issue in the sister SpineMed project)

---

## Planned work (fill in at first working session)

_No items yet — add epics here as scope is defined._

---

## Completed

- [x] **Changelog gate made requirable** (2026-06-25) — removed the `paths:` filter so the
      gate runs on every PR and can be a *required* status check without stranding docs-only
      PRs. Enables branch-protection Layer 1 (require PR + check, no admin bypass).
- [x] **CI gate hardened** (2026-06-24) — gate now requires CHANGELOG.md + BACKLOG.md + SESSION_STATE.md; nothing on honor system
- [x] **Docs scaffold** (PR #12, 2026-06-24) — CLAUDE.md, SYSTEM_BLUEPRINT.md, BACKLOG.md, CHANGELOG.md seed, changelog CI gate
- [x] LEDD outcome assessment added to `CIG_Outcome_Assessments.html`
- [x] Spanish Procedure Consent + dashboard tiles
- [x] Spanish versions of Signature Packet, Intake, Outcome Assessments
- [x] AI clinical tools cloned + rebranded from SpineMed (Note Optimizer,
      Clinical Polish, MRI Distiller, ICD-10 Lookup, CPT Lookup)
- [x] HIPAA email delivery on Signature Packet submit
- [x] Dual-location support (Tallahassee + Panama City) — estimate builders,
      weather widgets
