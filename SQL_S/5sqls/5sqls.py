#!


# 基本思路：
# 1. 先使用sqlalchemy，写5个提取查询最后一条数据的函数，添加入一个列表然后打印这个列表看看效果


# 数据表名称
# | A50_OneStock_PL       |
# | J225_OneStock_PL      |
# | MHI_OneStock_PL       |
# | OneStock_ES500_PL     |
# | oneStock_FTSE100_PL




# 每个数据表的字段名称
# | id           | int(11)     | NO   | PRI | NULL    | auto_increment |
# | index_PL     | varchar(10) | YES  |     | NULL    |                |
# | stock_PL     | varchar(10) | YES  |     | NULL    |                |
# | profilo_PL   | varchar(10) | YES  |     | NULL    |                |
# | profilo_PL_R | varchar(10) | YES  |     | NULL    |                |
# +--------------+-------------+------+-----+---------+------------


from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, String, Integer
import pymysql
from sqlalchemy.ext.declarative import declarative_base

#
# _5sqls = []
# # from flask import Flask
#
# from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy import Column, String, Integer
# import pymysql
# from sqlalchemy.ext.declarative import declarative_base
#
#
#
# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@localhost/web_monitor'
# # app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)
#
# Base = declarative_base()
# class A50_OneStock_PL(Base):
#     __tablename__ = 'A50_OneStock_PL'
#     id = Column(Integer,primary_key=True,nullable=False, autoincrement=True)
#     index_PL = Column(String(10),nullable=True)  # String在数据库中常见为varchar类型
#     stock_PL = Column(String(10),nullable=True)  #
#     profilo_PL = Column(String(10),nullable=True)  #
#     profilo_PL_R = Column(String(10),nullable=True)  #
#
#     @staticmethod
#     def last_data():
#         # lone = db.session.query(A50_OneStock_PL.profilo_PL_R).filter_by.first()
#         lone = A50_OneStock_PL.query,filter()
#         _5sqls.append(lone)
#         return _5sqls

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@localhost/web_monitor'
# # app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)
#
# Base = declarative_base()
# class A50_OneStock_PL(Base):
#     __tablename__ = 'A50_OneStock_PL'
#     id = Column(Integer,primary_key=True,nullable=False, autoincrement=True)
#     index_PL = Column(String(10),nullable=True)  # String在数据库中常见为varchar类型
#     stock_PL = Column(String(10),nullable=True)  #
#     profilo_PL = Column(String(10),nullable=True)  #
#     profilo_PL_R = Column(String(10),nullable=True)  #
#
#     @staticmethod
#     def last_data():
#         # lone = db.session.query(A50_OneStock_PL.profilo_PL_R).filter_by.first()
#         lone = A50_OneStock_PL.query,filter()
#         _5sqls.append(lone)
#         return _5sqls


_5sqls_values = []


# 其实没有必要做映射！直接把数据表名打包成一个列表，遍历进入一个查询最后一条的方法，遍历查询，遍历插入一个全局遍历即可，然后再插入一个新的数据库和数据表即可
# 尝试着写类，也是将方法的顺序条理化，这个这是需要练习的！

# 写类的方法的时候，都要考虑方法会接收几个参数
class Sql5:
    global connection,cursor ,_5sqls,_5sqls_values# 对于数据库参数设置，　设置为全局参数，所有方法都能使用
    # 第一此专门写类，每一个方法一个一个去试
    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='web_monitor',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    cursor = connection.cursor()
    _5sqls = []
    _5sqls_values = []

    def __init__(self):
        pass
   # 等到5个查询最后一条记录的列表的方法

    # 1.遍历制作５条查询语句的方法　　　(测试成功)
    @staticmethod
    def sel_5_Into():

        tables_name = ["A50_OneStock_PL ","J225_OneStock_PL","MHI_OneStock_PL","OneStock_ES500_PL","oneStock_FTSE100_PL"]
        for item  in tables_name:
            sql = "SELECT profilo_PL_R FROM web_monitor." + "%s" % item + " order by id desc limit 1;"
            _5sqls.append(sql)
        return _5sqls

     # 用来执行查询sql的方法  （接收１个参数）(只需要self本身即可) 执行成功！
    def sel_5sql(self):

        connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='web_monitor',
                                     charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
        cursor = connection.cursor()
        # self.sql = sql  # 实例化参数 应该是在def __init__()方法中你去定义的，不能在这个地方定义
        sql = self
        cursor.execute(sql)  # 这里只是执行sql语句，执行的返回结果放在了cursor中
        result = cursor.fetchall()
        r_dict = result[0]
        # return r_dict["profilo_PL_R"] #字典取值
        _5sqls_values.append(r_dict["profilo_PL_R"])
        connection.commit()
        connection.close()




    # 用来插入数据表的方法(操作)

    def exec_5sql(self):
        connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='Daily5m_sql',
                                     charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
        cursor = connection.cursor()
        # 这里是判断big_list的长度，不是content字符的长度
        if len(big_list) == 5:
            cursor.executemany(
                'insert into AJHKLUS (_As,_Js,_HKs,_Ls,_USs) values (%s,%s,%s,%s,%s)', self)
            connection.commit()
            connection.close()
            print('向MySQL中添加数据成功！')
        else:
            print('出列啦')



a =Sql5
t5 = a.sel_5_Into() #
for sql in t5:
    a.sel_5sql(sql)
print(_5sqls_values)

big_list = [('-23.5', '-37.1', '-18.1', '-22.2', '-34.385')]
a.exec_5sql(big_list)

# SELECT profilo_PL_R FROM web_monitor.A50_OneStock_PL  order by id desc limit 1;
# SELECT profilo_PL_R FROM web_monitor.J225_OneStock_PL order by id desc limit 1;
# SELECT profilo_PL_R FROM web_monitor.MHI_OneStock_PL order by id desc limit 1;
# SELECT profilo_PL_R FROM web_monitor.OneStock_ES500_PL order by id desc limit 1;
# SELECT profilo_PL_R FROM web_monitor.oneStock_FTSE100_PL order by id desc limit 1;

#　create database Daily5m_sql;

# create table AJHKLUS(
# id int not null primary key auto_increment,
# _As varchar(10),
# _Js varchar(10),
# _HKs varchar(10),
# _Ls varchar(10),
# _USs varchar(10)
#  ) engine=InnoDB  charset=utf8;

