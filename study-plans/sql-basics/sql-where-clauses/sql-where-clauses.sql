-- Returns: name, salary.
SELECT name, salary
FROM employees
WHERE department IN ('Engineering', 'Marketing') AND salary > 70000
ORDER BY name, salary