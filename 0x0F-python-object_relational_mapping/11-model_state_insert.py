#!/usr/bin/python3
"""
Connect to MySQL database remotely using python’s sqlalchemy module
and add the State object “Louisiana” to the database hbtn_0e_6_usa
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    match = "Louisiana"
    port = 3306
    engine = create_engine(f"mysql+mysqldb://{username}:{password} \
                            @localhost:{port}/{database}")
    factory = sessionmaker(bind=engine)
    session = factory()

    c1 = State(name=match)

    session.add(c1)
    session.commit()
    result = session.query(State).order_by(State.id) \
        .filter_by(name=match).all()
    if len(result) == 0:
        print("Not found")
    else:
        for row in result:
            print("{}".format(row.id))
