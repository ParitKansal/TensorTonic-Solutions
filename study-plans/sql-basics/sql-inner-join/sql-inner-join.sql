-- Returns: name, salary, dept_name.
SELECT employees.name, employees.salary, departments.dept_name
FROM employees
INNER JOIN departments
ON employees.dept_id = departments.id
ORDER BY name NULLS LAST