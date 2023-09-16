#!/usr/bin/python3
'''
    script that takes in the name of a state as an argument
    and lists all cities of that state,
    using the database hbtn_0e_4_usa
'''

import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    sql_query = ("SELECT * FROM `cities` as `c` \
                 INNER JOIN `states` as `s` \
                 ON `c`.`state_id` = `s`.`id` \
                 ORDER BY `c`.`id`")
    cursor.execute(sql_query)
