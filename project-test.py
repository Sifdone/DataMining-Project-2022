from sqlite3 import Date, Time
import pandas as pd
from matplotlib import pyplot as plt
import glob
import os
import datetime


def transform(name):

    year = int(name[0:4])
    if name[4] == "0":
        month = int(name[5])
    else:
        month = int(name[4:6])
    if name[6] == "0":
        day = int(name[7])
    else:
        day = int(name[6:8])

    date = datetime.datetime(year,month,day)

    return date

files_joined = os.path.join('C:\\Users\\Dimitra\\Documents\\GitHub\\DataMining-Project-2022\\dataset\\sources', "*.csv")
files = glob.glob(files_joined)
df = pd.concat([pd.read_csv(fp).assign(Date=transform(os.path.basename(fp).split('.')[0]))
for fp in files])
print(df)

year1 = df[(df.Date <'2021-01-01') & (df.Date >'2019-12-31') ]

#Wind
#print(df.describe()[['Wind']])
#Graph of whole Wind Dataset
#plt.plot(df.Date, df.Wind)

#Graph of one year
ddate = year1.groupby('Date')['Wind'].mean()

yearByDate = year1.groupby('Date')

yearByDateMean = yearByDate.agg('mean').reset_index()


#test =ddate.to_frame()
#print(test)

plt.plot(yearByDateMean.Date, yearByDateMean.Wind)
plt.plot(yearByDateMean.Date, yearByDateMean.Solar)
plt.plot(yearByDateMean.Date, yearByDateMean.Geothermal)
plt.plot(yearByDateMean.Date, yearByDateMean.Nuclear)
plt.plot(yearByDateMean.Date, yearByDateMean['Natural Gas'])
plt.plot(yearByDateMean.Date, yearByDateMean.Imports)






plt.show()