#!/usr/bin/python3
"""
Script to connect a MySQL database remotely using python’s sqlalchemy module
and  changes the name of a State object from the database hbtn_0e_6_usa
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    match = "New Mexico"
    port = 3306
    engine = create_engine(f"mysql+mysqldb://{username}:{password} \
                            @localhost:{port}/{database}")
    factory = sessionmaker(bind=engine)
    session = factory()

    c1 = session.query(State).get(2)

    c1.name = match
    session.commit()
    c1 = session.query(State).first()
