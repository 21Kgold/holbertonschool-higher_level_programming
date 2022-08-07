#!/usr/bin/python3
"""
Connect to MySQL database remotely using python’s sqlalchemy module
The create_engine() method of sqlalchemy library takes in the connection URL
and returns a sqlalchemy engine that references both a Dialect and a Pool,
which together interpret the DBAPI’s module functions as well as the behavior
of the database.
"""

# Import the create_engine method from sqlalchemy library
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

# Guard script from be executed when imported
if __name__ == "__main__":
    # Define the database credentials
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    port = 3306
    # sintax: sqlalchemy.create_engine(url, **kwargs)
    # url sintax: “dialect+driver://username:password@host:port/database”
    # The dialect and driver for establishing the connection to MySQL database
    # are MySQL and mysqldb respectively
    engine = create_engine(f"mysql+mysqldb://{username}:{password} \
                            @localhost:{port}/{database}")
    factory = sessionmaker(bind=engine)
    session = factory()
    query = session.query(State).order_by(State.id).all()
    for item in query:
        print("{}: {}".format(item.id, item.name))
