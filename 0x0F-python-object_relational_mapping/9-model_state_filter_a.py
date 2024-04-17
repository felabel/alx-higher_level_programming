#!/usr/bin/python3
"""script that prints the first State object from the database hbtn_0e_6_usa"""
import sys
from model_state import Base, State
from sqlalchemy.orm import Session
from sqlalchemy import create_engine


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)
    
    # Query the first State object ordered by id
    state = session.query(State).order_by(State.id).first()
    
    if state is None:
        print("Nothing")
    else:
        print("{}: {}".format(state.id, state.name))
    
    session.close()

