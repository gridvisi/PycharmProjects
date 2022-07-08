# https://www.delftstack.com/zh/howto/python-pandas/write-a-pandas-dataframe-to-csv/

#1
import pandas as pd

mid_term_marks = {"Student": ["Kamal", "Arun", "David", "Thomas", "Steven"],
                  "Economics": [10, 8, 6, 5, 8],
                  "Fine Arts": [7, 8, 5, 9, 6],
                  "Mathematics": [7, 3, 5, 8, 5]}

mid_term_marks_df = pd.DataFrame(mid_term_marks)
mid_term_marks_df.to_csv("I:\\data_science\\csvTraining\\midterm.csv")
csv_file = "I:\\data_science\\csvTraining\\midterm.csv"
csv_data = pd.read_csv(csv_file, low_memory = False)#防止弹出警告
csv_df = pd.DataFrame(csv_data)
print(csv_df)


#2 index= False

import pandas as pd

mid_term_marks = {"Student": ["Kamal", "Arun", "David", "Thomas", "Steven"],
                  "Economics": [10, 8, 6, 5, 8],
                  "Fine Arts": [7, 8, 5, 9, 6],
                  "Mathematics": [7, 3, 5, 8, 5]}


#mid_term_marks_df = pd.DataFrame(mid_term_marks)
#mid_term_marks_df.to_csv("midterm.csv", index=False)

mid_term_marks_df = pd.DataFrame(mid_term_marks)
mid_term_marks_df.to_csv("I:\\data_science\\csvTraining\\midterm_F.csv",index = False)

csv_file = "I:\\data_science\\csvTraining\\midterm_F.csv"
csv_data = pd.read_csv(csv_file, low_memory = False)#防止弹出警告
csv_df = pd.DataFrame(csv_data)
print(csv_df)


#3 sep
import pandas as pd

mid_term_marks = {"Student": ["Kamal", "Arun", "David", "Thomas", "Steven"],
                  "Economics": [10, 8, 6, 5, 8],
                  "Fine Arts": [7, 8, 5, 9, 6],
                  "Mathematics": [7, 3, 5, 8, 5]}


mid_term_marks_df = pd.DataFrame(mid_term_marks)
mid_term_marks_df.to_csv("I:\\data_science\\csvTraining\\midterm_s.csv", index=False, sep="\t")


csv_file = "I:\\data_science\\csvTraining\\midterm_s.csv"
csv_data = pd.read_csv(csv_file, low_memory = False)#防止弹出警告
csv_df = pd.DataFrame(csv_data)
print(csv_df)



# DataFrame增加一条记录

score = mid_term_marks

#1. 如果记录是dict类型，直接append即可
course = {'python':[9,7,8,6,10]}
score = score.append(course,ignore_index=True)
print(score)

#2. 如果记录是list类型，则先把单条记录转为Series类型

#Series与DataFrame合并有两种方法

#法1：直接append
#record = record.append(s, ignore_index=True)
#法2：显式指定行进行合并
#record.loc[2] = s

