-- Returns: department, total_tickets, open_count, in_progress_count, closed_count.
SELECT department,
    COUNT(status) AS total_tickets,
    SUM(
        case
            WHEN status = 'open' THEN 1
            ELSE 0
        END
    ) AS open_count,
    SUM(
        case
            WHEN status = 'in_progress' THEN 1
            ELSE 0
        END
    ) AS in_progress_count,
    SUM(
        case
            WHEN status = 'closed' THEN 1
            ELSE 0
        END
    ) AS closed_count
    
FROM tickets
GROUP BY department
ORDER BY total_tickets DESC, department ASC
