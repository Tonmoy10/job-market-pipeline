SELECT title,description,location.display_name AS location_name,company.display_name AS company_name,
contract_time,salary_min,salary_max,created
FROM `project-e2b03ea7-6bdb-4d35-99b.raw_job_market_data.raw_jobs`