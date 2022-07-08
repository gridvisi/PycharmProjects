'''
Identify the Inflation
https://xhinker.medium.com/identify-the-inflation-cause-using-python-bb8306a1b23

https://api.stlouisfed.org/fred/series/search?api_key=abcdefghijklmnopqrstuvwxyz123456&search_text=canada
'''
from fredapi import Fred
fred = Fred("869346e4ddc734bfa3c5f4fd43e7128a")
sp500 = fred.get_series('SP500')


from calendar import month
from fredapi import Fred
import dateutil.parser as dp
import matplotlib.pyplot as plt
import datetime

fred = Fred("869346e4ddc734bfa3c5f4fd43e7128a")

start_date = dp.parse('2012-01-01')
ukraine_war = dp.parse('2022-02-24')

cpi_mom = fred.get_series('CPIAUCSL')
cpi_mom = cpi_mom[cpi_mom.index > start_date]

fed_bonds = fred.get_series('WSHONBNL')
fed_bonds = fed_bonds[fed_bonds.index > start_date]

fig, ax1 = plt.subplots(figsize=(12,8))
ax2 = ax1.twinx()

ax1.plot(cpi_mom,c='blue')
ax2.plot(fed_bonds,c='green')

ax1.axvline(ukraine_war,c='red')
ax1.text(ukraine_war+datetime.timedelta(days=-1500),287
         ,'Russia invaded Ukraine \n On 24 Feb 2022 -->'
         ,fontsize=20)
ax1.text(ukraine_war+datetime.timedelta(days=-2300),240
         ,'FED started unlimited QE\n in March 2020         -->'
         ,fontsize=20)
plt.show()



from calendar import month
from fredapi import Fred
import dateutil.parser as dp
import matplotlib.pyplot as plt
import datetime

fred = Fred("api key")

start_date = dp.parse('2012-01-01')
ukraine_war = dp.parse('2022-02-24')

cpi_mom = fred.get_series('CPIAUCSL')
cpi_mom = cpi_mom[cpi_mom.index > start_date]

plt.figure(figsize=(12,8))
plt.plot(cpi_mom)
plt.axvline(ukraine_war,c='red')
plt.text(ukraine_war+datetime.timedelta(days=-1500),287
         ,'Russia invaded Ukraine \n On 24 Feb 2022    -->'
         ,fontsize=20)
plt.text(ukraine_war+datetime.timedelta(days=-2200),265
         ,'Consumer Price Index \n started spike up in 2021 -->'
         ,fontsize=20)
plt.show()