'''
https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.loc.html
'''
import pandas as pd
df = pd.DataFrame([[1, 2], [4, 5], [7, 8]],
     index=['cobra', 'viper', 'sidewinder'],
     columns=['max_speed', 'shield'])
print(df)

print(df.loc['viper'])

print(df.loc[['viper', 'sidewinder']])

print(df.loc['cobra', 'shield'])

print(df.loc['cobra':'viper', 'max_speed']

import pygame
import wzj
import turtle as t
t.forward(100)
t.left(90)
