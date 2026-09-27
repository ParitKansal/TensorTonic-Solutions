-- Returns: avg_daily_orders, avg_daily_revenue, busiest_day_orders.
WITH temp AS (
    SELECT COUNT(id) AS order_count, SUM(amount) AS revenue
    FROM orders
    GROUP BY order_date
)
SELECT ROUND(AVG(order_count), 2) AS avg_daily_orders, 
    ROUND(AVG(revenue), 2) AS avg_daily_revenue,
    ROUND(MAX(order_count), 2) AS busiest_day_orders
FROM temp