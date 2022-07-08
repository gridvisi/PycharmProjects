# https://www.gairuo.com/p/pandas-data-modification

# https://blog.csdn.net/toshibahuai/article/details/79034829

'''
path_or_buf=None 字符串或文件目录，文件路径或对象，如果未提供，结果将作为字符串返回。如果传递了一个文件对象，应该用换行= ’ '，禁用通用换行符。

sep=’,’ 输出文件的字段分隔符,默认点

na_rep=’’,缺失数据填充

float_format=None，小数点保留几位

columns=None, 要写入的字段

header=True，列名的别名

index=True,写行名(索引)

index_label=None，索引列的列标签。如果没有给出，并且header和index为True，则使用索引名。
如果对象使用多索引，应该给出一个序列。如果不打印索引名称的字段。使用index _ label = Falser以便在R中更容易导入

mode=‘w’ 写入模式，默认为w，
r : 只能读, 必须存在, 可在任意位置读取

w : 只能写, 可以不存在, 必会擦掉原有内容从头写

a : 只能写, 可以不存在, 必不能修改原有内容, 只能在结尾追加写, 文件指针无效

r+ : 可读可写, 必须存在, 可在任意位置读写, 读与写共用同一个指针

w+ : 可读可写, 可以不存在, 必会擦掉原有内容从头写

a+ : 可读可写, 可以不存在, 必不能修改原有内容, 只能在结尾追加写, 文件指针只对读有效 (写操作会将文件指针移动到文件尾)

encoding=None , 表示输出文件中使用的编码的字符串，默认为“utf-8”

一、编码方式不同UTF-8编码采用的是一种多字节编码，在英文中8位代表一个字节，而中文字是24位代表一个字节。
而GBK编码方式都是通过双字节来表达，不管文字是英文还是中文字符都是一概而论，当然在区分中文的时候，会定位最高位为1。

二、UIF-8及GBK的兼容性这两种编码都是系统的字符编码，GBK是在国家标准GB2312基础上扩容后兼容GB2312的标准,
UTF-8编码的文字可以在各国各种支持UTF8字符集的浏览器上显示。

也就是说如果你的网站使用的是UTF-8编码，在国外观看你的网站浏览器上就会帮你切换到中文状态，而使用GBK编码的话，
在国外浏览网页就必须要下载中文语言支持包，如果没有下载就会出现乱码的现象。
三、UIF-8好还是GBK编码好？UTF-8在英文站点中所占用的字节是1个字节，而GBK编码所占用的是2个字节，这样如果是
在英文网站或者你的网站英文字符过多的话，建议使用UTF-8编码，这样能节省一些空间。
对于中文比较多的论坛 ，使用GBK则每个字符占用2个字节，而使用UTF－8中文却只占3个字节。可以采用GBK版本，但是
UIF-8在所以浏览器都能正常显示，而GBK可能有些浏览器会有不兼容的现象，所以根据实际情况来衡量网站到底使用哪种编码。

compression=‘infer’ 如果是字符串，表示压缩模式。如果为dict，则’ method '处的值是压缩模式。压缩模式可以
是以下任何可能的值:{ ’ infer ‘，’ gzip ‘，’ bz2 ‘，’ zip ‘，’ xz ‘，’ None}。如果压缩模式是“推断”和
path_or_buf类似于路径，则从以下扩展中检测压缩模式:“”。gz ‘，. bz2 ‘，’。zip’ or '。xz’。(否则不压缩)。
如果给定的dict和模式是{‘zip ‘，’ gzip ‘，’ bz2’}之一，或根据上述推断，则其他条目作为附加压缩选项传递

quoting=None, 默认为to csv.QUOTE_MINIMAL。如果你设置了一个浮点格式(_ f)然后浮点被转换成字符串，从而
转换成csv.QUOTE_MINIMALl将会将它们视为非数字

quotechar=’"’ 用于引用字段的字符

line_terminator=None 输出文件中使用的换行符或字符序列。默认为os.linesep，这取决于调用此方法的操作系统
(例如，对于linux为“n”，对于Windows为“rn”)

chunksize=None 一次写入行

date_format=None , 日期时间对象的格式字符串

doublequote=True, 引用路径在双引号内

escapechar=None, 用于转义的字符

decimal=’.’, 识别为十进制分隔符的字符

errors=‘strict’ 指定如何处理编码和解码错误
————————————————
版权声明：本文为CSDN博主「潘棋林」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/weixin_50220061/article/details/109232688


df.to_csv("test.csv",encoding='utf-8',index=False)

在后面加上index = False即可

Write DataFrame to a comma-separated values (csv) file

Parameters:
path_or_buf : string or file handle, default None

File path or object, if None is provided the result is returned as a string.

文件路径或对象，如果没有提供，则结果将作为字符串返回

sep : character, default ‘,’

Field delimiter for the output file.

输出文件的字段分隔符。

na_rep : string, default ‘’

Missing data representation

缺失数据表示

float_format : string, default None

Format string for floating point numbers

浮点数的转为字符串

columns : sequence, optional

Columns to write

要写的列

header : boolean or list of string, default True

Write out the column names. If a list of strings is given it is assumed to be aliases for the column names

写出列名。如果给出了字符串列表，则假定它是列名的别名

index : boolean, default True

Write row names (index)

写行名（索引）

index_label : string or sequence, or False, default None

Column label for index column(s) if desired. If None is given, and header and indexare True, then the index names are used. A  sequence should be given if the DataFrame uses MultiIndex. If False do not print fields for index names. Use index_label=False for easier importing in R

索引列的列标签（如果需要）。如果给出None，并且header和index为True，则使用索引名称。如果DataFrame使用MultiIndex，则应该给出一个序列。如果为False，则不输出索引名称的字段。使用index_label = False可以更轻松地导入R

mode : str

Python write mode, default ‘w’

写的模式：str

encoding : string, optional

A string representing the encoding to use in the output file, defaults to ‘ascii’ on Python 2 and ‘utf-8’ on Python 3.

表示要在输出文件中使用的编码的字符串，默认为Python 2上的“ascii”和Python 3上的“utf-8”。

compression : string, optional

A string representing the compression to use in the output file.
Allowed values are ‘gzip’, ‘bz2’, ‘zip’, ‘xz’.
This input is only used when the first argument is a filename.

表示要在输出文件中使用的压缩的字符串。允许的值为'gzip'，'bz2'，'zip'，'xz'。
仅当第一个参数是文件名时才使用此输入

line_terminator : string, default '\n'

The newline character or character sequence to use in the output file

要在输出文件中使用的换行符或字符序列

quoting : optional constant from csv module

defaults to csv.QUOTE_MINIMAL. If you have set a float_format then floats are converted to strings and thus csv.QUOTE_NONNUMERIC will treat them as non-numeric

quotechar : string (length 1), default ‘”’

character used to quote fields

doublequote : boolean, default True

Control quoting of quotechar inside a field

escapechar : string (length 1), default None

character used to escape sep and quotechar when appropriate

chunksize : int or None

rows to write at a time

tupleize_cols : boolean, default False

Deprecated since version 0.21.0: This argument will be removed and will always write each row of the multi-index as a separate row in the CSV file.

Write MultiIndex columns as a list of tuples (if True) or in the new, expanded format, where each MultiIndex column is a row in the CSV (if False).

date_format : string, default None

Format string for datetime objects

decimal: string, default ‘.’

Character recognized as decimal separator. E.g. use ‘,’ for European data
————————————————
版权声明：本文为CSDN博主「一只可爱的栗子」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/weixin_38987362/article/details/81327011
import pickle
coding='gbk'
# -*- coding:utf-8 -*-
# -*- coding: gbk -*-

'''

import pprint
import pandas as pd

# 定义表1
books_url = "I:\\data_science\\bookmis\\books.csv"
#books_header = ["书号", "书名", "出版社", "作者", "价格", "库存"]
books_header = ['bookid','booth','status','bname','publish','aurtor','price','number']
#books_header = ['book.No','bname','publish','aurtor','price','number']


# 定义表2
users_url = "I:\\data_science\\bookmis\\users.csv"
#users_header = ["会员号", "姓名", "性别", "会员年度"]
user_header = ['userid','name','gender', 'cell','expdate','credit','status']

# 定义表3
log_url = "I:\\data_science\\bookmis\\log.csv"
#log_header = ["会员号", "书号", "借阅日期"]
log_header = ['userid', 'bookid', 'date']



#csv_file = "I:\\data_science\\bookmis\\table1.csv"
csv_file = "I:\\data_science\\bookmis\\books.csv"
csv_data = pd.read_csv(csv_file, low_memory=False,encoding ="gbk")  # 防止弹出警告
csv_df = pd.DataFrame(csv_data,index=None)
bookdf = csv_df   #.drop([''],axis=1,inplace=True)
last = len(bookdf)
print(f"----------- {len(bookdf)} ---------------")
pprint.pprint(bookdf)
new = ['83', 'H','0','哈利波特', '儿童', 'J.K.罗琳', '30', '2']
# df2 = bookdf.append(new)
# print(df2)

bookdf.loc[last] = new
# print(bookdf)

print(f"{bookdf.loc[last][:]}******添加成功 ！********")

# https://peps.python.org/pep-0263/
bookdf.to_csv("I:\\data_science\\bookmis\\books.csv",encoding ="gbk",index=False)
print(bookdf)
# stock = csv_df.to_dict()


