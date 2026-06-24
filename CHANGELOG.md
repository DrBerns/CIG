# Changelog

All notable changes to the CIG / Capital Injury Group portal are recorded here.

**Policy:** every change to the site (HTML, JS, CSS, workflows) MUST be added here
as part of the same change. This file is the durable timeline — do not rely on
session memory or `docs/SESSION_STATE.md` alone. CI enforces this on every PR.

Format: reverse-chronological. Newest at top.

---

## 2026-06-24

### CI gate hardened: now requires CHANGELOG.md + BACKLOG.md + SESSION_STATE.md
- `changelog-gate.yml` updated — PRs missing any of the three required docs now fail CI
- `CLAUDE.md` updated to reflect the new three-doc rule
- `docs/SESSION_STATE.md` created with current session state (first-ever SESSION_STATE for CIG)
- Fixes the "honor system" gap: nothing is optional anymore

### Doc scaffold: CLAUDE.md, system blueprint, backlog, CI changelog gate
- `CLAUDE.md` added — auto-loads rules + doc index every session
- `docs/SYSTEM_BLUEPRINT.md` — full architecture reference (stack, site map,
  language parity status, Cloudflare Worker details, compliance notes)
- `docs/BACKLOG.md` — seeded with known gaps and completed history
- `.github/workflows/changelog-gate.yml` — CI gate: fails PRs that touch
  HTML/JS/CSS or workflows without a CHANGELOG.md entry

---

## Earlier history

_Entries below are seeded from git log at scaffold time. Exact dates not confirmed —
use `git log --oneline` for precise history._

- Added LEDD (Loss of Enjoyment & Duties Under Duress) to Outcome Assessments
- Added Spanish Procedure Consent (`CIG_Procedure_Consent_ES_v_04.22.26.html`)
  and dashboard tiles for ES consent + intake
- Dropped Hospital Bill Estimator clone (dead end)
- Cloned 4 SpineMed tools into CIG with brand swap: Note Optimizer, Clinical Polish,
  MRI Distiller, ICD-10 Lookup
- Added HIPAA email delivery on Signature Packet submit
- Localized Florida state seal asset (removed external dependency)
- Rebranded SpineMed color palette to CIG burgundy (`#9e1b32`)
- Initial Spanish Signature Packet and Intake forms
