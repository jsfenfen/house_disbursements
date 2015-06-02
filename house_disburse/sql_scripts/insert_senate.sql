copy senate_disburse_sod(source_doc, senator_flag, senator_name, raw_office, funding_year, fiscal_year, congress_no, reference_page, transaction_id, date_posted_raw, start_date_raw, end_date_raw, description, salary_flag, amount_raw, payee) from '/Users/jfenton/github-whitelabel/house_disbursements/house_disburse/senate_disburse/data/112_sdoc4_senate_data_cleaned.csv' with CSV header;

copy senate_disburse_sod(source_doc, senator_flag, senator_name, raw_office, funding_year, fiscal_year, congress_no, reference_page, transaction_id, date_posted_raw, start_date_raw, end_date_raw, description, salary_flag, amount_raw, payee) from '/Users/jfenton/github-whitelabel/house_disbursements/house_disburse/senate_disburse/data/112_sdoc7_senate_data_cleaned.csv' with CSV header;

copy senate_disburse_sod(source_doc, senator_flag, senator_name, raw_office, funding_year, fiscal_year, congress_no, reference_page, transaction_id, date_posted_raw, start_date_raw, end_date_raw, description, salary_flag, amount_raw, payee) from '/Users/jfenton/github-whitelabel/house_disbursements/house_disburse/senate_disburse/data/112_sdoc10_senate_data_cleaned.csv' with CSV header;


copy senate_disburse_sod(source_doc, senator_flag, senator_name, raw_office, funding_year, fiscal_year, congress_no, reference_page, transaction_id, date_posted_raw, start_date_raw, end_date_raw, description, salary_flag, amount_raw, payee) from '/Users/jfenton/github-whitelabel/house_disbursements/house_disburse/senate_disburse/data/113_sdoc2_senate_data_cleaned.csv' with CSV header;


copy senate_disburse_sod(source_doc, senator_flag, senator_name, raw_office, funding_year, fiscal_year, congress_no, reference_page, transaction_id, date_posted_raw, start_date_raw, end_date_raw, description, salary_flag, amount_raw, payee) from '/Users/jfenton/github-whitelabel/house_disbursements/house_disburse/senate_disburse/data/113_sdoc17_senate_data_cleaned.csv' with CSV header;

--
--ftpdata=# select count(*) from senate_disburse_sod;
-- count  
--------
-- 259381

copy senate_disburse_sod(source_doc, senator_flag, senator_name, raw_office, funding_year, fiscal_year, congress_no, reference_page, transaction_id, date_posted_raw, start_date_raw, end_date_raw, description, salary_flag, amount_raw, payee) from '/Users/jfenton/github-whitelabel/house_disbursements/house_disburse/senate_disburse/data/113_sdoc22_senate_data_cleaned.csv' with CSV header;

somehow a carriage return got in here ? 

copy senate_disburse_sod(source_doc, senator_flag, senator_name, raw_office, funding_year, fiscal_year, congress_no, reference_page, transaction_id, date_posted_raw, start_date_raw, end_date_raw, description, salary_flag, amount_raw, payee) from '/Users/jfenton/github-whitelabel/house_disbursements/house_disburse/senate_disburse/data/113_sdoc25_senate_data_cleaned.csv' with CSV header;