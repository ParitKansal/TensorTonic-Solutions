-- Returns: name, price, vs_avg.
WITH temp AS (
    SELECT AVG(price) as avg_price
    FROM products
    
),
sales_ AS (
    SELECT DISTINCT product_id as product_id
    FROM sales
)
SELECT 
    products.name, 
    products.price, 
    ROUND(products.price - temp.avg_price, 2) AS vs_avg
FROM sales_
LEFT JOIN products
ON sales_.product_id = products.id
CROSS JOIN temp
ORDER BY vs_avg DESC, name ASC

