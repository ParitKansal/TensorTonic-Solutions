-- Returns: customer, order_count, total_spent.
SELECT customer, COUNT(order_date) AS order_count, SUM(amount) AS total_spent
FROM orders
GROUP BY customer
HAVING order_count > 1
ORDER BY total_spent DESC , customer ASC