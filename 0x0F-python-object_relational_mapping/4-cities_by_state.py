#!/usr/bin/python3
"""script that lists all cities from the database hbtn_0e_4_usa"""

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
    c.execute("SELECT cities.id, cities.name, states.name FROM cities\
    JOIN states ON states.id = cities.state_id ORDER BY cities.id ASC")
    table = c.fetchall()

    for row in table:
        print(row)

    c.close()
    db.close()
