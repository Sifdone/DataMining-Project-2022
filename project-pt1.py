from sqlite3 import Date, Time
import pandas as pd
from matplotlib import pyplot as plt
import glob
import os
import datetime

"""
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

test = dataframe.loc[dataframe['Time'].isin(['00:00', '08:00', '16:00', '23:00'])]


plt.plot(test.Time, test.Wind)
#plt.plot(test.Time, test.Geothermal)
plt.show()
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



files_joined = os.path.join('D:\\Documents\\UNIVERSITY\\project_mining_2022\\dataset\\sources', "*.csv")
files = glob.glob(files_joined)
df = pd.concat([pd.read_csv(fp).assign(Date=transform(os.path.basename(fp).split('.')[0]))
for fp in files])
print(df)    

std =df['Wind'].std()

mn = df["Wind"].mean()

md = df['Wind'].median()



plt.plot(df.Date, df.Wind)

plt.show()


