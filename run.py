# web模块
from flask import Flask,render_template
from api.sample import sample_api
from flask_sqlalchemy import SQLAlchemy

# 生成应用
app = Flask(__name__)

# 初始化db
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@localhost:3306/sample'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # 跟踪对象的修改，在本例中用不到调高运行效率，所以设置为False
app.config['JSON_AS_ASCII'] = False
db = SQLAlchemy(app=app)  # 为哪个Flask app对象创建SQLAlchemy对象，赋值为db

# 根目录
@app.route("/")
def main():
    return render_template("index.html")

# 注册蓝图
app.register_blueprint(sample_api, url_prefix='')

#if __name__ == "__main__":
    #app.run(host="0.0.0.0", port=8080, debug=True)
