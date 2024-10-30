import smtplib
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import os

text = """
电子邮件的格式范文二：

    您好，我是北京雅致人生管理顾问有限公司的王艳。很高兴能够认识您，并有幸将我们公司介绍给您。我们公司培训主要以素质技能技巧为主，曾经成功的为

IBM/HP/SUMSUNG/微软、中海油、大唐移动、北京移动、信息产业部电信研究院服务过，欢迎您访问我们公司的网址：,对我们公司有更多的了解。

附件是我们公司擅长的培训课程及讲师简历。请您查收。

如有任何问题或者建议请您随时与我联系!

希望我们能达成互补，在未来有合作的机会!

感谢您对我工作的支持!

祝您工作开心快乐!


[玩泥巴大队黄班组][]

日期：2024年10月21日
"""
# 配置邮箱服务器信息
mail_host = "smtp.qq.com"  # 设置服务器
mail_user = "1538699506@qq.com"  # 用户名
mail_pass = "hdceokoscmqegiee"  # 授权码

# 配置发件人、收件人信息
sender = '1538699506@qq.com'  # 发件人邮箱
receivers = ["liyunfei19981019@163.com",'1720580941@qq.com']  # 收件人邮箱，可设置为多个邮箱


def message_config():
    """
    配置邮件信息
    :return: 消息对象
    """
    # 第三方 SMTP 服务
    # content = MIMEText('练习发送邮件无需关注')
    content = MIMEText(text)
    message = MIMEMultipart()  # 多个MIME对象
    message.attach(content)  # 添加内容
    message['From'] = Header(mail_user)  # 发件人
    message['To'] = Header("1720580941@qq.com", 'utf-8')  # 收件人
    message['Subject'] = Header('练习邮件发送', 'utf-8')  # 主题
    # 添加Excel类型附件
    # file_name = r'./reports/index.html'  # 文件名
    file_name = r'./datas\excel\ceshi.xlsx'
    file_path = os.path.join(file_name)  # 文件路径
    xlsx = MIMEApplication(open(file_path, 'rb').read())  # 打开Excel,读取Excel文件
    xlsx["Content-Type"] = 'application/octet-stream'  # 设置内容类型
    xlsx.add_header('Content-Disposition', 'attachment', filename=file_name)  # 添加到header信息
    message.attach(xlsx)
    return message


def send_mail(message):
    """
    发送邮件
    :param message: 消息对象
    :return: None
    """
    try:
        smtpObj = smtplib.SMTP_SSL(mail_host)  # 使用SSL连接邮箱服务器
        smtpObj.login(mail_user, mail_pass)  # 登录服务器
        smtpObj.sendmail(sender, receivers, message.as_string())  # 发送邮件
        print("邮件发送成功")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    print("开始执行")
    message = message_config()  # 调用配置方法
    send_mail(message)  # 发送邮件
    print("执行结束")