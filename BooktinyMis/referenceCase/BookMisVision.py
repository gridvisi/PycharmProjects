
import time

import pandas as pd
import os
import matplotlib.pyplot as plt

# 先定义一个配置类
#from Tools.scripts.treesync import raw_input


class Config:
    # 定义表一
    table1_url = "I:\\data_science\\bookmis\\table1.csv"
    table1_header = ["书号", "书名", "出版社", "作者", "价格", "库存"]
    # 定义表二
    table2_url = "I:\\data_science\\bookmis\\table2.csv"
    table2_header = ["学号", "书号", "借阅日期"]
    # 定义表三
    table3_url = "I:\\data_science\\bookmis\\table3.csv"
    table3_header = ["学号", "姓名", "性别", "年级"]

class library_system(object):
    def __init__(self):
        print("图书馆系统初始化中...")
        self.input_table1_table2()
        self.book_table, self.borrow_table, self.student_table = self.get_info_from_file()
        print("图书馆系统初始化完成！\n")
        self.menu()

    def input_table1_table2(self):
        print("请输入图书馆藏书表")

        #table1建议改写为 读取本地table1.csv！

        table1 = [[0, '学会担当', '', '', 0, 10], [1, '注音版红楼梦', '', '', 0, 10], [2, '三国演义', '', '', 0, 10],
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
                  [53, '作文小状元', '', '', 0, 10], [54, '人名言', '', '', 0, 10], [55, '成语故事', '', '', 0, 10], [56, '吹牛大王·历险记习', '', '', 0, 10],
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

        print("输入藏书表:书号 书名 出版社 作者 价格 库存\n")
        print(f'书号顺序按数字小到大,前一条书号是 {len(table1)}')
        #85 哈利波特 儿童 J.K.罗琳 30 2

        x = input('请输入数据：')
        while x != "none":
            y = x.split()
            if len(y) != 6:
                x = input('列数不一致\n请重新输入:')
            else:
                table1.append(y)
                x = input('下一条记录:')

        print(table1)

        print("请输入学生信息表")
        #table3 = [] #修改为读取table3.csv

        csv_file = "I:\\data_science\\bookmis\\table3.csv"
        csv_data = pd.read_csv(csv_file, low_memory=False)  # 防止弹出警告
        table3 = pd.DataFrame(csv_data)
        print(table3)
        print("************************************")
        print("输入会员信息 : 学号 姓名 性别 年级\n")
        prev = len(table3)
        studentid = str(10000 + prev)[1:]
        print(f'会员号按数字小到大,前一条学生号是 {studentid}')

        #0001 李晶 男 k10
        #0002 张敏 女 k12
        #0003 赵淼 男 k12

        x = input('请输入数据:')

        while x != "none":
            y = x.split()
            if len(y) != 4:
                x = input('数据列数不一致\n请重新输入:')
            else:
                table3.append(y)
                x = input('下一条记录:')

        print(table3)

        table1 = pd.DataFrame(table1)
        table3 = pd.DataFrame(table3)
        table1.to_csv(Config.table1_url, header=Config.table1_header, index=None)
        table3.to_csv(Config.table3_url, header=Config.table3_header, index=None)

    def get_info_from_file(self):
        book_table = pd.read_csv(Config.table1_url)
        borrow_table = []
        student_table = pd.read_csv(Config.table3_url)
        print("信息读取成功...")
        return book_table, borrow_table, student_table

    def save_file(self):
        self.book_table.to_csv(Config.table1_url, header=Config.table1_header, index=None)
        boo = pd.DataFrame(self.borrow_table)
        boo.to_csv(Config.table2_url, header=Config.table2_header, index=None)
        self.student_table.to_csv(Config.table3_url, header=Config.table3_header, index=None)
        print("保存文件成功")

    # 实现借阅功能：输入学号和书号，如果借阅成功
    # 学号所对应的学生在表3中并且
    # 书号所对应的图书在表1中且库存大于等于1，
    # 修改表1和表2，并保存到文件
    def borrow(self, student_id, book_id):
        flag1 =True
        for i in range(len(self.student_table["学号"])):
            if int(self.student_table["学号"][i])==int(student_id):
                print(f'查询到该学生：{self.student_table["学号"][i]} {self.student_table["姓名"][i]}')
                flag1 =False
                for j in range(len(self.book_table["书号"])):
                    if int(self.book_table["书号"][j+1] )==int(book_id) and int(self.book_table["库存"][j+1]) >0:
                        print("库存充足")
                        self.book_table["库存"][j+1] = str(int(self.book_table["库存"][j+1]) -1)
                        borrow = [student_id ,book_id, time.strftime("%d/%m/%Y")]
                        self.borrow_table .append(borrow)
                        self.save_file()
                        break
            if not flag1:
                break
        if flag1:
            print("未查询到该学生")
        print("借阅图书")

    # 实现还书功能：从表2中删除该学生的借阅信息，并修改表1的库存信息，并保存到文件
    def let_back(self, student_id, book_id):
        for j in range(len(self.book_table["书号"])):
            if int(self.book_table["书号"][j] )==int(book_id):
                self.book_table["库存"][j] = str(int(self.book_table["库存"][j] ) +1)
                for i in range(len(self.borrow_table)):
                    if int(self.borrow_table[i][0] )==int(student_id) and int(self.borrow_table[i][1] )==int(book_id):
                        del self.borrow_table[i]
                        self.save_file()
                        break
                break

        print("还书")

    # 输入某书号，可以查询借阅该书的学生信息
    def find_by_book_id(self, book_id):
        stu_ids =set()
        # 先获取对应人的学号
        for i in range(len(self.borrow_table)):
            if int(self.borrow_table[i][1] )==int(book_id):
                stu_ids.add(int(self.borrow_table[i][0]))
        stu =[]
        for i in range(len(self.student_table["学号"])):
            if int(self.student_table["学号"][i]) in stu_ids:
                stu.append(self.student_table.iloc[i])
        print("查询借了某本书的学生信息")
        print(stu)

    def sum_by_student_id(self, student_id):
        sum =0
        for i in range(len(self.borrow_table)):
            if int(self.borrow_table[i][0] )==int(student_id):
                sum+=1
        print("统计某学生当前借书量 " +str(sum))

    # 统计某出版社的藏书量，统计某学生当前借书量
    def sum_by_publish(self, publish_name):
        book_id = set()
        sum =0
        for i in range(len(self.book_table["出版社"])):
            if  str(self.book_table["出版社"][i] )==str(publish_name):
                book_id.add(int(self.book_table["出版社"][0]))
                sum+=int(self.book_table["库存"][i])
        for i in range(len(self.borrow_table)):
            if self.borrow_table[i][1] in book_id:
                sum+=1
        print(str(publish_name ) +"统计藏书量 " +str(sum))
        return sum

    # 输入某学生姓名，可以查询该生的借阅图书信息
    def find_by_student_name(self, student_name):
        stu_id =set()
        for i in range(len(self.student_table["姓名"])):
            if str(self.student_table["姓名"][i] )==str(student_name):
                stu_id.add(int(self.student_table["学号"][i]))
                print("找到")
        book_id =set()
        res =[]
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
        for i in range(len(self.student_table["学号"])):
            stu_id.add(int(self.student_table["学号"][i]))
        stuL = list(stu_id)
        numL = []
        for i in range(len(stuL)):
            numL.append(self.sum_by_student_id(stuL[i]))

        plt.rcParams['font.sans-serif'] = 'SimHei'  # 设置中文显示
        plt.figure(figsize=(6, 6))  # 将画布设定为正方形，则绘制的饼图是正圆
        plt.pie(numL,  labels=stuL, autopct='%1.1f%%')  # 绘制饼图
        plt.title('2018年饼图')  # 绘制标题
        plt.show()
    # 1绘制各出版社的藏书量折线图，2绘制各学生借书量的饼图
    def show_diaglo(self ,chos):
        if str(chos )=="1":
            self.get_publish()
        if str(chos )=='2':
            self.get_stu()
        print("展现图表")

    def cls(self):
        os.system("cls")

    def menu(self):
        level_1_choose = input("按回车继续")
        while level_1_choose != "none":
            self.cls()
            print("图书管理系统菜单\n")
            print("0 查看全库： 浏览书名")
            print("1 借阅功能 请输入： 1 学号 书号")
            print("2 还书功能 请输入： 2 学号 书号")
            print("3 查询学生借阅信息  请输入： 3 学生姓名")
            print("4 查询借该书的学生信息  请输入： 4 书号")
            print("5 统计某出版社的藏书量  请输入： 5 出版社名")
            print("6 统计某学生当前的借书量  请输入： 6 学生学号")
            print("7 绘图功能 请输入：7")
            print("++++++++++++++++++++++++++++++++++++++++++")
            level_1_choose = input("请选择0-7你要选择的功能,输入none退出: ")
            turn = True
            while turn:
                sp = level_1_choose.split()
                # 0-7

                #if sp[0] == '0':
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






#原文链接：https :/ /blog.csdn.ne t /qq_2017600 1 /articl e /detail s /91358427