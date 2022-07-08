# https://docs.python.org/3/library/pickle.html

import pandas as pd
import pickle

# 定义表1
books_url = "I:\\data_science\\bookmis\\books.csv"
books_header = ['bookid','booth','status','bname','publish','aurtor','price','number']
# books_header = ["书号", "书名", "出版社", "作者", "价格", "库存"]

# 定义表2
users_url = "I:\\data_science\\bookmis\\users.csv"
user_header = ['userid','name','gender', 'cell','expdate','credit','status']
# users_header = ["会员号", "姓名", "性别", "会员年度"]

# 定义表3
log_url = "I:\\data_science\\bookmis\\log.csv"
log_header = ['userid', 'bookid', 'date']
# log_header = ["会员号", "书号", "借阅日期"]



csv_file = "I:\\data_science\\bookmis\\books.csv"
csv_data = pd.read_csv(csv_file, low_memory=False,encoding='gbk')  # 防止弹出警告  ,encoding='gbk'
csv_df = pd.DataFrame(csv_data)
bookdf = csv_df
stock = csv_df.to_dict()
print(bookdf)

userdata = pickle.dumps(bookdf)
#print(userdata)

usefile = pickle.loads(userdata)
#print(usefile)

#pickle reference
'''

# dumps功能
import pickle
data = ['aa', 'bb', 'cc']
# dumps 将数据通过特殊的形式转换为只有python语言认识的字符串
p_str = pickle.dumps(data)
print(p_str)

# loads功能
# loads  将pickle数据转换为python的数据结构
ret = pickle.loads(p_str)
print(ret)

 # dump功能
# dump 将数据通过特殊的形式转换为只有python语言认识的字符串，并写入文件
with open('data.pkl', 'wb') as f:
    pickle.dump(data, f)

# load功能
# load 从数据文件中读取数据，并转换为python的数据结构
with open('data.pkl', 'rb') as f:
    data = pickle.load(f)

#输出结果
b'\x80\x03]q\x00(X\x02\x00\x00\x00aaq\x01X\x02\x00\x00\x00bbq\x02X\x02\x00\x00\x00ccq\x03e.'
['aa', 'bb', 'cc']

'''

# pickle
# 读取
import pickle

info = pickle.loads(open(usefile, 'rb').read())


# 写入
import pickle
open('data.pkl', 'wb').write(pickle.dumps(info))


# 纯文本
# 读取
txt = open(fn, 'r', encoding='utf-8').read()


# 写入
open(fn, 'w', encoding='utf-8').write(txt)


# 二进制
# 读取
data = open(fn, 'rb').read()


# 写入
open(fn, 'wb').write(data)