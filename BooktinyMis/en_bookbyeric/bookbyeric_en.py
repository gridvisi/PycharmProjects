
import time

import pandas as pd
import os
import matplotlib.pyplot as plt

# 1 生成书库
sheet = [[0, '学会担当', '', '', 0, 10], [1, '注音版红楼梦', '', '', 0, 10], [2, '三国演义', '', '', 0, 10],
         [3, '水许传', '', '', 0, 10], [4, '太阳溪农场的丽贝卡', '', '', 0, 10], [5, '海底两万里', '', '', 0, 10],
         [6, '草房子', '', '', 0, 10], [7, '积极才能成功', '', '', 0, 10], [8, '坦克与装甲车', '', '', 0, 10],
         [9, '语故事', '', '', 0, 10], [10, '夏洛的网', '', '', 0, 10], [11, '中小学公共安全与生命考有(四下)', '', '', 0, 10],
         [12, '三国演义(白化文)', '', '', 0, 10], [13, '综台实践活动(四下)', '', '', 0, 10],
         [14, '一年级生字墓写本', '', '', 0, 10], [15, '句子专项圳练', '', '', 0, 10],
         [16, '道德与法治', '', '', 0, 10], [17, '木公又玄秘塔', '', '', 0, 10],
         [18, '五下科等', '', '', 0, 10], [19, '老版高中语文知识手册', '', '', 0, 10],
         [20, '一年级的马小跳', '', '', 0, 10], [21, '宜家IKEA家居册', '', '', 0, 10],
         [22, '世界儿童周刊1-8', '', '', 0, 10], [23, '小哥白尼周刊', '', '', 0, 10],
         [24, '幽黑小读者周刊', '', '', 0, 10], [25, '课堂内外周刊', '', '', 0, 10],
         [26, '小学年级奥数', '', '', 0, 10], [27, '西游记(上)', '', '', 0, 10],
         [28, '给孩子的诗2', '', '', 0, 10], [29, '详一反三奥数', '', '', 0, 10],
         [30, '钢铁是怎样炼成的', '', '', 0, 10], [31, '马小跳·侦探小组在行动', '', '', 0, 10],
         [32, '疯狂学校我们的签班主任', '', '', 0, 10], [33, '孔乙己', '', '', 0, 10],
         [34, '阿Q正传', '', '', 0, 10], [35, '狂人日记', '', '', 0, 10],
         [36, '为了忘却的记念', '', '', 0, 10], [37, '论雷峰塔的倒掉', '', '', 0, 10],
         [38, '大学书法', '', '', 0, 10], [39, '岛蛋鬼日记', '', '', 0, 10],
         [40, '北大门暑夫', '', '', 0, 10], [41, '老人与海', '', '', 0, 10],
         [42, '彷徨', '', '', 0, 10], [43, '月花夕拾', '', '', 0, 10], [44, '免骨寻踪', '', '', 0, 10],
         [45, '烙材童话', '', '', 0, 10], [46, '三上所写给孩子的名人传记习', '', '', 0, 10],
         [47, '同桌冤家', '', '', 0, 10], [48, '洋葱头历险记', '', '', 0, 10],
         [49, '些成语故事', '', '', 0, 10], [50, '科普馆', '', '', 0, 10],
         [51, '西游记·田文', '', '', 0, 10], [52, '中国神话故事', '', '', 0, 10],
         [53, '作文小状元', '', '', 0, 10], [54, '人名言', '', '', 0, 10], [55, '成语故事', '', '', 0, 10],
         [56, '吹牛大王·历险记习', '', '', 0, 10],
         [57, '假如给我三天光明', '', '', 0, 10], [58, '野草习夏日历险', '', '', 0, 10],
         [59, '安徒生童话', '', '', 0, 10], [60, '少年侦探团', '', '', 0, 10],
         [61, '少年侦探团5', '', '', 0, 10], [62, '马小跳6年级', '', '', 0, 10],
         [63, '学语文之友', '', '', 0, 10], [64, '中华民族是一家人', '', '', 0, 10],
         [65, '中华民方族是一家2', '', '', 0, 10], [66, '马小北5年级', '', '', 0, 10],
         [67, '马小跳1年级', '', '', 0, 10], [68, '马小跳4年级', '', '', 0, 10],
         [69, '爱我中华', '', '', 0, 10], [70, '科科技托起强因梦', '', '', 0, 10],
         [71, '少年优探团2', '', '', 0, 10], [72, '鲁鲁龙的礼物', '', '', 0, 10],
         [73, '小贝弟的大梦想', '', '', 0, 10], [74, '一个长上天的大苹果', '', '', 0, 10],
         [75, '是谁在门外', '', '', 0, 10], [76, '作文起步', '', '', 0, 10],
         [77, '优秀作文', '', '', 0, 10], [78, '看图说话', '', '', 0, 10],
         [79, '好词好句', '', '', 0, 10], [80, '看图写话', '', '', 0, 10],
         [81, '看图作文', '', '', 0, 10], [82, '日记起步', '', '', 0, 10], [83, '', '', '', 0, 10]]

# 1-1 列表转为DataFrame

book_df = pd.DataFrame(sheet,
                       columns=["book.No", "bname", "publish", "aurtor", "price", "number"])
book_df.to_csv('I:\\data_science\\bookmis\\books.csv' ,index=False)

# 2 生成会员表
# "会员号", "姓名", "性别", "会员年度"
users = {"会员号": ["0001" ,"0002" ,"0003" ,"0004" ,"0005"],
         "姓名": ["Candy", "Bowen", "David", "Thomas", "Steven"],
         "性别": ["女", "男", "男", "男", "男"],
         "会员年度": [1, 3, 1, 2, 1]}

users_df = pd.DataFrame(users,
                        columns=["userid", "name", "gender", "years"])
users_df.to_csv('I:\\data_science\\bookmis\\users.csv' ,index=False)


# 先定义一个配置类
# from Tools.scripts.treesync import raw_input


class Config:
    # 定义表一
    books_url = "I:\\data_science\\bookmis\\books.csv"
    books_header = ["bookNo", "bname", "publish", "aurtor", "price", "number"]
    # 定义表二
    log_url = "I:\\data_science\\bookmis\\log.csv"
    log_header = ["会员号", "书号", "借阅日期"]
    # 定义表三
    users_url = "I:\\data_science\\bookmis\\users.csv"
    users_header = ["userid", "name", "gender", "years"]

class library_system(object):
    def __init__(self):
        print("图书馆系统初始化中...")
        self.input_books_users()
        self.book_table, self.borrow_table, self.student_table = self.get_info_from_file()
        print("图书馆系统初始化完成！\n")
        self.menu()

    def input_books_users(self):
        print("请输入图书馆藏书表")

        # table1建议改写为 读取本地table1.csv！

        csv_file = "I:\\data_science\\bookmis\\books.csv"
        csv_data = pd.read_csv(csv_file, low_memory=False)  # 防止弹出警告
        csv_df = pd.DataFrame(csv_data)
        print(csv_df)
        books = csv_df

        print("输入藏书表:书号 书名 出版社 作者 价格 库存\n")
        print(f'书号顺序按数字小到大,前一条书号是 {len(books)}')

        '''
        Series与DataFrame合并有两种方法
        法1：直接append
            record = record.append(s, ignore_index=True)
        法2：显式指定行进行合并
            record.loc[2] = s
        '''

        # 86 哈利波特 儿童 J.K.罗琳 30 2
        # 87 世界地理 national whit 30 1
        print("&&&   请输入格式如：|86 哈利波特 儿童 J.K.罗琳 30 2|" ,"  &&&&")
        book = input('请输入数据：')
        while book != "none":
            bk = book.split()
            if len(bk) != 6:
                book = input('列数不一致\n请重新输入:')
            else:
                # table1.append([bk])
                deltaBook = pd.Series(bk, index=["book.No", "bname", "publish", "aurtor", "price", "number"])
                books = books.append(deltaBook ,ignore_index=True)
                book = input('下一条记录:')

        books.to_csv("I:\\data_science\\bookmis\\books.csv" ,index=False)
        print("&&&&&&&&&&&&&&&&&&& 书库  &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
        print(books)

        print("请输入会员信息表")
        # users 读取users.csv

        csv_file = "I:\\data_science\\bookmis\\users.csv"
        csv_data = pd.read_csv(csv_file, low_memory=False)  # 防止弹出警告
        users = pd.DataFrame(csv_data)
        print(users)
        print("**************输入会员信息 : 会员号 姓名 性别 会员年度**********************")
        print("  \n")
        prev = len(users)
        studentid = str(10000 + prev)[1:]
        print(f'会员号按数字小到大,前一条学生号是 {studentid}')

        # 0001 李晶 男 k10
        # 0002 张敏 女 k12
        # 0003 赵淼 男 k12
        print("请输入格式如：" ,"0001 李喵 男 1")
        user = input('请输入会员数据:')

        while user != "none":
            use = user.split()
            if len(use) != 4:
                user = input('数据列数不一致,请重新输入:')
            else:
                # DataFrame添加记录
                deltauser = pd.Series(use, index=["会员号", "姓名", "性别", "会员年度"])
                users = users.append(deltauser, ignore_index=True)
                user = input('输入下一条会员数据:')

            users.to_csv("I:\\data_science\\bookmis\\table3.csv", index=False)
            print("&&&&&&&&&&&&&&&&&&&  会员表  &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
            # print(users)

        books = pd.DataFrame(books)
        users = pd.DataFrame(users)
        books.to_csv(Config.books_url, header=Config.books_header, index=None)
        users.to_csv(Config.users_url, header=Config.users_header, index=None)
        print(users)

    '''
    table2_url = "I:\\data_science\\bookmis\\table2.csv"
    table2_header = ["学号", "书号", "借阅日期"]
    # 定义表三
    table3_url = "I:\\data_science\\bookmis\\table3.csv"
    table3_header = ["会员号", "姓名", "性别", "会员年度"]
    '''

    def get_info_from_file(self):
        book_table = pd.read_csv(Config.books_url)
        borrow_table = []
        student_table = pd.read_csv(Config.users_url)
        print("信息读取成功...")
        print(" book_table 信息\n " ,book_table['库存'][3])
        return book_table, borrow_table, student_table

    def save_file(self):
        self.book_table.to_csv(Config.books_url, header=Config.books_header, index=None)
        boo = pd.DataFrame(self.borrow_table)
        boo.to_csv(Config.log_url, header=Config.log_header, index=False)
        self.student_table.to_csv(Config.users_url, header=Config.users_header, index=None)
        print("保存文件成功")

    # 实现借阅功能：输入学号和书号，如果借阅成功
    # 学号所对应的学生在表3中并且
    # 书号所对应的图书在表1中且库存大于等于1，
    # 修改books表 和 log表，并保存到文件

    # https://www.jianshu.com/p/72274ccb647a
    # SettingWithCopyWarning:A value is trying to be set on a copy of a slice from a DataFrame
    # 解决之道 C:\Users\29358\PycharmProjects\BooktinyMis\DF_Keynotes
    # print(dfmi.loc[:, ('one', 'second')][0])
    # https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
    '''
    # 设置新值
    data.loc[data.bidder == 'parakeet2004', 'bidderrate'] = 100
    # 检查结果
    data[data.bidder == 'parakeet2004']['bidderrate']


    6    100
    7    100
    8    100
    Name: bidderrate, dtype: int64

    链式索引详细见 https://www.jianshu.com/p/72274ccb647a
    '''

    # 增加一个书号查书名相互查询的子函数


    def borrow(self, student_id, book_id):
        flag1 =True

        for i in range(len(self.student_table["会员号"])):
            if int(self.student_table["会员号"][i]) == int(student_id):

                # print(f'查询到该会员：{self.student_table.get(["姓名"][i],"不是会员")} ')
                # get(user,tips) 输出整个会员表！

                print(f'查询到{self.student_table["会员号"][i]}号会员是：{self.student_table["姓名"][i]} ')

                flag1 = False

                for j in range(len(self.book_table["书号"])):
                    if int(self.book_table["书号"][j]) == int(book_id) and int(self.book_table["库存"][j]) > 0:
                        print(f'库存剩余 {self.book_table["书名"][j]}共 {self.book_table["库存"][j]} 本！')

                        # self.book_table.loc[self.book_table["书号"] == book_id, "库存"] = str(int(self.book_table["库存"][j])-1)
                        # self.book_table.loc[:,"库存"][j] -= 1 # 导致 settingwithCopyWarning

                        # 减去库存
                        print(f'{self.student_table["name"][i]}借走{self.book_table["bname"][j]}')
                        print(f'库存剩余 {self.book_table["书名"][j]}共 {self.book_table["库存"][j]} 本！')

                        # 注意下列写法不成立！
                        # mid = self.book_table["库存"][j] - 1
                        # self.book_table["库存"][j] = mid

                        borrow = [student_id, book_id, time.strftime("%d/%m/%Y")]
                        self.borrow_table.append(borrow)
                        self.save_file()
                        break
            if not flag1:
                break
        if flag1:
            print("未查询到该会员")
        print("借阅图书")

    # 实现还书功能：从表2中删除该学生的借阅信息，并修改表1的库存信息，并保存到文件

    def let_back(self, student_id, book_id):
        for j in range(len(self.book_table["书号"])):
            if int(self.book_table["书号"][j]) == int(book_id):

                self.book_table["库存"][j] = str(int(self.book_table["库存"][j]) + 1)
                for i in range(len(self.borrow_table)):
                    if int(self.borrow_table[i][0]) == int(student_id) and int(self.borrow_table[i][1]) == int(book_id):
                        del self.borrow_table[i]
                        self.save_file()
                        break
                break

        print("还书")

    # 输入某书号，可以查询借阅该书的学生信息
    def find_by_book_id(self, book_id):
        stu_ids = set()
        # 先获取对应人的学号
        for i in range(len(self.borrow_table)):
            if int(self.borrow_table[i][1]) == int(book_id):
                stu_ids.add(int(self.borrow_table[i][0]))
        stu = []
        for i in range(len(self.student_table["会员号"])):
            if int(self.student_table["会员号"][i]) in stu_ids:
                stu.append(self.student_table.iloc[i])
        print("查询借了某本书的会员信息")
        print(stu)

    def sum_by_student_id(self, student_id):
        sum = 0
        for i in range(len(self.borrow_table)):
            if int(self.borrow_table[i][0]) == int(student_id):
                sum += 1
        print("统计某学生当前借书量 " + str(sum))

    # 统计某出版社的藏书量，统计某学生当前借书量
    def sum_by_publish(self, publish_name):
        book_id = set()
        sum = 0
        for i in range(len(self.book_table["出版社"])):
            if str(self.book_table["出版社"][i]) == str(publish_name):
                book_id.add(int(self.book_table["出版社"][0]))
                sum += int(self.book_table["库存"][i])
        for i in range(len(self.borrow_table)):
            if self.borrow_table[i][1] in book_id:
                sum += 1
        print(str(publish_name) + "统计藏书量 " + str(sum))
        return sum

    # 输入某学生姓名，可以查询该生的借阅图书信息
    def find_by_student_name(self, student_name):
        stu_id = set()
        for i in range(len(self.student_table["姓名"])):
            if str(self.student_table["姓名"][i]) == str(student_name):
                stu_id.add(int(self.student_table["会员号"][i]))
                print("找到")
        book_id = set()
        res = []
        for i in range(len(self.borrow_table)):
            if int(self.borrow_table[i][0]) in stu_id:
                book_id.add(int(self.borrow_table[i][1]))
        for i in range(len(self.book_table["书号"])):
            if int(self.book_table["书号"][i]) in book_id:
                res.append(self.book_table.iloc[i])
        print("查询某学生的借书信息：")
        print("没有借过书！" if len(res) else f"{student_name}借过的书是 {res}")

    # 获取各出版社的藏书量折线图
    def get_publish(self):
        pub = set()
        for i in range(len(self.book_table["出版社"])):
            pub.add(str(self.book_table["出版社"][i]))
        pubL = list(pub)
        x1 = range(len(pubL))
        numL = []
        for i in range(len(pubL)):
            numL.append(self.sum_by_publish(pubL[i]))
        plt.title('各出版社的藏书量折线图')
        plt.xlabel('出版社名字')
        plt.ylabel('藏书量')
        plt.plot(pubL, numL, 'r', label='藏书量')
        plt.xticks(x1, pubL, rotation=0)
        plt.legend()
        plt.grid()
        plt.show()
        # 利用第三方库matplotlib中的pyplot绘制统计图，如绘制各出版社的藏书量折线图，绘制各学生借书量的饼图等

    def get_stu(self):
        stu_id = set()
        for i in range(len(self.student_table["会员号"])):
            stu_id.add(int(self.student_table["会员号"][i]))
        stuL = list(stu_id)
        numL = []
        for i in range(len(stuL)):
            numL.append(self.sum_by_student_id(stuL[i]))

        plt.rcParams['font.sans-serif'] = 'SimHei'  # 设置中文显示
        plt.figure(figsize=(6, 6))  # 将画布设定为正方形，则绘制的饼图是正圆
        plt.pie(numL, labels=stuL, autopct='%1.1f%%')  # 绘制饼图
        plt.title('2018年饼图')  # 绘制标题
        plt.show()

    # 1绘制各出版社的藏书量折线图，2绘制各学生借书量的饼图
    def show_diaglo(self, chos):
        if str(chos) == "1":
            self.get_publish()
        if str(chos) == '2':
            self.get_stu()
        print("展现图表")

    def cls(self):
        os.system("cls")

    def menu(self):
        level_1_choose = input("按回车继续菜单选项：")
        while level_1_choose != "N":
            self.cls()
            print("---- 图书管理系统菜单 -----\n")
            print("已完成的功能标记为 -> ")
            print("1 借阅功能 请输入-> 1 学号 书号")
            print("2 还书功能 请输入-> 2 学号 书号")
            print("3 查询会员借阅历史->  请输入： 3 学生姓名")
            print("4 按书名查询借阅会员  请输入： 4 书号")
            print("5 统计按出版社的藏书量  请输入： 5 出版社名")
            print("6 统计会员当前的借书量  请输入： 6 学生学号")
            print("7 绘图功能 请输入：7")
            print("++++++++++++++++++++++++++++++++++++++++++")
            level_1_choose = input("请选择0-7你要选择的功能,输入N退出: ")
            turn = True
            while turn:
                sp = level_1_choose.split()
                # 0-7

                # if sp[0] == '0':
                #    self.book_table
                #    turn = False

                if sp[0] == "1":
                    if len(sp) == 3:
                        self.borrow(sp[1], sp[2])
                        turn = False
                    else:
                        turn = True
                        level_1_choose = input("输入错误，请重新输入\n")
                elif sp[0] == "2":
                    if len(sp) == 3:
                        self.let_back(sp[1], sp[2])
                        turn = False
                    else:
                        turn = True
                        level_1_choose = input("输入错误，请重新输入\n")
                elif sp[0] == "3":
                    if len(sp) == 2:
                        self.find_by_student_name(sp[1])
                        turn = False
                    else:
                        turn = True
                        level_1_choose = input("输入错误，请重新输入\n")
                elif sp[0] == "4":
                    if len(sp) == 2:
                        self.find_by_book_id(sp[1])
                        turn = False
                    else:
                        turn = True
                        level_1_choose = input("输入错误，请重新输入\n")
                elif sp[0] == "5":
                    if len(sp) == 2:
                        self.sum_by_publish(sp[1])
                        turn = False
                    else:
                        turn = True
                        level_1_choose = input("输入错误，请重新输入\n")
                elif sp[0] == "6":
                    if len(sp) == 2:
                        self.sum_by_student_id(sp[1])
                        turn = False
                    else:
                        turn = True
                        level_1_choose = input("输入错误，请重新输入\n")
                elif sp[0] == "7":
                    if len(sp) == 2:
                        self.show_diaglo(sp[1])
                        turn = False
                    else:
                        turn = True
                        level_1_choose = input("输入错误，请重新输入\n")
                else:
                    turn = True
                    level_1_choose = input("输入错误，请重新输入\n")


if __name__ == '__main__':
    ls = library_system()

