'''
5万多位专业开发者的反馈是：
11% 很喜欢 very favorable
20% 喜欢   favorable
26% 不关心，中性 indifferent
15% 不喜欢 unfavorable
17% 很不喜欢 very unfavorable
10% 不知道 unsure
基本上是个正态分布，很符合现在 web3 极早期的现状
'''
import pandas as pd
my_data = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 8, 6, 4, 2])
my_data.hist()