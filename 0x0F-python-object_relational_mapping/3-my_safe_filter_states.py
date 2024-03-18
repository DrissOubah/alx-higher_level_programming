#!/usr/bin/python3
"""
script that takes in arguments and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument
"""

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
    c.execute("SELECT * FROM states WHERE name = (%s)\
    ORDER BY states.id ASC", (state_name,))
    table = c.fetchall()

    for row in table:
        print(row)

    c.close()
    db.close()
