# coding:utf-8
import json
from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False  # 显示中文


# 在Flask里 sqlachemy是非常方便的，但是假如数据量很大的话，
# 后台返回的json速度就很慢，很影响用户体验，所以用paginate来分页返回数据paginate(id, num)
#  #id为第几页 num表示一页有几条数据很明显
# 我们的页数应该是 [1,sum/num]所以在前台的页数应该是 1到 数据总数/一页的数据量例如 有7311条数据，
# 我们需要一页10条数据的话页数就是 1 ~ 732 因为还有 最后一页 只有一条数据

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@localhost/web_monitor'
# app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

Base = declarative_base()

# sqlalchemy 对已有表做操作需要先做一个映射类

class A50_OneStock_PL(Base):
    __tablename__ = 'A50_OneStock_PL'
    id = Column(Integer,primary_key=True,nullable=False, autoincrement=True)
    index_PL = Column(String(10),nullable=True)  # String在数据库中常见为varchar类型
    stock_PL = Column(String(10),nullable=True)  #
    profilo_PL = Column(String(10),nullable=True)  #
    profilo_PL_R = Column(String(10),nullable=True)  #



    def to_json(self):
        dict = self.__dict__
        if "_sa_instance_state" in dict:
            del dict["_sa_instance_state"]
        return dict



@app.route('/')
def index():
    return '<h1>"欢迎来到接口界面"</h1>'



# 使用接口后的渲染接口
# 这还只是一个静态的页面,不会自助
@app.route('/astock/v1')
def asVali():
    return render_template('astock.html')


@app.route('/astock/count')
def asdata_count():
    num = db.session.query(A50_OneStock_PL.profilo_PL_R).count()
    # return "'<h1>数据库的字段数为:% </h1>' % num "
    return jsonify({"数据库的字段总数":num})






# 思考如何把查询的数据变成一个大字典！而不是若干个小字典！
# 从数据库中一次全部查询展示成功
# 数据接口,API
@app.route('/astock', methods=['GET'])
def asdata():
    big_list = []
    pls = db.session.query(A50_OneStock_PL.profilo_PL_R).all()  # [[0.19],[0.19]] 需要两层遍历来做一个大列表
    for item in pls:
         for i in item:
             num_float = float(i)
             big_list.append(num_float)  # 需要把字符串类型转换为浮点型,而不是整型
# 有时候需要用int()函数转换字符串为整型，但是切记int()只能转化由纯数字组成的字符串，如下例：a
    t = {}
    t['data'] = big_list
    return jsonify(t)

# 关键是前端可以使用的数据格式是什么！　所以前端也要开始　了 也就是前端好不好用！接口有没有用！
    # big_list = {}
    # for item in comments:
    #     big_list.insert(item)
    # return jsonify({'data':big_list})
    # result = []
    # for comment in comments:
    #     result.append(comment.to_json())   # 用到了模型中的转换方法！　映射是成功的！　先做思考分页
    # return jsonify(result), 200



@app.route('/astock/ajax')
def asdata_ajax():
    return render_template('astock_ajax.html')





if __name__ == '__main__':
    app.run(debug=True)