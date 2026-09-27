-- Returns: segment_name, metric_name.
SELECT segments.segment_name, metrics.metric_name
FROM segments
CROSS JOIN metrics
ORDER BY 
    segment_name ASC NULLS LAST,
    metric_name ASC NULLS LAST
