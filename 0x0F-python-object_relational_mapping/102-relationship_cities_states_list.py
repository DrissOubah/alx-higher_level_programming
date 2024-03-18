#!/usr/bin/python3
"""
Script that lists all City objects from the database hbtn_0e_101_usa.
"""

from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Lists all City objects from the database.
    """

    # Check if the correct number of command-line arguments is provided
    if len(argv) != 4:
        print("Usage: {} <username> <password> <database_name>".format(
            argv[0]))
        exit(1)

    # Get command-line arguments
    username, password, database_name = argv[1], argv[2], argv[3]

    # Construct the database URI
    db_url = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        username, password, database_name)

    # Create an SQLAlchemy engine
    engine = create_engine(db_url)

    # Create a session factory
    Session = sessionmaker(bind=engine)

    # Create a session
    session = Session()

    # Query all City objects
    cities = session.query(City).order_by(City.id).all()

    # Display the results
    for city in cities:
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))

    # Close the session
    session.close()
