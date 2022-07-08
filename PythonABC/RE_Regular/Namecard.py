'''
定义函数名：def namecard(name,corporation)

输入: 姓名，机构名称

输出：email地址

​

定义函数名：def splitNamecard(email):

输入: email地址

输出: 姓名，机构名称

建议两种方式实现，并比较Regx正则表达式实现的优点。

请参考往期链接
'''
import re
string = "Happy 2 vaccine to us"
result = re.findall("[a-zA-Z]", string)
print(result)

email = 'eric@gridvisi.com'

def splitNamecard(email):
    return re.findall("[a-zA-Z]", email)
print(splitNamecard(email))


result = re.split("@", email, 1)
print(result[1])
print(result[1].split("."))
corp = re.split(".",result[1],1)
print(corp)

result = re.findall( "[a-z]", email)
print(result)

