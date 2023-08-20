
When doing compound queries the number of queried columns has to match, but not the names. The names are inferred from the first compoundable table. What follows is that when sorting the ORDER BY has to follow one of the columns of the same (first) table.

Subquery often needs an alias (especially in PostgreSQL) when performing other quaries on it later on.