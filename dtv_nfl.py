import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from unicodedata import normalize
import html5lib 
from bs4 import BeautifulSoup

soup = BeautifulSoup(open('./dtv_week_3_mod.html'), 'html.parser')
prev_date_time = ''
results = soup.find_all("div", class_="row d-print-none mt-3 no-gutters")
for result in results:
    #print('-----------------------------------------------')
    if result.find("h2", "group-header-text"):
        date_read = result.find("h2", "group-header-text")
    time_read = result.find("span", {'data-v-42822f8f': True})
    teams = result.find_all('a', {'data-v-2306d078': True})
    home = teams[1].text.strip()
    away = teams[3].text.strip()
    i = 0 
    ch_string = ''
    channels = result.find_all('span', class_="v-chip__content")
    while i < len(channels):
        if len(channels[i].text.split()) == 3:
            channel,sep,name = channels[i].text.split()
            ch_string = ch_string + f' {name} {channel}  '
        else:
            ch_string = ch_string + f'Name: {name}  '
        i +=1
    date_time_str = date_read.text.strip() + ' ' + time_read.text.strip()

    if date_time_str == prev_date_time:
        print('%10s %10s %15s %15s %60s' % (date_read.text.strip(),time_read.text.strip(),away,home,ch_string))
    else:
        print('\n%10s %10s %15s %15s %60s' % (date_read.text.strip(),time_read.text.strip(),away,home,ch_string))
    prev_date_time = date_time_str



'''
odds_tables = pd.read_html('./dtv_week_3.html')

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
'''



