'''
https://www.codewars.com/kata/5e5b7f55c2e8ae0016f42339/train/python

你的任务是编写一个函数calculate，它接受一个用前缀波兰语符号写成的数学表达式的字符串，并对其进行评估。
这意味着所有的运算都放在其操作数之前。
例如，表达式3 + 5用波兰语符号写成+ 3 5，
(3 + 5) / (2 * 2) 是 / + 3 5 * 2 2

唯一有效的操作是+、-、*和/。输入的字符串保证是一个有效的表达式。

如果你的语言可用的话，你可以使用eval或alternative，但对于一个习惯性的解决方案来说，它绝不是必需的。

例子

calculate('123.456') == 123.456
calculate('+ -5 5') == 0
calculate('* + 2 2 3') == 12
calculate('/ + 3 5 * 2 2') == 2


输入
一个由数字和算术运算符组成的非空字符串，用空格分隔。这个字符串是一个有效的算术表达式，用前缀波尔符号书写。
'''

def calculate(expression):
    # for division, use true division, not floor division
    # should return a float
    pass

def calculate(expression):
    stack = []
    for x in expression.split()[::-1]:
        if x in '+-*/':
            a, b = stack.pop(), stack.pop()
            stack.append(eval(f'{a}{x}{b}'))
        else:
            stack.append(x)
    return float(stack.pop())

expression = '(3 + 5) / (2 * 2)'
expression = '123.456'
print(calculate(expression))
expression = '/ + 3 5 * 2 2'
print(calculate(expression))

#逆操作改为Polish表达
# 如何将下面expA,expB有微小差别，改为polish表达
A = 10 / ((5 - 3) * (1 + 4))  #= 1
B = 10 / (5 - 3) * (1 + 4)    #= 25

# 一步一步对比着看A和B
#Step1 优先级最高的括号先入手

# 先看A
expA1,expA2 = '- 5 3 ', '+ 1 4'  #1
exp = '* ' + expA1 + expA2       #2
exp = '/ 10 ' + exp             #3
print('A = ',exp)               #4
print('calculate(exp) = ',calculate(exp))

#再看B的变化

expB1,expB2 = '- 5 3 ','+ 1 4 '
exp = '/ 10 ' + expB1
exp = '* ' + exp + expB2
print('B = ',exp)
print('calculate(exp) = ',calculate(exp))


'''
B =  * + 3 4 / 10 - 5 2 
calculate(exp) =  23.333333333333336

B =  * / 10 - 5 3 + 3 4 
calculate(exp) =  35.0
'''
# 请熟悉eval()
a1,a2 = eval('5-3'),eval('1+4')
b1,b2 = eval('5-3'),eval('1+4')

#first1 * first2->'* first1 first2'
second = eval(f"{a1} * {a2}")
print(second)
exp = '* - 5 2 + 3 4'

#3 步骤2表达步骤3
third = eval(f'{10 / second}')
print(third)
exp = '/ 10 ' + exp
exp = '/ 10 ' + exp
exp = '*' + exp

expression = exp
#print(calculate(exp))


#from operator import add, sub, mul, truediv
from operator import add, sub, mul, truediv
def calculate(exp):
    stack = []
    ops = {'+' : add, '-' : sub, '*' : mul, '/' : truediv}
    for a in reversed(exp.split()):
        stack.append(ops[a](stack.pop(), stack.pop()) if a in ops else float(a))
    return stack.pop()




ops = {
    '+': float.__add__,
    '-': float.__sub__,
    '*': float.__mul__,
    '/': float.__truediv__,
}

def calculate(expression):
    stack = []
    for term in reversed(expression.split()):
        if term in ops:
            term = ops[term](stack.pop(), stack.pop())
        stack.append(float(term))
    return stack.pop()

