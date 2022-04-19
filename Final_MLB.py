import pandas as pd

hitterDF = pd.read_csv('data/mlb_hitting_stats_zScore.csv')
reliefDF = pd.read_csv('data/mlb_relief_pitcher_stats_zScore.csv')
starterDF = pd.read_csv('data/mlb_starting_pitcher_stats_zScore.csv')
hitterDF = hitterDF.drop(columns=['R','HR','RBI','SB','BA','zR','zSB','zRBI','zBA','zHR'], axis=1)
reliefDF = reliefDF.drop(columns=['W','ERA','G','SV','IP','SO','WHIP','zW','zSV','zSO','realzWHIP','zWHIP','realzERA','zERA'])
starterDF = starterDF.drop(columns=['W','ERA','IP','SO','WHIP','zW','zSO','realzWHIP','zWHIP','realzERA','zERA'])
hitterDF.rename(columns = {'PLAYER':'Name'}, inplace = True)
finalDF = pd.concat([hitterDF, reliefDF, starterDF], ignore_index=True)
finalDF.sort_values('zTotal', axis=0, ascending=False, inplace=True, na_position='first')
finalDF = finalDF.reset_index(drop=True)
finalDF.to_csv(r"/Users/ethanbauer/Desktop/mlb_FINAL_stats.csv", index = True, sep=',', encoding='utf-8')