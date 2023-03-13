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
    2.5 超链接
        - 跳转到其他网站: <a href="https://cn.bing.com/">点击跳转</a>
        - 跳转到自己网站其他的地址： <a href="/get/news">点击跳转</a>
    2.6 图片
        -显示别人的图片： <img src="//www.baidu.com/img/pcdoodle_2a77789e1a67227122be09c5be16fe46.png">
        -显示自己的图片： <img src="/static/xxx.png">
        -设置图片高度和宽度：
            <img src="/static/xxx.png" style="height:100px; width:200px">
            <img src="/static/xxx.png" style="height:10%; width:20%">
    2.7 列表
        -无序列表
        <ul>
            <li>中国联通</li>
            <li>中国移动</li>
        </ul>
        -有序列表
        <ol>
            <li>中国联通</li>
            <li>中国移动</li>
        </ol>
    2.8 表格
        <table border="1">  # border="1"表示添加边框，可不带
            <thead>
                <tr> <th>ID</th> <th>name</th> <th>age</th> </tr>
            </thead>
            <tbody>
                <tr> <td>10</td> <td>张三</td> <td>12</td> <tr>
                <tr> <td>11</td> <td>李四</td> <td>33</td> <tr>
            </tbody>
        </table>
    2.9 input标签
        -普通文本框： <input type="text" />
        -密码框： <input type="password">
        -单选框： <input type="radio" name="n1">男
                  <input type="radio" name="n1">女
        -复选框： <input type="checkbox">篮球
        -普通按钮： <input type="button" value="提交">
        -提交按钮： <input type="submit" value="提交">
    2.10 下拉框
        <select multiple>   # multiple表示可以多选，可不带
            <option>北京</option>
            <option>上海</option>
            <option>深圳</option>
        </select>
    2.11 多行文本
        <textarea row="3"></textarea>    # row="3"表示默认3行，可不带

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


@app.route("/get/news")
def get_news():
    return render_template("get_news.html")


if __name__ == '__main__':
    app.run()
    # 网页端访问 http://127.0.0.1:5000/show/info 即可显示网页
