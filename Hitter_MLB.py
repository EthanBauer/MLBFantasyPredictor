import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

#creates a csv file with the statistics of the 2021 batters
#data pulled from espn and sorted by batting average

url = 'http://www.espn.com/mlb/history/leaders/_/breakdown/season/year/2021/start/1'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')
header = soup.find('tr', attrs={'class': 'colhead'})
columns = [col.get_text() for col in header.find_all('td')]
final_df = pd.DataFrame(columns=columns)
final_df
for i in range(1, 339, 50):
    url = 'http://www.espn.com/mlb/history/leaders/_/breakdown/season/year/2021/start/{}'.format(i)
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    
    players = soup.find_all('tr', attrs={'class': re.compile('row player-10-')})
    for player in players:

        stats = [stat.get_text() for stat in player.find_all('td')]

        temp_df = pd.DataFrame(stats).transpose()
        temp_df.columns = columns
        final_df = pd.concat([final_df, temp_df], ignore_index=True)
# final_df['Scores'] = 0
final_df

#change line below's string to wherever you would like to store the file
final_df.to_csv(r"/Users/ethanbauer/Desktop/mlb_stats.csv", index = True, sep=',', encoding='utf-8')
