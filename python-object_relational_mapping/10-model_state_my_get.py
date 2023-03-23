#!/usr/bin/python3
""" Lists all state from database. """

from sys import argv
from model_state import State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).order_by(State.id).first()

    for state in session.query(State):
        if state.name == sys.argv[4]:
            print("{}".format(state.id))
            quit()
    print("Not found")
