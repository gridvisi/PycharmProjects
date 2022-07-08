# https://zhuanlan.zhihu.com/p/401921763
# https://zhuanlan.zhihu.com/p/27049969
# python进行数据分析之数据加载、存储与文件格式（五
# https://github.com/wesm/pydata-book


import pandas as pd
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

print(dfmi.loc[:, ('one', 'second')][0])

dfmi.loc[:, ('one', 'second')][0] = 'B'
print(dfmi.loc[:, ('one', 'second')][0])

print(dfmi.loc[:, ('one', 'second')][2].upper())

dfmi.loc[:, ('one', 'second')][0] = 10
dfmi.loc[:, ('one', 'second')][0] += 7
print(dfmi.loc[:, ('one', 'second')][0])

'''
    one          two       
  first second first second
0     a      b     c      d
1     e      f     g      h
2     i      j     k      l
3     m      n     o      p


但事实证明，分配给链式索引的乘积本质上具有不可预测的结果。
要看到这一点，请考虑 Python 解释器如何执行此代码：

dfmi.loc[:, ('one', 'second')] = value
# becomes
dfmi.loc.__setitem__((slice(None), ('one', 'second')), value)
But this code is handled differently:
但是这段代码的处理方式不同：

dfmi['one']['second'] = value
# becomes
dfmi.__getitem__('one').__setitem__('second', value)
'''

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
