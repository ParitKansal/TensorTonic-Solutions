-- Returns: username, session_count, activity_level, platform_type.
WITH temp AS (
    SELECT 
        username, session_count,
        CASE
            WHEN session_count >= 50 THEN 'Power'
            WHEN session_count >= 10 THEN 'Casual'
            ELSE 'Dormant'
        END AS activity_level,
        CASE
            WHEN session_count >= 50 THEN 1
            WHEN session_count >= 10 THEN 2
            ELSE 3
        END AS activity_level_,
        CASE
            WHEN platform IN ('ios','android') THEN 'Mobile'
            WHEN platform IN ('web','desktop') THEN 'Desktop'
            ELSE 'Other'
        END AS platform_type
    FROM user_sessions
    ORDER BY activity_level_, username ASC
    
)
SELECT username, session_count, activity_level, platform_type
FROM temp


