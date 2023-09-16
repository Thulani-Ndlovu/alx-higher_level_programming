#!/usr/bin/python3
'''
    write a script that takes in arguments and displays all
    values in the states
    table of hbtn_0e_0_usa where name matches the argument. But this time,
    write one that is safe from MySQL injections!
'''
import sys
import MySQLdb

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    stateName = sys.argv[4]
    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )
    cursor = db.cursor()
    sql_query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cursor.execute(sql_query, (stateName,))
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()
