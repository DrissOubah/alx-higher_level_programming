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

    # Get command-line arguments
    username, password, database_name = argv[1], argv[2], argv[3]

    # Construct the database URI
    db = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format
    (username, password, database_name)

    # Create an SQLAlchemy engine
    engine = create_engine(db)

    # Create a session factory
    Session = sessionmaker(bind=engine)

    # Create a session
    session = Session()

    try:
        cities = session.query(City).order_by(City.id).all()

        # Display the results
        for city in cities:
            print("{}: {} -> {}".format(city.id, city.name, city.state.name))

    finally:
        # Close the session
        if session:
            session.close()
