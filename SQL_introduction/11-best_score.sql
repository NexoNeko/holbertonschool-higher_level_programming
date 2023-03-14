-- Lists score, name from second table for all values with a score of
-- More than 10. ORders high to low
SELECT score, name FROM second_table
WHERE score >= 10
ORDER BY score DESC;
