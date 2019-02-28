# 邮件相关 smtp邮件服务
# From、To 要与 sendmail 中的前两个参数保持一致
# To 多个邮箱用逗号隔开，sendmail 中的第二个参数要用 list
# 注意点：subject 中不能含有 "test" 关键字，否则会被视为垃圾邮件
# 注意点: 如果使用授权码登录第三方邮件客户端，则此处的密码(mail_pass)使用授权码


import smtplib, poplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
from email.parser import Parser
from email.header import decode_header
from email.utils import formataddr, parseaddr

sender = 'zhujiang.shishi@foxmail.com'  # 发件人邮箱账号
sender_password = 'gzfmizeoldsrbgbb'  # 发件人邮箱密码
receiver = 'za2576514@qq.com'
smtp_server = 'smtp.qq.com'
smtp_port = 465


# receivers = ['za2576514@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

# 发送普通文本
# 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
# message = MIMEText('Python 邮件发送测试...', 'plain', 'utf-8')


# 发送html
# message = MIMEText('<html><body><h1>Hello</h1>' +
#                    '<p>send by <a href="http://www.python.org">Python</a>...</p>' +
#                    '</body></html>', 'html', 'utf-8')

# 发送附件
# message = MIMEMultipart()
# 邮件正文是MIMEText:
# message.attach(MIMEText('我将要发送一个文件给你', 'plain', 'utf-8'))

# 要把图片嵌入到邮件正文中，我们只需按照发送附件的方式，先把邮件作为附件添加进去，
# 然后，在HTML中通过引用src="cid:0"就可以把附件作为图片嵌入了。如果有多个图片，
# 给它们依次编号，然后引用不同的cid:x即可。
# message.attach(MIMEText('<html><body><h1>Hello</h1>' +
#                         '<p><img src="cid:0"></p>' +
#                         '</body></html>', 'html', 'utf-8'))

# 同时支持HTML和Plain格式
# message = MIMEMultipart('alternative')
# message.attach(MIMEText('hello', 'plain', 'utf-8'))
# message.attach(MIMEText('<html><body><h1>Hello</h1></body></html>', 'html', 'utf-8'))
#
# # 添加附件就是加上一个MIMEBase，从本地读取一个图片:
# with open('zev.jpg', 'rb') as f:
#     # 设置附件的MIME和文件名，这里是jpg类型:
#     mime = MIMEBase('image', 'jpg', filename='zev.jpg')
#     # 加上必要的头信息:
#     mime.add_header('Content-Disposition', 'attachment', filename='zev.jpg')
#     mime.add_header('Content-ID', '<0>')
#     mime.add_header('X-Attachment-Id', '0')
#     # 把附件的内容读进来:
#     mime.set_payload(f.read())
#     # 用Base64编码:
#     encoders.encode_base64(mime)
#     # 添加到MIMEMultipart:
#     message.attach(mime)

# message['From'] = Header("zhujiang", 'utf-8')  # 发送者（昵称）
# message['To'] = Header('Zev', 'utf-8')  # 接收者（昵称）
# message['From'] = formataddr(["zhujiang", sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
# message['To'] = formataddr(["Zev", receiver])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
#
# subject = 'Python SMTP 邮件主题'
# message['Subject'] = Header(subject, 'utf-8')
#
# try:
#     smtpObj = smtplib.SMTP_SSL(smtp_server, smtp_port, timeout=10)  # smtp服务器地址以及端口号,安全连接ssl
#     smtpObj.set_debuglevel(1)  # 打印log
#     # 括号中对应的是发件人邮箱账号、邮箱密码（ps:如果是qq注册的foxmail，必须使用qq授权码作为密码）
#     smtpObj.login(sender, sender_password)
#     # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
#     smtpObj.sendmail(sender, [receiver, ], message.as_string())
#     smtpObj.quit()  # 关闭连接
#     print("邮件发送成功")
# except smtplib.SMTPException as error:
#     print("Error: 无法发送邮件", error.__str__())


# POP3解析邮件

def guess_charset(msg):
    # 先从msg对象获取编码:
    charset = msg.get_charset()
    if charset is None:
        # 如果获取不到，再从Content-Type字段获取:
        content_type = msg.get('Content-Type', '').lower()
        pos = content_type.find('charset=')
        if pos >= 0:
            charset = content_type[pos + 8:].strip()
    return charset


def decode_str(s):
    value, charset = decode_header(s)[0]
    if charset:
        value = value.decode(charset)
    return value


def print_info(msg, indent=0):
    if indent == 0:
        # 邮件的From, To, Subject存在于根对象上:
        for header in ['From', 'To', 'Subject']:
            value = msg.get(header, )
            if value:
                if header == 'Subject':
                    # 需要解码Subject字符串:
                    value = decode_str(value)
                else:
                    # 需要解码Email地址:
                    hdr, addr = parseaddr(value)
                    name = decode_str(hdr)
                    value = u'%s <%s>' % (name, addr)
                    print('%s%s: %s' % ('  ' * indent, header, value))
    if msg.is_multipart():
        # 如果邮件对象是一个MIMEMultipart,
        # get_payload()返回list，包含所有的子对象:
        parts = msg.get_payload()
        for n, part in enumerate(parts):
            print('%s part %s' % (' ' * indent, n))
            print('%s-------------------' % (' ' * indent))
            # 递归打印每一个子对象:
            print_info(part, indent + 1)
    else:
        # 邮件对象不是一个MIMEMultipart,
        # 就根据content_type判断:
        content_type = msg.get_content_type()
        if content_type == 'text/plain' or content_type == 'text/html':
            # 纯文本或HTML内容:
            content = msg.get_payload(decode=True)
            # 要检测文本编码:
            charset = guess_charset(msg)
            print('content:%s,charset:%s' % (content, charset))
            if charset:
                content = content.decode(charset)
                print('%sText:%s' % (' ' * indent, content + '...'))
        else:
            # 不是文本,作为附件处理:
            print('%sAttachment:%s' % (' ' * indent, content_type))


# 通过POP3下载邮件
pop_server = 'pop.qq.com'
pop_port = 995
# 连接到POP3服务器:
server = poplib.POP3_SSL(pop_server, pop_port)
# 可以打开或关闭调试信息:
server.set_debuglevel(1)
# 可选:打印POP3服务器的欢迎文字:
print(server.getwelcome())
# 身份认证:
server.user(sender)
server.pass_(sender_password)
# stat()返回邮件数量和占用空间:
print('Message:%s . Size:%s' % server.stat())
# list()返回所有邮件的编号:
resp, mails, octets = server.list()
# 可以查看返回的列表类似['1 82923', '2 2184', ...]
print(mails)
# 获取最新一封邮件, 注意索引号从1开始:
index = len(mails)
resp, lines, octets = server.retr(index)
# lines存储了邮件的原始文本的每一行,
# 可以获得整个邮件的原始文本:
msg_content = b'\r\n'.join(lines).decode('utf-8')
# 稍后解析出邮件:
msg = Parser().parsestr(msg_content)
print_info(msg)
# 可以根据邮件索引号直接从服务器删除邮件:
# server.dele(index)
# 关闭连接:
server.quit()
