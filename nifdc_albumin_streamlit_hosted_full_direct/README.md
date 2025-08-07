# NIFDC Albumin — Cloud-Scraped & Hosted Dashboard (2025 YTD)

This repository contains:
- **Streamlit app** (`app.py`) that visualizes weekly market share (batch / bottles / grams).
- **Scraper** (Playwright) that collects 2025 YTD human albumin batches across all regions.
- **GitHub Actions workflow** (`.github/workflows/scrape.yml`) to run the scraper in the cloud and **commit the CSVs** back to the repo.

## Quick start
1) Create a new repo on GitHub (e.g., `nifdc_albumin_streamlit_hosted_full`) and upload these files (unzip first).
2) In the repo, go to **Actions** → enable workflows → run **Scrape NIFDC (2025 YTD)**.
3) Deploy on Streamlit Cloud (Repo `.../nifdc_albumin_streamlit_hosted_full`, file `app.py`).

The workflow commits the CSVs into `data/`, and the app reads them.
