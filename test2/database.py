# 导入SQLite驱动:
# import sqlite3

# 连接到SQLite数据库
# 数据库文件是test.db
# 如果文件不存在，会自动在当前目录创建:
# conn = sqlite3.connect('test.db')

# #创建一个Cursor:
# cursor = conn.cursor()

# # 执行一条SQL语句，创建user表:
# cursor.execute('create table user(id varchar(20) primary key ,name varchar(20))')
# # 继续执行一条SQL语句，插入一条记录:
# cursor.execute("insert into user (id,name) values ('1','zev')")
# # 通过rowcount获得插入的行数:
# print(cursor.rowcount)
# # 关闭Cursor:
# cursor.close()
# # 提交事务:
# conn.commit()
# # 关闭Connection:
# conn.close()

# # 查询
# cursor = conn.cursor()
# cursor.execute("select * from user where id='1'")
# values = cursor.fetchall()
# print(values)
# # 关闭Cursor:
# cursor.close()
# # 关闭Connection:
# conn.close()


# # 导入MySQL驱动:
# import mysql.connector
#
# # 注意把password设为你的root口令:
#
# conn = mysql.connector.connect(user='root', password='123456', database='test', use_unicode=True)
# cursor = conn.cursor()
#
# # 创建user表:
# cursor.execute('create table user (id varchar(20) PRIMARY KEY ,name varchar(20))')
# # 插入一行记录，注意MySQL的占位符是%s:
# cursor.execute('insert into user (id,name) values (%s,%s)', ['1', 'Zev'])
# print(cursor.rowcount)
#
# # 提交事务:
# conn.commit()
# cursor.close()
#
# # 运行查询:
# cursor = conn.cursor()
# cursor.execute('select * from user where id = %s', ('1',))
# values = cursor.fetchall()
# print(values)
# cursor.close()
# conn.close()


# 使用ORM框架 sqlalchemy
from sqlalchemy import Column, String, create_engine, ForeignKey
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类:
Base = declarative_base()


# 定义User对象:
class User(Base):
    """表的名字:"""

    __tablename__ = 'user'

    # 表的结构:
    id = Column(String(20), primary_key=True)
    name = Column(String(20))


class Book(Base):
    _tablename__ = 'book'

    id = Column(String(20), primary_key=True)
    name = Column(String(20))

    # “多”的一方的book表是通过外键关联到user表的:
    user_id = Column(String(20), ForeignKey('user.id'))


# 初始化数据库连接: '数据库类型+数据库驱动名称://用户名:口令@机器地址:端口号/数据库名'
engine = create_engine('mysql+mysqlconnector://root:123456@localhost:3306/test')
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)

# 以上代码完成SQLAlchemy的初始化和具体每个表的class定义。如果有多个表，就继续定义其他class，例如School：
# class School(Base):
#     __tablename__ = 'school'
#     id = ...
#     name = ...

# 添加
# 创建session对象:
# session = DBSession()
# # 创建新User对象:
# new_user = User(id='5', name='Bob')
# # 添加到session:
# session.add(new_user)
# # 提交即保存到数据库:
# session.commit()
# # 关闭session:
# session.close()

# 查询
# 创建Session:
session = DBSession()
# 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
# user = session.query(User).filter(User.id == '5').one()
user_list = session.query(User).all()
# 打印类型和对象的name属性:
# print('type:', type(user))
# print('name:', user.name)
for user in user_list:
    print('id:', user.id)
    print('name:', user.name)
# 关闭Session:
session.close()
