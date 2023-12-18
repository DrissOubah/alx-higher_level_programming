#!/usr/bin/python3
"""
Script that lists all objects from a database
where the name contains the letter 'a'.
"""
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    sess = Session()

    for states_us in sess.query(State).filter(State.name.contains('%a')):
        print("{}: {}".format(states_us.id, states_us.name))
