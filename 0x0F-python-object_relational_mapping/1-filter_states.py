#!/usr/bin/python3
"""
Module: 1-filter_states.py
lists all states from the database hbtn_0e_0_usa
"""
if __name__ == '__main__':
    import MySQLdb
    import sys
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name \
                LIKE 'N%' ORDER BY states.id ASC")
    queries = cur.fetchall()
    for query in queries:
        print(query)
    cur.close()
    db.close()
