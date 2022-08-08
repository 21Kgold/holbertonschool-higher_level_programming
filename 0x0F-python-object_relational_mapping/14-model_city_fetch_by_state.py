#!/usr/bin/python3
"""
Script that prints all City objects from the database hbtn_0e_14_usa
"""

import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    port = 3306
    State.cities = relationship("City",
                                order_by=City.id, back_populates="state")
    engine = create_engine(f"mysql+mysqldb://{username}:{password} \
                            @localhost:{port}/{database}")
    factory = sessionmaker(bind=engine)
    session = factory()
    query = session.query(State, City).\
        filter(City.state_id == State.id).all()
    for row in query:
        print("{}: ({}) {}".format(row[0].name, row[1].id, row[1].name))
