#1 https://zhuanlan.zhihu.com/p/144256955
#1-1 pandas基本操作
# https://www.zhihu.com/question/57792219
# Pandas 筛选数据的 8 个骚操作
# https://zhuanlan.zhihu.com/p/415399590


#2 pickle
# https://zhuanlan.zhihu.com/p/196721208

# https://www.codenong.com/18171739/
'''

with open(self.bookpick, 'ab') as f:
    pickle.dump(book, f)
    # pickle.dump('pickle_data4', f)
'''

#3
#收藏！Python内置的轻量级数据库竟如此好用！全网最实用sqlite3实战项目

#性能对比
# https://h2oai.github.io/db-benchmark/


#轻松玩转 exel视频
# https://www.zhihu.com/zvideo/1297958821189873664
# Pandas快速入门系列1：初识、基本数据结构、读取和存储表格数据
# https://www.zhihu.com/zvideo/1436332872697901056

'''
当我们学习Python的时候，肯定避免不了与数据打交道，而提及数据，大部分人都会想起Python数据存储，
那么你知道Python常用的数据存储方式有哪些?我们一起来看看这五种存储方式吧。

1. json文件存储数据

json是一种轻量级的数据交换格式，采用完全独立于编程语言的文本格式来存储和表示数据，可以轻松解决py2和py3的编码问题，
内容结构类似于python中的字典和列表，层次结构简洁而清晰，易于人阅读和编写，同时也易于机器解析和生成，并有效地提升网络传输效率。

2. csv文件

Python可以将数据存储为CSV文件格式，我们可以用excel打开CSV文档，进行数据的浏览，十分方便。

3. MySQL数据库

MySQL数据库存储方式是使用Python数据存储最常用的存储方式，Python标准数据库接口为Python DB-API，
Python DB-API为开发人员提供了数据库应用程序接口，MySQLdb 是用于Python链接Mysql数据库的接口。
MySQL数据库存储过程是引入API模块、获取与数据库的连接、执行SQL语句和存储过程，最后关闭数据库连接。

4. Redis数据库

使用Python数据存储为Redis数据库，优点是方便、速度快，但是取出的数据是二进制数据，一般需要转为字符串再操作。

5. Mongdb数据库

使用Python数据存储为Mongdb数据库，优点是不在乎数据结构，需要注意的是取出来的时候需要写个脚本整理一下。
————————————————
版权声明：本文为CSDN博主「闵科夫斯基」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/weixin_29189377/article/details/113561250



import sys
reload(sys)
sys.setdefaultencoding('gbk')

刚刚遇到同样的问题，在网上找了很久，使用如下代码可以完美解决此问题：
all_data = pd.read_csv(file_name, encoding='ISO-8859-1', nrows=10)
你的错误提示为：UnicodeDecodeError: 'utf-8' codec can't decode byte 0x87 in position 1: invalid start byte而ISO-8859-1的编码范围是0x00-0xFF，所以这个解决方案应该适用。

作者：南雁
链接：https://www.zhihu.com/question/59902773/answer/373789751
来源：知乎
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
# https://docs.python.org/3/library/pickle.html

#coding:utf-8
import pandas as pd
import pickle

# 定义表一
books_url = "I:\\data_science\\bookmis\\books.csv"
#books_header = ["书号", "书名", "出版社", "作者", "价格", "库存"]
books_header = ['bookid','booth','status','bname','publish','aurtor','price','number']
# 定义表二
log_url = "I:\\data_science\\bookmis\\log.csv"
log_header = ["会员号", "书号", "借阅日期"]
# 定义表三
users_url = "I:\\data_science\\bookmis\\users.csv"
users_header = ["会员号", "姓名", "性别", "会员年度"]


csv_file = "I:\\data_science\\bookmis\\table1.csv"
csv_data = pd.read_csv(csv_file, low_memory=False)  # 防止弹出警告
csv_df = pd.DataFrame(csv_data)
bookdf = csv_df
stock = csv_df.to_dict()
print(bookdf)




import csv
import pickle
import pandas as pd





class Path(object):
    # 书的描述来源和存储定义表-1
    books_url = "I:\\data_science\\bookmis\\books.csv"
    #books_header = ["书号", "书名", "出版社", "作者", "价格", "库存"]
    books_header = ['bookNo', 'booth', 'status', 'bname', 'publish', 'aurtor', 'price', 'number']

    # 会员书架来源和存储定义表-2
    users_url = "I:\\data_science\\bookmis\\users.csv"
    users_header = ['userid', 'name', 'gender', 'cell', 'expdate', 'credit', 'status']

    # 流水日记账目 定义表-3
    log_url = "I:\\data_science\\bookmis\\log.csv"
    log_header = ['userid', 'bookid', 'date']

class Bookmis(object):
    def __init__(self):
        print("系统初始化，提取图书、会员和日志库...")
        # self.input_books_users()
        self.loadpick()
        self.book_table, self.users_table, self.log_table = self.get_pd_pattern()
        self.bookpick,self.userpick,self.logpick = self.loadpick()
        print("图书馆系统初始化完成！\n")
        self.menu()

    def loadpick(self):
        # 书籍定义表-1
        #books_url = "I:\\data_science\\bookmis\\books.csv"
        # books_header = ["书号", "书名", "出版社", "作者", "价格", "库存"]
        # csv_file = "I:\\data_science\\bookmis\\books.csv"
        bookcsv_pd = pd.read_csv(Path.books_url,encoding="gbk")  # 防止弹出警告
        bookpd_df = pd.DataFrame(bookcsv_pd)
        bookpick = pickle.dumps(bookpd_df)

        #stock = book_df.to_dict()
        print(bookpd_df)
        #self.bookpick = pickle.dumps(bookdf)

        # 会员书架来源和存储定义表-2
        #users_url = "I:\\data_science\\bookmis\\users.csv"
        # users_header = ["会员号", "姓名", "性别","手机号码","" "会员年度"]

        usercsv_pd = pd.read_csv(Path.users_url, low_memory=False)  # 防止弹出警告
        userpd_df = pd.DataFrame(usercsv_pd)
        userpick = pickle.dumps(userpd_df)
        # userfile = pd.read_pickle(userdata)
        # print(userfile)
        #print('会员库：',userpick)

        # 流水日记账目 定义表-3
        #log_url = "I:\\data_science\\bookmis\\log.csv"
        # log_header = ["会员号", "书号", "借阅日期"]
        logcsv_pd = pd.read_csv(Path.log_url,low_memory=False, encoding ="utf-8")  # 防止弹出警告
        logpd_df = pd.DataFrame(logcsv_pd)
        logpick = pickle.dumps(logpd_df)
        return bookpick,userpick,logpick

    def updateBook(self):
        print("录入新书信息,请按以上顺序输入字符串，每项之间以空格隔开:")
        bookdf = pd.DataFrame(self.book_table, index=None)
        last = len(bookdf)
        print(f"书库最后一条记录是：{len(bookdf)}, {bookdf.iloc[-1]}")
        print(f"下一个bookid输入:{last}")
        print("'bookid', 'booth', 'status', 'bname', 'publish', 'aurtor', 'price', 'number'")
        book = input(":")

        # 84 A 1 红与黑 中信 司汤达 40 3
        # 86 B 0 哈利波特 儿童 J.K.罗琳 30 2
        book = book.split(" ")
        #print(book)

        bookdf.loc[last] = book
        #print(bookdf.iloc[-1:])
        bookdf.to_csv("I:\\data_science\\bookmis\\books.csv", encoding="gbk", index=False)
        print(f"添加{bookdf.iloc[-1:]} \n 位于  {bookdf.iloc[-1:]['booth']}")
        #bookdict = self.book_table.to_dict()
        #print(bookdict)



        '''
        file = open(self.bookpick,'wb')
        pickle.dump(book,file)
        file.close()
        
        with open(self.bookpick,'wb') as f:
            pickle.dumps(book,f)
        
        
              rows_list = book
        for row in rows:
            rows_dict = {}
            rows_dict.update(row)
            rows_list.append(rows_dict)
        df = pd.DataFrame(rows_list)

        '''
    #"ISO-8859-1"
    #"utf-8"

    def get_pd_pattern(self):
        book_table = pd.read_csv(Path.books_url, low_memory=False,encoding ="gbk")
        users_table = pd.read_csv(Path.users_url, low_memory=False,encoding ="utf-8")
        log_table = pd.read_csv(Path.log_url, low_memory=False,encoding ="utf-8")
        print("信息读取成功...")
        #print(" book_table 信息\n " ,book_table['库存'][3])
        return book_table, users_table,log_table

    def save_file(self):

        self.book_table.to_csv(Path.books_url, header=Path.books_header, index=None)
        self.book_table.to_csv(Path.books_url, header=Path.books_header, index=None)
        boo = pd.DataFrame(self.log_table)
        boo.to_csv(Path.log_url, header=Path.log_header, index=False)
        self.users_table.to_csv(Path.users_url, header=Path.users_header, index=None)
        print("保存文件成功")

    def menu(self):
        print("**** 图书管理菜单 **** ")
        print("存Pickle数据to csv选择 1：")
        print("添加新书 选择 2：")
        print("添加新会员 选择 3：")
        print("存数据to csv选择 4：")

        op = input("你的选择 ：")
        if op == '1':
            Bookmis.get_pd_pattern(self)
            return self.menu()
        elif op == '2':
            Bookmis.updateBook(self)

        elif op == '3':
            Bookmis.updateuser(self)
        elif op == '4':
            Bookmis.save_file(self)
            return self.menu()

print(Path.books_url)

if __name__ == '__main__':
    booksys = Bookmis()


#C:\Users\29358\PycharmProjects\BooktinyMis\csv_training
'''

def gen_csv_file(file_name):
    csv_file = open(file_name, 'a+', encoding="utf-8", newline='')
    csv_writer = csv.writer(csv_file, dialect="excel")
    csv_headers = ['city', 'name', 'salary', 'telephone', 'create_time']

    # 判断csv第一行是否有数据，没有则增加头部字段名
    if csv_file.tell() == 0:
        csv_writer.writerow(csv_headers)

    # 写入测试数据
    csv_writer.writerows([
        ['广州', '张三', '4000.321', '85113246', '2018/09/11'],
        ['深圳', '里斯', '5121.3344', '', '2011/07/12'],
        ['上海', '老王', '6666.000', '暂无', '2000/04/14'],
        ['深圳', '乔四', '10000.00', '1245 3342', '2018/09/01'],
        ['佛山', '天天', '5450', '', '1998/04/14'],
        ['广州', '老二', '6000', '暂无', '2017/01/09'],
    ])
    csv_file.close()


if __name__ == "__main__":
    my_file_name = 'test.csv'
    gen_csv_file(my_file_name)
    

'''