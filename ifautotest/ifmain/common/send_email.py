# coding=utf-8

import os
import smtplib
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.utils import formataddr


def abs_path(path):
    PATH = lambda p: os.path.abspath(
        os.path.join(os.path.dirname(__file__), p)
    )
    return PATH(path)


def send_email(attach_name=None):
    sender = "jianghan@julanling.com"
    password = "jiangHAN11200"
    receivers = [
        "jianghan@julanling.com",
        "zhangchunli@julanling.com",
        "cuiguoen@julanling.com",
        "caiyichen@julanling.com",
        "liuyi@julanling.com",
    ]
    subject = "接口自动化日常报告"

    message = MIMEMultipart()
    # message['From'] = Header("慧贤测试小分队", 'utf-8')        # 发件人匿名
    # message['To'] = Header("慧贤科技大领导", 'utf-8')      # 收件人匿名
    message["From"] = formataddr(["测试小分队", sender])
    message["To"] = formataddr(["慧贤大领导", receivers[0]])
    message['Subject'] = Header(subject, 'utf-8')       # 邮件标题
    message.attach(email_content())         # 邮件正文内容
    message.attach(email_attachment(attach_name=attach_name))      # 附件

    try:
        # smtpObj = smtplib.SMTP('localhost')
        # smtpObj.sendmail(sender, receivers, message.as_string())
        # print("邮件发送成功")

        server=smtplib.SMTP_SSL("smtp.exmail.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是25
        server.login(sender, password)  # 括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(sender, receivers, message.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  # 关闭连接

    except smtplib.SMTPException:
        print("Error: 无法发送邮件")


def email_content():
    mail_msg = """
    <p>接口自动化测试报告(线上服务器)，详情见附件</p>
    """
    content = MIMEText(mail_msg, 'html', 'utf-8')
    return content


def email_attachment(attach_name=None):
    attach = MIMEApplication(open(abs_path('../report/{0}.html'.format(attach_name)), 'rb').read())
    attach.add_header('Content-Disposition', 'attachment', filename='api_uiautotest_report.html')

    return attach


if __name__ == "__main__":
    send_email()
