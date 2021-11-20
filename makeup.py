import ujson
import datetime
from database import *
from apscheduler.schedulers.blocking import BlockingScheduler
from dicts import *

scheduler = BlockingScheduler()


def algorithm_query_update():
    print(f'algorithm_query_update processing at {datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")}')
    db = pymysql.connect(host=host, user=user, password=password, database="algorithm")
    cursor = db.cursor()

    algorithmDict = {"1": {}, "2": {}, "3": {}, "4": {}, "5": {}, "6": {}}
    for weekType in algorithmDict.keys():
        sql_list = f"SELECT SUM(do_number) , SUM(algorithm_number) FROM algorithm.algorithm_list WHERE week_type = {weekType};"
        cursor.execute(sql_list)
        algorithm_data = cursor.fetchall()[0]
        algorithm_do_num = int(algorithm_data[0])
        algorithm_al_num = int(algorithm_data[1])

        sql = f"SELECT algorithm_json FROM algorithm.algorithm_list WHERE week_type = {weekType};"
        cursor.execute(sql)
        algorithm_table = cursor.fetchall()

        for atype in ALGORITHM.keys():
            if str(ALGORITHM[atype]["inTurn"]) == weekType or weekType == "6" or ALGORITHM[atype]["inTurn"] == 0:
                algorithmDict[weekType][atype] = {}

                for pos in [1, 2, 3]:
                    if ALGORITHM[atype]["position"] < pos:
                        break
                    algorithmDict[weekType][atype][str(pos)] = {}

                    for statsDefault in ATTRIBUTELIST[ALGORITHM[atype]['attribute']]:
                        algorithmDict[weekType][atype][str(pos)][str(statsDefault)] = 0

        for row in algorithm_table:
            al_list = ujson.loads(row[0])
            for al in al_list:
                algorithmDict[weekType][al['id']][al['position']][al['mainAttr']] += 1

        # 同时更新存在的和不存在的
        for atype in algorithmDict[weekType].keys():
            for pos in algorithmDict[weekType][atype].keys():
                for stats in algorithmDict[weekType][atype][pos].keys():
                    single = algorithmDict[weekType][atype][pos][stats]
                    sql = f"UPDATE algorithm.algorithm_total SET has = {single} WHERE " \
                          f"week_type = {weekType} AND algorithm_id = '{atype}' AND algorithm_pos = {pos} AND algorithm_stats = {stats}"
                    cursor.execute(sql)

        sql_week = f"UPDATE algorithm.algorithm_total SET allal = {algorithm_al_num} , done = {algorithm_do_num} WHERE week_type = {weekType} "
        cursor.execute(sql_week)

    db.commit()
    cursor.close()
    db.close()


def mind_fragment_query_update():
    print(f'mind_fragment_query_update processing at {datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")}')
    db = pymysql.connect(host=host, user=user, password=password, database="algorithm")
    cursor = db.cursor()

    for doll in DOLL.keys():
        sql_doll = f"SELECT fragment, gift1, gift2, gift3, stage, stage1, stage2, stage3, stage4, stage5, stage6 " \
                   f"FROM algorithm.mindfragment_list WHERE doll = '{doll}';"
        cursor.execute(sql_doll)
        doll_table = cursor.fetchall()

        doll_data = {
            "fragment": {"sum": 0, "num": 1},
            "gift1": {"sum": 0, "num": 1},
            "gift2": {"sum": 0, "num": 1},
            "gift3": {"sum": 0, "num": 1},
            "stage": {"sum": 0, "num": 1},
        }

        for i in [1, 2, 3, 4, 5, 6]:
            doll_data[f"stage{i}"] = {"sum": 0, "num": 1}
            doll_data[f"s{i}_f"] = {"sum": 0, "num": 0}
            doll_data[f"s{i}_g1"] = {"sum": 0, "num": 0}
            doll_data[f"s{i}_g2"] = {"sum": 0, "num": 0}
            doll_data[f"s{i}_g3"] = {"sum": 0, "num": 0}

        for data in doll_table:
            if not data[0]:
                continue
            doll_data["fragment"]["sum"] += int(data[0])
            doll_data["gift1"]["sum"] += int(data[1])
            doll_data["gift2"]["sum"] += int(data[2])
            doll_data["gift3"]["sum"] += int(data[3])
            doll_data["stage"]["sum"] += int(data[4])

            for i in [5, 6, 7, 8, 9, 10]:

                if int(data[i]) != 0:
                    doll_data[f"stage{i - 4}"]["sum"] += 1
                    doll_data[f"s{i - 4}_f"]["sum"] += float(data[0]) / float(data[4])
                    doll_data[f"s{i - 4}_f"]["num"] += 1
                    doll_data[f"s{i - 4}_g1"]["sum"] += float(data[1]) / float(data[4])
                    doll_data[f"s{i - 4}_g1"]["num"] += 1
                    doll_data[f"s{i - 4}_g2"]["sum"] += float(data[2]) / float(data[4])
                    doll_data[f"s{i - 4}_g2"]["num"] += 1
                    doll_data[f"s{i - 4}_g3"]["sum"] += float(data[3]) / float(data[4])
                    doll_data[f"s{i - 4}_g3"]["num"] += 1

        sql = f"UPDATE algorithm.mindfragment_total SET "
        for key in doll_data.keys():
            if doll_data[key]['num'] == 0:
                sql += f"{key} = {0}, "
            else:
                sql += f"{key} = {doll_data[key]['sum'] / doll_data[key]['num']}, "

        sql = sql[:-2] + f" WHERE doll = '{doll}';"
        cursor.execute(sql)

    db.commit()
    cursor.close()
    db.close()



if __name__ == "__main__":
    algorithm_query_update()
    # mind_fragment_query_update()
    # job = scheduler.add_job(algorithm_query_update, "interval", seconds=600)
    # job.modify(max_instances=1)
    # scheduler.start()
