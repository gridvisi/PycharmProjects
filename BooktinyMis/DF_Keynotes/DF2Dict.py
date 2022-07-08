# https://www.zhihu.com/question/507347374
import pandas as pd

df = pd.DataFrame([['Jay',16,'BBA'],
                   ['Jack',19,'BTech'],
                   ['Mark',18,'BSc']],
                  columns = ['Name','Age','Course'])

d1 = df.to_dict()
print(d1)

'''
2.Pandas DataFrame 转换字典的方法我们可以通过参数list、records、series、index、split和dict来改变最终字典的格式。例如，当我们传递list和series作为参数时，我们将列名作为键，但值对分别被转换为列表和系列行。下面的例子将证明这一点。

'''
import pandas as pd

df = pd.DataFrame([['Jay',16,'BBA'],
                   ['Jack',19,'BTech'],
                   ['Mark',18,'BSc']],
                  columns = ['Name','Age','Course'])

d_list  = df.to_dict('list')
print(d_list)

d_series = df.to_dict('series')
print(d_series)


'''
3.Pandas DataFrame 转换为字典列表

我们也可以将每一行作为一个单独的字典传递给函数 records。
最后的结果是一个列表，每一行都是一个字典。例如：
'''

import pandas as pd

df = pd.DataFrame([['Jay',16,'BBA'],
                   ['Jack',19,'BTech'],
                   ['Mark',18,'BSc']], columns = ['Name','Age','Course'])

d_records = df.to_dict('records')
print(d_records)

'''
4.Pandas DataFrame 按行转为字典

但是在很多情况下，我们可能不希望列名作为字典的键。对于这种情况，我们可以传递index来使 DataFrame 索引作为键。
下面的代码片段展示了这一点。
'''

import pandas as pd

df = pd.DataFrame([['Jay',16,'BBA'],
                   ['Jack',19,'BTech'],
                   ['Mark',18,'BSc']], columns = ['Name','Age','Course'])

d_index = df.to_dict('index')
print(d_index)

'''
5.Dataframe 转为以一列为键的字典

但是，如果我们喜欢用一列的元素作为键，而用其他列的元素作为值呢？这可以通过简单地将所需的列作为 DataFrame 的索引，
并使用 .T() 函数对其进行转置来实现。

例子:
'''

import pandas as pd

df = pd.DataFrame([['Jay',16,'BBA'],
                   ['Jack',19,'BTech'],
                   ['Mark',18,'BSc']], columns = ['Name','Age','Course'])

d_names = df.set_index('Name').T.to_dict('list')
print(d_names)


'''
6.使用 dict() 和 zip() 函数将 Pandas DataFrame 转为字典Python dict() 函数也可以将 Pandas DataFrame 转换为字典。
我们还应该使用 zip() 函数，将各个列作为它的参数来创建并行迭代器。然后 zip() 函数将在每次迭代中产生一行的所有值。

'''

import pandas as pd

df = pd.DataFrame([['Jay',16,'BBA'],
                   ['Jack',19,'BTech'],
                   ['Mark',18,'BSc']], columns = ['Name','Age','Course'])

d =  dict([(i,[a,b]) for i,a,b in zip(df['Name'], df['Age'],df['Course'])])
print(d)


