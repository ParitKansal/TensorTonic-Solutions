SELECT
    username,
    signup_date,
    YEAR(signup_date) AS signup_year,
    MONTH(signup_date) AS signup_month,
    QUARTER(signup_date) AS signup_quarter,
    DATE_TRUNC('month', signup_date) AS cohort_month
FROM signups
ORDER BY signup_date ASC, username ASC;