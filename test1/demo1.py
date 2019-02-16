# python 面向对象
# class Employee:
#     """
#     所有员工的基类
#     类的方法与普通的函数只有一个特别的区别——它们必须有一个额外的第一个参数名称, 按照惯例它的名称是 self。
#     以单下划线开头的表示的是 protected 类型的变量
#     双下划线的表示的是私有类型(private)的变量
#     """
#     empCount = 0
#     __id = 0  # 私有属性
#
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#         Employee.empCount += 1
#         self.__id += 1
#
#     def __displayCount(self):
#         print('Total employee count %d' % Employee.empCount)
#
#     def displayEmployee(self):
#         self.__displayCount()
#         print('编号：', self.__id, '姓名:', self.name, '薪资:', self.salary)
#
#
# # 创建Employee对象
# emp = Employee('Zev', 15000.5)
# emp.displayEmployee()
# print(emp._Employee__id)  # 使用 object._className__attrName（ 对象名._类名__私有属性名 ）访问属性

# class Test:
#     """self代表类的实例，而非类"""
#
#     def prt(self):
#         print(self)
#         print(self.__class__)


# 创建对象
# t = Test()
# t.prt()


# print('id=',id(emp))

# 修改属性
# emp.name = 'zhujiang'
# emp.salary = 13000.4
# emp.displayCount()
# emp.displayEmployee()
# print('员工数量：%d' % Employee.empCount)
# print('员工工资：%d' % emp.salary)

# 删除属性
# del Employee.empCount

# print('hasattr=', hasattr(emp, 'age'))  # 如果存在 'age' 属性返回 True。
# print('getattr=', getattr(emp, 'name'))  # 返回 'name' 属性的值
# setattr(emp, 'name', 'josh')  # 设置属性 'name' 值为 josh
# emp.displayEmployee()
# delattr(emp, 'name')  # 删除属性 'name'

# __dict__ : 类的属性（包含一个字典，由类的数据属性组成）
# __doc__ :类的文档字符串
# __name__: 类名
# __module__: 类定义所在的模块（类的全名是'__main__.className'
# ，如果类位于一个导入模块mymod中，那么className.__module__ 等于 mymod）
# __bases__ : 类的所有父类构成元素（包含了一个由所有父类组成的元组）
# print("Employee.__doc__:", Employee.__doc__)
# print("Employee.__name__:", Employee.__name__)
# print("Employee.__module__:", Employee.__module__)
# print("Employee.__bases__:", Employee.__bases__)
# print("Employee.__dict__:", Employee.__dict__)

# 多继承 class SubClassName (ParentClass1[, ParentClass2, ...]):
# class ProductEmployee(Employee):
#     """生产员工，员工类的子类"""
#     desc = ''
#     mission = ''
#
#     def __init__(self, name, salary, desc, mission):
#         self.name = name
#         self.salary = salary
#         self.desc = desc
#         self.mission = mission
#
#     def displayEmployee(self):
#         super().displayEmployee()
#         print('员工描述：', self.desc, '员工任务', self.mission)
#
#
# empProduct = ProductEmployee('zhujang', 15000.3, '我是研发部工程师', '我的任务是完成软件研发')
# empProduct.displayEmployee()

# 多继承 mro()函数查看继承顺序
# 使用Mix-in设计模式，与传统继承模式java不同的是，相当于拼积木的继承方式
# 如：胳膊、脑袋、腿组成人   mix-in 类 人作为继承的终点
# class A:        # 定义类 A
# .....
#
# class B:         # 定义类 B
# .....
#
# class C(A, B):   # 继承类 A 和 B
# simple

# class Animal:
#     """动物类"""
#
#     # 构造函数
#     def __init__(self, name):
#         self.name = name
#
#     def eat(self):
#         print('%s 正在吃东西' % self.name)
#
#     def breath(self):
#         print('%s 正在呼吸' % self.name)
#
#
# class Person(Animal):
#     """人类 继承自动物类"""
#
#     def __init__(self, name, money):
#         self.name = name
#         self.money = money
#
#     def speak(self):
#         print('%s说他有%s人民币' % (self.name, self.money))
#
#
# class Spider(Animal):
#     """蜘蛛类 继承自动物类"""
#
#     def climb(self):
#         print('%s 正在攀岩' % self.name)
#
#     def spin(self):
#         print('%s 正在吐丝' % self.name)
#
#
# class SpiderMan(Person, Spider):
#     """蜘蛛侠类 继承蜘蛛类 多继承simple,越靠右边的，则继承关系是越大，即父类
#         Person=>Spider
#     """
#     pass
#
#
# spiderMan = SpiderMan('蜘蛛侠', 100)
# spiderMan.spin()
# spiderMan.climb()
# spiderMan.speak()
# spiderMan.breath()
# spiderMan.eat()
# print(SpiderMan.mro())  # 查看继承结构
# print(SpiderMan.__mro__)  # 查看继承结构

# 运算符重载
# class Vector:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def __str__(self):
#         return 'Vector (%d,%d)' % (self.a, self.b)
#
#     def __add__(self, other):
#         return Vector(self.a + other.a, self.b + other.b)
#
#
# v1 = Vector(10, 33)
# v2 = Vector(5, -5)
# print(v1 + v2)

