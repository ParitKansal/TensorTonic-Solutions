-- Returns: account, txn_date, amount, running_total.
SELECT account, txn_date, amount,
SUM(amount) OVER(PARTITION BY account ORDER BY txn_date ASC, id ASC ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS running_total
FROM transactions
ORDER BY account, txn_date, id ASC

