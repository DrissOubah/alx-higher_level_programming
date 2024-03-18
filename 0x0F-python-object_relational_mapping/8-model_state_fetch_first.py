#!/usr/bin/python3
"""
Script that retrieves and prints the first object from
a database using SQLAlchemy.
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

    states_us = sess.query(State).first()
    if not states_us:
        print("Nothing")
    else:
        print("{}: {}".format(states_us.id, states_us.name))
