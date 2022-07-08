# https://zhuanlan.zhihu.com/p/398138112

# https://blog.csdn.net/weixin_43380311/article/details/108338190
'''
l = []
with open('test1.csv','rt') as f:
   cr = csv.reader(f)
   for row in cr:
       print(row)
       l.append(row) #将test.csv内容读入列表l，每行为其一个元素，元素也为list

with open('1.csv','wt') as f2:
   cw = csv.writer(f2)
   #采用writerow()方法
   for item in l:
      cw.writerow(item) #将列表的每个元素写到csv文件的一行
   #或采用writerows()方法
   #cw.writerows(l) #将嵌套列表内容写入csv文件，每个外层元素为一行，每个内层元素为一个数据

'''
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


import csv
csv_file = "I:\\data_science\\bookmis\\books.csv"
l = []
with open(csv_file,'rt') as f:
   cr = csv.reader(f)
   for row in cr:
       print(row)
       l.append(row)
print("****************")
print(l)

csv_data = pd.read_csv(csv_file, low_memory=False,encoding ="gbk")  # 防止弹出警告
csv_df = pd.DataFrame(csv_data,index=None)
bookdf = csv_df   #.drop([''],axis=1,inplace=True)
last = len(bookdf)
print(bookdf,len(bookdf))
new = ['83', 'H','0','哈利波特', '儿童', 'J.K.罗琳', '30', '2']
bookdf.loc[last] = new
# print(bookdf)

print(f"{bookdf.loc[last][:]}******添加成功 ！********")

# https://peps.python.org/pep-0263/
bookdf.to_csv("I:\\data_science\\bookmis\\books.csv",encoding ="gbk",index=False)
print(bookdf)


#2
print("************   **********************")
df = pd.DataFrame(bookdf, columns=books_header)
df.to_csv(books_url, index=False, encoding ="gbk")
print(df)
