#!/usr/bin/python3
"""
script that takes in the name of a state as an argument
and lists all cities of that state, using the database hbtn_0e_4_usa
"""
if __name__ == '__main__':
    import MySQLdb
    import sys

    """
    Get MySQL username, password, and database
    name from command line arguments
    """
    username, password, dbname, state_name = sys.argv[1:5]
    """ Connect to the MySQL server running on localhost at port 3306"""
    db = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=username,
            passwd=password,
            db=dbname
            )

    c = db.cursor()
    c.execute("""
              SELECT cities.name
              FROM cities
              LEFT JOIN states ON states.id = cities.state_id
              WHERE states.name LIKE BINARY %s
              ORDER BY cities.id ASC
              """, (state_name,))
    rows = c.fetchall()
    city_names = ", ".join(row[0] for row in rows)
    print(city_names)
    c.close()
    db.close()
