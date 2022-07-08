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

原文链接：
https://blog.csdn.net/weixin_44285715/article/details/100116192

https://zhuanlan.zhihu.com/p/415399590
'''

# 定义表一
books_url = "I:\\data_science\\bookmis\\books.csv"
books_header = ["书号", "书名", "出版社", "作者", "价格", "库存"]
# 定义表二
log_url = "I:\\data_science\\bookmis\\log.csv"
log_header = ["会员号", "书号", "借阅日期"]
# 定义表三
users_url = "I:\\data_science\\bookmis\\users.csv"
users_header = ["会员号", "姓名", "性别", "会员年度"]

import pandas as pd

csv_file = "I:\\data_science\\bookmis\\table1.csv"
csv_data = pd.read_csv(csv_file, low_memory=False)  # 防止弹出警告
csv_df = pd.DataFrame(csv_data)

bookstock = csv_df.to_dict()

# DataFrame
'''
#print(bookshelf.values)
print(bookstock.loc[:,'书名'][:-1])
print(bookstock.loc[:,'书名'][3],len(bookstock))
'''

#train.loc[train['Name'].str.contains('Mrs|Lily'),:].head()
#print(bookstock.loc[bookstock['书名'].str.contains('安'),:].head())
ans = bookstock.loc[bookstock['书名'].str.contains('三国演义',na=False),:].head()
print(ans['书名'])

# csv 转 为字典，库存等操作在字典执行，执行汇总结果存入csv



print(" *************************************   ")
#.set_index("last_name", inplace=True)
#bookstock.set_index("书名",inplace=True)
#print(bookstock.head())
#print('bookstock.head:',len(bookstock.head()))
#print(bookstock.loc['安徒生童话']['库存'] , len(bookstock.loc['安徒生童话']))
#print(bookstock.loc['看图作文']['书号'])
#print(bookstock.loc[bookstock['书名'].str.contains('安'),:].head())

#print(bookstock)
print("####### 库存书的数量修改函数 ######")
#bookstock = dict(zip(bookshelf, [2] * len(bookshelf)))
#bookname = input("测试输入准确完整的书名，看剩余的本数：", )
#print(bookstock.get(bookname, f"库存里没有《{bookname}》"))


print("####### book module 搜索书函数 ######")


# 查询库存里是否有会员想借的书？


#https://blog.csdn.net/weixin_44285715/article/details/100116192
def search(name):
    df_name = bookstock.loc[bookstock['书名'].str.contains(name,na=False),:].head()
    print(df_name)
    num = input("没有键入0,如有则输入书号：",)
    return num if num else 0

name = "安"
print(search(name)) #return 书号 或 0：表示没有符合需要

print("####### book module 借出书并减库存函数 ######")


# module_lend_book
def lend_book(name, user):
    cunt = 0
    #search(name)
    n = search(name)
    print(" **********  ***************  ************")
    print('   tpoint',n,type(n),bookstock['库存'][int(n)])
    print(" **********  ***************  ************")
    if search(name) and int(bookstock['库存'][int(n)]) >= 1:
        #lendorNot = input("同意借此书，请输入 1，否则输入 0:")
        cunt += 1
        print(cunt)
        return bookstock['书名'][int(n)]
    '''
     if bookstock.get(name, '没有这本书') != '没有这本书':
            print(f"显示库存剩余{bookname}共有 {bookstock[bookname]} 本！")
            if lendorNot == '1':
                # 在库存量里减去1
                bookstock[bookname] = bookstock.get(bookname, 0) - 1
                print(f"{bookname}现在剩余：{bookstock[bookname]}本")
                return print(f"《{bookname}》已经借给{user}, 《{bookname}》还剩{bookstock[bookname]}本")
    
    elif not bookstock.get(bookname) or bookstock[bookname] == 0:

        return print(f"{bookname}无法借给{user},{bookname}还剩{bookstock.get(bookname)}本")
    '''

name, user = "安",'lijing'
print(lend_book(name,user))




# used coding

'''

def search(name):
    bool_in = 0
    for i in range(len(bookstock)):
        if bookstock['书名'][i] == name:
            print(f"库存里有《{name}》在bookshelf")
            bool_in = not bool_in

        else:
            if name in bookstock['书名'][i]:
                bool_in = not bool_in
                print("你找的是不是: ", f"《{bookstock['书名'][i]}》在bookshelf里面，\n")
                inp = input(f"你需要借这本书吗？0=借/1=不借 :")
                if inp == 'y':  bool_in = bool_in and inp
    return bool_in
#error explain
#https://blog.csdn.net/qq_38403590/article/details/104431948

#if data["unit"] is np.nan:
#data["unit"]=" "
#print(json.dumps(method_dis(data),ensure_ascii=False))
'''