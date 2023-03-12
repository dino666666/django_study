"""
一、快速开发网站
    pip install flask
二、HTML标签
    2.1 编码
        <meta charset="UTF-8">
    2.2 tittle
        <title>Title</title>
    2.3 标题
        <body>
                <h1>1级标题</h1>
                <h2>2级标题</h2>
                <h3>3级标题</h3>
                <h4>4级标题</h4>
                <h5>5级标题</h5>
        </body>
    2.4 div和span
        <div>一个人占一行【块级标签】</div>
        <span>自己多大占多大【行内标签、内联标签】</span>
            -<span style='color:red;'>联通</span> ->字体变红色
"""
from flask import Flask, render_template

app = Flask(__name__)


# 创建了网址 /show/info 和函数index 的对应关系
# 以后用户在浏览器上访问/show/info, 网站自动执行index
@app.route("/show/info")
def index():
    # return "中国联通"
    # return "中<h1>国</h1>"
    # Flask内部会自动打开这个文件，并读取内容，将内容给用户返回
    # 默认： 取当前项目目录的templates文件夹中找。
    return render_template("index.html")


if __name__ == '__main__':
    app.run()
    # 网页端访问http://127.0.0.1:5000/show/info即可显示网页
