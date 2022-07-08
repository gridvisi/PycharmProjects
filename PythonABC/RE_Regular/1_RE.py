# https://automatetheboringstuff.com/2e/chapter7/
def isPhoneNumber(text):
    if len(text) != 12: #➊
         return False
    for i in range(0, 3):
         if not text[i].isdecimal(): # ➋
             return False
    if text[3] != '-':   # ➌
         return False
    for i in range(4, 7):
        if not text[i].isdecimal(): # ➍
             return False
    if text[7] != '-':     # ➎
         return False
    for i in range(8, 12):
        if not text[i].isdecimal(): # ➏
             return False
    return True                     # ➏

print('Is 415-555-4242 a phone number?')
print(isPhoneNumber('415-555-4242'))
print('Is Moshi moshi a phone number?')
print(isPhoneNumber('Moshi moshi'))

'''
isPhoneNumber()函数有一些代码，用于检查文本中的字符串是否是一个有效的电话号码。
如果其中任何一项检查失败，该函数就会返回False。

首先，代码检查字符串是否正好是12个字符➊。
然后，它检查区号（即文本中的前三个字符）是否只由数字字符组成➋。
该函数的其余部分检查该字符串是否符合电话号码的模式：该号码必须在区号之后有第一个连字符➌，
还有三个数字字符➍，然后是另一个连字符➎，最后还有四个数字➏。如果程序执行成功地通过了所有的检查，它就会返回True ➐。

调用isPhoneNumber()，参数为'415-555-4242'，将返回True。用'Moshi moshi'调用isPhoneNumber()将返回False；
第一次测试失败是因为'Moshi moshi'不是12个字符长。

如果你想在一个更大的字符串中找到一个电话号码，你将不得不添加更多的代码来找到电话号码模式。
将isPhoneNumber.py中的最后四个print()函数调用替换为以下内容。

message = '明天给我打电话：415-555-1011。415-555-9999是我的办公室'。
'''
message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
for i in range(len(message)):
    chunk = message[i:i+12]  #  ➊
    if isPhoneNumber(chunk): #  ➋
          print('Phone number found: ' + chunk)
print('Done')


#在for循环的每一次迭代中，一个由12个字符组成的新消息块被分配到变量chunk ➊中。
# 例如，在第一次迭代时，i是0，chunk被分配到message[0:12]（即字符串 "4点给我打电话"）。
# 在下一次迭代中，i为1，chunk被分配到message[1:13]（字符串'all me at 41'）。
# 换句话说，在for循环的每一次迭代中，chunk都有以下值。

'在4点给我打电话'
'all me at 41'
'll me at 415'
'我在415-'

import re
'''
. .等等。
你把chunk传给isPhoneNumber()，看它是否符合电话号码模式➋，如果是，你就打印这个chunk。

继续循环浏览消息，最终chunk中的12个字符将是一个电话号码。循环遍历整个字符串，测试每一个12个字符，
并打印它发现的满足isPhoneNumber()的任何块。一旦我们完成了对消息的检查，我们就打印Done。

在这个例子中，虽然消息中的字符串很短，但它可能有几百万个字符，程序仍然会在一秒钟内运行。
使用正则表达式查找电话号码的类似程序也会在一秒钟内运行，但正则表达式使编写这些程序更加快捷。

用正则表达式查找文本的模式
前面的电话号码查找程序是可行的，但它使用了大量的代码来做一些有限的事情：isPhoneNumber()函数有17行，
但只能找到一个电话号码的模式。如果一个电话号码的格式是415.555.4242或（415）555-4242呢？

如果电话号码有分机，如415-555-4242 x99呢？isPhoneNumber()函数将无法验证它们。你可以为这些额外的模
式添加更多的代码，但有一个更简单的方法。

正则表达式，简称为regexes，是对文本模式的描述。
例如，regex中的一个\d代表一个数字字符--即从0到9的任何一个数字。
Python 使用 regex \d\d-\d\d-\d-\d-\d\d 匹配与先前 isPhoneNumber() 函数相同的文本模式：
一个由三个数字、一个连字符、另外三个数字、另一个连字符和四个数字组成的字符串。
任何其他的字符串都不会与 \d\d\d-\d-\d-\d-\d-\d 的正则匹配。

但正则表达式可以更加复杂。例如，在一个模式后面加一个3的大括号（{3}）就像说："匹配这个模式三次"。
因此，稍短的正则表达式 \d{3}-\d{3}-\d{4} 也能匹配正确的电话号码格式。

创建REGEX对象
Python中所有的雷格函数都在re模块中。在交互式 shell 中输入以下内容来导入这个模块。
注意本章中的大多数例子都需要 re 模块，所以记得在你写的任何脚本的开头或者在你重新启动 Mu 的时候导入它。
否则，你会得到一个NameError: name 're' is not defined的错误信息。

向re.compile()传递一个代表你的正则表达式的字符串值，会返回一个Regex模式对象（或者简单地说，一个Regex对象）。

要创建一个匹配电话号码模式的Regex对象，请在交互式外壳中输入以下内容。
(记住，\d的意思是 "一个数字字符"，\d\d-\d-\d-\d-\d-\d\d是电话号码模式的正则表达式）。
'''
phoneNumRegex = re.compile(r'\d\d-\d\d-\d\d')
#现在phoneNumRegex变量包含一个Regex对象

'''
匹配Regex对象
Regex对象的search()方法搜索它所传递的字符串，以寻找任何与regex匹配的字符串。
如果在字符串中没有找到regex模式，search()方法将返回None。
如果找到该模式，search()方法将返回一个Match对象，该对象有一个group()方法，
将从搜索过的字符串中返回实际匹配的文本。(我很快就会解释分组。) 
例如，在交互式外壳中输入以下内容。
'''

#phoneNumRegex = re.compile(r'\d\d-\d\d-\d-\d-\d\d') # not match!
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('My number is 415-555-4242.' )
print(mo)
print('Phone number found: ' + mo.group())

'''
找到的电话号码。415-555-4242

mo变量名称只是一个通用名称，用于Match对象。这个例子一开始可能看起来很复杂，
但它比之前的isPhoneNumber.py程序要短得多，而且做的是同样的事情。

在这里，我们将我们想要的模式传递给re.compile()，并将生成的Regex对象存储在phoneNumRegex中。
然后我们在phoneNumRegex上调用search()，并在搜索过程中向search()传递我们想要匹配的字符串。
搜索的结果被存储在变量mo中。在这个例子中，我们知道我们的模式将在字符串中被找到，所以我们知道
将返回一个Match对象。知道 mo 包含一个 Match 对象，而不是空值 None，
我们就可以对 mo 调用 group() 来返回匹配结果。将mo.group()写在我们的print()函数调用中，可以
显示整个匹配，即415-555-4242。
'''

#对正则表达式匹配的回顾
'''
虽然在 Python 中使用正则表达式有几个步骤，但每个步骤都相当简单。

用 import re 导入 regex 模块。
用 re.compile() 函数创建一个 Regex 对象。(记住要使用一个原始字符串。)
将你要搜索的字符串传入 Regex 对象的 search() 方法。这将返回一个Match对象。
调用Match对象的group()方法来返回实际匹配的文本字符串。

注意虽然我鼓励你在交互式IDE中输入示例代码，但你也应该使用基于网络的正则表达式测试器，它可以准确地
显示出一个重码如何匹配你输入的文本。我推荐使用 https://pythex.org/ 上的测试器。

用正则表达式进行更多的模式匹配
现在你知道了使用 Python 创建和查找正则表达式对象的基本步骤，你已经准备好尝试它们的一些更强大的模式匹配功能。

用括号分组
假设你想把区号和电话号码的其他部分分开。添加小括号将在词组中创建分组：(\d\d\d)-(\d\d\d-\d\d)
然后你可以使用group()匹配对象方法，从一个组中抓取匹配的文本。

Regex字符串中的第一组()小括号将是第1组，第二组()将是第2组。 
通过向group() match对象方法传递整数1或2，你可以抓取匹配文本的不同部分。
向group()方法传入0或不传入，将返回整个匹配的文本。在交互式外壳中输入以下内容。
'''
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is 415-555-4242.')
mo.group(1)
'415'
mo.group(2)
'555-4242'
mo.group(0)
'415-555-4242'
mo.group()
'415-555-4242'

'''如果你想一次检索所有的组，使用group()方法--注意名称的group+s复数形式。
.groups() instead of group() !!!'''

print('mo.groups:',mo.groups())
'''('415', '555-4242')'''
areaCode, mainNumber = mo.groups()
print(areaCode)
'415'
print(mainNumber)
'555-4242'

'''
由于 mo.groups() 返回一个由多个值组成的元组，你可以使用多重赋值技巧将每个值赋给一个单独的变量，
就像前面的 areaCode, mainNumber = mo.groups() 一行。

小括号在正则表达式中具有特殊的意义，但如果你需要匹配文本中的小括号，你会怎么做？例如，也许你要匹
配的电话号码的区号设置在小括号中。在这种情况下，你需要用反斜杠来转义（和）字符。输入以下内容。
'''
phoneNumRegex = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)' )
mo = phoneNumRegex.search('My phone number is (415) 555-4242.')
mo.group(1)
'(415)'
mo.group(2)
'555-4242'

'''
传递给re.compile()的原始字符串中的 \(和 \)转义字符将匹配实际的小括号字符。在正则表达式中，以下字符具有特殊含义。

.  ^ $ * + ?  { } [ ] \ | ( )

如果你想检测这些字符作为你的文本模式的一部分，你需要用反斜杠来转义它们。

\.  \^ \$ \* \+ \?  \{ \}  \[ \] \\ \| \( \)

请确保仔细检查你没有把正则表达式中的转义小括号\( 和\) 错当成小括号( 和 ) 。
如果你收到关于 "缺少）"或 "不平衡的小括号 "的错误信息，你可能忘记为一个组包含未转义小括号的结尾，就像在这个例子中。
'''
#re.compile(r'(\(Parentheses\)' )
'''回溯（最近一次调用）。
    --snip--
re.error: missing ), unterminated subpattern at position 0
这个错误信息告诉你，在r'(\(Parentheses\)'字符串的索引0处有一个打开的小括号，但缺少相应的关闭小括号。

用管子匹配多个组
|字符被称为管道。你可以在任何你想匹配许多表达式之一的地方使用它。
例如，正则表达式r'Batman|Tina Fey'将匹配'Batman'或'Tina Fey'。
当搜索的字符串中同时出现蝙蝠侠和蒂娜-菲时，第一次出现的匹配文本将作为匹配对象返回。在交互式外壳中输入以下内容。
'''

heroRegex = re.compile (r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey')
mo1.group()
'Batman'#蝙蝠侠

mo2 = heroRegex.search('Tina Fey and Batman')
mo2.group()
'Tina Fey'

'''
注意

你可以用findall()方法找到所有匹配的出现，该方法在第171页的 "findall()方法 "中讨论。

你也可以使用管道来匹配几个模式中的一个，作为你的regex的一部分。
例如，假设你想匹配 "Batman"、"Batmobile"、"Batcopter "和 "Batbat "中的任何一个字符串。
由于所有这些字符串都以Bat开头，如果你能只指定一次这个前缀就更好了。这可以用圆括号来实现。
输入以下内容。
'''

batRegex = re.compile(r'Bat(man|mobile|copter|bat)' )
mo = batRegex.search('Batmobile lost a wheel')
mo.group()
'Batmobile'
mo.group(1)
'mobile'

'''
方法调用mo.group()返回完整的匹配文本'Batmobile'，而mo.group(1)只返回第一个括号组内匹配文本的部分，
'mobile'。通过使用管道字符和分组小括号，你可以指定几个你想让你的重构函数匹配的替代模式。

如果你需要匹配一个实际的管道字符，请用反斜杠转义，如\|

用问号进行可选的匹配
有时，有一种模式你只想选择性地匹配。也就是说，无论该文本是否在那里，重构函数都应该找到一个匹配? 
字符将其前面的组标记为模式的可选部分。例如，输入以下内容。

'''
batRegex = re.compile(r'Bat(wo)?man')
mo1 = batRegex.search('The Adventures of Batman')
mo1.group()
'Batman'

mo2 = batRegex.search('The Adventures of Batwoman')
mo2.group()
'Batwoman'

'''
正则表达式中的(wo)? 部分意味着模式wo是一个可选的组。该正则表达式将匹配其中有wo的零个实例或一个实例的文本。
这就是为什么这个词组同时匹配 "Batwoman "和 "Batman"。

使用前面的电话号码的例子，你可以让这个词组寻找有或没有区号的电话号码。在输入以下内容。
'''
phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d')
mo1 = phoneRegex.search('My number is 415-555-4242')
mo1.group()
'415-555-4242'

mo2 = phoneRegex.search('My number is 555-4242')
mo2.group()
'555-4242'

'''
你可以把"? "看作是说："匹配这个问号前面的组中的零或一个"。
如果你需要匹配一个实际的问号字符，可以用"？"转义。

用星号匹配零或更多
*（称为星号或星标）意味着 "匹配零或更多"--星号之前的组别可以在文本中出现任何次数。
它可以完全没有，也可以反复出现。让我们再看看《蝙蝠侠》的例子。

'''
batRegex = re.compile(r'Bat(wo)*man')
mo1 = batRegex.search('The Adventures of Batman')
mo1.group()
'Batman'

mo2 = batRegex.search('The Adventures of Batwoman')
mo2.group()
'Batwoman'

mo3 = batRegex.search('The Adventures of Batwowowoman')
mo3.group()
'Batwowowoman'

'''
对于'Batman'来说，regex的(wo)*部分匹配字符串中wo的零个实例；
对于'Batwoman'，(wo)*匹配wo的一个实例；对于'Batwowowoman'，(wo)*匹配wo的四个实例。

如果你需要匹配一个实际的星形字符，在正则表达式中的星形前加上一个反斜杠，*。

用加号匹配一个或多个
*表示 "匹配零或更多"，而+（或加号）表示 "匹配一个或更多"。与星号不同的是，星号不要求其组别出现在匹配的字符串中，
而加号前面的组别必须至少出现一次。它不是可选的。在交互式外壳中输入以下内容，并将其与上一节中的星形重码进行比较。
'''
batRegex = re.compile(r'Bat(wo)+man')
mo1 = batRegex.search('The Adventures of Batwoman')
mo1.group()
'Batwoman'

mo2 = batRegex.search('The Adventures of Batwowowoman')
mo2.group()
'Batwowowoman'

mo3 = batRegex.search('The Adventures of Batman')
mo3 == None
'True'

'''
重码Bat(wo)+man不会匹配字符串'The Adventures of Batman'，因为加号至少需要一个wo。

如果你需要匹配一个实际的加号字符，可以在加号前加一个反斜杠来转义。\+.

用大括号匹配特定的重复内容
如果你有一个组，你想重复特定的次数，在你的regex中用大括号跟着这个组的数字。
例如，重词(Ha){3}将匹配字符串'HaHaHa'，但它不会匹配'HaHa'，因为后者只有两个(Ha)组的重复次数。

你可以通过在大括号之间写一个最小值、一个逗号和一个最大值来指定一个范围，而不是一个数字。
例如，重词(Ha){3,5}将匹配'HaHaHa'、'HaHaHa'和'HaHaHa'。

你也可以省略大括号中的第一个或第二个数字，使最小或最大不受限制。
例如，(Ha){3,}将匹配三个或更多的(Ha)组实例，而(Ha){,5}将匹配零到五个实例。
大括号可以帮助你缩短正则表达式。这两个正则表达式匹配相同的模式。

(Ha){3}
(Ha)(Ha)(Ha)

而这两个正则表达式也匹配相同的模式。

(Ha){3,5}
((Ha)(Ha)(Ha))|((Ha)(Ha)(Ha))|((Ha)(Ha)))

输入以下内容。
'''

haRegex = re.compile(r'(Ha){3}')
mo1 = haRegex.search('HaHaHa')
mo1.group()
'HaHaHa'

mo2 = haRegex.search('Ha')
mo2 == None
'True'

'''
这里，(Ha){3}匹配'HaHaHa'但不匹配'Ha'。因为它不匹配'Ha'，所以 search() 返回 None。

贪婪匹配和非贪婪匹配
由于(Ha){3,5}可以匹配字符串'HaHaHaHa'中Ha的三个、四个或五个实例，你可能想知道为什么在前面的括号例子中，
Match对象对group()的调用返回'HaHaHaHa'而不是更短的可能性。毕竟，'HaHaHa' 和 'HaHaHa' 也是正则表达式
 (Ha){3,5}的有效匹配。

Python 的正则表达式默认是贪婪的，这意味着在模棱两可的情况下，它们会尽可能地匹配最长的字符串。非贪婪 (也叫懒惰) 
版本的大括号会匹配可能的最短字符串，它的收尾大括号后面是一个问号。

在交互式外壳中输入以下内容，注意搜索同一字符串的大括号的贪婪和非贪婪形式之间的区别。
'''
greedyHaRegex = re.compile(r'(Ha){3,5}')
mo1 = greedyHaRegex.search('HaHaHaHa')
mo1.group()
'HaHaHaHa'

nongreedyHaRegex = re.compile(r'(Ha){3,5}?' )
mo2 = nongreedyHaRegex.search('HaHaHaHa')
mo2.group()
'HaHaHa'

'''
请注意，问号在正则表达式中可以有两种含义：声明一个非贪婪的匹配或标记一个可选组。这些含义是完全不相关的。

findall()方法
除了search()方法，Regex对象还有一个findall()方法。search()将返回搜索字符串中第一个匹配文本的Match对象，
而findall()方法将返回搜索字符串中每个匹配的字符串。要了解search()如何只在第一个匹配文本的实例上返回一个Match对象，
请在交互式shell中输入以下内容。
'''
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('Cell: 415-555-9999 Work: 212-555-0000')
mo.group()
'415-555-9999'

'''
另一方面，findall()不会返回一个Match对象，而是一个字符串的列表--只要正则表达式中没有组。
列表中的每个字符串都是搜索到的与正则表达式匹配的一段文本。在交互式 shell 中输入以下内容。
'''
phoneNumRegex = re.compile(r'\d\d-\d\d-\d-\d\d\d') # 没有分组
phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
'''['415-555-9999', '212-555-0000']'''

'''
如果正则表达式中存在分组，那么findall()将返回一个元组列表。每个元组代表一个找到的匹配，其项目是正则表达式中每个
组的匹配字符串。要看findall()的操作，请在交互式shell中输入以下内容（注意，正在编译的正则表达式现在有括号内的组）。
'''
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d)-(\d\d\d)' ) #有组
phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
'''[('415', '555', '9999'), ('212', '555', '0000')]'''

'''
为了总结findall()方法的返回结果，请记住以下内容。

当对一个没有分组的regex进行调用时，例如\d\d-\d\d-\d-\d\d\d，findall()方法返回一个字符串匹配列表，
例如['415-555-9999', '212-555-0000']。
当对一个有分组的regex进行调用时，例如(\d\d\d)-(\d\d)-(\d\d)，findall()方法返回一个字符串的图元列表（
每组一个字符串），例如[('415', '555', '9999'), ('212', '555', '0000')]。

字符类
在前面的电话号码重组例子中，你了解到 \d 可以代表任何数字。也就是说，\d是正则表达式(0|1|2|3|4|5|6|7|8|9)的简写。
有许多这样的速记字符类，如表7-1所示。

表7-1：常见字符类的速记代码

速记字符类  代表

\d   从0到9的任何数字。

\D   任何不是0到9的数字的字符。

\w  任何字母、数字、或下划线字符。(将此视为匹配的 "单词 "字符）。

\W  任何不是字母、数字或下划线字符的字符。

\s  任何空格、制表符或换行符。(将此视为匹配 "空格 "字符。）

\S  任何不是空格、制表符或换行符的字符。

字符类是缩短正则表达式的好办法。
字符类 [0-5] 将只匹配 0 到 5 的数字；这比输入 (0|1|2|3|4|5) 要短得多。
注意，虽然 \d 匹配数字， \w 匹配数字、字母和下划线，但没有只匹配字母的速记字符类。
(虽然你可以使用[a-zA-Z]字符类，接下来会解释）。

例如，在输入以下内容。
'''
xmasRegex = re.compile(r'\d+\s\w+')

xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge')
'''
['12 drummers', '11 pipers', '10 lords', '9 ladies', '8 maids', '7 swans', '6
geese', '5 rings', '4 birds', '3 hens', '2 doves', '1 partridge']'''
'''
天鹅，6只鹅，5个环，4只鸟，3只母鸡，2只鸽子，1只鹧鸪' )
['12个鼓手'，'11个吹奏者'，'10个领主'，'9个女士'，'8个女仆'，'7只天鹅'，'6只
鹅'，'5环'，'4鸟'，'3母鸡'，'2鸽子'，'1鹧鸪']
'''
'''
正则表达式\d+\s\w+将匹配有一个或多个数字(\d+)，后面有一个空白字符(\s)，
后面有一个或多个字母/数字/下划线字符（\w+）的文本。
findall()方法在一个列表中返回regex模式的所有匹配字符串。

制作你自己的字符类
有些时候，你想匹配一组字符，但速记字符类（\d, \w, \s, 等等）过于宽泛。你可以用方括号定义你自己的字符类。
例如，字符类[aeiouAEIOU]将匹配任何元音，包括小写和大写。在交互式外壳中输入以下内容。
'''
vowelRegex = re.compile(r'[aeiouAEIOU]')
vowelRegex.findall('RoboCop eats baby food. BABY FOOD.')
'''['o', 'o', 'o', 'e', 'a', 'a', 'o', 'o', 'A', 'O', 'O']'''
'''
你也可以通过使用连字符包括字母或数字的范围。例如，字符类[a-zA-Z0-9]将匹配所有小写字母、大写字母和数字。

请注意，在方括号内，正常的正则表达式符号不会被解释成这样。这意味着你不需要用前面的反斜杠来转义.、*、？或（）字符。
例如，字符类[0-5.]将匹配数字0到5和一个句号。你不需要把它写成[0-5\.]。

通过在字符类的开头括号后放置一个托号字符（^），你可以创建一个负字符类。一个负的字符类将匹配所有不在该字符类中的字符。
例如，在交互式外壳中输入以下内容。

'''
consonantRegex = re.compile(r'[^aeiouAEIOU]' )
consonantRegex.findall('RoboCop eats baby food. BABY FOOD.')
'''['R', 'b', 'C', 'p', '', 't', 's', '', 'b', 'y', '', 'f', 'd', ' 
', 'b', 'b', 'y', ' ', 'f', 'd', '. '] '''
'''
现在，我们不再匹配每个元音，而是匹配每个不是元音的字符。

逗号和美元符号字符
你也可以在一个词组的开头使用圆点符号（^）来表示匹配必须发生在被搜索文本的开头。
同样，你也可以把美元符号($)放在搜索结果的末尾，表示字符串必须以该搜索模式结束。
你还可以把^和$放在一起，表示整个字符串必须与该词组相匹配--也就是说，仅仅在字符串的某个子集上进行匹配是不够的。

例如，r'^Hello'正则表达式字符串匹配以'Hello'开头的字符串。在交互式外壳中输入以下内容。
'''
beginsWithHello = re.compile(r'^Hello')
beginsWithHello.search('Hello, world!')
#<re.Match对象; span=(0, 5), match='Hello'>。
beginsWithHello.search('He said hello.') == None
'True'

'''
r'\d$'正则表达式字符串匹配以0到9的数字字符结尾的字符串。在交互式外壳中输入以下内容。
'''

endsWithNumber = re.compile(r'\d$')
endsWithNumber.search('Your number is 42')
# <re.Match对象; span=(16, 17), match='2'>。
endsWithNumber.search('你的号码是四十二') == None
'True'

'''
r'^\d+$'正则表达式字符串匹配以一个或多个数字字符开始和结束的字符串。在交互式外壳中输入以下内容。
'''
wholeStringIsNum = re.compile(r'^\d+$')
wholeStringIsNum.search('1234567890')
#<re.Match对象; span=(0, 10), match='1234567890'>
wholeStringIsNum.search('12345xyz67890') == None
'True'
wholeStringIsNum.search('12 34567890') == None
#True

'''
前面的交互式shell例子中的最后两个search()调用演示了如果使用^和$，整个字符串必须与regex匹配。
我总是混淆这两个符号的含义，所以我使用记忆法 "胡萝卜要花钱 "来提醒自己，圆点在先，美元符号在后。

通配符字符
正则表达式中的.（或点）字符被称为通配符，可以匹配除换行之外的任何字符。例如，在交互式外壳中输入以下内容。
'''
atRegex = re.compile(r'.at')
atRegex.findall('The cat in the hat sat on the flat mat.')
'''['猫', '帽子', '坐', '纬', '垫子']'''

'''
请记住，点字符将只匹配一个字符，这就是为什么在前面的例子中，对文本flat的匹配只匹配lat。要匹配一个真正的点，
请用反斜杠转义点。\..

用Dot-Star匹配一切
有时，你想匹配所有的东西和任何东西。例如，假设你想匹配字符串 "First Name:"，后面是任何和所有的文本，
后面是 "Last Name:"，然后再后面是任何东西。你可以用点星（.*）来代替 "任何东西"。
记住，点字符意味着 "除换行外的任何单个字符"，而星字符意味着 "前面字符的零或更多"。

'''

nameRegex = re.compile(r'First Name: (.*) Last Name:(.*)')
mo = nameRegex.search('First Name: Al Last Name: Sweigart')
mo.group(1)
'Al'
mo.group(2)
'Sweigart'

'''
dot-star使用贪婪模式。它总是试图尽可能多地匹配文本。要以非贪婪方式匹配任何和所有文本，
可以使用点、星和问号 (.*?)。和大括号一样，问号告诉 Python 以非贪婪的方式进行匹配。

在交互式 shell 中输入以下内容，看看贪婪和非贪婪版本之间的区别。
'''
nongreedyRegex = re.compile(r'<.*?>')
mo = nongreedyRegex.search('<To serve man> for dinner.>')
print(mo.group())
# <To serve man>


greedyRegex = re.compile(r'<.*>')
mo = greedyRegex.search('<To serve man> for dinner.>')
print(mo.group())
# <To serve man> for dinner.>


'''
这两个词组大致上都翻译为 "匹配一个开头的角括号，后面是任何东西，后面是一个结尾的角括号"。
但是字符串'<To serve man> for dinner.>'有两个可能匹配的结尾角括号。
在 regex 的非贪婪版本中，Python 匹配最短的字符串：'<To serve man>'。在贪婪版本中，
Python 匹配最长的字符串：'<To serve man> for dinner.>'。

用点字符匹配换行符
点星将匹配除换行之外的所有内容。通过将 re.DOTALL 作为 re.compile() 的第二个参数，你可以使点字符匹配所有字符，包括换行符。

在交互式外壳中输入以下内容。
'''

noNewlineRegex = re.compile('.*')
noNewlineRegex.search('Serve the public trust.\nProtect the innocent.Uphold the law.').group()
#'Serve the public trust.'


newlineRegex = re.compile('.*', re.DOTALL)
newlineRegex.search('Serve the public trust.\nProtect the innocent.uphold the law.').group()
'Serve the public trust.\nProtect the innocent.\nUphold the law'

'''
regex noNewlineRegex，在创建它的re.compile()调用中没有传递re.DOTALL，它将只匹配到第一个换行字符的所有内容，
而newlineRegex，在re.compile()中传递了re.DOTALL，它匹配所有内容。
这就是为什么newlineRegex.search()调用会匹配整个字符串，包括其换行字符。

回顾Regex符号
这一章涵盖了很多符号，所以这里要快速回顾一下你所学到的基本正则表达式语法的内容。

? 匹配前面一组中的零或一个。
* 匹配前一组中的零个或多个。
+ 匹配前一组中的一个或多个。
{n} 准确地匹配前一组的n个。
{n,}匹配前一组中的n个或更多。
{,m}匹配前一组中的0到m。
{n,m}与前一组中的至少n和最多m相匹配。
{n,m}? 或 *? 或 +? 对前面的组进行非贪婪的匹配。
^spam表示字符串必须以spam开头。
spam$表示该字符串必须以spam结尾。
.匹配任何字符，除了换行字符。
\d, \w, 和 \s 分别匹配一个数字、单词或空格字符。
\D、\W和\S分别匹配除数字、单词或空格字符以外的任何字符。
[abc] 匹配括号内的任何字符（如a、b或c）。
[^abc] 匹配不在大括号内的任何字符。
不区分大小写的匹配
通常情况下，正则表达式以你指定的确切大小写来匹配文本。例如，下面的正则表达式匹配完全不同的字符串。
'''
regex1 = re.compile('RoboCop')
regex2 = re.compile('ROBOCOP')
regex3 = re.compile('RobOcop')
regex4 = re.compile('RobocOp')

'''
但有时你只关心字母的匹配，而不关心它们是大写还是小写。为了使你的regex对大小写不敏感，
你可以把re.IGNORECASE或re.I作为第二个参数传给re.compile()。在交互式shell中输入以下内容。
'''
robocop = re.compile(r'robocop', re.I)
robocop.search('RoboCop is part man, part machine, all cop.') .group()
'RoboCop'

robocop.search('ROBOCOP保护无辜者。').group()
'ROBOCOP'

robocop.search('艾尔，为什么你的编程书这么多地谈及robocop？').group()
'robocop'

'''
用sub()方法替换字符串
正则表达式不仅可以找到文本模式，还可以用新的文本来代替这些模式。
Regex对象的sub()方法被传递两个参数。第一个参数是一个用来替换任何匹配的字符串。第二个是正则表达式的字符串。
sub()方法返回一个应用了替换结果的字符串。

例如，在交互式外壳中输入以下内容。
'''
namesRegex = re.compile(r'Agent \w+')
namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.' )
'CENSORED把秘密文件给了CENSORED'

'''
有时你可能需要使用匹配的文本本身作为替换的一部分。在sub()的第一个参数中，你可以输入 \1, \2, \3, 以此类推，
意思是 "在替换中输入第1、2、3组的文本"。

例如，假设你想审查特工人员的名字，只显示他们名字的第一个字母。要做到这一点，你可以使用重词代理(\w)\w*，
并将r'1\****'作为第一个参数传给sub()。该字符串中的\1将被第1组即正则表达式的(\w)组所匹配的任何文本所替换。
'''
agentNamesRegex = re.compile(r'Agent (\w)\w*')
agentNamesRegex.sub(r'\1****', 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.')
#A****告诉C****，E****知道B****是双重间谍。'

'''
管理复杂的Regexes
如果你需要匹配的文本模式很简单，那么正则表达式就很好。但是，匹配复杂的文本模式可能需要冗长、复杂的正则表达式。
你可以通过告诉re.compile()函数忽略正则表达式字符串中的空格和注释来减轻这种情况。

这种 "verbose 模式 "可以通过传递变量 re.VERBOSE 作为 re.compile() 的第二个参数来启用。
现在，不再是像这样一个难以阅读的正则表达式了。
'''
phoneRegex = re.compile(r'((\d{3}|\(\d{3}\))?(\s|-|\.)?\d{3}(\s|-|\.)\d{4}(\s*(ext|x|ext.)\s*\d{2,5})?)')

'''
你可以用注释将正则表达式分散到多行，像这样:
'''
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?            # area code
    (\s|-|\.)?                    # separator
    \d{3}                         # first 3 digits
    (\s|-|\.)                     # separator
    \d{4}                         # last 4 digits
    (\s*(ext|x|ext.)\s*\d{2,5})?  # extension
    )''', re.VERBOSE)
'''
注意前面的例子是如何使用三引号语法（）来创建一个多行字符串的，这样你就可以把正则表达式的定义分散到许多行中，
使其更加清晰易读。

正则表达式字符串中的注释规则与 Python 正则代码相同：# 符号和它之后到行尾的所有内容都被忽略。另外，正则表达
式的多行字符串内的额外空格不被视为要匹配的文本模式的一部分。这可以让你组织正则表达式，使其更容易阅读。

结合使用 re.IGNORECASE、re.DOTALL 和 re.VERBOSE
如果你想使用 re.VERBOSE 在你的正则表达式中写入注释，但又想使用 re.IGNORECASE 忽略大写字母，怎么办？不幸的是，re.compile()函数只接受一个值作为其第二个参数。你可以通过使用管道字符（|）组合 re.IGNORECASE、re.DOTALL 和 re.VERBOSE 变量来绕过这个限制，管道字符在这里被称为位操作符（bitwise or）。

因此，如果你想要一个不区分大小写且包含换行符的正则表达式来匹配点字符，你可以这样形成你的re.compile()调用。
'''
someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL)
'''
在第二个参数中包括所有三个选项将看起来像这样。'''

someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL | re.VERBOSE)

'''
这种语法有点老套，起源于早期版本的 Python。比特运算符的细节超出了本书的范围，
但请查看 https://nostarch.com/automatestuff2/ 上的资源以获得更多信息。
你也可以为第二个参数传递其他选项；它们不常见，但你也可以在资源中读到更多关于它们的信息。

项目。电话号码和电子邮件地址提取器
假设你有一个无聊的任务，要在一个长的网页或文档中找到每一个电话号码和电子邮件地址。
如果你手动滚动页面，你可能最终会搜索很长时间。但是，如果你有一个程序可以在剪贴板中搜索电话号码和电子邮件地址，你可以简单地按CTRL-A选择所有文本，按CTRL-C将其复制到剪贴板，然后运行你的程序。它可以用它找到的电话号码和电子邮件地址替换剪贴板上的文本。
每当你要处理一个新的项目时，你可能很想立即投入到编写代码中去。但更多的时候，最好是退一步，考虑一下大局。我建议首先为你的程序需要做什么制定一个高层次的计划。先不要考虑实际的代码--你可以以后再担心这个问题。现在，要坚持大体上的计划。
例如，你的电话和电子邮件地址提取器将需要做以下工作。

从剪贴板上获取文本。
找到文本中的所有电话号码和电子邮件地址。
将它们粘贴到剪贴板上。
现在你可以开始考虑这在代码中如何工作。代码将需要做以下工作。


使用pyperclip模块来复制和粘贴字符串。
创建两个词组，一个用于匹配电话号码，另一个用于匹配电子邮件地址。
找到所有匹配的，而不仅仅是第一个匹配的，这两个词组。
将匹配的字符串整齐地格式化为一个单一的字符串来粘贴。
如果在文本中没有找到匹配项，则显示某种信息。
这个列表就像项目的路线图。当你编写代码时，你可以分别关注这些步骤中的每一步。每个步骤都是相当容易管理的，并以你已经知道如何在Python中做的事情来表达。

第1步：为电话号码创建一个Regex
首先，你必须创建一个正则表达式来搜索电话号码。创建一个新文件，输入以下内容，并将其保存为 phoneAndEmail.py
'''

#! python3
# phoneAndEmail.py - 查找剪贴板上的电话号码和电子邮件地址。

import pyperclip, re

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?                # area code
    (\s|-|\.)?                        # separator
    (\d{3})                           # first 3 digits
    (\s|-|\.)                         # separator
    (\d{4})                           # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?    # extension
    )''', re.VERBOSE)

# TODO: Create email regex.

# TODO: Find matches in clipboard text.

# TODO: Copy results to the clipboard.
# TODO: 创建电子邮件重码。
# TODO: 在剪贴板文本中查找匹配的内容.
# TODO: 复制结果到剪贴板。
'''

TODO注释只是程序的一个骨架。它们会在你编写实际代码时被替换掉。电话号码以一个可选的区号开始，所以区号组后面有一个问号。由于区号可以是三个数字（即：\d{3}）或括号内的三个数字（即：\(\d{3}\)），你应该有一个管道连接这些部分。你可以在多行字符串的这一部分添加regex注释#区域代码，以帮助你记住(\d{3}|(\d{3}\)?应该匹配什么。
电话号码的分隔符可以是空格（\s）、连字符（-）或句号（.），所以这些部分也应该用管道连接。正则表达式的后面几个部分很简单：三个数字，后面是另一个分隔符，后面是四个数字。最后一部分是一个可选的扩展，由任意数量的空格组成，后面是ext、x或ext.，然后是两到五个数字。
注意
含有小括号（ ）和转义小括号（ ）的正则表达式很容易被搞混。如果你得到一个 "缺少），未结束的子模式 "的错误信息，请记得仔细检查你使用的是正确的。
第2步：为电子邮件地址创建一个Regex
你还将需要一个可以匹配电子邮件地址的正则表达式。让你的程序看起来像下面这样。
'''
#! python3
# phoneAndEmail.py - 查找剪贴板上的电话号码和电子邮件地址。

import pyperclip, re

#phoneRegex = re.compile(r'''(--snip--))

# Create email regex.
emailRegex = re.compile(r'''(
      [a-zA-Z0-9._%+-]+      # ➊ username
       @                      # ➋ @ symbol
      [a-zA-Z0-9.-]+         # ➌ domain name
        (\.[a-zA-Z]{2,4})       # dot-something
        )''', re.VERBOSE)

# TODO: Find matches in clipboard text.

# TODO: Copy results to the clipboard.

# TODO: 在剪贴板文本中查找匹配的内容。

# TODO: 复制结果到剪贴板。
'''
电子邮件地址的用户名部分
➊是一个或多个字符，可以是以下任何一种：小写和大写字母、数字、一个点、下划线、百分号、加号或连字符。你可以把所有这些放到一个字符类中。[a-zA-Z0-9._%+-]。

域名和用户名用@符号➋分开。域名➌有一个稍微不那么允许的字符类，只有字母、数字、句号和连字符：[a-zA-Z0-9.-]。最后是 "dot-com "部分（技术上被称为顶级域名），它实际上可以是dot-anything。这是在两到四个字符之间。

电子邮件地址的格式有很多奇怪的规则。这个正则表达式不会匹配所有可能的有效电子邮件地址，但它会匹配你遇到的几乎所有典型的电子邮件地址。

第3步：查找剪贴板文本中的所有匹配项
现在你已经为电话号码和电子邮件地址指定了正则表达式，你可以让 Python 的 re 模块做艰苦的工作，在剪贴板上找到所有匹配的内容。pyperclip.paste() 函数将得到剪贴板上文本的一个字符串值，findall() regex 方法将返回一个图元列表。

让你的程序看起来像下面这样。
'''

# ! python3
# phoneAndEmail.py - Finds phone numbers and email addresses on the clipboard.

import pyperclip, re

#phoneRegex = re.compile(r'''(      --snip--

  # Find matches in clipboard text.
text = str(pyperclip.paste())

matches = []  #➊
for groups in phoneRegex.findall(text):  #➋
      phoneNum = '-'.join([groups[1], groups[3], groups[5]])
      if groups[8] != '':
          phoneNum += ' x' + groups[8]
      matches.append(phoneNum)
for groups in emailRegex.findall(text):   #➌
      matches.append(groups[0])

# TODO: Copy results to the clipboard.
# 在剪贴板文本中查找匹配的内容。
text = str(pyperclip.paste())

# TODO: 复制结果到剪贴板。

'''
每个匹配都有一个元组，每个元组包含正则表达式中每个组的字符串。记住，第0组匹配整个正则表达式，所以元组中索引为0的组是你感兴趣的组。

正如你在➊看到的那样，你将在一个名为 matches 的列表变量中存储匹配的内容。
它开始时是一个空的列表，和几个for循环。对于电子邮件地址，你把每个匹配的0组追加到➌。
对于匹配的电话号码，你不想只附加第0组。虽然程序检测到了几种格式的电话号码，你希望附加的电话号码是单一的、标准的格式。
phoneNum变量包含一个由匹配的文本➋的1、3、5和8组构建的字符串。(这些组是区号、前三位数字、后四位数字和分机号码）。

第4步：将匹配的内容连接成一个字符串，用于剪切板
现在你有了电子邮件地址和电话号码作为匹配的字符串列表，你想把它们放在剪贴板上。pyperclip.copy()函数只接受一个单一的字符串值，而不是一个字符串列表，所以你对matches调用join()方法。

为了更容易看出程序在工作，让我们把你找到的任何匹配信息打印到终端。如果没有找到电话号码或电子邮件地址，程序应该告诉用户这一点。

让你的程序看起来像下面这样。
'''
#! python3
# phoneAndEmail.py - 查找剪贴板上的电话号码和电子邮件地址。

#--snip--
for groups in emailRegex.findall(text):
    matches.append(groups[0])
# 复制结果到剪贴板上。

# Copy results to the clipboard.
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')
'''
运行该程序
举个例子，打开你的网络浏览器，进入No Starch Press的联系页面
https://nostarch.com/contactus/，按CTRL-A选择页面上的所有文本，然后按CTRL-C将其复制到剪贴板。
当你运行这个程序时，输出结果会是这样的。

复制到剪贴板
800-420-7240
415-863-9900
415-863-9950
info@nostarch.com
media@nostarch.com
academic@nostarch.com
info@nostarch.com
'''

#类似程序的想法
'''
识别文本的模式（并可能用sub()方法替代它们）有许多不同的潜在应用。例如，你可以

查找以http:// 或https:// 开始的网站URL。
清理不同日期格式的日期（如3/14/2019、03-14-2019和2015/3/19），用单一的、标准格式的日期替换它们。
删除敏感信息，如社会安全号或信用卡号。
查找常见的错别字，如单词之间的多个空格，不小心重复的单词，或句子末尾的多个感叹号。这些都是令人讨厌的！!
总结
虽然计算机可以快速搜索文本，但必须准确地告诉它要寻找什么。正则表达式允许你指定你要寻找的字符模式，而不是准确的文本本身。事实上，一些文字处理和电子表格应用程序提供了查找和替换功能，允许你使用正则表达式进行搜索。
Python 自带的 re 模块可以让你编译 Regex 对象。这些对象有几个方法：search()用于查找单个匹配项，findall()用于查找所有匹配的实例，sub()用于对文本进行查找和替换的替换。
你可以在官方的Python文档中找到更多信息，网址是https://docs.python.org/3/library/re.html。另一个有用的资源是教程网站https://www.regular-expressions.info/。

练习题
1. 创建Regex对象的函数是什么？

2. 为什么在创建Regex对象时经常使用原始字符串？

3. search()方法的返回结果是什么？

4. 如何从Match对象中获得符合模式的实际字符串？

5. 在由r'(\d\d)-(\d\d-\d\d)'创建的regex中，0组包括什么？第1组？第2组？

6. 在正则表达式语法中，括号和句号有特定的含义。你如何指定你想让一个正则表达式匹配实际的括号和句号字符？

7. findall()方法返回一个字符串的列表或一个字符串的图元的列表。是什么让它返回一个或另一个？

8. |字符在正则表达式中表示什么？

9. 在正则表达式中，"？"字符表示哪两件事？

10. 正则表达式中的+和*字符有什么区别？

11. 正则表达式中的{3}和{3,5}有什么区别？

12. 正则表达式中的 \d, \w, 和 \s 速记字符类表示什么？

13. 在正则表达式中， \D, \W, 和 \S 速记字符类表示什么？

14. .*和.*之间有什么区别？

15. 匹配所有数字和小写字母的字符类语法是什么？

16. 如何使正则表达式不区分大小写？


17. .字符通常匹配什么？如果re.DOTALL作为re.compile()的第二个参数被传递，它将匹配什么？

18. 如果numRegex = re.compile(r'\d+')，numRegex.sub('X', '12 drummers, 11 pipers, five rings, 3 hens')会返回什么？

19. 将re.VERBOSE作为re.compile()的第二个参数允许你做什么？

20. 你如何写一个匹配每三位数都有逗号的数字的regex？它必须匹配以下内容。

'42'
'1,234'
'6,368,745'
但不能匹配以下内容。

'12,34,567'（逗号之间只有两个数字）。
'1234'（其中缺少逗号）

21. 你将如何写一个匹配全名为Watanabe的人的重码？你可以假设前面的第一个名字总是以大写字母开头的一个词。
这个词组必须匹配以下内容。

'Haruto Watanabe'
'Alice Watanabe'
'RoboCop Watanabe'

but not the following:

'haruto Watanabe' (where the first name is not capitalized)
'Mr. Watanabe' (where the preceding word has a nonletter character)
'Watanabe' (which has no first name)
'Haruto watanabe' (where Watanabe is not capitalized)

但不能匹配以下内容
'Haruto Watanabe'（其中名字没有大写）。
'Watanabe先生'（前面的词有一个非字母字符的地方）
'Watanabe'（其中没有名字）
'Haruto watanabe'（其中Watanabe未被大写）。


22. 你如何写一个词条来匹配一个句子，其中第一个词是Alice, Bob, 或Carol；第二个词是eats, pets, 或throws；
第三个词是apples, cats, 或baseballs；并且句子以句号结束？这个重构词应该是不区分大小写的。它必须匹配以下内容。

'Alice eats apples.'
'Bob pets cats.'
'Carol throws baseballs.'
'Alice throws Apples.'
'BOB EATS CATS.'
but not the following:

'RoboCop eats apples.'
'ALICE THROWS FOOTBALLS.'
'Carol eats 7 cats.'

'Alice吃苹果'。
'鲍勃养猫'。
'卡罗尔投掷棒球'。
'爱丽丝扔苹果'。
'Bob吃猫'。
但不包括以下内容。

'机械战警吃苹果'。
'爱丽丝投掷脚球'。
'卡罗尔吃7只猫'。

练习项目
为了练习，编写程序来完成以下任务。

日期检测
编写一个可以检测DD/MM/YYYY格式的日期的正则表达式。
假设日从01到31，月从01到12，年从1000到2999。注意，如果日或月是一个数字，它将有一个前导零。

正则表达式不需要检测每个月或闰年的正确日期；它可以接受不存在的日期，如31/02/2020或31/04/2021。
然后将这些字符串存储到名为月、日和年的变量中，并编写额外的代码来检测它是否是一个有效的日期。
四月、六月、九月和十一月有30天，二月有28天，其余月份有31天。闰年的二月有29天。闰年是指每一个能被4整除的年份，
除了能被100整除的年份，除非该年也能被400整除。
请注意，这种计算方式使得我们不可能做出一个合理大小的正则表达式来检测一个有效的日期。

强密码检测
编写一个函数，使用正则表达式来确保传递给它的密码字符串是强密码。
一个强密码被定义为至少有8个字符长，包含大写和小写字符，并且至少有一个数字。
你可能需要用多个重码模式来测试该字符串，以验证其强度。

Regex strip() 方法
编写一个函数，接收一个字符串，做与 strip() 字符串方法相同的事情。
如果除了要剥离的字符串外没有传递其他参数，那么将从字符串的开头和结尾处删除空白字符。
否则，函数的第二个参数中指定的字符将被从字符串中删除。

'''