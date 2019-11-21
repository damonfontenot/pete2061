# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
#import seaborn as sns

import pandas as pd
import sqlite3

#Question 1
conn = sqlite3.connect("DCA.db")
cur = conn.cursor()

titleFontSize = 18
axisLabelFontSize = 15
axisNumFontSize = 13

for wellID in range(1,18):
    dcadf = pd.read_sql_query(f"SELECT time,rate, Cum FROM Rates WHERE wellID={wellID};", conn)
    seconddf = pd.read_sql_query("SELECT * FROM DCAparams ;", conn)
    
    fig, ax1 = plt.subplots()

    ax2 = ax1.twinx()
    ax1.plot(dcadf['time'], dcadf['rate'],)
    ax2.plot(dcadf['time'], dcadf['Cum']/1000,)

    ax1.set_xlabel('Time, Months')
    ax1.set_ylabel('Production Rate, bopm')
    ax2.set_ylabel('Cumulative Oil Production, Mbbls')

    plt.show()
    
#Question 2
wellID = 9
df9 = pd.read_sql_query(f"SELECT time,rate, Cum,Cum_model FROM Rates WHERE wellID={wellID};", conn)
wellID = 11
df11 = pd.read_sql_query(f"SELECT time,rate, Cum,Cum_model FROM Rates WHERE wellID={wellID};", conn)
wellID = 13
df13 = pd.read_sql_query(f"SELECT time,rate, Cum,Cum_model FROM Rates WHERE wellID={wellID};", conn) 
wellID = 15
df15 = pd.read_sql_query(f"SELECT time,rate, Cum,Cum_model FROM Rates WHERE wellID={wellID};", conn) 
wellID = 16
df16 = pd.read_sql_query(f"SELECT time,rate, Cum,Cum_model FROM Rates WHERE wellID={wellID};", conn) 
labels = ["well 9", "well 11", "well 13", "well 15", "well 16"]
fig, ax = plt.subplots()
ax.stackplot(df9['time'], df9['rate'], df11['rate'], df13['rate'], df13['rate'], df15['rate'], df16['rate'], labels=labels)
ax.legend(loc='upper left')
plt.show()
    
#Question 3
        