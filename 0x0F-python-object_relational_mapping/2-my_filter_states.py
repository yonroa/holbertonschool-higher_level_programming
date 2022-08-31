#!/usr/bin/python3
"""displays all values in the states table of hbtn_0e_0_usa
where name matches the argument
"""
if __name__ == '__main__':
    import MySQLdb
    import sys
    db = MySQLdb.connect(host='localhost', port=3306,
                         user=sys.argv[1], password=sys.argv[2],
                         database=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY '{}'\
             ORDER BY states.id ASC".format(sys.argv[4]))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    db.close()
