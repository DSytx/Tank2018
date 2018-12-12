import tkinter
import tkinter.messagebox

def plane():
    user=""
    playr=0
    top = tkinter.Tk()
    top.title('主界面')
    top.geometry('1000x600+500+200')
    top.resizable(0,0)
    # img = tkinter.PhotoImage(file=r'main1.gif')
    img = tkinter.PhotoImage(file=r'Image/main1.gif')
    label = tkinter.Label(top,image=img)
    label.pack()
    labelName = tkinter.Label(top,
                            text='用户名',
                            justify=tkinter.RIGHT,
                            width=30,
                            font=('微软雅黑',12,'normal'))
    labelName.place(x=300,y=150,width=60,height=30)
    
    def single_game():
        nonlocal user,playr
        user=entryName.get() #获取文本框内容
        playr=1
        top.destroy()
    def double_game():
        nonlocal user,playr
        user=entryName.get() #获取文本框内容
        playr=2
        top.destroy()
    def three_game():
        nonlocal user,playr
        user=entryName.get() #获取文本框内容
        playr=3
        top.destroy()
    def more_game():
        nonlocal user,playr
        user=entryName.get() #获取文本框内容
        playr=4
        top.destroy()
    #输入用户名文本框
    varName = tkinter.StringVar(top,value='')
    entryName = tkinter.Entry(top,
                              width=80,
                              textvariable=varName,
                              font=('楷体',16,'bold'))
    entryName.place(x=400,y=150,width=200,height=30)

    buttonSg = tkinter.Button(top,
                                text='单人游戏',
                                command=single_game,
                                font=('微软雅黑',10,'bold')
                            )
    buttonSg.place(x=233,y=270,width=56,height=36)

    buttonDg = tkinter.Button(top,
                                text='双人游戏',
                                command=double_game,
                                font=('微软雅黑',10,'bold')
                                )
    buttonDg.place(x=363,y=270,width=56,height=36)
    buttonDg = tkinter.Button(top,
                                text='三人游戏',
                                command=three_game,
                                font=('微软雅黑',10,'bold')
                                )
    buttonDg.place(x=500,y=270,width=56,height=36)

    buttonTg = tkinter.Button(top,
                                text='多人乱斗',
                                command=more_game,
                                font=('微软雅黑',10,'bold')
                                )
    buttonTg.place(x=633,y=270,width=56,height=36)
    top.mainloop()
    return user,playr








