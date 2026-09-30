-- Returns: name, display_email, status.
SELECT name, 
case
    WHEN email is NOT NULL THEN email
    ELSE 'N/A'
END as display_email,
CASE
    WHEN deactivated_at IS NULL THEN 'active'
    ELSE 'inactive'
END AS status
FROM customers
WHERE phone IS NOT NULL
ORDER BY name ASC