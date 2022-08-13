from sqlite3 import Date, Time
import pandas as pd
from matplotlib import pyplot as plt
import glob
import os
import datetime
import numpy as np

"""#simple csv merge
# merging the files
files_joined = os.path.join('D:\\Documents\\UNIVERSITY\\project_mining_2022\\dataset\\sources', "*.csv")
#print(files_joined)
# Return a list of all joined files
list_files = glob.glob(files_joined)
print(list_files)

print("** Merging multiple csv files into a single pandas dataframe **")
# Merge files by joining all files
dataframe = pd.concat(map(pd.read_csv, list_files), ignore_index=True)
print(dataframe)
"""

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

def find_outliers_IQR(df):

   q1=df.quantile(0.25)

   q3=df.quantile(0.75)

   IQR=q3-q1

   outliers = df[((df<(q1-1.5*IQR)) | (df>(q3+1.5*IQR)))]

   return outliers


files_joined = os.path.join('D:\\Documents\\UNIVERSITY\\project_mining_2022\\DataMining-Project-2022\\dataset\\sources', "*.csv")
files_joined = os.path.join('C:\\Users\\Dimitra\\Documents\\GitHub\\DataMining-Project-2022\\dataset\\sources', "*.csv")
files = glob.glob(files_joined)
df = pd.concat([pd.read_csv(fp).assign(Date=transform(os.path.basename(fp).split('.')[0]))
for fp in files])

print(df) 


#dt = df.groupby('Date')
#dd = dt.get_group('2019-01-01')
#print(dd)
mn = df.describe()[['Wind','Geothermal','Natural Gas' ]]


print(mn)

outliers = find_outliers_IQR(df['Natural Gas'])

print("number of outliers: "+ str(len(outliers)))

print("max outlier value: "+ str(outliers.max()))

print("min outlier value: "+ str(outliers.min()))

print(outliers)


plt.plot(df.Date, df['Natural Gas'])

plt.show()


