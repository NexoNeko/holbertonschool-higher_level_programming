SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
HAVING COUNT(*) > 1
ORDER BY number DESC;
