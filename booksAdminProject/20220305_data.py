
#周刊统计:(本)(8)    (5)            (2)              (1)
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
《看图说话》《好词好句》《看图写话》《看图作文》。《日记起步》

'''
c = "abcd , ."
a=c.replace('a','z')
print(a)

last_date = "1/2/3"  #   目标为"123"

#之一：repalce

date =last_date.replace('/','')
print(date)

mark = ["。","？","\n","、",","]
ans = book
for dot in mark:
    #print(ans)
    ans = ans.replace(dot,"")
print("anstring:",ans)

qwe=book.replace("。","")
aaa=qwe.replace("？","")
abc=aaa.replace("\n","")
ewq=abc.replace("、","")
print(ewq)
booklist = ewq.split("》")
#booklist.replace
print(booklist)
print(len(booklist))

bookshelf = []
for w in booklist:
    bookshelf.append(w[1:])
print(bookshelf)


print(sorted(bookshelf,reverse=True)) #lambda x:x[0]

while True:
    wasd=input("查询：")
    if wasd in bookshelf:
        print(wasd,"在bookshelf里面")
    elif wasd not in bookshelf:
        for book in bookshelf:
            if wasd in book:
                print("你找的是不是",f"《{book}》" "在bookshelf里面，你借的是这本书吗？")

            continue
    else:
        print("你把书名打错了")

