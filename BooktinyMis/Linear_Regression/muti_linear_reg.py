import matplotlib.pyplot as plt

import numpy as np
import seaborn as sns
from scipy.stats import skew
#%matplotlib inline
import pandas as pd
plt.style.use("ggplot")
plt.rcParams['figure.figsize'] = (15, 10)

csv_url = "I:\\data_science\\csvTraining\\Multiple-Linear-Regression-main\\Datav1.0.csv"
ad = pd.read_csv(csv_url)
ad.info()

print(ad)

sns.pairplot(ad,x_vars=['TV','radio','newspaper'],y_vars='sales',height=7,aspect=0.7)


from sklearn.linear_model import LinearRegression
X= ad[['TV','radio','newspaper']]
y=ad.sales
l = LinearRegression()
l.fit(X,y)
print(l.intercept_)
print(l.coef_)

sns.heatmap(ad.corr(),annot=True)

from sklearn.metrics import r2_score
l2=LinearRegression().fit(X[['TV','radio']],y)
l2_preds = l2.predict(X[['TV','radio']])
print('R^2 score',r2_score(y,l2_preds))

from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
X= ad[['TV','radio','newspaper']]
y= ad.sales
X_train, X_test, y_train, y_test = train_test_split(X,y,random_state=1)
l4 =LinearRegression().fit(X_train,y_train)
l4_preds = l4.predict(X_test)
print("RMSE",np.sqrt(mean_squared_error(y_test,l4_preds)))
print("R^2:", r2_score(y_test,l4_preds))