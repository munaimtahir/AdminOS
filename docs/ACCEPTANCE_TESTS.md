# Acceptance Tests (Plain English)

## PDF Truth
- *Given* a user fills a Temperature page for today, *When* they save, *Then* a **single A4 PDF** is created under that register/date and is retrievable from Search.

## Reminders Linkage
- *Given* a register with a daily schedule, *When* the day starts, *Then* a reminder appears; *When* the page is completed, *Then* the reminder auto‑clears.

## Waste Register Compliance
- *Given* a filled Waste record, *When* the PDF is generated, *Then* it displays all Waste table fields (Date, Time, Yellow Bags #/Weight, Labeling, Sharps #/Weight, Labeling, Handed Over By, Vehicle #, Receiver’s Signature).

## Calibration Compliance
- *Given* a calibration entry is saved, *Then* the PDF shows Date of Calibration, Equipment/Serial, Standard, Result, Tolerance (P/F), Calibrated By, Verified By, Remarks.
