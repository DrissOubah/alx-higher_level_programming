#!/usr/bin/python3
"""
Script that lists all cities from the database hbtn_0e_4_usa
"""
import MySQLdb
import sys

if __name__ == '__main__':
    """ Get MySQL username, password, and database name from
    command line arguments"""
    username, password, dbname = sys.argv[1:4]

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
              SELECT cities.id, cities.name, states.name
              FROM cities
              JOIN states ON states.id = cities.state_id
              ORDER BY cities.id ASC
              """)

    rows = c.fetchall()

    for row in rows:
        print(row)

    c.close()
    db.close()
