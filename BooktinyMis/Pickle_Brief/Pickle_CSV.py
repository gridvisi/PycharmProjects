'''
https://blog.csdn.net/ly17809212771/article/details/120606584

https://www.zhihu.com/zvideo/1376174929470136321

# 原文链接 https://blog.csdn.net/helunqu2017/article/details/116334680
with open(r'1.pkl', "rb") as f:
    object = pkl.load(f)

df = pd.DataFrame(object)
df.to_csv(r'2.csv')
'''

import pickle as pkl
import pandas as pd


# 将信息保存至pkl文件
import pickle as pkl
import pandas as pd
books_url = "I:\\data_science\\bookmis\\books.csv"
# books_header = ["书号", "书名", "出版社", "作者", "价格", "库存"]
books_header = ['bookid', 'booth', 'status', 'bname', 'publish', 'aurtor', 'price', 'number']

bookdf = pd.read_csv(books_url, low_memory=False,encoding="gbk")#创建一个列表
print(bookdf)

pickle_file = open("I:\\data_science\\bookmis\\bookspick.pkl", 'wb')
#创建一个pickle文件，文件后缀名随意,但是打开方式必须是wb（以二进制形式写入）
pkl.dump(bookdf, pickle_file)               #将列表倒入文件
pickle_file.close()

# open pkl
bookspick_url = "I:\\data_science\\bookmis\\bookspick.pkl"
'''
bookdf = open(bookspick_url,'rb')
bookdf = pd.DataFrame(bookdf)
print(bookdf)
'''

bookdf = pd.read_pickle(bookspick_url)

print(bookdf)


# error Solve
# https://stackoverflow.com/questions/64402773/pandas-indexed-dataframe-to-csv-writing-x-cols-but-got-y-aliases
# Writing x cols but got y aliases
'''
              Open    High     Low   Close  Adjusted_close  Volume                                                                            
Date
2020-10-16  618.50  630.75  615.50  625.25          625.25       0
2020-10-15  596.75  619.50  596.50  618.25          618.25   90299
2020-10-14  594.75  600.25  587.25  596.75          596.75   58370
2020-10-13  596.25  604.25  590.75  594.00          594.00   56418
2020-10-12  592.50  599.00  587.00  594.25          594.25   63837
'''

#df.to_csv(price_filename, header=['Date', 'Open', 'High', 'Low', 'Close', 'Adjusted_close', 'Volume'], index=True)