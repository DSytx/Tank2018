from socket import *
import os
import time
import signal
import pymysql
import sys
from multiprocessing import Process

#定义全局变量
HOST = '0.0.0.0'
PORT = 6666
ADDR = (HOST,PORT)

def main():
    #创建数据库连接
    db = pymysql.connect('localhost','root','123456','tanke')

    #创建套接字
    s = socket()
    s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    s.bind(ADDR)
    s.listen(5)

    while True:
        try:
            c,addr = s.accept()
            print('Connect from',addr)
        except KeyboardInterrupt:
            s.close()
            sys.exit('服务器退出')
        except Exception as e:
            print(e)
            continue

        #创建子进程
        # pid = os.fork()
        # if pid == 0:
        #     pid1=os.fork()
        #     if pid1==0:
        #         s.close()
        #         print('子进程准备处理请求')
        #         do_child(c,db)
        #     else:
        #         sys.exit()
        # else:
        #     pid,start=os.wait()
        #     c.close()
        #     continue
        p = Process(target=do_child,args=(c,db))
        p.start()


#判断请求类型
def do_child(c,db):
    while True:
        data = c.recv(1024).decode()
        if data[0] == 'L':
            do_login(c,db,data)
        if data[0] == 'R':
            do_register(c,db,data)

#注册函数
def do_register(c,db,data):
    l = data.split(' ')
    name = l[1]
    pwd = l[2]
    cursor = db.cursor()
    sql = "select * from user where name='%s'"%name
    cursor.execute(sql)
    r = cursor.fetchone()

    if r!=None:
        c.send('NO'.encode())
        return
    else:   
        sql = "insert into user (name,password) value('%s','%s')"%(name,pwd)
        
        cursor.execute(sql)
        db.commit()
        c.send('OK'.encode())
    
#登录判断函数
def do_login(c,db,data):
    l = data.split(' ')
    name = l[1]
    pwd = l[2]
    cursor = db.cursor()
    sql = "select * from user where name='%s'"%name
    cursor.execute(sql)

    r = cursor.fetchone()

    if r != None:
        if r[1] == pwd:
            c.send('OK'.encode())
            print('%s登录成功'%name)
        else:
            c.send('pwd erro'.encode())
    else:
        c.send('None'.encode())
main()
