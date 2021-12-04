import os
import ujson
from flask import Flask, render_template, Response, request, send_from_directory
from flask import abort
from dicts import *
from database import *

# 创建Flask对象app并初始化
app = Flask(__name__)
DATA = "./data"


@app.route("/")
def root():
    return render_template("mainpage.html")


# 网站icon的返回
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')


# 请求图片 暂时不使用服务器内的资源 图片展示采用外链的方式
@app.route("/image/<image_id>.png")
def get_frame(image_id):
    # 去对应的文件夹找到对应名字的图片
    with open(r'./res/{}.png'.format(image_id), 'rb') as f:
        image = f.read()
        # 返回给用户
        resp = Response(image, mimetype="image/png")
        return resp


# 请求静态资源 如CSS、和JavaScript资源
@app.route("/src/<src_id>")
def get_src(src_id):
    return send_from_directory(os.path.join(app.root_path, 'static'), src_id)


# 算法相关内容的提交与展示

@app.route("/algorithm")
def algorithm_submit_page():
    return render_template("al.html")


@app.route("/algorithm/submit", methods=["GET", "POST"])
def algorithm_submit():
    algorithm = {}
    # 由于POST、GET获取数据的方式不同，需要使用if语句进行判断
    if request.method == "POST":
        algorithm['doNumber'] = int(request.form.get('doNumber'))
        algorithm['inTurnType'] = int(request.form.get('inTurnType'))
        algorithm_json = request.form.get('algorithm')
        algorithm['algorithm'] = ujson.loads(algorithm_json)
    elif request.method == "GET":
        algorithm['doNumber'] = int(request.args.get('doNumber'))
        algorithm['inTurnType'] = int(request.args.get('inTurnType'))
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

    sql = "INSERT INTO algorithm_list VALUES (null, NOW(), %s, %s, %s, %s, %s);"
    db = pymysql.connect(host=host, user=user, password=password, database="algorithm")
    cursor = db.cursor()

    try:
        # 防止SQL注入 采用Python的格式化字符串功能
        print("algorithm -", ip, algorithm['doNumber'], algorithm['inTurnType'], length)
        cursor.execute(sql, (ip, algorithm['doNumber'], algorithm['inTurnType'], length, algorithm_json))
        db.commit()

    except Exception as e:
        db.rollback()
        cursor.close()
        db.close()
        return {'status': "error", 'message': ",数据库录入失败！<br/>" + str(e)}

    cursor.close()
    db.close()
    return {'message': "success"}


@app.route("/algorithm/display")
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


# 心智碎片相关内容的提交与展示

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

    sql = "INSERT INTO algorithm.mindfragment_list VALUES (null, NOW(), %s, %s, %s, %s, %s, %s, %s, "
    for num in fragment["stage"].keys():
        sql += f"1, " if fragment["stage"][num] else "0, "
    sql = sql[:-2] + f") ;"

    db = pymysql.connect(host=host, user=user, password=password, database="algorithm")
    cursor = db.cursor()

    try:
        print(sql)
        cursor.execute(sql, (fragment['ip'], fragment['doll_id'], fragment['fragment'], fragment['gift1'],
                             fragment['gift2'], fragment['gift3'], fragment['stage_num']))
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


# 基础检索相关内容的提交与展示

@app.route("/retrieval")
def retrieval_submit_display():
    return render_template("ret.html")


@app.route("/retrieval/submit", methods=["POST"])
def retrieval_submit():
    retrieval = {
        "number": request.form.get('number'),
        "get_json": request.form.get('get'),
    }
    get_list = []
    ip = request.remote_addr

    try:
        retrieval["get_list"] = ujson.loads(retrieval["get_json"])
        if len(retrieval["get_list"]) > 10:
            return {'status': "error", 'message': "数据大于10项！<br/>"}
        for get in get_list:
            get_item = get.split("_")[0]
            test = ITEM[get_item][get]
    except Exception as e:
        return {'status': "error", 'message': "数据格式错误！<br/>" + str(e)}

    sql = "INSERT INTO algorithm.retrieval_list VALUES (null, NOW(), %s, %s, "

    i = 0
    while i < 10:
        if i < len(retrieval["get_list"]):
            if retrieval['get_list'][i] not in ITEM_ALL.keys():
                return {'status': "error", 'message': "数据格式错误！"}
            sql += f"'{retrieval['get_list'][i]}', "
        else:
            sql += "'', "
        i += 1

    sql = sql[:-2] + f") ;"

    db = pymysql.connect(host=host, user=user, password=password, database="algorithm")
    cursor = db.cursor()

    try:
        print(sql)
        cursor.execute(sql, (ip, retrieval['number']))
        db.commit()

    except Exception as e:
        db.rollback()
        cursor.close()
        db.close()
        return {'status': "error", 'message': ",数据库录入失败！<br/>" + str(e)}

    cursor.close()
    db.close()

    return {'message': "success"}


@app.route("/retrieval/display")
def retrieval_display():
    db = pymysql.connect(host=host, user=user, password=password, database="algorithm")
    cursor = db.cursor()

    statistic = {}
    sql_statistic = f"SELECT COUNT(*) , SUM(number) FROM algorithm.retrieval_list"
    cursor.execute(sql_statistic)
    data = cursor.fetchall()[0]
    statistic["listNum"] = data[0]
    statistic["getNum"] = data[1]

    limit = 20
    sql = f"select * from algorithm.retrieval_list order by id desc limit {limit} ;"
    cursor.execute(sql)
    algorithm_table = cursor.fetchall()

    html_list = []
    for row in algorithm_table:
        this_html_dict = {
            "no": row[0],
            "time": row[1],
            "number": row[3],
            "data": []
        }

        i = 0
        while i < 10:
            this_html_dict["data"].append(row[i + 4])
            i += 1

        html_list.append(this_html_dict)

    return render_template("retdisplay.html", retrieval_list=html_list, statistic=statistic)


@app.route("/retrieval/query")
def retrieval_query():
    db = pymysql.connect(host=host, user=user, password=password, database="algorithm")
    cursor = db.cursor()

    sql_total = f"SELECT SUM(number) FROM algorithm.retrieval_list;"
    cursor.execute(sql_total)
    item_total = cursor.fetchall()[0][0]

    sql = f"SELECT * FROM algorithm.retrieval_total;"
    cursor.execute(sql)
    table = cursor.fetchall()

    item_dict = {}
    for row in table:
        item_dict[row[0]] = row[1]

    return render_template("retquery.html", item_dict=item_dict, item_total=item_total)


# 为截图识别服务的图片资源传输 若图片模板不存在则返回404
@app.route("/retrieval/template/<name>")
def retrieval_template(name):
    try:
        with open(r'./template/{}'.format(name), 'rb') as f:
            image = f.read()
            resp = Response(image, mimetype="image/png")
            return resp
    except:
        abort(404)


@app.route("/retrieval/screenshot")
def retrieval_opencv():
    return render_template("retopencv.html")


# 定义app在4222端口运行
app.run(port=83, debug=True)

