#!/usr/bin/python3
"""
Module: 2-my_filter_states.py
lists all states from the database hbtn_0e_0_usa
"""
if __name__ == '__main__':
    import MySQLdb
    import sys
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.name FROM cities JOIN states ON\
                states.id = cities.state_id WHERE states.name = %s\
                ORDER BY cities.id ASC", (sys.argv[4], ))
    queries = cur.fetchall()
    print(", ".join(query[0] for query in queries))
    cur.close()
    db.close()
