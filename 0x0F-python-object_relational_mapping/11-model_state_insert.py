#!/usr/bin/python3
"""
This script adds the State object Louisiana
to the database `hbtn_0e_6_usa`.
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Access to the database and get a state
    from the database.
    """

    db = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3])
    eng = create_engine(db)
    sess = sessionmaker(bind=eng)

    session = sess()

    l_state = State(name='Louisiana')
    session.add(l_state)
    session.commit()
    print('{0}'.format(l_state.id))
    session.close()
