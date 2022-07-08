
# input name -> output :"你好，name"
# nmae，name

# input people's name
name = input("输入人姓名：") #李乐然 回车
print(name)
print(f"hello, {name}")
age = 10
print(f"我小哲今年是")

#profile ->
#sex
name, age, gender = 'li',40,'male' #,'female'
location, hight, work_exp, family = 'cq',150,7,5

class Person():
    def __init__(self):
        self.name = name
        self.gender = gender

    def talk(self):
        return f"hello, {self.name}"

    def eat(self):
        return '奶茶' if self.gender == 'female' else "汉堡"


fei = Person()
print(fei.talk(),fei.eat())

#数组 _>>> list #backspace
#no  #item  #price
#1   orange   5

'''

import string  # 字符

# .ascii_letters 字母 信件

print(string.ascii_letters)
print(string.digits)
print(string.ascii_lowercase) #lower小写

a = string.ascii_letters
print(a)

#import turtle as t
#t.forward(300)

names = ['李俊霖','李乐然','王子杰','秦子东','liuchengxin']
          #names[0] [1]   [2]     [3]       [4]

for name in names: #for 循环
    if name[0] == '李':
        print(name)

# 数组和字符串都用切片
name = '李俊霖我是中国人'
print('s:',name[1:6:2]) # 切片 李




# python 面向对象语言

#class person()

'''

def persons(**kwgs):
    return