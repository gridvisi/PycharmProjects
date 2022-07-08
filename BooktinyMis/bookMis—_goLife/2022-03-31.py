

import csv
import pandas as pd
import pickle

class Path:
    # 3 张表的csv存储地址
    # 定义表-1 books_url 存放书的信息csv 和 pickle
    # 定义表-2 user_url 存放会员信息csv 和 pickle
    # 定义表-3 log_url 存放日志csv 和 pickle

    # 生成book.csv
    books_url = "I:\\data_science\\bookmis\\books.csv"
    #books_header = ["书号", "书架","状态", "书名", "出版社", "作者", "价格", "库存"]
    books_header = ['bookid','booth','status','bname','publish','aurtor','price','number']
    bookpkl_url = "I:\\data_science\\bookmis\\bookspick.pkl"

    # 会员书架来源和存储定义表-2
    # 生成会员csv
    users_url = "I:\\data_science\\bookmis\\users.csv"
    users_header = ['userid','name','gender', 'cell','expdate','credit','status']
    userpkl_url = "I:\\data_science\\bookmis\\userpick.pkl"

    # 流水日记账目 定义表-3
    log_url = "I:\\data_science\\bookmis\\log.csv"
    log_header = ['userid', 'bookid', 'op','date']
    logpkl_url = "I:\\data_science\\bookmis\\logpick.pkl"
    # 生成log.csv
    #bookpick, userpick, logpick




print(" *************************************   ")
print("####### 库存书的数量修改函数 ######")

# 书的属性：书名，作者，状态，位置
# 管理系统：
class Book(object):  # 定义一个书类

    def __init__(self, booth, name, author, publish, status, price, stock):
        self.booth = booth      # 存放书架的编号
        self.status = status    # 借出状态
        self.name = name        # 书名
        self.author = author    # 书作者
        self.publish = publish  # 出版社

        self.price = price      # 价格
        self.stock = stock      # 库存数

class User(object):
    def __init__(self,name,gender,cell,expdate,credit,status):
        self.name = name        # 会员姓名
        self.gender = gender    # 性别
        self.cell = cell        # 手机号码
        self.expdate = expdate  # 有效期
        self.credit = credit    # 积分
        self.status = status    # 有效状态


class Bookmis(object):
    def __init__(self):

        #self.bookpkl = bookpkl
        #self.userpkl = Path.userpkl_url
        #self.logpkl = Path.logpkl_url

        print("系统初始化，提取图书、会员和日志库...")

        self.book_table, self.users_table,self.log_table = self.get_pd_pattern()
        self.bookpick, self.userpick, self.logpick = self.loadpick()
        print("图书馆系统初始化完成！\n")
        print(self.book_table)
        print( " %%%%%%%%%%%%%%%%   %%%%%%%%%%%%%%%%%")
        print(self.bookpick, self.userpick, self.logpick)
        print(" %%%%%%%%%%%%%%%%   %%%%%%%%%%%%%%%%%")
        self.main()

    def loadpick(self):
        # 完成 3 张表 csv文档转pandas格式
        # "ISO-8859-1"
        # 输入数据来自书籍csv文档存放地址 ->
        # books_url = "I:\\data_science\\bookmis\\books.csv"

        # "I:\\data_science\\bookmis\\bookspick.pkl"
        # "I:\\data_science\\bookmis\\userpick.pkl"
        # "I:\\data_science\\bookmis\\logpick.pkl"
        # 返回 3个pickle文件
        # 会员书架来源和存储定义表-2
        # 流水日记账目 定义表-3

        # get_pattern 传入 3个csv文档
        # books_url = "I:\\data_science\\bookmis\\books.csv"
        # books_header = ["书号", "书架","状态", "书名", "出版社", "作者", "价格", "库存"]

        #books_header = ['bookid', 'booth', 'status', 'bname', 'publish', 'aurtor', 'price', 'number']
        #bookdf = pd.read_csv(self.book_table, low_memory=False, encoding="gbk")  # 防止弹出警告

        # 生成bookpick.pkl
        bookpick = self.book_table.to_pickle # ("bookpick")

        # 会员书架来源和存储定义表-2
        # 生成会员csv
        # users_url = "I:\\data_science\\bookmis\\users.csv"
        # users_header = ['userid', 'name', 'gender', 'cell', 'expdate', 'credit', 'status']
        # userpd = pd.read_csv(self.users_table, low_memory=False, encoding="gbk")  # 防止弹出警告

        # 生成会员pkl
        userpick = self.users_table.to_pickle


        # 流水日记账目 定义表-3
        # log_url = "I:\\data_science\\bookmis\\log.csv"
        # log_header = ['userid', 'bookid', 'op', 'date']
        # 生成log.csv
        # logdpd = pd.read_csv(self.log_table, low_memory=False, encoding="gbk")  # 防止弹出警告
        #logdf = pd.DataFrame(logdata)
        # 生成log.pkl
        logpick = self.log_table.to_pickle

        # bookpick, userpick, logpick
        return bookpick, userpick, logpick


    def get_pd_pattern(self):
        # 输入数据来自 Path class
        # 3 张表由csv格式转换后返回为pandas格式
        book_table = pd.read_csv(Path.books_url, low_memory=False, encoding="gbk")
        users_table = pd.read_csv(Path.users_url, low_memory=False, encoding="gbk")
        log_table = pd.read_csv(Path.log_url, low_memory=False, encoding="gbk")
        print("书、会员和日志共 3 张 table 信息读取成功...")
        return book_table, users_table,log_table

    def save_file(self):
        bdf = self.bookpick
        bdf.to_csv(Path.books_url, header=Path.books_header, index=None)

        udf = self.userpick
        udf.to_csv(Path.log_url, header=Path.log_header, index=None)

        logdf = self.logpick
        logdf.to_csv(Path.users_url, header=Path.users_header, index=False)
        print("保存3张表文件到Path成功！！！")

    def updateBook(self):
        # 输入数据来自 uerspick
        # 命令行交互完成新增会员信息
        print("录入新书信息,请按以上顺序输入字符串，每项之间以空格隔开:")
        #bookdf = pd.DataFrame(self.book_table, index=None)
        bookdf = pd.read_pickle(self.bookpick)
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


    def search(self):
        # 搜索书 该子函数被lend_book 调用
        # 输入数据来自 bookpick
        bookdf = self.bookpick
        #bookdf = pd.DataFrame(bookdf)
        print(bookdf['bname'])
        #stock = bookdf.to_dict()

        name = input("输入书名包含的关键词 ：")
        print(" ********** search() 搜索书库完毕  *************** 所有满足的结果 ************")
        dfname_select = bookdf.loc[bookdf['bname'].str.contains(name,na=False),:].head()
        print(dfname_select)
        #dfs = dfname_select.loc[bookdf['bookid']==83,:].head()  # ['bname', 'price', 'number']
        #print(dfs)
        #print(dfname_select['bookid'])
        id = input("符合您的👆要求，请输入书号：bookid,没有则输入 0 ：",)

        if id == '0':
            repeat = input("继续查找其他书吗？y/n：")
            if repeat == 'y':
                name = input("请输入书名：")
                return Bookmis.search
            else:
                print("&&&&&&&&&&&&&&&  不再继续查找！&&&&&&&&&&&&")
                return Bookmis.main(self)

        elif id != '0':  # 剩余{dfname_select['bname']}本
            print(f"您选择的书的价格和库存如下：")
            print(bookdf.loc[bookdf['bookid']==int(id),['bname','price','number']])
            a = str(input("确认借这本书：y/n: "))
            if a == "y":return self.lend_book(id)
            return dfname_select

    '''
    name = "安"
    print(search(name),type(search(name)))  # return 书号 或 0：表示没有符合需要
    print("####### book module 借出书并减库存函数 ######")
    '''
    # 库存子函数 输入书名和数量  输出库存表

    def stockop(self,id):
        # search()结果不空，且
        # user同意借阅->lend_book()
        # 字典操作库存
        # 输入数据来自 bookpick
        # lend_book()调用stockop

        # 返回文本提示 库存调整后的状态
        bookdf = pickle.loads(self.bookpick)
        stock = bookdf.to_dict()
        last = len(stock)

        stock['number'][int(id)] = str(int(stock['number'][int(id)]) - 1)
        bookdfs = pd.DataFrame.from_dict(stock)

        # df -> to pickle 库存更新状态到pickle
        self.bookpick = pickle.dumps(bookdfs)
        return self.bookpick


    def lend_book(self,id):
        # 借书 module_lend_book
        # 调用search | stockop | 会员搜索共 3 子函数
        # 命令行交互完成搜索书、库存调整、会员搜索、log记录
        # 显示借书成功与否、库存调整后的状态
        # 输入数据来自 bookpick
        bdf = pickle.loads(Bookmis.stockop(self,id))
        bookdf = pd.read_pickle(bdf)
        print(" ********** 搜索书库完毕  *************** 以上是满足的结果 ************")

        print('   书的id ：', id, '书名：', bookdf['bname'][int(id)], "剩余:",bookdf['number'][int(id)])
        print(" **********  ***************  ************")
        lend = input("同意借此书，请输入 y，否则输入 n: ",)
        user = input("请输入会员号：")
        if lend == 'y':

            print(bdf)
            print(f"会员号为{'userid'}的会员{user}借到\n {bdf.loc[bdf['bookid'] == int(id)].head()}")
            print(f"{bdf.loc[bdf['bookid'] == int(id),['bname']]}的库存剩余：\n {bdf.loc[bdf['bookid'] == int(id),['number']]}本")
            self.save_file()
            return self.main()

        elif lend == '0':
            return Bookmis.main(self)


    def find(self):
        # 该子函数被lend_book()调用
        # 查询会员，返回会员id和姓名
        # 输入数据来自 uerpick
        userfile = pickle.loads(self.userpick)
        userdf = pd.DataFrame(userfile)
        users = userdf.to_dict()
        name = input("输入查询的会员号：")
        print(" ********** 搜索书库完毕  *************** 所有满足的结果 ************")
        username_select = users.loc[userdf['name'].str.contains(name,na=False),:].head()
        print(username_select)
        return userdf['userid'],userdf['name']

    def userAdd(self):
        # 添加新会员的关键信息
        # 输入数据来自 uerpick
        userfile = pickle.loads(self.userpick)
        userdf = pd.DataFrame(userfile)
        users = userdf.to_dict()
        print(" ********** 输入会员格式 姓名 性别 手机号 ************")
        profile = input("输入新会员信息：")
        name,gender,cell = profile.split(" ")
        id = userdf[-1:]['userid']
        userdf.append(id,name,gender,cell)
        print(userdf)
        return userdf['userid'],userdf['name']


    def main(self):
        print("---- 图书管理系统菜单 -----\n")
        #print("已完成的功能标记为 -> ")
        print("1 查书 请输入书名")
        print("2 借书 请输入会员姓名")
        print("3 查询是否为会员，输入姓名")
        print("4 注册新会员，输入姓名")
        print("5 录入新书刊，输入姓名")


        op = input('请输入选项 1-4：')
        print(f" 您输入的选项是 {op}")
        while op != "N":
            #self.cls()
            '''
            print("---- 图书管理系统菜单 -----\n")
            print("  已完成的功能标记为 -> ")
            print("1 借阅功能 请输入书名：")
            print("2 还书功能 请输入会员姓名：")
            print("3 录入新书 请输入书名：")
            print("4 还书功能 请输入会员姓名：")
            print("5 录入新书 输入姓名")
            '''

            if op == '1':
                Bookmis.search(self)

            elif op == '2':
                #num = input("-- 请输入书号：")
                Bookmis.lend_book(self,id)
                #Bookmis.save_file(self)

            elif op == '3':
                self.find()

            elif op == '4':
                self.userAdd()

            elif op == '5':
                self.updateBook()

            else:
                inp = input("请确认是否回到主菜单：y/n ")
                if inp == 'y':return self.main()
                else:print("欢迎再来！")

print("####### book module 搜索书函数 ######")


manager = Bookmis()  # 类的实例化
manager.main()