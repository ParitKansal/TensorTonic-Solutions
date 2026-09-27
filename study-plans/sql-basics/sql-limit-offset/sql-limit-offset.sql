-- Returns: product, revenue, sale_date.
SELECT product, revenue, sale_date
FROM sales
ORDER BY 
    revenue DESC  NULLS LAST, 
    sale_date ASC  NULLS LAST
OFFSET 1 LIMIT 3 