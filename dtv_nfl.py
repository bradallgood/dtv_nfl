import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from unicodedata import normalize
import html5lib 
from bs4 import BeautifulSoup

odds_tables = pd.read_html('./dtv_week_2.html')

#print(len(odds_tables))
#print(odds_tables[0])

table = odds_tables[0]

prev_time = ''

for index, row in table.iterrows():
    if row['Date'] !=  row['Event']:
        if prev_time != row['Time']:
            print('')
        count = row['Channels'].split(' ')
        if len(count) == 4 :
             #print(f'{row["Date"]:15}{row["Event"]:15}{row["Time"]:15}{count[0]:15}')
             print('%s %30s %20s %20s' % (row['Date'],row['Event'],row['Time'],count[0])) 
        elif len(count) == 9 or len(count)==14:
             if len(count) == 9:
                 if count[3] in ['FOXe','CBSe']:
                    print('%s %30s %20s %20s' % (row['Date'],row['Event'],row['Time'],count[5]))
                 else:
                    if count[3] == 'PRIMETNF':
                       print('%s %30s %20s %20s' % (row['Date'],row['Event'],row['Time'],count[0]))
                    else:
                       print('%s %30s %20s %20s' % (row['Date'],row['Event'],row['Time'],count[3]))
             else:
                 #print(f'{row["Date"]:15}{row["Event"]:15}{row["Time"]:15}{count[3]:15}')
                print('%s %30s %20s %20s' % (row['Date'],row['Event'],row['Time'],count[3]))
        prev_time = row['Time']




