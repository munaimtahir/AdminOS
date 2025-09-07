# CURSOR STAGE 1: Data Models & Seed

## Tasks

- Create models & migrations:
  - Register (name, schedule: daily/weekly/monthly, mode: digital/print/both)
  - RegisterPage (FK register, date, status, pdf_path)
  - TemperatureEntry, CalibrationEntry, WasteEntry with fields from `/docs/MSDS_FIELD_TABLES.md`
- Implement seed command: create 3 registers and today’s pages + sample rows


## Acceptance (run or add tests)

- Model migrations run successfully
- Seeding works and creates today’s pages
- RegisterPage is unique per (register, date)


## Expected Outputs

- `registers/models.py` with the models
- `scripts/seed.py` executable
- Initial tests under `tests/` covering uniqueness & seed


**Do not proceed** until all Expected Outputs exist and tests pass.
