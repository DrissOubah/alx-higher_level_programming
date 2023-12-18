#!/usr/bin/python3
"""
script that takes in the name of a state as an argument
and lists all cities of that state, using the database hbtn_0e_4_us
a"""
if __name__ == '__main__':
    import MySQLdb
    import sys

    """
    Get MySQL username, password, and database
    name from command line arguments
    """
    username, password, dbname = sys.argv[1], sys.argv[2], sys.argv[3]
    state_name = sys.argv[4]
    """ Connect to the MySQL server running on localhost at port 3306"""
    db = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=username,
            passwd=password,
            db=dbname
            )

    c = db.cursor()
   c.execute("SELECT cities.name FROM cities\
                 LEFT JOIN states\
                 ON states.id = cities.state_id\
                 WHERE states.name LIKE BINARY (%s) ORDER BY cities.id ASC",
                (state_name,))
    table = c.fetchall()

    end_string = ""
    string_cities = ""
    for row in table:
        string_cities = string_cities + end_string + row[0]
        end_string = ", "

    print(string_cities)
    c.close()
    db.close()
