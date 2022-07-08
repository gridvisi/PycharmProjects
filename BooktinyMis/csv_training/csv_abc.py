# https://zhuanlan.zhihu.com/p/27049969
# python进行数据分析之数据加载、存储与文件格式（五
# https://github.com/wesm/pydata-book

# https://zhuanlan.zhihu.com/p/30970391

import pandas as pd

csv_file = "I:\\data_science\\bookmis\\table3.csv"
csv_data = pd.read_csv(csv_file, low_memory=False)#防止弹出警告
csv_df = pd.DataFrame(csv_data)
print(csv_df)
print(csv_df.get('借阅日期',"没有这一项"))


data = '''
| City         | State        | Capital | Population    |
| ------------ | ------------ | ------- | ------------- |
| Philadelphia | Pennsylvania | No      | 1.581 Million |
| Sacramento   | California   | Yes     | 0.5 Million   |
| New York     | New York     | No      | 8.623 Million |
| Austin       | Texas        | Yes     | 0.95 Million  |
| Miami        | Florida      | No      | 0.463 Million |
'''

import pandas as pd


city = pd.DataFrame({'City':['Sacramento', 'California'],
                     'State':['Miami', 'Florida']
                     })

city.to_csv('I:\\data_science\\csvTraining\\city.csv')
print(city)

#columns
city = pd.DataFrame([['Sacramento', 'California'], ['Miami', 'Florida']],
                    columns=['City', 'State'])
city.to_csv('I:\\data_science\\csvTraining\\city.csv')

print(city)


# https://zhuanlan.zhihu.com/p/401921763

dfmi = pd.DataFrame([list('abcd'),
                     list('efgh'),
                      list('ijkl'),
                      list('mnop')],
                     columns=pd.MultiIndex.from_product([['one', 'two'],
                                                         ['first', 'second']]))
print(dfmi)
print(dfmi['one']['second'])

#Better solve
print(dfmi.loc[:, ('one', 'second')])

'''
但事实证明，分配给链式索引的乘积本质上具有不可预测的结果。要看到这一点，请考虑 Python 解释器如何执行此代码：

dfmi.loc[:, ('one', 'second')] = value
# becomes
dfmi.loc.__setitem__((slice(None), ('one', 'second')), value)
But this code is handled differently:
但是这段代码的处理方式不同：

dfmi['one']['second'] = value
# becomes
dfmi.__getitem__('one').__setitem__('second', value)
'''



import pandas as pd
import csv

books_url = "I:\\data_science\\bookmis\\books.csv"
#books_header = ["书号", "书名", "出版社", "作者", "价格", "库存"]
books_header = ['bookid','booth','status','bname','publish','aurtor','price','number']

# 读取
reader = csv.reader(open(books_url, 'r', encoding='gbk'))
#reader = csv.reader(open(books_url, 'r', encoding='cp936'))
r = pd.DataFrame(reader)
print(r)



data_or_path = reader
df = pd.read_clipboard()
df = pd.read_csv(data_or_path)
df = pd.read_html(data_or_path)
df = pd.read_json(data_or_path)
df = pd.read_msgpack(data_or_path)
df = pd.read_pickle(data_or_path)

df.to_clipboard()
df.to_csv()
df.to_csv(fn)
df.to_excel(fn)
df.to_html()
df.to_html(fn)
df.to_json()
df.to_json(fn)
df.to_msgpack()
df.to_msgpack(fn)
df.to_pickle(fn)

# 转 dict 时 orient
# orient : str {‘dict’, ‘list’, ‘series’, ‘split’, ‘records’, ‘index’}
# Determines the type of the values of the dictionary.
#    dict (default) : dict like {column -> {index -> value}}
#    list : dict like {column -> [values]}
#    series : dict like {column -> Series(values)}
#    split : dict like {index -> [index], columns -> [columns], data -> [values]}
#    records : list like [{column -> value}, ... , {column -> value}]
#    index : dict like {index -> {column -> value}}


# 转 json 时 orient
# orient : string
# The format of the JSON string
#    split : dict like {index -> [index], columns -> [columns], data -> [values]}
#    records : list like [{column -> value}, ... , {column -> value}]
#    index : dict like {index -> {column -> value}}
#    columns : dict like {column -> {index -> value}}
#    values : just the values array
#    table : dict like {‘schema’: {schema}, ‘data’: {data}} describing the data, and the data component is like orient='records'.

# 其余不一一列出，详见
# http://pandas.pydata.org/pandas-docs/stable/api.html#id12