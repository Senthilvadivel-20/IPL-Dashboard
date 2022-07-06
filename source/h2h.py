import pandas as pd

df = pd.read_csv('D:/PROJECT/IPL Dashboard/Data/IPL.csv')
dt=pd.read_json('D:/PROJECT/IPL Dashboard/Data/Match.json')
dt['season']= dt['season'].astype(str)


# FInd winner

def get_total_matches(team_1,team_2):
    t = dt[((dt['team_1'] == team_1) | (dt['team_1'] == team_2)) & ((dt['team_2'] == team_1) | (dt['team_2'] == team_2)) ]
    return len(t)

def head2head_win(team_1,team_2):
#     temp = df[((df['batting_team'] == team_1) | (df['batting_team'] == team_2)) & ((df['bowling_team'] == team_1) | (df['bowling_team'] == team_2)) ]
    t = dt[((dt['team_1'] == team_1) | (dt['team_1'] == team_2)) & ((dt['team_2'] == team_1) | (dt['team_2'] == team_2)) ]
    t = t.groupby('winner').loser.count().reset_index()
    val = t.loc[t['winner'] == team_1,'loser'].values
    return val[0] 

def is_any_tie(team_1,team_2):
    t = dt[((dt['team_1'] == team_1) | (dt['team_1'] == team_2)) & ((dt['team_2'] == team_1) | (dt['team_2'] == team_2)) ]
    t = t.groupby('winner').loser.count().reset_index()
    try:
        val = t.loc[t['winner'] == '','loser'].values
        return val[0]
    except:
        return 0
    
def match_high_score(bat,bowl):
    temp = df[(df['batting_team'] == bat) & (df['bowling_team'] == bowl)]
    temp = temp.groupby(['match_id','batting_team','bowling_team']).total_runs.sum().sort_values(ascending = False)
    return temp.iloc[0]

def match_low_score(bat,bowl):
    temp = df[(df['batting_team'] == bat) & (df['bowling_team'] == bowl)]
    temp = temp.groupby(['match_id','batting_team','bowling_team']).total_runs.sum().sort_values()
    return temp.iloc[0]

def target(bat,bowl):
    temp = df[(df['batting_team'] == bat) & (df['bowling_team'] == bowl)]
    temp = temp.groupby(['match_id','start_date']).total_runs.sum().reset_index()
    lis = [temp['start_date'].to_list(), temp['total_runs'].to_list()]
    return lis