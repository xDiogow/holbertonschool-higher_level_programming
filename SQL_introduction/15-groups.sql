-- Lists the number of records with the same score in the table second_table
SELECT score, DISTINCT COUNT(score) AS number FROM second_table;