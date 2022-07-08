
'''

    读取csv文件
    该文本中的分割符既有空格又有制表符（‘/t’），sep参数用‘/s+’，可以匹配任何空格。
    """
    import pandas as pd
    dataset1 = pd.read_csv('C:/Users/62497/Desktop/data1.csv',sep='\s+')
    # header=None:没有每列的column name，可以自己设定
    # encoding='gb2312':其他编码中文显示错误
    # sep=',':用逗号来分隔每行的数据
    # index_col=0:设置第1列数据作为index
    data = pd.read_table('Z:/test.txt',header=None,encoding='gb2312',sep=',',index_col=0)
————————————————
        csv_file = "I:\\data_science\\bookmis\\table1.csv"
        csv_data = pd.read_csv(csv_file, low_memory=False)  # 防止弹出警告
        bookdf = pd.DataFrame(csv_data)

https://zhuanlan.zhihu.com/p/415399590
'''
import pandas as pd
df = pd.DataFrame( columns=['X', 'y'])

# 定义表一
books_url = "I:\\data_science\\bookmis\\books.csv"
books_header = ["书号", "书名", "出版社", "作者", "价格", "库存"]
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

# DataFrame操作-本程序不要另外文件见
# C:\Users\29358\PycharmProjects\BooktinyMis\en_bookbyeric\allbyddm.py
'''

name = "安"
print(search(name),type(search(name)))  # return 书号 或 0：表示没有符合需要


'''
# csv 转 为字典，库存等操作在字典执行，执行汇总结果存入csv



print(" *************************************   ")


# print(bookstock)
print("####### 库存书的数量修改函数 ######")


print("####### book module 搜索书函数 ######")


# 查询库存里是否有会员想借的书？


class Config:
    # 定义表一
    books_url = "I:\\data_science\\bookmis\\books.csv"
    books_header = ["book.No", "bname", "publish", "aurtor", "price", "number"]
    # 定义表二
    log_url = "I:\\data_science\\bookmis\\log.csv"
    log_header = ["会员号", "书号", "借阅日期"]
    # 定义表三
    users_url = "I:\\data_science\\bookmis\\users.csv"
    users_header = ["userid", "name", "gender", "years"]



class Book(object):  # 定义一个书类

    def __init__(self, n, book, user, publish,status,price,num,bookdf,stock):
        self.n = n
        self.book = book
        self.user = user
        self.publish = publish
        self.status = status
        self.price = price
        self.num = num
        self.bookdf = bookdf
        self.stock = stock

class BookManage(object):
    def __init__(self):
        print("图书馆系统初始化中...")
        self.input_BookUser()
        #self.search_book, self.lend_book, self.user_table = self.get_info_from_file()
        print("图书馆系统初始化完成！\n")
        self.menu()
        #books = []

    def get_info_from_file(self):
        bookdf = pd.read_csv(Config.books_url)
        borrow_table = []
        user_table = pd.read_csv(Config.users_url)
        print("信息读取成功...")
        print("bookdf ：",bookdf['书名'])
        return bookdf, borrow_table, user_table

    def input_BookUser(self):
        self.book = input('请输入  书名 ：')
        self.user = input('请输入会员名 ：')
        return self.book,self.user

    def search_book(self,bookdf):
        print('开始搜索>>>>')
        #name = input("输入书名：")
        df_name = bookdf.loc[bookdf['书名'].str.contains(self.book,na=False),:].head()
        print(df_name)

        num = input("查询无果则键入 0,如查找到则输入书号：",)

        if num == '0':
            repeat = input("继续查找其他书吗？y/n：")
            if repeat == 'y':
                name = input("请输入书名：")
                #return self.search(self,name)
            else:
                print("&&&&&&&&&&&&&&&  不再继续查找！&&&&&&&&&&&&")
                #return self.main(self)

        elif num != '0':
            print(f"{stock['书名'][int(num)]}剩余{stock['库存'][int(num)]}本")
            return stock['书名'][int(num)]



    print("####### book module 借出书并减库存函数 ######")


    # module_lend_book
    def lend_book(self):

        # search(name)
        n = self.search_book()
        print(" **********  ***************  ************")
        print('   tpoint' ,n ,type(n) ,bookdf['库存'][int(n)])
        print(" **********  ***************  ************")
        if n !='0' and stock['库存'][int(n)] >= 1:
            lend = input("同意借此书，请输入 1，否则输入 0:")
            if lend == '1':
                #stock['书名'][int(n)] = str(int(stock['书名'][int(n)]) - 1)
                stock['库存'][int(n)] = str(int(stock['库存'][int(n)]) - 1)
                return f"{self.user}借到《{stock['书名'][int(n)]}》，《{stock['书名'][int(n)]}》库存剩余：{stock['库存'][int(n)]}"
            else:pass

        else:print("没有找到书")



    def menu(self):
        print("---- 图书管理系统菜单 -----\n")
        print("已完成的功能标记为 -> ")
        print("1 借阅功能 请输入-> 1 ")
        print("2 还书功能 请输入-> 2 ")
        op = input('请输入选项 1-3：')
        while op != "N":
            # self.cls()
            print("---- 图书管理系统菜单 -----\n")
            print("0 输入书名和用户名 -> ")
            print("1 借阅功能 请输入-> 1 学号 书号")
            print("2 还书功能 请输入-> 2 学号 书号")

            if op == '0':
                self.input_BookUser()

            if op == '1':
                self.search_book(bookdf)

            elif op == '2':
                self.lend_book()

            else:
                "没有选，是否继续？否==N"

manager = BookManage()  # 类的实例化
manager.menu()




'''

name, user = "安",'李俊霖'
print(lend_book(name ,user))


class BookManage(object):
    books = []

    def start(self):
        # 添加图书
        # num, name, author, publish,status,price,stock,bookindex
        #

        self.books.append(Book('python', 'guido', 1, 'ISO9001'))
        self.books.append(Book('c', '谭浩强', 1, 'NFS8102'))
        self.books.append(Book('java', 'westos', 1, 'PKA7844'))
               # 0:借出 1：存在
        # python 1
        # c 1
        # java 1

    def Menu(self):
        self.start()
        while True:
            print("""
                        图书管理系统
        1.查询图书
        2.增加图书
        3.借阅图书
        4.归还图书
        5.退出系统
        """)

            choice = input('请选择：')

            if choice == '1':
                self.showAllBook()  # 调用显示所有书籍的函数
            elif choice == '2':
                self.addBook()  # 调用添加书籍的函数
            elif choice == '3':
                self.borrowBook()  # 调用借书的函数
            elif choice == '4':
                self.returnBook()  # 调用还书的函数
            elif choice == '5':
                print('欢迎下次使用...')
                exit()
            else:
                print('请输入正确选择')
                continue

    def showAllBook(self):
        print(books)
        for book in self.books:
            print(book)

    def addBook(self):
        name = input('图书名称:')
        self.books.append(Book(name, input('作者:'), 1, input('存储位置:')))
        print('图书《%s》增加成功' % name)

    def checkBook(self, name):


        for book in self.books:
            if book.name == name:
                return book
            else:
                return None



    def borrowBook(self):
        name = input('借阅图书名称: ')
        ret = self.checkBook(name)
        print(ret)
        # 判断书是否存在，如果存在，判断书是否已借出，如果没有借出，借阅并将其状态改为0
        if ret != None:
            if ret.status == 0:
                print('书籍《%s》已经借出' % name)
            else:
                ret.status = 0
                print('书籍《%s》借阅成功' % name)
        else:
            print('书籍《%s》不存在' % name)

    def returnBook(self):
        name = input('归还图书名称:')
        ret = self.checkBook(name)

        if ret != None:
            if ret.status == 0:
                ret.status = 1
                print('书籍《%s》归还成功' % name)
                print(ret)
            else:
                print('书籍《%s》未借出' % name)
        else:
            print('书籍《%s》不存在' % name)


manager = BookManage()  # 类的实例化
manager.Menu()


'''