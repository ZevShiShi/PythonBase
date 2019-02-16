# 以单下划线开头 _foo 的代表不能直接访问的类属性，需通过类提供的接口进行访问，不能用 from xxx import * 而导入。
# 以双下划线开头的 __foo 代表类的私有成员，以双下划线开头和结尾的 __foo__ 代表 Python 里特殊方法专用的标识，如 __init__() 代表类的构造函数。

# print("你好世界!")
# print("hello")
# print("zev")
# if True:
#     print("ok")
# else:
#     print("no")

# Python 可以使用引号( ' )、双引号( " )、三引号( ''' 或 """ ) 来表示字符串，引号的开始与结束必须的相同类型的。
# 其中三引号可以由多行组成，编写多行文本的快捷语法，常用于文档字符串，在文件的特定地点，被当做注释。
# word = 'hello'
# sentenct = "这是一句话"
# paragraph = """哈哈哈
# 嘻嘻嘻
# 么么哒"""
# print(word)
# print(sentenct)
# print(paragraph)

# 单行注释
'''
这是多行注释，使用单引号。
这是多行注释，使用单引号。
'''
from pip._vendor.distlib.compat import raw_input

"""
这是多行注释，使用双引号。
这是多行注释，使用双引号。
"""

# 等待用户输入
# from pip._vendor.distlib.compat import raw_input
# my_name=raw_input("按下 enter 键退出，其他任意键显示...\n")
# print(my_name)

# Python可以在同一行中使用多条语句，语句之间使用分号(;)分割
# import sys;x = "hello";sys.stdout.write(x+"\n");sys.stdout.write("zev")

# x="a"
# y="b"
# # 换行输出
# print(x)
# print(y)
# print("----------")
# # 不换行输出
# print(x,y)
# print(x,end='')   3.x使用


# 代码块
# isUser = True
# if isUser:
#     print("haha")
# elif isUser:
#     print("xixi")
# else:
#     print("hehe")

# counter = 100  # 赋值整型变量
# miles = 100.5  # 浮点型
# name = "zev"   # 字符串
# print(counter)
# print(miles)
# print(name)

# 同时为多个变量赋值
# a = b = c = d = 3
# 多个对象指定多个变
# a, b, c = 50, 111.5, "哈哈"
# print(a)
# print(b)
# print(c)

# var1 = 10
# var2 = 12
# # 使用del语句删除一些对象的引用。
# del var1,var2

# 截取字符串，[头下标:尾下标] 获取的子字符串包含头下标的字符，但不包含尾下标的字符。
# s = "abcdefg"
# print(s[1:5])

# str = "hello,world"
# print(str)            # 输出完整字符串
# print(str[0])         # 输出字符串中的第一个字符
# print(str[2:5])       # 输出字符串中第三个至第五个之间的字符串
# print(str[2:])        # 输出从第三个字符开始的字符串
# print(str * 2)        # 输出字符串两次
# print(str + " zev")   # 输出连接的字符串
# print(str[0:8:2])       # 输出从第一个字符到第八个字符，步长为2

# Python列表可以完成大多数集合类的数据结构实现。它支持字符，数字，字符串甚至可以包含列表（即嵌套）。
# list = ['zev', 786, 2.23, 'join', 70.2]
# tinylist = [123, 'demo']
# print(list)  # 输出完整列表
# print(list[0])  # 输出列表的第一个元素
# print(list[1:3])  # 输出第二个至第三个元素
# print(list[2:])  # 输出从第三个开始至列表末尾的所有元素
# print(tinylist * 2)  # 输出列表两次
# print(list + tinylist)  # 打印组合的列表
# list[0] = 'haha'

# Python元组用 () 标识。内部元素用逗号隔开。但是元组不能二次赋值，相当于只读列表。
# tuple = ('runoob', 786, 2.23, 'john', 70.2)
# tinytuple = (123, 'john')
#
# print(tuple)  # 输出完整元组
# print(tuple[0])  # 输出元组的第一个元素
# print(tuple[1:3])  # 输出第二个至第三个的元素
# print(tuple[2:])  # 输出从第三个开始至列表末尾的所有元素
# print(tinytuple * 2)  # 输出元组两次
# print(tuple + tinytuple)  # 打印组合的元组

# Python 字典 用"{ }"标识。字典由索引(key)和它对应的值value组成。
# dict = {'one': 'zev', 2: 'demo'}
# tinydict = {'name': 'john', 'code': 6734, 'dept': 'sales'}
#
# print(dict['one'])  # 输出键为'one' 的值
# print(dict[2])  # 输出键为 2 的值
# print(tinydict)  # 输出完整的字典
# print(tinydict.keys())  # 输出所有键
# print(tinydict.values())  # 输出所有值

# python 数据类型转换
# print(int())  # 不传入参数时，得到结果0
# print(int(3))
# print(int(3.5))
# print(int('12', 16))  # 十六进制的12转为十进制
# print(int('0xa', 16))  # 十六进制0xa转为十进制数字
# print(int('10', 8))  # 八进制的10转为十进制

# 复数
# print(complex(1,2))

# str() 函数
# s = 'Runner'
# print(str(s))
# dict = {'runoob': 'runoob.com', 'google': 'google.com'};
# print(str(dict))

# repr() 函数 将对象转化为供解释器读取的形式。
# print(repr(s))
# print(repr(dict))

# eval() 函数用来执行一个字符串表达式，并返回表达式的值。
# x = '7'
# y = eval('3 * x')
# print(y)
# print(eval('pow(2,2)'))
# print(eval('2+2'))

# set() 函数创建一个无序不重复元素集，可进行关系测试，删除重复数据，还可以计算交集、差集、并集等。
# x = set('runner')
# y = set('google')
# print(x)
# print(y)

# a = 21
# b = 10
# c = 0
# if a == b:
#     print("1 - a 等于 b")
# else:
#     print("1 - a 不等于 b")
# if a != b:
#     print("1 - a 不等于 b")
# else:
#     print("1 - a 等于 b")

# a += b
# print(a)

# if a and b:
#     print('haha')
# else:
#     print('xixi')

# a = 10
# b = 20
# list = [1, 2, 3, 4, 5]
# in 元素是否包含在list中
# if a in list:
#     print('a 在list中')
# else:
#     print('a 不在list中')
#
# if b not in list:
#     print('b 不在list中')
# else:
#     print('b 在list中')

# if a is b:
#     print('a和b有相同标示')
# else:
#     print('a和b无相同标示')

# if a or b:
#     print('a 或 b')

# 循环
# numbers = [12, 37, 5, 42, 8, 3]
# even = []
# odd = []

# while len(numbers) > 0:
#     number = numbers.pop()
#     if number % 2 == 0:
#         even.append(number)
#     else:
#         odd.append(number)
#
# print(even)
# print(odd)

# while else
# count = 0
# while count < 9:
#     print('count is ', count)
#     count = count + 1
# else:
#     print("Good Bye")

# for in
# for letter in "Python":
#     print('当前字母：',letter)

# fruits = ['banana', 'apple', 'mongo']
# for fruit in fruits:
#     print('当前水果：',fruit)

# # for 索引
# for index in range(len(fruits)):
#     print('当前水果：', fruits[index])

# for num in range(10, 20):
#     for i in range(2, num):
#         if num % i == 0:
#             j = num / i
#             print('%d 等于 %d * %d ' % (num, i, j))
#             break
#     else:
#         print(num, '是一个质数')

# 冒泡排序
# arrays = [1, 8, 4, 5, 7, 11, 3]
# for i in range(len(arrays)):
#     for j in range(i + 1):
#         if arrays[i] > arrays[j]:
#             arrays[i], arrays[j] = arrays[j], arrays[i]
# print(arrays)

# 打印菱形 |x - w/2| + |y - w/2| = w/2 轻松搞定。
# width = int(raw_input('输入对角线长度'))
# for row in range(width + 1):
#     for col in range(width + 1):
#         if abs(row - width / 2) + abs(col - width / 2) == width / 2:
#             print('*', end='')
#         else:
#             print(' ', end='')
#     print(' ')

# pass 不做任何事情，一般用做占位语句。
# for letter in 'Python':
#     if letter == 'h':
#         pass
#         print('这是pass块')
#     print('当前字母', letter)

# Number 类型转换
# int(x [,base ])         将x转换为一个整数
# long(x [,base ])        将x转换为一个长整数
# float(x )               将x转换到一个浮点数
# complex(real [,imag ])  创建一个复数
# str(x )                 将对象 x 转换为字符串
# repr(x )                将对象 x 转换为表达式字符串
# eval(str )              用来计算在字符串中的有效Python表达式,并返回一个对象
# tuple(s )               将序列 s 转换为一个元组
# list(s )                将序列 s 转换为一个列表
# chr(x )                 将一个整数转换为一个字符
# unichr(x )              将一个整数转换为Unicode字符
# ord(x )                 将一个字符转换为它的整数值
# hex(x )                 将一个整数转换为一个十六进制字符串
# oct(x )                 将一个整数转换为一个八进制字符串

# import cmath
# import math
# import random
#
# print(dir(math))
# print(dir(cmath))
# print(random.choice(range(10)))

# 转义特殊符号
# print(r'/n')

# 字符串格式化占位
# print('My name is %s,My age is %d' % ('ZevZhu', 30))

# 三引号，三引号解决从引号和特殊字符串的泥潭里面解脱出来
# my_str = '''
# <HTML><HEAD><TITLE>
# Friends CGI Demo</TITLE></HEAD>
# <BODY><H3>ERROR</H3>
# <B>%s</B><P>
# <FORM><INPUT TYPE=button VALUE=Back
# ONCLICK="window.history.back()"></FORM>
# </BODY></HTML>
# '''
# print(my_str)
# print(u'Hello\u0020World!')

# List
# from filecmp import cmp
#
# list1 = ['physics', 'chemistry', 1997, 2000]
# list2 = [1, 2, 3, 4, 5, 6, 7]
# # 使用下标索引来访问列表中的值，同样你也可以使用方括号的形式截取字符
# print('list1[0]:', list1[0])
# print('list2[1:5]', list2[1:5])
# print('list1[-2]', list1[-2])
# print(cmp(list1,list2))
# print(len(list2))
# print(max(list2))
# print(min(list2))

# # 新增元素
# list1.append("haha")
# list2.append(10)
# print(list1)
# print(list2)
# # 删除元素
# del list1[0]
# print(list1)

#       Python表达式	                  结果	                            描述
#       len([1, 2, 3])	               3	                            长度
#       [1, 2, 3] + [4, 5, 6]	    [1, 2, 3, 4, 5, 6]	                组合
#       ['Hi!'] * 4	        ['Hi!', 'Hi!', 'Hi!', 'Hi!']	            重复
#       3 in [1, 2, 3]	              True	                            元素是否存在于列表中
#       for x in [1, 2, 3]: print x,	  1 2 3	                        迭代

# 序号	方法
# 1	list.append(obj)
# 在列表末尾添加新的对象
# 2	list.count(obj)
# 统计某个元素在列表中出现的次数
# 3	list.extend(seq)
# 在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
# 4	list.index(obj)
# 从列表中找出某个值第一个匹配项的索引位置
# 5	list.insert(index, obj)
# 将对象插入列表
# 6	list.pop([index=-1])
# 移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
# 7	list.remove(obj)
# 移除列表中某个值的第一个匹配项
# 8	list.reverse()
# 反向列表中元素
# 9	list.sort(cmp=None, key=None, reverse=False)
# 对原列表进行排序


# 字典
# dict = {'Name': 'Zev', 'Age': 30, 'Class': 'First'}

# 更新
# dict['Name'] = 'david'
# dict['Age'] = 20
# print('dict=', dict)

# 访问
# print(dict['Name'])
# name=dict.get('Name')
# print(name)
# print(dict.keys())

# 删除
# del dict['Name']
# print('dict=', dict)
# dict.clear()  # 删除所有字段元素
# print('dict=', dict)
# del dict  # 删除字段对象

# # 日期
# import time
# # 时间戳
# ticks = time.time()
# print('当前时间戳', ticks)
# # 本地时间对象
# localtime = time.localtime(time.time())
# print('本地时间为 :', localtime)
# # 获取可读的时间模式的函数是asctime():
# localtime = time.asctime(time.localtime(time.time()))
# print('本地时间为 :', localtime)
# # 格式化日期 2019-02-13 14:30:09
# localtime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
# # Wed Feb 13 14:29:16 2019
# # localtime=time.strftime('%a %b %d %H:%M:%S %Y',time.localtime())
# print(localtime)
# # # 将格式字符串转换为时间戳
# a = "Sat Mar 28 22:24:24 2016"
# print(time.mktime(time.strptime(a, "%a %b %d %H:%M:%S %Y")))

# 日历
# import calendar
#
# cal = calendar.month(2019, 1)
# print('以下输出2019年1月份的日历:')
# print(cal)

# datetime 获取相关时间
# import datetime
#
# i = datetime.datetime.now()
# print("当前的日期和时间是 %s" % i)
# print("ISO格式的日期和时间是 %s" % i.isoformat())
# print("当前的年份是 %s" % i.year)
# print("当前的月份是 %s" % i.month)
# print("当前的日期是  %s" % i.day)
# print("dd/mm/yyyy 格式是  %s/%s/%s" % (i.day, i.month, i.year))
# print("当前小时是 %s" % i.hour)
# print("当前分钟是 %s" % i.minute)
# print("当前秒是  %s" % i.second)


# 函数
# def hello(content):
#     """这是函数注释，是我的第一个函数"""
#     print(content)
#     return
#
#
# hello("hello zev")
# hello('你好世界')


# 默认值
# def hello(content, age=20):
#     """这是函数注释，是我的第一个函数"""
#     print(content, age)
#     return


# 传入参数和顺序无关
# hello(content='Love', age=30)
# hello(content='xixi')

# 在 python 中，strings, tuples, 和 numbers 是不可更改的对象，而 list,dict 等则是可以修改的对象
# 不可更改对象sample
# def changeInt(a):
#     a = 10
#
#
# b = 2
# changeInt(b)
# print(b)

# def changeMe(mylist):
#     """修改传入的列表"""
#     mylist.append([1,2,3,4])
#     print('函数内取值',mylist)
#     return
#
#
# mylist = [10,20,30]
# changeMe(mylist)
# print('函数外取值',mylist)


# 不定长参数
# def printInfo(arg1, *vartuple):
#     """不定长参数演示"""
#     print('arg1=', arg1)
#     for var in vartuple:
#         print(var)
#     return
#
#
# printInfo('哈哈', 10, 30, 40, 50)
# printInfo('zev')

# 匿名参数 lambda表达式编写
# lambda [arg1 [,arg2,.....argn]]:expression
# sum = lambda arg1, arg2: arg1 + arg2
#
# print('相加1', sum(11, 22))
# print('相加2', sum(100, 22))

# return 用法
# def sum(arg1, arg2):
#     total = arg1 + arg2
#     print('函数内部总和=', total)
#     return total
#
#
# total = sum(100, 20)
# print('函数外部总和=', total)

# 全局变量和局部变量
# total = 0  # 全局变量

# def sum(arg1, arg2):
#     """
#     如果使用global关键字，可以将不可变的Number类型的值带出来，如果不带则不可变，即外部的值不会变化
#     一个global语句可以同时定义多个变量，如 global x, y, z
#     """
#     global total
#     total = arg1 + arg2
#     print('函数内部总和', total)
#     return total
#
#
# sum(100, 20)
# print('函数外部总和=', total)

# 二分查找算法做反转,索引为正数取列表前半段元素，索引为负数取列表后半段元素，相互两两交互，达到反转的目的
# def reverse(li):
#     for i in range(0, int(len(li) / 2)):
#         # print("li[i]=", li[i])
#         # print("li[-i-1]=", li[-i - 1])
#         temp = li[i]
#         li[i] = li[-i - 1]
#         li[-i - 1] = temp
#
#
# my_list = [1, 2, 3, 4, 5, 30, 22, 40]
# print(my_list[-1])
# reverse(my_list)
# print(my_list)

# 反转简化
# def reverse(li):
#     for i in range(0, int(len(li) / 2)):
#         li[i], li[-i - 1] = li[-i - 1], li[i]
#
#
# my_list = [1, 2, 3, 4, 5, 30, 22, 40]
# reverse(my_list)
# print(my_list)


# 利用列表pop函数，移除列表最后一个元素，并返回该元素
# def reverse(mylist):
#     rev_list = []
#     for i in range(len(mylist)):
#         rev_list.append(mylist.pop())
#     return rev_list


# my_list = [1, 2, 3, 4, 5, 30, 22, 40]
# print('hello_world=', reverse(my_list))

# 导入math 的所有模块 from math import *
# globals() 和 locals() 函数可被用来返回全局和局部命名空间里的名字。
# globals()
# locals()


# I/O
# my_str = raw_input('raw_input请输入')
# print("输入内容：",my_str)

# my_str = input('input请输入内容')
# print("输入内容：",my_str)

# file object = open(file_name [, access_mode][, buffering])
"""
ile_name：file_name变量是一个包含了你要访问的文件名称的字符串值。
access_mode：access_mode决定了打开文件的模式：只读，写入，追加等。所有可取值见如下的完全列表。这个参数是非强制的，默认文件访问模式为只读(r)。
buffering:如果buffering的值被设为0，就不会有寄存。如果buffering的值取1，访问文件时会寄存行。如果将buffering的值设为大于1的整数，
表明了这就是的寄存区的缓冲大小。如果取负值，寄存区的缓冲大小则为系统默认。
"""

# 打开一个文件
# my_file = open('test.txt', 'w')
# my_file = open('test.txt', 'a+')
# print("文件名: ", my_file.name)
# print("是否已关闭 : ", my_file.closed)
# print("访问模式 : ", my_file.mode)
# # 写入文件内容
# my_file.write('hello,python! \nwelcome python world!\n')
# # 关闭文件
# my_file.close()

# # 读取文件
# my_file = open('test.txt', 'r')
# my_str = my_file.read(10)
# print('读取的内容：', my_str)
#
# # 查找读取当前指针位置
# position = my_file.tell()
# print('文件位置：', position)
# # 把指针再次重新定位到13的位置
# position = my_file.seek(13, 0)
# my_str = my_file.read()
# print('重新定位后读取的内容：', my_str)
#
# my_file.close()

# 重新命名文件名称
# import os
# 设置文件路径 获取路径最后的文件名称
# fn = os.path.basename("xixi.txt")
# open(fn, 'w').write("haha")

# os.rename('test.txt', 'text.txt')

# 删除文件
# os.remove('text.txt')

# 创建目录
# os.mkdir('../test1')
# 指定工作目录
# os.chdir('../test0')
# 返回当前工作目录
# print('当前工作目录：',os.getcwd())
# 删除目录
# os.rmdir('../test1')

# 异常处理 try/except语句
# try:
#     my_file = open('testfile.txt', 'w')
#     my_file.write('testfile my name is zev')
#     my_file.close()
# except IOError:
#     print('Error: 没有找到文件或读取文件失败')
# else:
#     print('没有Error')


# def setup(num):
#     try:
#         return int(num)
#     except ValueError as arg:
#         print('参数没有包含数字\n', arg.args.__str__())
#
#     return int(num)
#
#
# print(setup(10))

# 使用 raise 关键字触发异常
# def my_method(level):
#     if level < 1:
#         raise Exception('Invalid level!', level)
#         # 触发异常后，后面的代码就不会再执行
#
#
# try:
#     my_method(0)
# except Exception as err:
#     print('Exception=', err.args.__str__())
# else:
#     print('正常执行')

# 自定义异常
# class NetworkError(RuntimeError):
#     def __init__(self, arg):
#         self.args = arg
#
#
# try:
#     raise NetworkError('Bad hostname')
# except NetworkError as e:
#     print('NetworkError=', e.args.__str__())
# finally:
#     print('最后总是要执行')
