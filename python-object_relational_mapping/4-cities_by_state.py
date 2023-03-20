#!/usr/bin/python3
# lists all states from the database hbtn_0e_0_usa
""" Use: ./[SCRIPTCALL] [USERNAME] [PASSWORD] [DATABASE] """
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name FROM \
                cities INNER JOIN states ON states.id=cities.state_id")
    [print(state) for state in cur.fetchall()]
