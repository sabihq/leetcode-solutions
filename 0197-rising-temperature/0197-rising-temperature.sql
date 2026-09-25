SELECT today.id
FROM Weather AS today
JOIN Weather AS yesterday
    ON yesterday.recordDate = DATE_SUB(today.recordDate, INTERVAL 1 DAY)
WHERE today.temperature > yesterday.temperature;