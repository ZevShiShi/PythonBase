# 文件操作
import os

# print(os.name)  # 操作系统类型
# print(os.uname())  # 注意uname()函数在Windows上不提供
# print(os.environ)  # 环境变量
# print(os.environ.get('PATH'))

# # 查看当前目录的绝对路径:
# curr_dir = os.path.abspath('.')
# print(curr_dir)
#
# # 拼接路径,不要直接拼接，不同操作系统路径分隔符不一致
# child_dir = os.path.join(curr_dir, 'child')
# print(child_dir)
#
# # 通过os.path.split()函数，这样可以把一个路径拆分为两部分，后一部分总是最后级别的目录或文件名：
# split_dir = os.path.split(child_dir)
# print(split_dir)
# os.mkdir(child_dir) # 创建目录
# # os.rmdir(child_dir)  # 删除目录
#
# # 直接获取文件后缀os.path.splitext()函数
# child_file = os.path.join(curr_dir, 'test.txt')
# suffix_text = os.path.splitext(child_file)
# print(suffix_text)


# 对文件重命名:
# os.rename('test.py','test.txt')
# 删掉文件:
# os.remove('test.py')

# import shutil
# 复制文件 1、源文件 2、复制到哪里的目标文件
# shutil.copyfile('test.txt', 'test.py')


# 要列出当前目录下的所有目录
# all_dir = [x for x in os.listdir('.') if os.path.isdir(x)]
# print(all_dir)

# 要列出所有的.py文件
# py_file = [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py']
# print(py_file)

# for x in os.listdir('.'):
#     print('x=', x)

# 获取当前目录和子目录下的所有文件并打印文件路径
# curr_dir = os.path.abspath('.')
# word = input('请输入要查找的字符')
#
#
# def find_file(child, dir=curr_dir):
#     """child 待查找的单词，dir当前所处的目录"""
#     for x in os.listdir(dir):
#         # print('dir:%s,x:%s' % (dir, x))
#         f = os.path.join(dir, x)
#         if os.path.isfile(f) and child in x:
#             print(f)
#         if os.path.isdir(f):
#             find_file(child, f)  # 如果是目录，递归
#
#
# find_file(word)

# Python提供了pickle模块来实现序列化。
# import pickle

# pickle.dumps()方法把任意对象序列化成一个bytes，然后，就可以把这个bytes写入文件
# d = dict(name='Bob', age=20, score=88)
# b = pickle.dumps(d)
# print(b)

# 用另一个方法pickle.dump()直接把对象序列化后写入一个file-like Object：
# with open('dump.txt', 'wb') as f:
#     pickle.dump(d, f)

# 反序列化，读出字典数据
# with open('dump.txt', 'rb') as f:
#     d = pickle.load(f)
#     print(d)


# Python JSON
import json


# 将对象转换为json数据
# dumps()方法返回一个str
# dump()方法可以直接把JSON写入一个file-like Object。
# d = dict(name='Bob', age=20, score=88)
# json_str = json.dumps(d)
# print(json_str)

# 要把JSON反序列化为Python对象，用loads()或者对应的load()方法，
# 前者把JSON的字符串反序列化，后者从file-like Object中读取字符串并反序列化：
# d = json.loads(json_str)
# print(d)


# class Student:
#     def __init__(self, name, age, score):
#         self.name = name
#         self.age = age
#         self.score = score
#
#
# def student2dict(std):
#     """Student实例首先被student2dict()函数转换成dict，然后再被顺利序列化为JSON："""
#     return {
#         'name': std.name,
#         'age': std.age,
#         'score': std.score
#     }
#
#
# def dict2student(d):
#     """如果我们要把JSON反序列化为一个Student对象实例，loads()方法首先转换出一个dict对象
#     ，然后，我们传入的object_hook函数负责把dict转换为Student实例："""
#     return Student(d['name'], d['age'], d['score'])
#
#
# s = Student('Zev', 30, 100)
# json_str = json.dumps(s, default=student2dict)
# print(json_str)
#
# d=json.loads(json_str,object_hook=dict2student)
# print(d.name)


