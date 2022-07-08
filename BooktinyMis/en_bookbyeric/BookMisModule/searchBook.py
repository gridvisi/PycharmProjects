

name, user = "安",'李俊霖'
print(lend_book(name ,user))

def search(name):
    name = input("输入书名：")
    df_name = bookdf.loc[bookdf['书名'].str.contains(name,na=False) ,:].head()
    print(df_name)

    num = input("查询无果则键入 0,如查找到则输入书号：",)

    if num == '0':
        repeat = input("继续查找其他书吗？y/n：")
        if repeat == 'y':
            name = input("请输入书名：")
            return search(name)
        else:
            print("&&&&&&&&&&&&&&&  不再继续查找！&&&&&&&&&&&&")
            return main()

    elif num != '0':
        print(f"{stock['书名'][int(num)]}剩余{stock['库存'][int(num)]}本")
        return lend_book(name,user)


