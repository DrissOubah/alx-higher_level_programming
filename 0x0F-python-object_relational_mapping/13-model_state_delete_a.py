#!/usr/bin/python3
"""
This script deletes all State objects
with a name containing the letter `a`
from the database `hbtn_0e_6_usa`.
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Deletes State objects on the database.
    """

    # Construct the database URI
    db = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3])

    # Create an SQLAlchemy engine
    engine = create_engine(db)

    # Create a session factory
    Session = sessionmaker(bind=engine)

    # Create a session
    session = Session()

    # Delete State objects with a name containing the letter 'a'
    for stat_instance in session.query(State).filter(State.name.contains('a')):
        session.delete(stat_instance)

    # Commit the changes
    session.commit()

    # Close the session
    session.close()
