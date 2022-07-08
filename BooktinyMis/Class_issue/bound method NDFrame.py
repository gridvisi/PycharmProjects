'''
https://stackoverflow.com/questions/62113891/i-am-getting-as-bound-method-ndframe-head-of-while-displaying-output-in-pytho
'''

import pandas as pd
def date_calendar(table, startdate, enddate, datefreq):

    # create a df
    df = pd.DataFrame({
        'Year': [],
        'FY Year': [],
        'Quarter': [],
        'MonthNum': [],
        'YearMonth': [],
        'YearMonthShort': [],
        'YearMonthNum': [],
        'Date': [],
        })

    # create a date_range specified in function inputs
    per1 = pd.date_range(start=startdate,
                         end=enddate, freq=datefreq)

    # make the date_range into a series because .append method doesn't work if per1 is not a series
    per2 = per1.to_series()

    # append series to df
    df['Date'].append(per2)
    return df

table = []
print(date_calendar(table, startdate='1-1-2019', enddate='6-30-2024', datefreq='D'))


def date_calendar(startdate, enddate, datefreq):

# create a df
    df = pd.DataFrame({
            'Year': [],
            'FY Year': [],
            'Quarter': [],
            'MonthNum': [],
            'YearMonth': [],
            'YearMonthShort': [],
            'YearMonthNum': [],
            'Date': [],
        })

    # create a date_range specified in function inputs
    per1 = pd.date_range(start=startdate,
                             end=enddate, freq=datefreq)

    # make the date_range into a series because .append method doesn't work if per1 is not a series
    per2 = per1.to_series()

    # append series to df
    df['Date'] = df['Date'].append(per2)
    return df

print(date_calendar(startdate='1-1-2019', enddate='6-30-2024', datefreq='D'))