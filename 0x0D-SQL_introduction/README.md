0. List databases:

Script (0-list_databases.sql) lists all databases on the MySQL server.
Example usage: cat 0-list_databases.sql | mysql -hlocalhost -uroot -p
1. Create a database:

Script (1-create_database_if_missing.sql) creates the database hbtn_0c_0 if it doesn't exist.
Example usage: cat 1-create_database_if_missing.sql | mysql -hlocalhost -uroot -p
2. Delete a database:

Script (2-remove_database.sql) deletes the database hbtn_0c_0 if it exists.
Example usage: cat 2-remove_database.sql | mysql -hlocalhost -uroot -p
3. List tables:

Script (3-list_tables.sql) lists all tables of a specified database.
Example usage: cat 3-list_tables.sql | mysql -hlocalhost -uroot -p mysql
4. First table:

Script (4-first_table.sql) creates a table called first_table with specified columns in the current database.
Example usage: cat 4-first_table.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
5. Full description:

Script (5-full_table.sql) prints the full description of the table first_table in a specified database.
Example usage: cat 5-full_table.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
6. List all in table:

Script (6-list_values.sql) lists all rows of the table first_table in a specified database.
Example usage: cat 6-list_values.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
7. First add:

Script (7-insert_value.sql) inserts a new row into the table first_table in a specified database.
Example usage: cat 7-insert_value.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
8. Count 89:

Script (8-count_89.sql) displays the number of records with id = 89 in the table first_table.
Example usage: cat 8-count_89.sql | mysql -hlocalhost -uroot -p hbtn_0c_0 | tail -1
9. Full creation:

Script (9-full_creation.sql) creates a table second_table and adds multiple rows in a specified database.
Example usage: cat 9-full_creation.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
10. List by best:

Script (10-top_score.sql) lists all records of the table second_table ordered by score in a specified database.
Example usage: cat 10-top_score.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
11. Select the best:

Script (11-best_score.sql) lists records with a score >= 10 in the table second_table in a specified database.
Example usage: cat 11-best_score.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
12. Cheating is bad:

Script (12-no_cheating.sql) updates the score of a specific name in the table second_table.
Example usage: cat 12-no_cheating.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
13. Score too low:

Script (13-change_class.sql) removes records with a score <= 5 in the table second_table.
Example usage: cat 13-change_class.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
14. Average:

Script (14-average.sql) computes the score average of all records in the table second_table.
Example usage: cat 14-average.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
15. Number by score:

Script (15-groups.sql) lists the number of records with the same score in the table second_table.
Example usage: cat 15-groups.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
16. Say my name:

Script (16-no_link.sql) lists all records of the table second_table excluding rows without a name value, ordered by descending score.
Example usage: cat 16-no_link.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
