#!/usr/bin/python3
"""
This script changes the name of a State object
from the database `hbtn_0e_6_usa`
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Update a State object on the database.
    """

    db = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3])
    engine = create_engine(db)
    sess = sessionmaker(bind=engine)

    session_m = sess()

    a_state = session_m.query(State).filter(State.id == '2').first()
    a_state.name = 'New Mexico'
    session_m.commit()
    session_m.close()
