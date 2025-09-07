# AdminOS‑Lab — Plain-English Blueprint (MVP)

**What it is:** A digital cupboard for lab offices. Generates the right forms each day and stores each finished page as a **single A4 PDF per register per date**. Auditors never log in — you print or export.

**Users:** 
- **Admin**: sets up registers/templates/reminders/documents; reviews activity.
- **User (staff)**: opens bundles, fills forms (digital or print+scan), uploads scans, views docs.

**Main sections:**
- **Dashboard**: Today, Pending/Overdue, quick links (Daily/Weekly/Pending‑Due), health snapshot.
- **Bundles**: Daily / Weekly / Pending‑Due; open to fill digitally or **Print blank**; optional **bulk print/ZIP**.
- **Registers**: list (Temperature, Calibration, Waste); status per date; each date opens an **A4 page** (digital when filling; final PDF when done).
- **Documents**: Fixed (SOPs/licenses), Dynamic (complaints/appraisals), Physical (signboards); **versions** start at **v1**.
- **Reminders**: auto-created from schedules; editable dates/priority; auto‑clear when page completed.
- **Search**: filters (register/date/status) → open the PDF.
- **Activity Log**: who did what and when.
- **Admin (Settings)**: Registers (name, schedule, mode), Templates (A4), Branding (lab header), Time zone (**GMT+5** default), Backups (weekly; keep 5), Health page.

**Rules:**
- The **PDF is the truth** (internal typed values are secondary).
- **One A4 PDF per register per date**.
- Schedules create reminders; completion clears them.

**Out of scope (MVP):** email/SMS, OCR, auditor portal, advanced analytics, retention policies, cloud storage.
