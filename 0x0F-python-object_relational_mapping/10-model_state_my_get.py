#!/usr/bin/python3
"""
Script that lists all objects that contain the a letter from the database
"""
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == "__main__":

    import sys
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]))
    Base.metadata.create_all(engine)

    sess = Session(engine)
    state_us = sess.query(State).filter(State.name == sys.argv[4]).first()
    if state_us:
        print("{}".format(state_us.id))
    else:
        print("Not found")
    sess.close()
