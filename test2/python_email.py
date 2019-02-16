# 邮件相关 smtp邮件服务
# From、To 要与 sendmail 中的前两个参数保持一致
# To 多个邮箱用逗号隔开，sendmail 中的第二个参数要用 list
# 注意点：subject 中不能含有 "test" 关键字，否则会被视为垃圾邮件
# 注意点: 如果使用授权码登录第三方邮件客户端，则此处的密码(mail_pass)使用授权码


import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
from email.utils import formataddr

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
message = MIMEMultipart('alternative')
message.attach(MIMEText('hello', 'plain', 'utf-8'))
message.attach(MIMEText('<html><body><h1>Hello</h1></body></html>', 'html', 'utf-8'))

# 添加附件就是加上一个MIMEBase，从本地读取一个图片:
with open('zev.jpg', 'rb') as f:
    # 设置附件的MIME和文件名，这里是jpg类型:
    mime = MIMEBase('image', 'jpg', filename='zev.jpg')
    # 加上必要的头信息:
    mime.add_header('Content-Disposition', 'attachment', filename='zev.jpg')
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-Id', '0')
    # 把附件的内容读进来:
    mime.set_payload(f.read())
    # 用Base64编码:
    encoders.encode_base64(mime)
    # 添加到MIMEMultipart:
    message.attach(mime)

# message['From'] = Header("zhujiang", 'utf-8')  # 发送者（昵称）
# message['To'] = Header('Zev', 'utf-8')  # 接收者（昵称）
message['From'] = formataddr(["zhujiang", sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
message['To'] = formataddr(["Zev", receiver])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号

subject = 'Python SMTP 邮件主题'
message['Subject'] = Header(subject, 'utf-8')

try:
    smtpObj = smtplib.SMTP_SSL(smtp_server, smtp_port, timeout=10)  # smtp服务器地址以及端口号,安全连接ssl
    smtpObj.set_debuglevel(1)  # 打印log
    # 括号中对应的是发件人邮箱账号、邮箱密码（ps:如果是qq注册的foxmail，必须使用qq授权码作为密码）
    smtpObj.login(sender, sender_password)
    # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
    smtpObj.sendmail(sender, [receiver, ], message.as_string())
    smtpObj.quit()  # 关闭连接
    print("邮件发送成功")
except smtplib.SMTPException as error:
    print("Error: 无法发送邮件", error.__str__())
