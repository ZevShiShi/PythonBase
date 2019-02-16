# 正则表达式
import re

# re.I 忽略大小写
# re.L 表示特殊字符集 \w, \W, \b, \B, \s, \S 依赖于当前环境
# re.M 多行模式
# re.S 即为 . 并且包括换行符在内的任意字符（. 不包括换行符）
# re.U 表示特殊字符集 \w, \W, \b, \B, \d, \D, \s, \S 依赖于 Unicode 字符属性数据库
# re.X 为了增加可读性，忽略空格和 # 后面的注释

# print(re.match('www', 'www.baidu.com').span())  # 在起始位置匹配
# print(re.match('www', 'www.baidu.com'))  # 不在起始位置匹配

# line = "Cats are smarter than dogs"
#
# isMatch = re.match(r'(.*) are (.*?) .*', line, re.M | re.I)
# if isMatch:
#     print('isMatch.group():', isMatch.group())
#     print('isMatch.group(1):', isMatch.group(1))
#     print('isMatch.group(2):', isMatch.group(2))

# re.search 扫描整个字符串并返回第一个成功的匹配。
# print(re.search('www', 'www.runoob.com').span())  # 在起始位置匹配
# print(re.search('com', 'www.runoob.com').span())  # 不在起始位置匹配

# line = "Cats are smarter than dogs"

# searchObj = re.search(r'(.*) are (.*?) .*', line, re.M | re.I)
#
# if searchObj:
#     print("searchObj.group() : ", searchObj.group())
#     print("searchObj.group(1) : ", searchObj.group(1))
#     print("searchObj.group(2) : ", searchObj.group(2))
# else:
#     print("Nothing found!!")


# re.match与re.search的区别
# re.match只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，函数返回None；
# 而re.search匹配整个字符串，直到找到一个匹配。
# line = "Cats are smarter than dogs"
#
# matchObj = re.match(r'dogs', line, re.M | re.I)
# if matchObj:
#     print("match --> matchObj.group() : ", matchObj.group())
# else:
#     print("No match!!")
#
# matchObj = re.search(r'dogs', line, re.M | re.I)
# if matchObj:
#     print("search --> matchObj.group() : ", matchObj.group())
# else:
#     print("No match!!")

# Python 的 re 模块提供了re.sub用于替换字符串中的匹配项。

# phone = "2004-959-559 # 这是一个国外电话号码"
# # 删除字符串中的 Python注释
# num = re.sub(r'#.*$', "", phone)
# print('电话号码', num)
#
# # 删除非数字(-)的字符串
# num = re.sub(r'\D', "", phone)
# print('电话号码', num)
#
#
# # repl 参数是一个函数
# # 将匹配的数字乘以 2
# def double(matched):
#     value = int(matched.group('value'))
#     return str(value * 2)
#
#
# s = 'A23G4HFD567'
# print(re.sub('(?P<value>\d+)', double, s))

# group([group1, …]) 方法用于获得一个或多个分组匹配的字符串，当要获得整个匹配的子串时，可直接使用 group() 或 group(0)；
# # start([group]) 方法用于获取分组匹配的子串在整个字符串中的起始位置（子串第一个字符的索引），参数默认值为 0；
# # end([group]) 方法用于获取分组匹配的子串在整个字符串中的结束位置（子串最后一个字符的索引+1），参数默认值为 0；
# # span([group]) 方法返回 (start(group), end(group))。

# compile 函数用于编译正则表达式，生成一个正则表达式（ Pattern ）对象，供 match() 和 search() 这两个函数使用。
# pattern = re.compile(r'\d+')  # 用于匹配至少一个数字
# m = pattern.match('one12twothree34four')  # 查找头部，没有匹配
# print(m)
#
# m = pattern.match('one12twothree34four', 2, 10)  # 从'e'的位置开始匹配，没有匹配
# print(m)
#
# m = pattern.match('one12twothree34four', 3, 10)  # 从'1'的位置开始匹配，正好匹配
# print(m)
# print(m.group(0))  # 可省略 0 返回匹配成功的整个子串
# print(m.start(0))  # 可省略 0
# print(m.end(0))  # 可省略 0
# print(m.span(0))  # 可省略 0  返回匹配成功的整个子串的索引

# pattern = re.compile(r'([a-z]+) ([a-z]+)', re.I)  # re.I 表示忽略大小写
# m = pattern.match('Hello World Wide Web')
# print(m)
# print(m.group(1))
# print(m.groups())  # 等价于 (m.group(1), m.group(2), ...)

# findall
# 在字符串中找到正则表达式所匹配的所有子串，并返回一个列表，如果没有找到匹配的，则返回空列表。
# match 和 search 是匹配一次 findall 匹配所有。

# string : 待匹配的字符串。
# pos : 可选参数，指定字符串的起始位置，默认为 0。
# endpos : 可选参数，指定字符串的结束位置，默认为字符串的长度。
# pattern = re.compile(r'\d+')   # 查找数字
# # result1 = pattern.findall('runoob 123 google 456')
# # result2 = pattern.findall('run88oob123google456', 0, 10)
# #
# # print(result1)
# # print(result2)

# 和 findall 类似，在字符串中找到正则表达式所匹配的所有子串，并把它们作为一个迭代器返回。
# pattern	匹配的正则表达式
# string	要匹配的字符串。
# flags	标志位，用于控制正则表达式的匹配方式，如：是否区分大小写，多行匹配等等。参见：正则表达式修饰符 - 可选标志
# it = re.finditer(r"\d+", "12a32bc43jf3")
# for match in it:
#     print(match.group())

# split 方法按照能够匹配的子串将字符串分割后返回列表，它的使用形式如下：
# pattern	匹配的正则表达式
# string	要匹配的字符串。
# maxsplit	分隔次数，maxsplit=1 分隔一次，默认为 0，不限制次数。
# flags	标志位，用于控制正则表达式的匹配方式，如：是否区分大小写，多行匹配等等。参见：正则表达式修饰符 - 可选标志

# str = re.split('\W+', 'runoob, runoob, runoob.')
# print(str)
# str = re.split('(\W+)', ' runoob, runoob, runoob.')
# print(str)
# str = re.split('a*', 'hello world')  # 对于一个找不到匹配的字符串而言，split 不会对其作出分割
# print(str)

