Task 0: Get all states

This task requires writing a Python script (0-select_states.py) that lists all states from a MySQL database (hbtn_0e_0_usa).
The script takes three command-line arguments: MySQL username, MySQL password, and the database name.
It connects to a MySQL server running on localhost at port 3306.
The results should be sorted in ascending order by states.id, and the script should print each row.

Task 1: Filter states

The script (1-filter_states.py) lists all states with a name starting with 'N' (upper 'N') from the database hbtn_0e_0_usa.
Similar to Task 0, it takes three command-line arguments.
The results should be sorted in ascending order by states.id, and the script should print each row.

Task 2: Filter states by user input

The script (2-my_filter_states.py) takes an argument and displays all values in the states table where the name matches the argument.
It takes four command-line arguments: MySQL username, MySQL password, database name, and state name searched.
The SQL query is created using the format method to include the user input.
Results should be sorted in ascending order by states.id, and the script should print each row.

Task 3: SQL Injection...

This task emphasizes SQL injection vulnerability and urges users to remember the risk demonstrated in Task 2.
It recommends testing the script with an input like "Arizona'; TRUNCATE TABLE states ; SELECT * FROM states WHERE name = '".
The goal is to raise awareness about the importance of handling user input securely.

Task 4: Cities by states

The script (4-cities_by_state.py) lists all cities from the database hbtn_0e_4_usa.
It takes three command-line arguments: MySQL username, MySQL password, and the database name.
Results are sorted in ascending order by cities.id, and the script should print each row.

Task 5: All cities by state

The script (5-filter_cities.py) takes the name of a state as an argument and lists all cities of that state from the database hbtn_0e_4_usa.
Four command-line arguments are expected: MySQL username, MySQL password, database name, and state name.
Results are sorted in ascending order by cities.id, and the script should print the city names for the specified state.

Task 6: First state model

A Python file (model_state.py) contains the class definition of a State and an instance Base = declarative_base().
The State class inherits from Base and links to the MySQL table states.
It has two class attributes: id and name.
A script (6-model_state.py) connects to a MySQL server and creates the states table based on the defined class.

Task 7: All states via SQLAlchemy

The script (7-model_state_fetch_all.py) lists all State objects from the database hbtn_0e_6_usa using SQLAlchemy.
Three command-line arguments are required: MySQL username, MySQL password, and database name.
Results are sorted in ascending order by states.id, and the script should print each state's id and name.

Task 8: First state

The script (8-model_state_fetch_first.py) prints the first State object from the database hbtn_0e_6_usa.
Three command-line arguments are needed: MySQL username, MySQL password, and database name.
It should connect to a MySQL server, fetch and print the first state's id and name.

Task 9: Contains a

The script (9-model_state_filter_a.py) lists all State objects that contain the letter 'a' from the database hbtn_0e_6_usa.
Three command-line arguments are required: MySQL username, MySQL password, and database name.
Results are sorted in ascending order by states.id, and the script should print each state's id and name.

Task 10: Get a state

The script (10-model_state_my_get.py) prints the State object's id with the name passed as an argument from the database hbtn_0e_6_usa.
Four command-line arguments are expected: MySQL username, MySQL password, database name, and state name to search.
It should connect to a MySQL server, fetch and print the state's id, or print "Not found" if the state is not in the database.

Task 11: Add a new state

The script (11-model_state_insert.py) adds the State object "Louisiana" to the database hbtn_0e_6_usa.
Three command-line arguments are needed: MySQL username, MySQL password, and database name.
It should connect to a MySQL server, add the new state, and print the new state's id.

Task 12: Update a state

The script (12-model_state_update_id_2.py) changes the name of a State object with id = 2 to "New Mexico" in the database hbtn_0e_6_usa.
Three command-line arguments are required: MySQL username, MySQL password, and database name.
It should connect to a MySQL server, update the state, and commit the change.

Task 13: Delete states

The script (13-model_state_delete_a.py) deletes all State objects with a name containing the letter 'a' from the database hbtn_0e_6_usa.
Three command-line arguments are needed: MySQL username, MySQL password, and database name.
It should connect to a MySQL server, delete the states, and commit the change.

Task 14: Cities in state

The script (14-model_city_fetch_by_state.py) prints all City objects from the database hbtn_0e_14_usa.
Three command-line arguments are expected: MySQL username, MySQL password, and database name.
Results should be sorted in ascending order by cities.id, and the script should print each city's id, name, and state name.

Task 15: City relationship

The script (15-model_city_relationship.py) creates the City class and a relationship with the State class using SQLAlchemy.
It connects to a MySQL server, creates the tables states and cities, adds a state with a city, and prints the city and its state.

Task 16: List relationship

The script (100-model_relationship_states_cities_list.py) lists all State objects, their City objects, and respective cities' names from the database hbtn_0e_101_usa.
Three command-line arguments are required: MySQL username, MySQL password, and database name.
Results should be sorted in ascending order by states.id and cities.id, and the script should print each state, city id, and city name.

Task 17: From city

The script (101-relationship_states_cities.py) adds the City object with the name "San Francisco" to a State object from the database hbtn_0e_101_usa.
Three command-line arguments are expected: MySQL username, MySQL password, and database name.
It should connect to a MySQL server, fetch the state with the name "California," add a city, and commit the change.
