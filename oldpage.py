from flask import Flask, render_template


# 创建Flask对象app并初始化
app = Flask(__name__)


@app.route("/")
def root_1():
    return render_template("oldpage.html")


@app.route("/<sth>")
def root_2(sth):
    return render_template("oldpage.html")


@app.route("/<sth>/<sth_2>")
def root_3(sth, sth_2):
    return render_template("oldpage.html")


# 定义app在4222端口运行
app.run(host='0.0.0.0', port=4222)