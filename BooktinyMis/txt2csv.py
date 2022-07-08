
import time

import pandas as pd
import os
import matplotlib.pyplot as plt

book = '''《学会担当》《注音版红楼梦》《三国演义》《水许传》《太阳溪农场的丽贝卡》《海底两万里》
《草房子》《积极才能成功》《坦克与装甲车》成语故事》《夏洛的网》《中小学公共安全与生命考有(四下)》
《三国演义(白化文)》《综台实,践活动(四下)》《一年级生字墓写本》《句子专项圳练》《道德与法治》、
《木公又玄秘塔》、《五下科等》、《老版高中语文知识手册》、《一年级的马小跳》《宜家IKEA家居册》
《世界儿童周刊1-8》《小哥白尼周刊》《幽黑小读者周刊》《课堂内外周刊》

《小学年级奥数》、《西游记(上)》、《给孩子的诗2》、《详一反三奥数》、《钢铁是怎样炼成的》
《马小跳·侦探小组在行动》、《疯狂学校我们的签班主任》《孔乙己》《阿Q正传》《狂人日记》、
《为了忘却的记念》、《论雷峰塔的倒掉》《大学书法》《岛蛋鬼日记》、《北大门暑夫》、《老人与海》
《彷徨》、《月花夕拾》、《免骨寻踪》、《烙材童话》《三上所写给孩子的名人传记习》、《同桌冤家》、
《洋葱头历险记》。《些成语故事》《科普馆》、《西游记·田文》、《中国神话故事》《作文小状元》。
《人名言》《成语故事》。
《吹牛大王·历险记习》、《假如给我三天光明》。《野草习夏日历险》、《安徒生童话》《少年侦探团》、
《少年侦探团5》《马小跳6年级》《学语文之友》《中华民族是一家人》《中华民方族是一家2》、
《马小北5年级》《马小跳1年级》《马小跳4年级》、《爱我中华》《科科技托起强因梦》、《少年优探团2》、
《鲁鲁龙的礼物》《小贝弟的大梦想》。《一个长上天的大苹果》《是谁在门外》《作文起步》、《优秀作文》
《看图说话》《好词好句》《看图写话》《看图作文》。《日记起步》'''


mark = ["。","？","\n","、",","]
ans = book
for dot in mark:
    ans = ans.replace(dot,"")
start = time.time()
print("filterPunctuation:",ans)
end = time.time()
print(end - start)
bookstring = '''《学会担当》《注音版红楼梦》《三国演义》《水许传》《太阳溪农场的丽贝卡》《海底两万里》《草房子》《积极才能成功》《坦克与装甲车》成语故事》《夏洛的网》《中小学公共安全与生命考有(四下)》《三国演义(白化文)》《综台实践活动(四下)》《一年级生字墓写本》《句子专项圳练》《道德与法治》《木公又玄秘塔》《五下科等》《老版高中语文知识手册》《一年级的马小跳》《宜家IKEA家居册》《世界儿童周刊1-8》《小哥白尼周刊》《幽黑小读者周刊》《课堂内外周刊》《小学年级奥数》《西游记(上)》《给孩子的诗2》《详一反三奥数》《钢铁是怎样炼成的》《马小跳·侦探小组在行动》《疯狂学校我们的签班主任》《孔乙己》《阿Q正传》《狂人日记》《为了忘却的记念》《论雷峰塔的倒掉》《大学书法》《岛蛋鬼日记》《北大门暑夫》《老人与海》《彷徨》《月花夕拾》《免骨寻踪》《烙材童话》《三上所写给孩子的名人传记习》《同桌冤家》《洋葱头历险记》《些成语故事》《科普馆》《西游记·田文》《中国神话故事》《作文小状元》《人名言》《成语故事》《吹牛大王·历险记习》《假如给我三天光明》《野草习夏日历险》《安徒生童话》《少年侦探团》《少年侦探团5》《马小跳6年级》《学语文之友》《中华民族是一家人》《中华民方族是一家2》《马小北5年级》《马小跳1年级》《马小跳4年级》《爱我中华》《科科技托起强因梦》《少年优探团2》《鲁鲁龙的礼物》《小贝弟的大梦想》《一个长上天的大苹果》《是谁在门外》《作文起步》《优秀作文》《看图说话》《好词好句》《看图写话》《看图作文》《日记起步》
'''

#booklist = bookstring.split("》")
booklist = []
for w in bookstring.split("》"):
    booklist.append(w[1:])
print(len(booklist), booklist)





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
        table1 = []
        print("输入藏书表:书号 书名 出版社 作者 价格 库存\n")
        for i,book in enumerate(booklist):
            strg = [i,book,"","",0,10]

            if len(strg) != 6:
                print(f'列数不一致,请重新输入第 {i} 行')
            else:
                table1.append(strg)

        print(table1)

        table1 = pd.DataFrame(table1)
        table1.to_csv(Config.table1_url, header=Config.table1_header, index=None)

    def get_info_from_file(self):
        book_table = pd.read_csv(Config.table1_url)
        borrow_table = []
        student_table = pd.read_csv(Config.table3_url)
        print("信息读取成功...")

    def save_file(self):
        self.book_table.to_csv(Config.table1_url, header=Config.table1_header, index=None)
        boo = pd.DataFrame(self.borrow_table)
        boo.to_csv(Config.table2_url, header=Config.table2_header, index=None)
        self.student_table.to_csv(Config.table3_url, header=Config.table3_header, index=None)
        print("保存文件成功")





if __name__ == '__main__':
    ls = library_system()


'''

table1 = pd.DataFrame(table1)
table3 = pd.DataFrame(table3)
table1.to_csv(Config.table1_url, header=Config.table1_header, index=None)
table3.to_csv(Config.table3_url, header=Config.table3_header, index=None)

'''