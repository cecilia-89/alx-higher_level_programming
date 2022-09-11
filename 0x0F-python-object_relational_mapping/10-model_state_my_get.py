#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(bind=engine)
    queries = session.query(State).filter(State.name.like(sys.argv[4])).all()
    if len(queries) == 0:
        print("Not found")
    else:
        for query in queries:
            print(f"{query.id}")
    session.close()
