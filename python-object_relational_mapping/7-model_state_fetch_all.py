#!/usr/bin/python3
""" lists all state from database """

from sys import argv
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
        "script that will execute"

        databased = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3])

        engine = create_engine(databased)
        Session = sessionmaker(bind=engine)
        session = Session()

        results = session.query(State).order_by(State.id);

        for r in results:
                print(f'{r.id}: {r.name}')
