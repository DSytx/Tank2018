import smtplib  #发邮件
import random
from  email.mime.text import MIMEText #邮件文本

class  SendMail:
    def __init__(self,SMTPserver, Sender, password ):
        self.SMTPsever = SMTPserver  # 服务器
        self.Sender = Sender  # 发送邮件的地址
        self.password = password # 密码
        self.mailserver = smtplib.SMTP(self.SMTPsever, 25)  # 邮件服务器25端口
        self.mailserver.login(self.Sender, self.password)  # 登陆
    def Send(self,Message,title,maillist):
        msg = MIMEText(Message)  # 转化邮件文本
        msg["Subject"] =title  # 邮件标题  
        msg["From"]=self.Sender #邮件发送者
 
        self.mailserver.sendmail(self.Sender,
                           maillist,
                           msg.as_string())#发送邮件函数
    def exit(self):
        self.mailserver.quit()

#随机生成验证码
def main(email):
    l=[0,1,2,3,4,5,6,7,8,9]
    l1=[]
    s=str()
    for _ in range(1,7):
        l1.append(int(random.random()*10))
    for index in l1:
        s+=str(l[index])
    content="验证码是%s，请不要把验证码告诉其他人" % s

    sender1= SendMail("smtp.163.com","tank_2018@163.com","tank2018")

    sender1.Send(content,"坦克大战2018验证码",[email])
    sender1.exit()
    return s


