-- Lists all records with a name from second_table, ordered by score (desc)
SELECT score, name FROM second_table WHERE name IS NOT NULL AND name != '' ORDER BY score DESC;
