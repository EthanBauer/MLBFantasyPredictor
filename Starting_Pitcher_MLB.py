import requests
from bs4 import BeautifulSoup
import pandas as pd
import re


url = 'https://www.fangraphs.com/leaders.aspx?pos=all&stats=sta&lg=all&qual=y&type=0&season=2021&month=0&season1=2021&ind=0&team=0&rost=0&age=0&filter=&players=0&startdate=2021-01-01&enddate=2021-12-31&sort=5,a&page=1_30'

page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')
columns = [col.get_text() for col in soup.find_all('th', attrs={'class':'rgHeader'})]
final_df = pd.DataFrame(columns=columns)
for i in range(1, 3):

    url = 'https://www.fangraphs.com/leaders.aspx?pos=all&stats=sta&lg=all&qual=y&type=0&season=2021&month=0&season1=2021&ind=0&team=0&rost=0&age=0&filter=&players=0&startdate=2021-01-01&enddate=2021-12-31&sort=5,a&page={}_30'.format(i)
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    players = soup.find_all('tr', attrs={'class': re.compile('rgRow')})
    playersO = soup.find_all('tr', attrs={'class': re.compile('rgAltRow')})
    for player in players:
        stats = [stat.get_text() for stat in player.find_all('td')]
        temp_df = pd.DataFrame(stats).transpose()
        temp_df.columns = columns
        final_df = pd.concat([final_df, temp_df], ignore_index=True)
    for player1 in playersO:
        stats1 = [stat1.get_text() for stat1 in player1.find_all('td')]
        temp_df1 = pd.DataFrame(stats1).transpose()
        temp_df1.columns = columns
        final_df = pd.concat([final_df, temp_df1], ignore_index=True)
final_df = final_df.drop(columns=['#', 'Team','ShO','CG','BS','HLD','H','R','ER','HR','BB','IBB','HBP','BK','WP','TBF','GS','G','L','SV'],axis=1)

url = 'https://www.fangraphs.com/leaders.aspx?pos=all&stats=sta&lg=all&qual=y&type=1&season=2021&month=0&season1=2021&ind=0&team=0&rost=0&age=0&filter=&players=0&startdate=2021-01-01&enddate=2021-12-31&sort=17,a&page=1_30'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')
columns = [col.get_text() for col in soup.find_all('th', attrs={'class':'rgHeader'})]
final_df1 = pd.DataFrame(columns=columns)
for i in range(1, 3):
    url = 'https://www.fangraphs.com/leaders.aspx?pos=all&stats=sta&lg=all&qual=y&type=1&season=2021&month=0&season1=2021&ind=0&team=0&rost=0&age=0&filter=&players=0&startdate=2021-01-01&enddate=2021-12-31&sort=17,a&page={}_30'.format(i)
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    players = soup.find_all('tr', attrs={'class': re.compile('rgRow')})
    playersO = soup.find_all('tr', attrs={'class': re.compile('rgAltRow')})
    for player in players:
        stats = [stat.get_text() for stat in player.find_all('td')]
        temp_df = pd.DataFrame(stats).transpose()
        temp_df.columns = columns
        final_df1 = pd.concat([final_df1, temp_df], ignore_index=True)
    for player1 in playersO:
        stats1 = [stat1.get_text() for stat1 in player1.find_all('td')]
        temp_df1 = pd.DataFrame(stats1).transpose()
        temp_df1.columns = columns
        final_df1 = pd.concat([final_df1, temp_df1], ignore_index=True)
whip = []
for player in final_df1.values:
    whip.append(player[11])
final_df['WHIP'] = whip

final_df.to_csv(r"/Users/ethanbauer/Desktop/mlb_starting_pitcher_stats.csv", index = True, sep=',', encoding='utf-8')
