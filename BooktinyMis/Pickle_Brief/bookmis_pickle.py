

'''
"""
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
版权声明：本文为CSDN博主「&quot;灼灼其华&quot;」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/weixin_44285715/article/details/100116192

https://zhuanlan.zhihu.com/p/415399590
'''
import pandas as pd
import pickle
# 书籍定义表一
books_url = "I:\\data_science\\bookmis\\books.csv"
books_header = ["书号", "书名", "出版社", "作者", "价格", "库存"]

#csv_file = "I:\\data_science\\bookmis\\books.csv"
bookcsv_pd = pd.read_csv(books_url, low_memory=False,encoding='gbk')  # 防止弹出警告
bookpd_df = pd.DataFrame(bookcsv_pd)
bookdf = bookpd_df
stock = bookdf.to_dict()
print(bookdf)
bookpick = pickle.dumps(bookdf)

# 流水日记账目 定义表二
log_url = "I:\\data_science\\bookmis\\log.csv"
log_header = ["会员号", "书号", "借阅日期"]

#会员书架来源和存储定义表三
users_url = "I:\\data_science\\bookmis\\users.csv"
#users_header = ["会员号", "姓名", "性别","手机号码","" "会员年度"]

usercsv_pd = pd.read_csv(users_url, low_memory=False)  # 防止弹出警告
userpd_df = pd.DataFrame(usercsv_pd)
userpick = pickle.dumps(userpd_df)
#userfile = pd.read_pickle(userdata)
#print(userfile)
print('会员库：',userpick)
#usefile = pickle.loads(userdata)

with open(bookpick, 'rb') as f:
    bookdf = pickle.loads(f)
print('初始化bookdf：',bookdf)