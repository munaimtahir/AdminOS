# Supervisor Playbook (Summary)

**Goal:** Build in **stages**, verify **Definition of Done** each stage, keep the repo clean.

1) **Stage 0 – Scaffold**: Create repo, Django project, app folder, env files, README, tests harness.
2) **Stage 1 – Data Models**: Registers, RegisterPage, entries for Temperature/Calibration/Waste; migrations; seed.
3) **Stage 2 – Admin & Basics**: Django admin, simple list/detail views, templates skeletons.
4) **Stage 3 – Bundles**: Daily/Weekly/Pending‑Due logic + pages.
5) **Stage 4 – PDFs**: WeasyPrint/ReportLab; generate one A4 PDF per register/date.
6) **Stage 5 – Reminders**: Auto‑create from schedules; auto‑clear on completion.
7) **Stage 6 – Search & Activity Log**: Filters; human‑readable audit trail.
8) **Stage 7 – Branding, Time Zone, Health, Backups (weekly keep 5)**.
9) **Stage 8 – Deploy**: Replit/Ubuntu VPS; (optional) Docker & CI.

**Stage Gate:** Do not proceed until tests pass and README updated.
