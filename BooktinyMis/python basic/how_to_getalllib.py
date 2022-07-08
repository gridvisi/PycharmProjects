
import distutils.sysconfig as sysconfig
import os
import sys

std_lib = sysconfig.get_python_lib(standard_lib=True)

for top, dirs, files in os.walk(std_lib):
    for nm in files:
        prefix = top[len(std_lib)+1:]
        if prefix[:13] == 'site-packages':
            continue
        if nm == '__init__.py':
            print(top[len(std_lib)+1:].replace(os.path.sep,'.'))
        elif nm[-3:] == '.py':
            print(os.path.join(prefix, nm)[:-3].replace(os.path.sep,'.'))
        elif nm[-3:] == '.so' and top[-11:] == 'lib-dynload':
            print(nm[0:-3])

for builtin in sys.builtin_module_names:
    print (builtin,'\n',len(builtin))
    print(builtin)


#keywords function
'''


一、目标
1、了解python的关键字有哪些

2、了解python2和python3关键字的异同

3、注意False/True/None在python2中表示内置模块的变量，在python3中是解释器的内置关键字。

4、False/True/None本质都是object对象，False/True属于int对象，None属于空object对象。

二、要点
1、用来定义的关键字
def : 定义一个函数或者方法

class : 定义一个类对象

lamba ： 定义一个匿名函数

2、布尔关键字
False

True

3、控制流关键字
if elif else 条件判断

for in

for in else

continue 继续循环

break 跳出循环

while 循环结构

4、逻辑判断关键字
and

or

not

in

not in

is

5、异常
try:

代码1

except:

代码2

else:

代码3

finally:

代码4

raise: 主动出发异常

6、命令空间
global : 将模块空间变量引入到局部空间修改。

nonlocal: 将本局部空间的外层空间变量引入到本层局部空间修改，用于嵌套函数内。

7、其他
None

from imort

imort

imort as

with

assert

pass

return

yield

del

三、代码说明
'''
import  keyword  # 导入keyword模块

print(keyword.__all__)  # 列出可查看python keyword关键字的方法keyword.all方法
# ['iskeyword', 'kwlist']

print(keyword.kwlist)  # 调出keyword.kwlist方法输出所有关键字
"""
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 
'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 
'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 
'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 
'yield']
"""

print(keyword.iskeyword('as'))  # 判断是否为关键字
