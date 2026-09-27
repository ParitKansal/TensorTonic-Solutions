-- Returns: username, experiment_name, variant, revenue.
SELECT users.username, experiment_assignments.experiment_name, experiment_assignments.variant, conversions.revenue
FROM users
INNER JOIN experiment_assignments
ON users.id = experiment_assignments.user_id
INNER join conversions
ON users.id = conversions.user_id
ORDER BY 
    experiment_name ASC NULLS LAST,
    revenue DESC NULLS LAST, 
    username ASC NULLS LAST
    
