import pandas as pd

df = pd.read_csv('data/mlb_stats.csv')

#clean the data
df = df.drop(columns=['Unnamed: 0', 'Unnamed: 1', 'YRS', 'G', 'AB', '2B', '3B', 'BB', 'SO', 'CS', 'H'], axis=1)
#all important categories
categories = ['R', 'SB', 'RBI', 'BA', 'HR']

#function for zScore of given category
def zScoreAdd(cat):
    #create new list
    zScore = []
    #for every player in our data frame
    for player in df.index:
        #add to our list the zscore for the specific category ((category-category mean)/category standard deviation)
        zScore.append((df.iloc[player][cat]-df[cat].mean())/df[cat].std())
    #add a column to our data frame that is the zScore
    df['z'+cat] = zScore
    #round the decimals
    df['z'+cat] = df['z'+cat].round(decimals=3)
#for every category in our columns, call the zScoreAdd function
for cat in categories:
    zScoreAdd(cat)
#Adding and rounding the final zScore and summing that new column
df['zTotal'] = df.loc[0:338,['zR','zSB','zRBI','zBA','zHR']].sum(axis=1)
df['zTotal'].round(decimals=3)

#sort by the zTotal column
df.sort_values('zTotal', axis=0, ascending=False, inplace=True, na_position='first')
df = df.reset_index(drop=True)
df.to_csv(r"/Users/ethanbauer/Desktop/mlb_stats.csv", index = False, sep=',', encoding='utf-8')

