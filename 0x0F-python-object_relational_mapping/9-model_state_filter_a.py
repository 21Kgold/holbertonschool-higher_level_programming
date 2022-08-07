#!/usr/bin/python3
"""
Connect to MySQL database remotely using python’s sqlalchemy module
and retrive all State objects that contain the letter a from a database
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    port = 3306
    engine = create_engine(f"mysql+mysqldb://{username}:{password} \
                            @localhost:{port}/{database}")
    factory = sessionmaker(bind=engine)
    session = factory()
    result = session.query(State).order_by(State.id) \
        .filter(State.name.ilike('%a%')).all()
    for row in result:
        print("{}: {}".format(row.id, row.name))
