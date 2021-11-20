import os
import ujson
import pymysql
from database import *
from dicts import *


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

    cursor.execute(sql_list)
    db.commit()

    cursor.close()
    db.close()


def algorithm_num_check():
    db = pymysql.connect(host=host, user=user, password=password, database="algorithm")
    cursor = db.cursor()

    sql = f"SELECT * FROM algorithm.algorithm_list;"

    cursor.execute(sql)
    algorithm_table = cursor.fetchall()

    for row in algorithm_table:
        length = int(row[5])
        length_truth = len(ujson.loads(row[6]))
        print(row[0], length, length_truth)
        if length != length_truth:
            print(row[0], length, length_truth)



def algorithm_query_create():
    db = pymysql.connect(host=host, user=user, password=password, database="algorithm")
    cursor = db.cursor()

    sql_exist_1 = "SELECT 1 FROM algorithm.algorithm_total WHERE "
    sql_exist_2 = " LIMIT 1;"

    algorithmDict = {"1": {}, "2": {}, "3": {}, "4": {}, "5": {}, "6": {}}
    for weekType in algorithmDict.keys():

        for atype in ALGORITHM.keys():
            if str(ALGORITHM[atype]["inTurn"]) == weekType or weekType == "6":
                algorithmDict[weekType][atype] = {}

                for pos in [1, 2, 3]:
                    if ALGORITHM[atype]["position"] < pos:
                        break
                    algorithmDict[weekType][atype][str(pos)] = {}

                    for statsDefault in ATTRIBUTELIST[ALGORITHM[atype]['attribute']]:
                        algorithmDict[weekType][atype][str(pos)][statsDefault] = 0

        # 同时更新存在的和不存在的
        for atype in algorithmDict[weekType].keys():
            for pos in algorithmDict[weekType][atype].keys():
                for stats in algorithmDict[weekType][atype][pos].keys():

                    sql = sql_exist_1 + \
                          f"week_type = {weekType} AND algorithm_id = '{atype}' AND algorithm_pos = {pos} AND algorithm_stats = {stats}" + \
                          sql_exist_2

                    cursor.execute(sql)
                    exist = cursor.fetchall()[0][0]

                    print(weekType, atype, pos, stats, exist)


def test():
    db = pymysql.connect(host=host, user=user, password=password, database="algorithm")
    cursor = db.cursor()


    algorithmDict = {"1": {}, "2": {}, "3": {}, "4": {}, "5": {}}
    for weekType in algorithmDict.keys():
        sql = f"SELECT id, algorithm_number, algorithm_json FROM algorithm.algorithm_list WHERE week_type = {weekType};"
        cursor.execute(sql)
        algorithm_table = cursor.fetchall()

        for row in algorithm_table:
            al_list = ujson.loads(row[2])
            if int(row[1]) != len(al_list):
                print(row[0], "len")

            for al in al_list:
                if str(ALGORITHM[al['id']]["inTurn"]) not in weekType and ALGORITHM[al['id']]["inTurn"] != 0 :
                    print(row[0], ALGORITHM[al['id']]["inTurn"])


if __name__ == '__main__':
    # main_algorithm_delete()
    # algorithm_query_create()
    test()
