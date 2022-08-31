#!/usr/bin/python3
"""prints all City objects from the database hbtn_0e_14_usa"""
if __name__ == '__main__':
    import sys
    from model_state import Base, State
    from model_city import City
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)
    data = session.query(State, City).order_by(
        City.id).filter(City.state_id == State.id).all()
    for state, city in data:
        print(f"{state.name}: ({city.id}) {city.name}")
    session.close()
