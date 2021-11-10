import os
import ujson
import pymysql
from flask import Flask, render_template, Response, request, jsonify, send_from_directory
from process import create_html
from process import format_algorithm_single
from dicts import *
from database import *

# 创建Flask对象app并初始化
app = Flask(__name__)
DATA = "./data"


# 通过python装饰器的方法定义路由地址
@app.route("/")
# 定义方法 用jinjia2引擎来渲染页面，并返回一个index.html页面
def root():
    return render_template("web.html")


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
        return {'message': "error!"}
    algorithm_format = format_algorithm_single(algorithm['algorithm'])
    length = len(algorithm['algorithm'])
    ip = request.remote_addr

    sql_1 = "INSERT INTO algorithm_list VALUES "
    sql_1 += f"(null, NOW(), '{ip}', {algorithm['doNumber']}, {algorithm['inTurnType']}, {length}, '{algorithm_json}');"
    sql_2_part1 = "INSERT INTO algorithm_single VALUES "

    db = pymysql.connect(host=host, user=user, password=password, database="algorithm")
    cursor = db.cursor()

    try:
        print(sql_1)
        cursor.execute(sql_1)
        db.commit()

        cursor.execute("SELECT LAST_INSERT_ID()")
        last_id = cursor.fetchall()[0][0]

        for keyname in algorithm_format.keys():
            key = keyname.split("-")
            sql_2_part2 = f"(null, {last_id}, NOW(), {algorithm['inTurnType']}, '{key[0]}', '{ALGORITHM[key[0]]['name']}', "
            sql_2_part2 += f"{key[1]}, {key[2]}, '{ATTRIBUTE[int(key[2])].replace(' ', '_')}', "
            sql_2_part2 += f"{algorithm_format[keyname]}, {algorithm['doNumber']});"
            print(sql_2_part1 + sql_2_part2)
            cursor.execute(sql_2_part1 + sql_2_part2)
        db.commit()

    except Exception as e:
        db.rollback()
        cursor.close()
        db.close()
        return {'status': "error", 'message': "code error"}

    cursor.close()
    db.close()
    return {'message': "success"}


# 通过python装饰器的方法定义路由地址
@app.route("/algorithm/display")
# 定义方法 用jinjia2引擎来渲染页面，并返回一个index.html页面
def algorithm_display():
    db = pymysql.connect(host=host, user=user, password=password, database="algorithm")
    cursor = db.cursor()

    limit = 20
    sql = f"select * from algorithm_list order by id desc limit {limit} ;"
    cursor.execute(sql)
    algorithm_table = cursor.fetchall()

    html_list = []
    for row in algorithm_table:
        this_html_dict = {
            "1": f"No.{row[0]}__周{row[4]}_执行{row[3]}次_掉落{row[5]}个算法_({str(row[1]).replace(' ', '_')})",
            "2": []
        }

        algorithm_list = ujson.loads(row[6])
        for j in algorithm_list:
            this_html_dict["2"].append(f"{ALGORITHM[j['id']]['name']}-{j['position']}_{ATTRIBUTE[int(j['mainAttr'])]}")

        html_list.append(this_html_dict)

    return render_template("aldisplay.html", data=ujson.dumps(html_list))


# 定义app在4222端口运行
app.run(port=4222)
