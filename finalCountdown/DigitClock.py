
import time
print('{:02}:{:02}:{:02}'.format(13,4,57))


def countdown(t): #函数
    t = int(t)
    while t:
        min,sec = divmod(t,60)
        #print(min,sec)
        timer = '{:02}:{:02}'.format(min,sec)
        #print(timer)
        # '{:02}:{:02}:{:02}'.format(13,4,57)
        #c = f"{min}:{sec}"
        print(timer)
        time.sleep(1)
        t -= 1
    print("time's up")

t = int(input("Enter the times in secs秒: "))
#countdown(t)


# skin
from tkinter import *
from tkinter.ttk import *
from time import strftime
root = Tk()
root.title('Digital clock')
label = Label(root,font=('aerial',40),background='black',foreground='white')
#label = Label(root,font=('Microsoft YaHei',40),background='dark grey',foreground='white')

def st(t):
    while t >= 0:
        min, sec = divmod(int(t), 60)
        # print(min,sec)
        strs = '{:02}:{:02}'.format(min, sec)
        time.sleep(1)
        t -= 1
        return strs

it = iter([i for i in range(t)][::-1])
def timer():
    #strs = strftime("%H:%M:%S %p")
    t = next(it)
    if t:
        time.sleep(0.1)
        label.config(text=st(t))
        label.after(1000, timer)
label.pack(anchor='center')
timer()
mainloop()

'''
while t:

    min, sec = divmod(t, 60)
    # print(min,sec)
    st = '{:02}:{:02}'.format(min, sec)
    # print(timer)
    # '{:02}:{:02}:{:02}'.format(13,4,57)
    # c = f"{min}:{sec}"
    st += " PM"
    print(st)
    time.sleep(1)
'''



print(type(strftime(("%H:%M:%S %p")))) #str

print(strftime("%H:%M:%S %p")[:-3])
H,M,S = 1,1,1
print(strftime("%H:%M:%S %p")[:-3])


'''

def timer():
    #t = 10
    strs = strftime("%H:%M:%S %p")
    #min, sec = divmod(t, 60)
    # print(min,sec)
    strs = '{:02}:{:02}'.format(min, sec)
    #strs =
    label.config(text=strs)
    label.after(1000,timer)

label.pack(anchor='center')
#timer()

mainloop()



def timerCountdown(t):
    t = int(t)
    while t:
        min, sec = divmod(t, 60)
        # print(min,sec)
        timer = '{:02}:{:02}'.format(min, sec)
        t -= 1
        #strs = strftime("H%:%M:%S %p")
        strs = timer
        print('strs:',strs)

        def timer():
            strs = strftime("%H:%M:%S %p")
            label.config(text=strs)
            label.after(1000, timer)

label.pack(anchor='center')
t = 3
#timerCountdown(t)

mainloop()

'''

'''
字体名称	英文名称	Unicode 编码
宋体	SimSun	\5B8B\4F53
新宋体	NSimSun	\65B0\5B8B\4F53
黑体	SimHei	\9ED1\4F53
微软雅黑	Microsoft YaHei	\5FAE\8F6F\96C5\9ED1
楷体_GB2312	KaiTi_GB2312	\6977\4F53_GB2312
隶书	LiSu	\96B6\4E66
幼园	YouYuan	\5E7C\5706
华文细黑	STXihei	\534E\6587\7EC6\9ED1
细明体	MingLiU	\7EC6\660E\4F53
新细明体	PMingLiU	\65B0\7EC6\660E\4F53
————————————————
版权声明：本文为CSDN博主「木森林哥哥」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/weixin_47021982/article/details/110789037


import datetime
dt=datetime.datetime(2006, 11, 21, 16, 30)
dt.strftime("%Y-%m-%d %H:%M")
'2006-11-21 16:30'

dt.strftime("%Y-%m-%d")
'2006-11-21'

dt.strftime("%A, %d. %B %Y %I:%M%p")
'Tuesday, 21. November 2006 04:30PM'

作者：小伍哥聊风控
链接：https://www.zhihu.com/question/516911959/answer/2351094694
来源：知乎
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''