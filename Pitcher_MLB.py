import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

url = 'https://www.fangraphs.com/leaders.aspx?pos=all&stats=rel&lg=all&qual=y&type=1&season=2021&month=0&season1=2021&ind=0&team=0&rost=0&age=0&filter=&players=0&startdate=2021-01-01&enddate=2021-12-31&sort=17,a&page=1_30'
# url = 'https://www.fangraphs.com/leaders.aspx?pos=all&stats=rel&lg=all&qual=y&type=8&season=2021&month=0&season1=2021&ind=0&team=0&rost=0&age=0&filter=&players=0&startdate=&enddate='
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')
columns = [col.get_text() for col in soup.find_all('th', attrs={'class':'rgHeader'})]
final_df = pd.DataFrame(columns=columns)
for i in range(1, 6):
    url = 'https://www.fangraphs.com/leaders.aspx?pos=all&stats=rel&lg=all&qual=y&type=1&season=2021&month=0&season1=2021&ind=0&team=0&rost=0&age=0&filter=&players=0&startdate=2021-01-01&enddate=2021-12-31&sort=17,a&page={}_30'.format(i)
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
final_df = final_df.drop(columns=['#', 'Team', 'K/9', 'BB/9', 'HR/9', 'K/BB', 'K%', 'AVG', 'BABIP','xFIP-', 'FIP', 'E-F','xFIP','SIERA','FIP-','ERA-','LOB%','K-BB%','BB%'], axis=1)


url = 'https://www.fangraphs.com/leaders.aspx?pos=all&stats=rel&lg=all&qual=y&type=0&season=2021&month=0&season1=2021&ind=0&team=0&rost=0&age=0&filter=&players=0&startdate=2021-01-01&enddate=2021-12-31&sort=5,a&page=1_30'
# url = 'https://www.fangraphs.com/leaders.aspx?pos=all&stats=rel&lg=all&qual=y&type=8&season=2021&month=0&season1=2021&ind=0&team=0&rost=0&age=0&filter=&players=0&startdate=&enddate='
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')
columns = [col.get_text() for col in soup.find_all('th', attrs={'class':'rgHeader'})]
final_df1 = pd.DataFrame(columns=columns)
for i in range(1, 6):
    url = 'https://www.fangraphs.com/leaders.aspx?pos=all&stats=rel&lg=all&qual=y&type=0&season=2021&month=0&season1=2021&ind=0&team=0&rost=0&age=0&filter=&players=0&startdate=2021-01-01&enddate=2021-12-31&sort=5,a&page={}_30'.format(i)
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
for player in final_df.values:
    whip.append(player[1])
final_df1['WHIP'] = whip
final_df1.sort_values('ERA', axis=0, ascending=True, inplace=True, na_position='first')
final_df1.to_csv(r"/Users/ethanbauer/Desktop/mlb_pitcher_stats.csv", index = True, sep=',', encoding='utf-8')