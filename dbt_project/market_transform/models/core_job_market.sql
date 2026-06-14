SELECT title,UPPER(company_name) as company,DESCRIPTION,(salary_max + salary_min)/2 as estimated_salary
FROM {{ref('stg_raw_jobs')}}