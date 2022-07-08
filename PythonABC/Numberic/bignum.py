
n = 999_999_99 + 1
print(n)

'''
1、网络编程，数据交换的时候需要对字节进行解析都是一个byte一个byte的处理，一
个byte可以用0xff两个16进制来表达，通过网络抓包，可以看到数据是通过16进制传输的

2、数据存储，储存到硬盘中是0101的二进制方式，储存到系统的表达方式都是byte方式

3、一些常用值的定义，比如前端CSS(层叠样式表) 的一些属性如：color:#f00这种就是用
16进制的方式，4个16进制可以表达好几百万的颜色信息。
'''
#color = R,G,B Channel
yellow = 0xff_ff_00
print(yellow)
import turtle as t
c = '#'+str(yellow)[2:]
c = '0xff_ff_00'
c =  '#FFFF00'
print(c)
t.color(c)
t.begin_fill()
for _ in range(4):
    t.pencolor()

    #t.pencolor('#ff0000')
    t.left(90)
    t.forward(100)
t.end_fill()
t.done()