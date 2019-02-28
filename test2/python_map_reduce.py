# reduce的用法。reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
# map()传入的第一个参数是f，即函数对象本身。由于结果r是一个Iterator，Iterator是惰性序列，
# 因此通过list()函数让它把整个序列都计算出来并返回一个list。
# def f(x):
#     return x * x
#
#
# r = map(f, [1, 2, 3, 4, 5, 6, 7])
# print(list(r))
#
# # 把这个list所有数字转为字符串：
# print(list(map(str, [1, 2, 3, 4, 5, 6, 7])))
import functools
from functools import reduce


# def add(x, y):
#     return x + y
#
#
# print(reduce(add, [1, 3, 5, 7, 9]))


# def fn(x, y):
#     return x * 10 + y
#
#
# print(reduce(fn, [1, 3, 5, 7, 9]))

# 将字符数字转换为数字
# DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
#
#
# def char2num(s):
#     return DIGITS[s]
#
#
# def str2int(s):
#     return reduce(lambda x, y: x * 10 + y, map(char2num, s))
#
#
# print(str2int('13579'))

# 将所有名字改为首字母大写，其他小写
# def normalize(name):
#     # new_name = ''
#     # new_name += name[0].upper()
#     # for i in range(len(name)):
#     #     if i != 0:
#     #         new_name += name[i].lower()
#     # print('name[:1] %s' % name[:1])
#     # print('name[1:] %s' % name[1:])
#
#     return name[:1].upper() + name[1:].lower()
#
#
# L1 = ['adam', 'LISA', 'barT']
# L2 = list(map(normalize, L1))
# print(L2)

# def ride(x, y):
#     return x * y
#
#
# def prod(L):
#     return reduce(ride, L)
#
#
# print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
# if prod([3, 5, 7, 9]) == 945:
#     print('测试成功!')
# else:
#     print('测试失败!')

# DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
#
#
# def str2float(s):
#     return float(s)
#
#
# print('str2float(\'123.456\') =', str2float('123.456'))
# if abs(str2float('123.456') - 123.456) < 0.00001:
#     print('测试成功!')
# else:
#     print('测试失败!')


# Python内建的filter()函数用于过滤序列。
# 获取偶数
# def is_odd(n):
#     return n % 2 == 0
#
#
# print(list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])))


# def not_empty(s):
#     return s and s.strip()
#
#
# print(list(filter(not_empty, ['A', '', 'B', None, 'C', '  '])))


# # sorted排序
# print(sorted([36, 5, -12, 9, -21]))
# # 按绝对值大小排序
# print(sorted([36, 5, -12, 9, -21], key=abs))
# print(sorted(['bob', 'about', 'Zoo', 'Credit']))
# # 忽略大小写的排序
# print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower))
# # 忽略大小写的反向排序
# print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True))


# 装饰器
# def log(func):
#     def wrapper(*args, **kw):
#         print('call %s():' % func.__name__)
#         return func(*args, **kw)
#
#     return wrapper


# def log(text):
#     def decorator(func):
#         def wrapper(*args, **kw):
#             print('%s %s():' % (text, func.__name__))
#             return func(*args, **kw)
#
#         return wrapper
#
#     return decorator

# def log(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kw):
#         print('call %s():' % func.__name__)
#         return func(*args, **kw)
#
#     return wrapper

# def log(text):
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kw):
#             print('%s %s():' % (text, func.__name__))
#             return func(*args, **kw)
#         return wrapper
#     return decorator
#
#

# def log(text):
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kw):
#             print('Begin call')
#             print('calling func: %s' % func.__name__)
#             r = func(*args, **kw)
#             print('Eng call')
#             return r
#
#         return wrapper
#
#     return decorator if isinstance(text, str) else decorator(text)


# @log('zev')
# def now():
#     print('2015-3-25')


# 将函数作为变量，函数对象有一个__name__属性，可以拿到函数的名字
# f = now
# print(f())
# 函数名称
# print(now.__name__)
# print(f.__name__)


