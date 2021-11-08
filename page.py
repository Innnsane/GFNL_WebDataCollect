import os
import ujson
import datetime
from flask import Flask, render_template, Response, request, jsonify
from process import create_html

# 创建Flask对象app并初始化
app = Flask(__name__)
DATA = "./data"


# 通过python装饰器的方法定义路由地址
@app.route("/")
# 定义方法 用jinjia2引擎来渲染页面，并返回一个index.html页面
def root():
    return render_template("web.html")


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
        algorithm['algorithm'] = ujson.loads(request.form.get('algorithm'))
    elif request.method == "GET":
        algorithm['doNumber'] = request.args.get('doNumber')
        algorithm['inTurnType'] = request.args.get('inTurnType')
        algorithm['algorithm'] = ujson.loads(request.args.get('algorithm'))
    else:
        algorithm = []

    print(algorithm)
    # 如果获取的数据为空
    if not algorithm or not algorithm['algorithm']:
        return {'message': "error!"}

    previous = []
    today = "".join(str(datetime.date.today()).split("-")) + ".json"
    if os.path.exists(os.path.join(DATA, today)):
        with open(os.path.join(DATA, today), "r", encoding='utf-8') as f:
            previous = ujson.load(f)
            f.close()

    previous.append(algorithm)
    with open(os.path.join(DATA, today), "w", encoding='utf-8') as f:
        ujson.dump(previous, f)
        f.close()

    return {'message': "success"}


# 通过python装饰器的方法定义路由地址
@app.route("/algorithm/display")
# 定义方法 用jinjia2引擎来渲染页面，并返回一个index.html页面
def algorithm_display():
    return render_template("aldisplay.html", data=create_html(11))


# 定义app在8080端口运行
app.run(host='0.0.0.0', port=4222)
