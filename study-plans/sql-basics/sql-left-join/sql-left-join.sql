SELECT
    customers.name,
    customers.city,
    CASE
        WHEN SUM(orders.amount) IS NULL THEN 0
        ELSE SUM(orders.amount)
    END AS total_spent
FROM customers
LEFT JOIN orders
    ON customers.id = orders.customer_id
GROUP BY
    customers.id,
    customers.name,
    customers.city
ORDER BY total_spent DESC NULLS LAST, name ASC NULLS LAST