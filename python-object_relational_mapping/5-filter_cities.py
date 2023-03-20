#!/usr/bin/python3
""" Use: ./[SCRIPTCALL] [USERNAME] [PASSWORD] [DATABASE] [STATE NAME]"""
import MySQLdb
import sys

if __name__ == "__main__":

    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.name FROM cities \
                    INNER JOIN states ON states.id=cities.state_id \
                    WHERE states.name=%s", (sys.argv[4],))
    [print(state) for state in cur.fetchall()]
