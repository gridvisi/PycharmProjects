import pandas as pd

csv_file = "I:\\data_science\\bookmis\\table1.csv"
csv_data = pd.read_csv(csv_file, low_memory=False)  # 防止弹出警告
csv_df = pd.DataFrame(csv_data)
print(csv_df.values)
books = csv_df
bookshelf = csv_df

# ["书号", "书名", "出版社", "作者", "价格", "库存"]

# 书的属性：书名，作者，状态，位置
# 管理系统：
class Book(object):  # 定义一个书类

    def __init__(self, booth, name, author, publish, status, price, stock, books):
        self.booth = booth  #存放书架的编号
        self.name = name    #书名
        self.author = author  #书作者
        self.publish = publish  #出版社
        self.status = status    #借出状态
        self.price = price      #价格
        self.stock = stock      #库存数
        #self.bookindex = bookindex
        #self.books = books

        #print(self.books)
    def __str__(self):
        if self.status == 1:
            stats = '未借出'
        elif self.status == 0:
            stats = '已借出'
        else:
            stats = '状态异常'
        return '书名: 《%s》 作者: %s 状态: <%s> 位置: %s' \
               % (self.name, self.author, stats, self.booth)


class BookManage(object):
    books = []

    def start(self):
        # 添加图书
        # num, name, author, publish,status,price,stock,bookindex
        '''

        self.books.append(Book('python', 'guido', 1, 'ISO9001'))
        self.books.append(Book('c', '谭浩强', 1, 'NFS8102'))
        self.books.append(Book('java', 'westos', 1, 'PKA7844'))
        :return:
        '''
        print('["书架", "书名", "出版社", "作者", "价格", "库存"]')
        bookinp = input("请输入书的概况：")
        self.books.append(Book('A','python', 'guido', 1, 'ISO9001',20,2,books))
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
                print('["书号", "书名", "出版社", "作者", "价格", "库存"]')
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


    def checkBook(self, name): #, bookshelf
        '''

        for book in self.books:
            if book.name == name:
            return book
        else:
            return None
        :param self:
        :param name:
        :return:
        '''
        #name = input("输入书名：")
        print(self.books)
        bool_in = 0
        for name in self.books:
            if name in books.name:
                print(f"库存里有《{name}》在bookshelf")
                bool_in = not bool_in
                return name

            else: #name not in self.books:
                for book in bookshelf:
                    if name in book:
                        print("你找的是不是: ", f"《{book}》在bookshelf里面，\n"
                            f"你需要借这本书吗？")
                        lendorNot = input("确认借输入Y，否则N:")
                        bool_in = not bool_in
                        return book
        return None #库里是否有书，会员是否决定借


    def borrowBook(self):
        print(self.books)
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