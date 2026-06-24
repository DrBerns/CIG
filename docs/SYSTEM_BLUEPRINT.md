# CIG / Capital Injury Group — System Blueprint
_Last updated: 2026-06-24_

---

## What it is

Patient-facing and staff-facing portal for Capital Injury Group — a medical injury/pain
management clinic with offices in Tallahassee, FL and Panama City, FL. Provides intake
forms, consent packets, clinical outcome assessments, AI-powered documentation tools,
cost estimators, and a staff dashboard. No backend; entirely static HTML on GitHub Pages.

---

## Hosting & Deploy

| Item | Value |
|---|---|
| Platform | GitHub Pages |
| URL | `https://drberns.github.io/CIG/` |
| Deploy trigger | Push to `main` → `mri_script.yml` → Pages deploy (~1 min) |
| Build step | None — pure static HTML, no compilation |
| CDN/CORS | Cloudflare Workers proxy locks CORS to `drberns.github.io` |

---

## Stack

```
Browser
  ├── HTML5 / CSS3 / Vanilla JavaScript (no frameworks)
  ├── pdf-lib v1.17.1        — client-side PDF merge/manipulation
  ├── html2pdf.js v0.10.1    — client-side form-to-PDF export
  └── Google Fonts (Libre Baskerville, DM Sans)

Claude API (via Cloudflare Worker proxy)
  └── spinemed-anthropic-proxy.drberns.workers.dev
        ├── Auth: x-api-secret: SpineMed2026
        ├── Model: claude-sonnet-4-6
        └── CORS: locked to drberns.github.io

External APIs (no auth required)
  ├── Open-Meteo       — weather widgets (free, no key)
  └── NHTSA VIN API    — VIN lookup (free, no key)
```

**Shared JS utility:** `widget_common.js` — shared helper for all Claude API calls.

---

## Site Map

### Dashboard
| File | What it does |
|---|---|
| `index.html` | Main portal — tile grid to all tools, time/weather widgets (Tallahassee + Panama City), PDF merger, fax cover generator, VIN lookup, Florida Bar attorney lookup |

### Consent & Intake
| File | Language | What it does |
|---|---|---|
| `CIG_Signature_Packet.html` | EN | HIPAA, TOA, AOB, IOT, Medical Records Release — emails HIPAA PDF on submit |
| `CIG_Signature_Packet_ES_v_04.22.26.html` | ES | Spanish version |
| `CIG_Procedure_Consent.html` | EN | Informed consent for injections (2-page PDF output) |
| `CIG_Procedure_Consent_ES_v_04.22.26.html` | ES | Spanish version |
| `CIG_Intake.html` | EN | New patient intake — demographics, injury history, PMH; multi-step wizard |
| `CIG_Intake_ES_v_04.22.26.html` | ES | Spanish version |

### Clinical Outcome Assessments
| File | Language | Instruments |
|---|---|---|
| `CIG_Outcome_Assessments.html` | EN | ODI, NDI, PDI, HDI, UEFI, LEFS, SPADI, ACE, LEDD |
| `CIG_Outcome_Assessments_es.html` | ES | Spanish version |

### AI-Powered Clinical Tools (all use Claude Sonnet via Worker)
| File | What it does |
|---|---|
| `CIG_Note_Optimizer.html` | SOAP note rewriting |
| `CIG_Clinical_Polish.html` | Rough notes → fluent physician English |
| `CIG_MRI_Distiller.html` | PDF MRI report → findings + ICD-10 codes |
| `CIG_ICD10_Lookup.html` | Plain English → ICD-10 code suggestions |
| `CIG_CPT_Lookup.html` | Procedure description → CPT codes + modifiers |

### Financial
| File | What it does |
|---|---|
| `CIG_PanamaCity_Estimate_Builder.html` | Surgical cost calculator — Panama City |
| `CIG_Tallahassee_Estimate_Builder.html` | Surgical cost calculator — Tallahassee |
| `CIG_Combined_Ledger.html` | Patient balance tracking across both offices |

### Imaging
| File | What it does |
|---|---|
| `CIG_MRI_Script_Builder_FIXED (1).html` | MRI prescription order form builder (uses `CIG MRI SCRIPT CODE.txt`) |

---

## Key Assets

| File | Purpose |
|---|---|
| `widget_common.js` | Shared Claude API call helper |
| `CIG MRI SCRIPT CODE.txt` | 1.8 MB MRI prescription code data (loaded by Script Builder) |
| `CIG_Logo_transparent.png` | Logo (full size) |
| `CIG_Logo_transparent_small.png` | Logo (small) |
| `Eldeeb_Signature.png` | Physician signature (black variant) |
| `Eldeeb_Signature_Navy.png` | Physician signature (navy variant) |
| `Florida_State_Seal.png` | State seal (for consent documents) |

---

## Cloudflare Worker Proxy

All Claude API calls go through the Worker — the API key is never in the HTML.

| Field | Value |
|---|---|
| Worker URL | `spinemed-anthropic-proxy.drberns.workers.dev` |
| Auth header | `x-api-secret: SpineMed2026` |
| Model | `claude-sonnet-4-6` |
| CORS | Locked to `drberns.github.io` |

A secondary Worker (`spinemed-imap-worker.drberns.workers.dev`) handles email/fax
delivery from consent forms.

---

## Language Parity

English and Spanish versions must stay in sync. Current parity status:

| Document | EN | ES |
|---|---|---|
| Signature Packet | ✅ | ✅ |
| Procedure Consent | ✅ | ✅ |
| Intake | ✅ | ✅ |
| Outcome Assessments | ✅ | ✅ |
| Note Optimizer | ✅ | ❌ |
| Clinical Polish | ✅ | ❌ |
| MRI Distiller | ✅ | ❌ |
| ICD-10 Lookup | ✅ | ❌ |
| CPT Lookup | ✅ | ❌ |
| Estimate Builders | ✅ (×2 locations) | ❌ |
| Combined Ledger | ✅ | ❌ |

---

## GitHub Actions Workflows

| Workflow | Trigger | What it does |
|---|---|---|
| `mri_script.yml` | Push to `main` | Deploy to GitHub Pages |
| `changelog-gate.yml` | Pull request | Fail PR if CHANGELOG.md not updated |

---

## Compliance Notes

- HIPAA form wording has legal significance — never alter substance without explicit instruction.
- CIG and SpineMed/PainMed must never be cross-linked or cross-branded.
- The Cloudflare Worker CORS restriction (`drberns.github.io`) must not be widened.
- Claude API key must never appear in any HTML/JS file.
