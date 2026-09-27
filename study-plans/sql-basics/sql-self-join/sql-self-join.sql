-- Returns: username, referrer_name.
SELECT a.username AS username,
    CASE
        WHEN b.username IS NULL THEN 'organic'
        ELSE b.username
    END AS referrer_name
FROM user_referrals AS a
LEFT JOIN user_referrals AS b
ON a.referred_by = b.id
ORDER BY username ASC NULLS LAST