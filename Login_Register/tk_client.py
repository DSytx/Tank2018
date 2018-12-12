from socket import *
import sys
import tkinter
import tkinter.messagebox
import time
import idcode
from settings import *



asd = ''
# def main():
#     if len(sys.argv)<3:
#         print('argv is error')
#         return
    # HOST = sys.argv[1]
    # PORT = int(sys.argv[2])
s = socket()
try:
    s.connect((HOST,PORT))
except Exception as e:
    print(e)




def jiemian(s):
        #创建应用程序窗口
    root = tkinter.Tk()
    root.title('登录')
    root.geometry('%dx%d'%(650,400))
    photo = tkinter.PhotoImage(file=r'Image/main.gif')
    label = tkinter.Label(root,image=photo)
    label.pack()
    #用户名标签
    labelName = tkinter.Label(root,
                            text='用户名',
                            justify=tkinter.RIGHT,
                            width=30,
                            font=('微软雅黑',12,'normal'))
    labelName.place(x=300,y=150,width=60,height=30)

    #输入用户名文本框
    varName = tkinter.StringVar(root,value='')
    entryName = tkinter.Entry(root,
                              width=80,
                              textvariable=varName,
                              font=('楷体',10,'bold'))
    entryName.place(x=400,y=150,width=200,height=30)

    #密码标签
    labelPwd = tkinter.Label(root,
                             text='密码', 
                             justify=tkinter.RIGHT,
                             width=100,
                             font=('微软雅黑',12,'normal'))
    labelPwd.place(x=300,y=220,width=60,height=30)

    #密码文本框
    varPwd = tkinter.StringVar(root,value='')
    entryPwd = tkinter.Entry(root,
                             show="*",
                              width=80,
                              textvariable=varPwd,
                              font=('楷体',10,'bold'))
    entryPwd.place(x=400,y=220,width=200,height=30)
    #登录按钮事件处理函数
    def login():
        #获取用户名和密码
        name = entryName.get()
        pwd = entryPwd.get()
        msg = 'L {} {}'.format(name,pwd)
        s.send(msg.encode())
        data = s.recv(1024).decode()
        if data == 'OK':
            tkinter.messagebox.showinfo(title='恭喜',
                                        message='登陆成功!')
            root.destroy()

            
        else:
            print(111)
            tkinter.messagebox.showerror(title="警告",
                                         message='用户名不存在或密码错误')
            print(222)
    #注册按钮事件处理函数
    def register():
        root.destroy()
        root1 = tkinter.Tk()
        root1.title('注册')
        photo = tkinter.PhotoImage(file=r'Image/main.gif')
        label = tkinter.Label(root1,image=photo)
        label.pack()
        root1.geometry('%dx%d'%(650,400))
        #用户名标签
        labelName = tkinter.Label(root1,
                                text='用户名',
                                justify=tkinter.RIGHT,
                                width=80,
                                font=('微软雅黑',12,'normal'))
        labelName.place(x=50,y=50,width=70,height=30)
        #输入用户名文本框
        varName = tkinter.StringVar(root1,value='')
        entryName = tkinter.Entry(root1,
                                  width=80,
                                  textvariable=varName,
                                  font=('楷体',12,'bold'))
        entryName.place(x=150,y=50,width=200,height=30)
        #密码标签
        labelPwd = tkinter.Label(root1,
                                 text='密码',
                                 justify=tkinter.RIGHT,
                                 width=80,
                                 font=('微软雅黑',12,'normal'))
        labelPwd.place(x=50,y=100,width=70,height=30)

        #密码文本框
        varPwd = tkinter.StringVar(root1,value='')
        entryPwd = tkinter.Entry(root1,
                                 show="*",
                                  width=80,
                                  textvariable=varPwd,
                                  font=('楷体',12,'bold'))
        entryPwd.place(x=150,y=100,width=200,height=30)
        #确认密码标签
        labelPwd2 = tkinter.Label(root1,
                                  text='确认密码',
                                  justify=tkinter.RIGHT,
                                  width=80,
                                  font=('微软雅黑',12,'normal'))
        labelPwd2.place(x=50,y=150,width=70,height=30)
        #确认密码文本框
        varPwd2 = tkinter.StringVar(root1,value='')
        entryPwd2 = tkinter.Entry(root1,
                                show="*",
                                width=80,
                                textvariable=varPwd2,
                                font=('楷体',12,'bold'))
        entryPwd2.place(x=150,y=150,width=200,height=30)
        #邮箱标签
        labelEm1 = tkinter.Label(root1,
                                text='电子邮箱',
                                justify=tkinter.RIGHT,
                                width='80',
                                font=('微软雅黑',12,'normal'))
        labelEm1.place(x=50,y=200,width=70,height=30)
        #邮箱文本框
        varEm1 = tkinter.StringVar(root1,value='')
        entryEm1 = tkinter.Entry(root1,
                                width=80,
                                textvariable=varEm1,
                                font=('楷体',12,'bold'))
        entryEm1.place(x=150,y=200,width=200,height=30)
        #验证码标签
        labelEm2 = tkinter.Label(root1,
                                text='验证码',
                                justify=tkinter.RIGHT,
                                width='80',
                                font=('微软雅黑',12,'normal'))
        labelEm2.place(x=50,y=250,width=70,height=30)

        #验证码文本框
        varEm2 = tkinter.StringVar(root1,value='')
        entryEm2 = tkinter.Entry(root1,
                                width=80,
                                textvariable=varEm2,
                                font=('楷体',12,'bold'))
        entryEm2.place(x=150,y=250,width=100,height=30)
        def email_fs():
            email = varEm1.get()
            global asd
            asd = idcode.main(email)
            print(asd)
        #判断注册输入是否正确
        def register_bt():

            name = entryName.get()
            pwd1 = entryPwd.get()
            pwd2 = entryPwd2.get()
            email = varEm2.get()
            if (pwd1 != pwd2):
                tkinter.messagebox.showerror(title="警告",
                                            message='两次输入的密码不一致')
            elif not pwd1 or not pwd2:
                tkinter.messagebox.showerror(title="警告",
                                            message='用户名和密码中不能为空')
            elif (' ' in name) or (' ' in pwd1):
                tkinter.messagebox.showerror(title="警告",
                                            message='用户名和密码中不能有空格')
            elif asd!=email:
                print(asd)

                tkinter.messagebox.showerror(title="警告",
                                            message='验证码输入错误')
            else:
                msg = 'R {} {}'.format(name,pwd1)
                s.send(msg.encode())
                data = s.recv(1024).decode()
                print(data)
                if data == 'NO':
                    tkinter.messagebox.showerror(title="警告",
                                            message='用户名已存在')
                elif data == 'OK':
                    tkinter.messagebox.showinfo(title='恭喜',
                                        message='注册成功！')

                    root1.destroy()
                    jiemian(s)
        buttonEm2 = tkinter.Button(root1,
                                text='发送验证码',
                                command=email_fs)
        buttonEm2.place(x=280,y=250,width=70,height=30)
        #返回登录界面
        def register_fh():
            root1.destroy()
            jiemian(s)
        #提交按钮
        buttonOk = tkinter.Button(root1,
                                text='提交',
                                command=register_bt)
        buttonOk.place(x=150,y=300,width=50,height=30)
        
        buttonFh = tkinter.Button(root1,
                                text='返回',
                                command=register_fh)
        buttonFh.place(x = 300,y=300,width=50,height=30)


        root1.mainloop()

    #创建按钮组件，同时设置按钮事件按钮事件处理函数
    buttonOk = tkinter.Button(root,
                            text='登录',
                            command=login)
    buttonOk.place(x=400,y=270,width=50,height=30)

    buttonRe = tkinter.Button(root,
                            text='注册',
                            command=register)
    buttonRe.place(x=550,y=270,width=50,height=30)


    root.mainloop()


jiemian(s)