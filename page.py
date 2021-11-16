import os
import ujson
from flask import Flask, render_template, Response, request, send_from_directory
from dicts import *
from database import *

# 创建Flask对象app并初始化
app = Flask(__name__)
DATA = "./data"


# 通过python装饰器的方法定义路由地址
@app.route("/")
# 定义方法 用jinjia2引擎来渲染页面，并返回一个index.html页面
def root():
    return render_template("al.html")


# 设置网站icon
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')


# 请求图片
@app.route("/image/<image_id>.png")
def get_frame(image_id):
    # 去对应的文件夹找到对应名字的图片
    with open(r'./res/{}.png'.format(image_id), 'rb') as f:
        image = f.read()
        # 返回给用户
        resp = Response(image, mimetype="image/png")
        return resp


# app的路由地址"/algorithm/submit"即为ajax中定义的url地址，采用POST、GET方法均可提交
@app.route("/algorithm/submit", methods=["GET", "POST"])
# 从这里定义具体的函数 返回值均为json格式
def algorithm_submit():
    algorithm = {}
    # 由于POST、GET获取数据的方式不同，需要使用if语句进行判断
    if request.method == "POST":
        algorithm['doNumber'] = request.form.get('doNumber')
        algorithm['inTurnType'] = request.form.get('inTurnType')
        algorithm_json = request.form.get('algorithm')
        algorithm['algorithm'] = ujson.loads(algorithm_json)
    elif request.method == "GET":
        algorithm['doNumber'] = request.args.get('doNumber')
        algorithm['inTurnType'] = request.args.get('inTurnType')
        algorithm_json = request.args.get('algorithm')
        algorithm['algorithm'] = ujson.loads(algorithm_json)
    else:
        algorithm = []
        algorithm_json = ""

    # 如果获取的数据为空
    if not algorithm or not algorithm['algorithm']:
        return {'message': "算法为空!"}
    if len(algorithm['algorithm']) < int(algorithm['doNumber']):
        return {'message': "算法数量少于出击次数!"}
    length = len(algorithm['algorithm'])
    ip = request.remote_addr

    try:
        a = ATTRIBUTE[int(algorithm['algorithm'][0]['mainAttr'])]
    except:
        return {'message': "数据格式错误！"}

    sql = "INSERT INTO algorithm_list VALUES "
    sql += f"(null, NOW(), '{ip}', {algorithm['doNumber']}, {algorithm['inTurnType']}, {length}, '{algorithm_json}');"

    db = pymysql.connect(host=host, user=user, password=password, database="algorithm")
    cursor = db.cursor()

    try:
        print(sql)
        cursor.execute(sql)
        db.commit()

    except Exception as e:
        db.rollback()
        cursor.close()
        db.close()
        return {'status': "error", 'message': ",数据库录入失败！<br/>" + str(e)}

    cursor.close()
    db.close()
    return {'message': "success"}


# 通过python装饰器的方法定义路由地址
@app.route("/algorithm/display")
# 定义方法 用jinjia2引擎来渲染页面，并返回一个index.html页面
def algorithm_display():
    db = pymysql.connect(host=host, user=user, password=password, database="algorithm")
    cursor = db.cursor()

    statistic = {}
    sql_statistic = f"SELECT COUNT(*) , SUM(do_number) , SUM(algorithm_number) FROM algorithm.algorithm_list"
    cursor.execute(sql_statistic)
    data = cursor.fetchall()[0]
    statistic["listNum"] = data[0]
    statistic["doNum"] = data[1]
    statistic["alNum"] = data[2]

    limit = 20
    sql = f"select * from algorithm.algorithm_list order by id desc limit {limit} ;"
    cursor.execute(sql)
    algorithm_table = cursor.fetchall()

    html_list = []
    for row in algorithm_table:
        this_html_dict = {
            "number": row[0],
            "weekType": row[4],
            "doNum": row[3],
            "dropNum": row[5],
            "time": row[1],
            "data": []
        }

        algorithm_list = ujson.loads(row[6])
        for j in algorithm_list:
            this_html_dict["data"].append({
                "name": ALGORITHM[j['id']]['name'],
                "position": j['position'],
                "stats": ATTRIBUTE[int(j['mainAttr'])],
            })

        html_list.append(this_html_dict)

    return render_template("aldisplay.html", algorithm_list=html_list, statistic=statistic)


# 通过python装饰器的方法定义路由地址
@app.route("/algorithm/query")
def algorithm_query():
    algorithm_list = []
    db = pymysql.connect(host=host, user=user, password=password, database="algorithm")
    cursor = db.cursor()

    sql_4 = f"SELECT * FROM algorithm.algorithm_total WHERE algorithm_id IS NOT null AND algorithm_pos IS NOT null AND algorithm_stats IS NOT null;"
    cursor.execute(sql_4)
    algorithm_table_4 = cursor.fetchall()

    for row in algorithm_table_4:
        algorithm_list.append({
            "week": row[1],
            "name_id": row[2],
            "name": ALGORITHM[row[2]]['name'],
            "pos": row[3],
            "stats_id": row[4],
            "stats": ATTRIBUTE[row[4]],
            "getNum": row[5],
            "allNum": row[6],
            "doNum": row[7],
            "drop": "0%" if (row[6] == 0) else str(round(float(row[5]) / float(row[6]) * 100, 2)) + "%",
            "frequent": "0%" if (row[7] == 0) else str(round(float(row[5]) / float(row[7]) * 100, 2)) + "%",
        })

    return render_template("alquery.html", algorithm_list=algorithm_list)


@app.route("/mind")
def mind_submit_page():
    return render_template("mind.html")


@app.route("/mind/submit", methods=["POST"])
def mind_submit():
    fragment = {
        "doll_id": request.form.get('doll_id'),
        "stage_json": request.form.get('stage'),
        "stage_num": 0,
        "fragment": request.form.get('frag_num'),
        "gift1": request.form.get('gift_num1'),
        "gift2": request.form.get('gift_num2'),
        "gift3": request.form.get('gift_num3'),
        "ip": request.remote_addr,
    }

    try:
        fragment["stage"] = ujson.loads(fragment["stage_json"])
        for num in fragment["stage"].keys():
            if fragment["stage"][num]:
                fragment["stage_num"] += 1

        print(fragment["doll_id"], fragment["stage"], fragment["fragment"])
    except Exception as e:
        return {'status': "error", 'message': "数据格式错误！<br/>" + str(e)}

    sql = "INSERT INTO algorithm.mindfragment_list VALUES "
    sql += f"(null, NOW(), '{fragment['ip']}', {fragment['doll_id']}, {fragment['fragment']}, " \
           f"{fragment['gift1']}, {fragment['gift2']}, {fragment['gift3']}, {fragment['stage_num']}, "
    for num in fragment["stage"].keys():
        if fragment["stage"][num]:
            sql += f"1, "
        else:
            sql += "0, "
    sql = sql[:-2] + f") ;"

    print(sql)
    db = pymysql.connect(host=host, user=user, password=password, database="algorithm")
    cursor = db.cursor()

    try:
        cursor.execute(sql)
        db.commit()

    except Exception as e:
        db.rollback()
        cursor.close()
        db.close()
        return {'status': "error", 'message': ",数据库录入失败！<br/>" + str(e)}

    cursor.close()
    db.close()

    return {'message': "success"}


@app.route("/mind/display")
def mind_display():
    db = pymysql.connect(host=host, user=user, password=password, database="algorithm")
    cursor = db.cursor()

    sql = f"SELECT * FROM algorithm.mindfragment_total;"
    cursor.execute(sql)
    fragment_table = cursor.fetchall()

    fragment_dict = {}
    for row in fragment_table:
        fragment_dict[row[0]] = {
            "doll_id": row[0],
            "fragment": row[1],
            "stage": row[2],
            "gift1": row[3],
            "gift2": row[4],
            "gift3": row[5],
        }

        for i in [1, 2, 3, 4, 5, 6]:
            fragment_dict[row[0]][f"stage{i}"] = row[i + 5]
            fragment_dict[row[0]][f"s{i}_f"] = row[i + 11]
            fragment_dict[row[0]][f"s{i}_g1"] = row[i + 17]
            fragment_dict[row[0]][f"s{i}_g2"] = row[i + 23]
            fragment_dict[row[0]][f"s{i}_g3"] = row[i + 29]

    return render_template("minddisplay.html", fragment_dict=fragment_dict)


# 定义app在4222端口运行
app.run(port=4222, debug=True)

