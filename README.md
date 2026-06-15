# Automated Job Market Analytics Pipeline & BI Dashboard

## Project Overview
This repository has an end-to-end data engineering pipeline designed to ingest, process, clean and visualize real-time software engineering job postings. The automated data flow from an external job market API to a cloud data warehouse provides data-driven insights into hiring trends, company volumes and salary distributions to empower job seekers.

## Data Architecture & Pipeline Flow
The entire architecture follows a structured ELT (Extract, Load, Transform) design pattern, organized into modular processing layers:

1. **Extraction (`src/extract.py`)**: Fetches paginated, raw JSON payloads dynamically from the Adzuna API, capturing titles, companies, descriptions, and salary baselines.
2. **Loading (`src/load.py`)**: Uses the Google Cloud BigQuery SDK to stream raw JSON files into a landing table (`raw_jobs`) using automated schema detection.
3. **Transformation (`dbt`)**:
   - `stg_raw_jobs`: Deduplicates raw records, casts text types, and extracts nested components.
   - `core_job_market`: Shows analytics-ready business entities optimized for visualization.
4. **Data Quality & Testing (`schema.yml`)**: Implements data validation schemas, enforcing `not_null` assertions across critical columns like job titles and company names to prevent dashboard corruption.
5. **Orchestration (`pipeline.py`)**: A master script that controls execution with safety check (check=True), ensuring the pipeline stops completely if any upstream task fails.


## Local Setup & Orchestration
To replicate this pipeline locally, ensure you have Python 3.x installed along with your Google Cloud credentials configured, then follow these steps:

1. **Clone the repository:**
    ```bash
        git clone <YOUR_REPOSITORY_URL>
        cd job-market-pipeline
    ```

2. **Configure virtual environment and dependencies:**
    ```bash
        python -m venv .venv
        # Activate on Windows (PowerShell):
        .\.venv\Scripts\activate.ps1
        # Activate on Mac/Linux:
        source .venv/bin/activate

        pip install -r requirements.txt
    ```

3. **Set up environment variables:**
    Create a root directory to specify API credentials:
    JOB_API_ID=your_adzuna_api_id
    JOB_API_KEY=your_adzuna_api_key
    JOB_API_URL=adzuna_url

4. **Execute the complete end-to-end pipeline:**
    ```bash
        python pipeline.py
    ```

## Business Intelligence Layer
The pipeline feeds directly into a reporting layer built inside Power BI Desktop (job_market_dashboard.pbix), connecting to BigQuery.

**Key Insights Tracked:**
- **Market Velocity:** Real-time counter of total open postings within the targeted tech sector.
- **Employer Demand Breakdown:** Horizontal clustered bar chart highlighting companies with the highest active hiring volume.
- **Salary Analytics:** Dynamic financial charts monitoring the overall average market salary mapped across job titles.
- **Job Deep-Diving:** A minimal, fully responsive relational table allowing developers to click into any metric to read individual job descriptions instantly.