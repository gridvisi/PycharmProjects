# https://zhuanlan.zhihu.com/p/338309095
import csv
#C:\Users\29358\PycharmProjects\BooktinyMis\csv_training

with open('csv_training.csv', 'a', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames = header) # 提前预览列名，当下面代码写入数据时，会将其一一对应。
    writer.writeheader() # 写入列名
    writer.writerows('csv_training.csv') # 写入数据
print("数据已经写入成功！！！")

def csv_writer():
    a = []
    dict = student_infos[0]
    for headers in sorted(dict.keys()):  # 把字典的键取出来
        a.append(headers)
    header = a  # 把列名给提取出来，用列表形式呈现