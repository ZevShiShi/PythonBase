# I/O

# try:
#     f = open('test.txt', 'r')
#     print(f.read())
# except IOError:
#     pass
# finally:
#     if f:
#         f.close()

# Python引入了with语句来自动帮我们调用close()方法：
# 这和前面的try ... finally是一样的，但是代码更佳简洁，并且不必调用f.close()方法。
# 遇到有些编码不规范的文件，你可能会遇到UnicodeDecodeError，因为在文本文件中可能夹杂了一些非法编码的字符。
# 遇到这种情况，open()函数还接收一个errors参数，表示如果遇到编码错误后如何处理。最简单的方式是直接忽略：
# with open('test.txt', 'r', encoding='utf-8', errors='ignore') as f:
#     # print(f.read())
#     for line in f.readlines():
#         print(line.strip())  # 把末尾的'\n'删掉
#
# # 要读取二进制文件，比如图片、视频等等，用'rb'模式打开文件即可：
# with open('zev.jpg', 'rb') as f:
#     print(f.read())


# 写入 w模式（会覆盖内容） 和 wb二进制模式 ，使用 a模式（追加内容）
# with open('test.txt', 'a') as f:
#     f.write('My name is zev.\n')
# with open('test.txt', 'r') as f:
#     print(f.read())

# StringIO顾名思义就是在内存中读写str
# from io import StringIO
#
# f = StringIO()
# f.write('hello')
# f.write(' ')
# f.write('world!')
# print(f.getvalue())
#
#
# f = StringIO('Hello!\nHi!\nGoodbye!')
# while True:
#     s = f.readline()
#     if s == '':
#         break
#     print(s.strip())


# 如果要操作二进制数据，就需要使用BytesIO。
# from io import BytesIO
#
# f = BytesIO()
# f.write('中文'.encode('utf-8'))  # 写入的不是str，而是经过UTF-8编码的bytes。
# print(f.getvalue())
#
#
# f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
# print(f.read())
