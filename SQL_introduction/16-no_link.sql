-- Lists all records from second table with a name, sorted descending by score
SELECT score, name
FROM second_table
WHERE name != ""
ORDER BY score DESC;
