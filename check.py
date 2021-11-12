import os
import pymysql
from database import *


def main_algorithm_delete():
    while True:
        process = input("type in delete id or quit(0)\n--")
        if process == "0":
            break
        else:
            algorithm_delete(process)


def algorithm_delete(list_id):
    db = pymysql.connect(host=host, user=user, password=password, database="algorithm")
    cursor = db.cursor()

    sql_list = f"DELETE FROM algorithm.algorithm_list WHERE (id = {list_id});"
    sql_single = f"DELETE FROM algorithm.algorithm_single WHERE (list_id = {list_id});"

    cursor.execute(sql_list)
    db.commit()

    cursor.execute(sql_single)
    db.commit()

    cursor.close()
    db.close()


if __name__ == '__main__':
    main_algorithm_delete()
