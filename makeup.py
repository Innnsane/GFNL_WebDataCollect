import ujson
import datetime
from database import *
from apscheduler.schedulers.blocking import BlockingScheduler

scheduler = BlockingScheduler()


def algorithm_query_update():
    print(f'algorithm_query_update processing at {datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")}')
    db = pymysql.connect(host=host, user=user, password=password, database="algorithm")
    cursor = db.cursor()

    # 暂时使用 algorithm_single

    algorithmDict = {"1": {}, "2": {}, "3": {}, "4": {}, "5": {}, "6": {}}
    for weekType in algorithmDict.keys():
        sql_list = f"SELECT SUM(do_number) FROM algorithm.algorithm_list WHERE week_type = {weekType};"
        cursor.execute(sql_list)
        algorithm_do_num = int(cursor.fetchall()[0][0])

        sql = f"SELECT algorithm_json FROM algorithm.algorithm_list WHERE week_type = {weekType};"
        cursor.execute(sql)
        algorithm_table = cursor.fetchall()

        for row in algorithm_table:
            al_list = ujson.loads(row[0])
            for al in al_list:
                if al['id'] not in algorithmDict[weekType]:
                    algorithmDict[weekType][al['id']] = {}
                if al['position'] not in algorithmDict[weekType][al['id']].keys():
                    algorithmDict[weekType][al['id']][al['position']] = {}
                if al['mainAttr'] not in algorithmDict[weekType][al['id']][al['position']].keys():
                    algorithmDict[weekType][al['id']][al['position']][al['mainAttr']] = 0
                algorithmDict[weekType][al['id']][al['position']][al['mainAttr']] += 1

        for atype in algorithmDict[weekType].keys():
            num_atype = 0
            for pos in algorithmDict[weekType][atype].keys():
                num_pos = 0
                for stats in algorithmDict[weekType][atype][pos].keys():
                    single = algorithmDict[weekType][atype][pos][stats]
                    sql_stats = f"UPDATE algorithm.algorithm_total SET has = {single} , done = {algorithm_do_num} WHERE " \
                                f"week_type = {weekType} AND algorithm_id = '{atype}' AND algorithm_pos = {pos} AND algorithm_stats = {stats}"

                    cursor.execute(sql_stats)
                    num_pos += single
                    num_atype += single

                sql_pos = f"UPDATE algorithm.algorithm_total SET has = {num_pos} , done = {algorithm_do_num} WHERE " \
                          f"week_type = {weekType} AND algorithm_id = '{atype}' AND algorithm_pos = {pos} AND algorithm_stats is null"
                cursor.execute(sql_pos)

            sql_atype = f"UPDATE algorithm.algorithm_total SET has = {num_atype} , done = {algorithm_do_num} WHERE " \
                        f"week_type = {weekType} AND algorithm_id = '{atype}' AND algorithm_pos is null AND algorithm_stats is null"
            cursor.execute(sql_atype)

        sql_week = f"UPDATE algorithm.algorithm_total SET has = {algorithm_do_num} , done = {algorithm_do_num} WHERE " \
                   f"week_type = {weekType} AND algorithm_id is null AND algorithm_pos is null AND algorithm_stats is null"
        cursor.execute(sql_week)

    db.commit()
    cursor.close()
    db.close()


if __name__ == "__main__":
    job = scheduler.add_job(algorithm_query_update, "interval", seconds=600)
    job.modify(max_instances=1)
    scheduler.start()
