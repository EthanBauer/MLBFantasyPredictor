import pandas as pd

df = pd.read_csv('data/mlb_starting_pitcher_stats.csv')

df = df.drop(columns=['Unnamed: 0'])
print(df)
categories = ['W', 'SO']

def zScoreAdd(cat):
    zScore = []
    for player in df.index:
        zScore.append((df.iloc[player][cat]-df[cat].mean())/df[cat].std())
    df['z'+cat] = zScore
    df['z'+cat] = df['z'+cat].round(decimals=3)
for cat in categories:
    zScoreAdd(cat)
zScore = []
realz = []
for player in df.index:
    value = (df.iloc[player]['WHIP']-df['WHIP'].mean())/df['WHIP'].std()
    realz.append(value)
    if value > 0:
        value = -(abs(value))
    else:
        value = abs(value)
    zScore.append(value)
df['realzWHIP'] = realz
df['realzWHIP'] = df['realzWHIP'].round(decimals=3)
df['zWHIP'] = zScore
df['zWHIP'] = df['zWHIP'].round(decimals=3)
zScore = []
realz = []
for player in df.index:
    value = (df.iloc[player]['ERA']-df['ERA'].mean())/df['ERA'].std()
    realz.append(value)
    if value > 0:
        value = -(abs(value))
    else:
        value = abs(value)
    zScore.append(value)
df['realzERA'] = realz
df['realzERA'] = df['realzERA'].round(decimals=3)
df['zERA'] = zScore
df['zERA'] = df['zERA'].round(decimals=3)

df['zTotal'] = df.loc[0:144,['zW', 'zSO', 'zWHIP', 'zERA']].sum(axis=1)/4
df['zTotal'].round(decimals=3)
df.sort_values('zTotal', axis=0, ascending=False, inplace=True, na_position='first')
df = df.reset_index(drop=True)
df.to_csv(r"/Users/ethanbauer/Desktop/mlb_starting_pitcher_stats_zScore.csv", index = False, sep=',', encoding='utf-8')
