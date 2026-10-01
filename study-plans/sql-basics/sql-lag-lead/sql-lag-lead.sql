SELECT
    month,
    revenue,

    CASE
        WHEN LAG(revenue) OVER (ORDER BY month ASC, id ASC) IS NOT NULL
        THEN LAG(revenue) OVER (ORDER BY month ASC, id ASC)
        ELSE 0
    END AS prev_revenue,

    CASE
        WHEN LAG(revenue) OVER (ORDER BY month ASC, id ASC) IS NOT NULL
        THEN revenue - LAG(revenue) OVER (ORDER BY month ASC, id ASC)
        ELSE revenue
    END AS revenue_change

FROM monthly_revenue
ORDER BY month, id ASC;