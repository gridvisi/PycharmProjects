import csv
import pandas as pd
import pickle as pkl

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
log_header = ['userid', 'bookid', 'op','date']

csv_file = "I:\\data_science\\bookmis\\books.csv"
csv_data = pd.read_csv(csv_file, low_memory=False,encoding ="gbk")  # 防止弹出警告
csv_df = pd.DataFrame(csv_data,index=None)
bookdf = csv_df   #.drop([''],axis=1,inplace=True)

bookdict = bookdf.to_dict()
last = len(bookdf)
#print(bookdf,len(bookdf))
new = ['83', 'H','0','哈利波特', '儿童', 'J.K.罗琳', '30', '2']

# I'm trying to load the dumped files, using the following code:
# https://stackoverflow.com/questions/53943907/a-bytes-like-object-is-required-not-io-bufferedreader


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

# bookdf.to_pickle(Path.bookpkl_url)
bookdf.to_pickle('book.pkl')
print(pd.read_pickle("book.pkl"))
#f = open(Path.bookpkl_url,'rb')
#bookpkl_df = pickle.loads('book.pkl')


class StrToBytes:
    def __init__(self, fileobj):
        self.fileobj = fileobj
    def read(self, size):
        return self.fileobj.read(size).encode()
    def readline(self, size=-1):
        return self.fileobj.readline(size).encode()

#原文链接：https://blog.csdn.net/u010899985/article/details/80827630

'''

print(bookdf)
f = open('book.pkl','wb')
#bookpkl = pickle.dumps(bookdict,f) #pandas 不能使用该命令
#f.close()


cols = None
with open("I:/data_science/bookmis/userpick.pkl", 'rb') as p:
    cols = pkl.loads(StrToBytes(p))


cols = None
with open(Path.userpkl_url, 'rb') as p:
    cols = pickle.loads(p)

bookpick = open(Path.bookpkl_url,'r')
bookdfs = pickle.loads(bookpick)
bookpick.close()
print(bookdfs)

'''
# csv 转 为字典，库存等操作在字典执行，执行汇总结果存入csv
'''
    def __init__(self,bookpick,userpick,logpick,stock):
        self.bookpick = bookpick
        self.userpick = userpick
        self.logpick = logpick
        self.stock = stock
'''