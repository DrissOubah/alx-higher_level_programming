#!/usr/bin/python3
"""
Script that lists all State objects, and corresponding City objects,
contained in the database hbtn_0e_101_usa.
"""

from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Lists all State objects and corresponding City objects from the database.
    """

    # Check if the correct number of command-line arguments is provided
    if len(argv) != 4:
        print("Usage: {} <username> <password> <database_name>".format(
            argv[0]))
        exit(1)

    # Get command-line arguments
    username, password, database_name = argv[1], argv[2], argv[3]

    # Construct the database URI
    db_url = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format
    (username, password, database_name)

    # Create an SQLAlchemy engine
    engine = create_engine(db_url)

    # Create a session factory
    Session = sessionmaker(bind=engine)

    # Create a session
    session = Session()

    try:
        states = session.query(State).order_by(State.id).all()

        # Display the results
        for state in states:
            print("{}: {}".format(state.id, state.name))
            for city in state.cities:
                print("    {}: {}".format(city.id, city.name))

    finally:
        # Close the session
        if session:
            session.close()
