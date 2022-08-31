#!/usr/bin/python3
"""lists all State objects that contain the letter a
from the database hbtn_0e_6_usa
"""
if __name__ == '__main__':
    import sys
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)
    data = session.query(State).order_by(
        State.id).filter(State.name.contains('a'))
    for states in data:
        print(f"{states.id}: {states.name}")
    session.close()
