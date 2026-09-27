-- Returns: customer, total_orders, total_spent.
SELECT customer, COUNT(product) AS total_orders, SUM(amount) AS total_spent
FROM orders
GROUP BY customer
HAVING COUNT(product) >= 2
ORDER BY total_spent DESC
