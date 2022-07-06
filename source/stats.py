import pandas as pd
import numpy as np

df = pd.read_csv('./Files/IPL.csv',dtype={'season':np.object})


#Source Function 
def ch(n):
    if n == '0':
        return "Not out"
    else:
        return "Out"

def get_batsman_high_score():
    t = df.groupby(['match_id','season','start_date', 'venue','batting_team','bowling_team','batting_hand','striker']).runs_off_bat.sum().reset_index()
    t['ball_faced'] = df.groupby(['match_id','season','start_date', 'venue','batting_team','bowling_team','batting_hand','striker']).is_ball.sum().reset_index()['is_ball']
    t['wicket_type'] = df.groupby(['match_id','season','start_date', 'venue','batting_team','bowling_team','batting_hand','striker']).wicket_type.max().reset_index()['wicket_type']
    t['is_wicket'] = t['wicket_type'].apply(ch)
    t['six'] = df.groupby(['match_id','season','start_date', 'venue','batting_team','bowling_team','batting_hand','striker']).six.sum().reset_index()['six']
    t['four'] = df.groupby(['match_id','season','start_date', 'venue','batting_team','bowling_team','batting_hand','striker']).four.sum().reset_index()['four']
    t['five'] = df.groupby(['match_id','season','start_date', 'venue','batting_team','bowling_team','batting_hand','striker']).five.sum().reset_index()['five']
    t['three'] = df.groupby(['match_id','season','start_date', 'venue','batting_team','bowling_team','batting_hand','striker']).three.sum().reset_index()['three']
    t['two'] = df.groupby(['match_id','season','start_date', 'venue','batting_team','bowling_team','batting_hand','striker']).two.sum().reset_index()['two']
    t['one'] = df.groupby(['match_id','season','start_date', 'venue','batting_team','bowling_team','batting_hand','striker']).one.sum().reset_index()['one']
    t['dot'] = df.groupby(['match_id','season','start_date', 'venue','batting_team','bowling_team','batting_hand','striker']).dot.sum().reset_index()['dot']

    t.drop(['match_id'],axis=1,inplace=True)
    t = t.sort_values(by=['runs_off_bat','ball_faced'],ascending=[False,True])

    api = []
    for i in range(len(t)):
        api.append(list(t.iloc[i].values))

    return api



def get_season_batsman_high_score(ssn):
    temp = df[df['season'] == ssn]
    t = temp.groupby(['match_id','season','start_date', 'venue','batting_team','bowling_team','batting_hand','striker']).runs_off_bat.sum().reset_index()
    t['ball_faced'] = temp.groupby(['match_id','season','start_date', 'venue','batting_team','bowling_team','batting_hand','striker']).is_ball.sum().reset_index()['is_ball']
    t['wicket_type'] = temp.groupby(['match_id','season','start_date', 'venue','batting_team','bowling_team','batting_hand','striker']).wicket_type.max().reset_index()['wicket_type']
    t['is_wicket'] = t['wicket_type'].apply(ch)
    t['six'] = temp.groupby(['match_id','season','start_date', 'venue','batting_team','bowling_team','batting_hand','striker']).six.sum().reset_index()['six']
    t['four'] = temp.groupby(['match_id','season','start_date', 'venue','batting_team','bowling_team','batting_hand','striker']).four.sum().reset_index()['four']
    t['five'] = temp.groupby(['match_id','season','start_date', 'venue','batting_team','bowling_team','batting_hand','striker']).five.sum().reset_index()['five']
    t['three'] = temp.groupby(['match_id','season','start_date', 'venue','batting_team','bowling_team','batting_hand','striker']).three.sum().reset_index()['three']
    t['two'] = temp.groupby(['match_id','season','start_date', 'venue','batting_team','bowling_team','batting_hand','striker']).two.sum().reset_index()['two']
    t['one'] = temp.groupby(['match_id','season','start_date', 'venue','batting_team','bowling_team','batting_hand','striker']).one.sum().reset_index()['one']
    t['dot'] = temp.groupby(['match_id','season','start_date', 'venue','batting_team','bowling_team','batting_hand','striker']).dot.sum().reset_index()['dot']
    t.drop(['match_id'],axis=1,inplace=True)
    t = t.sort_values(by=['runs_off_bat','ball_faced'],ascending=[False,True])

    lis = []
    for i in range(len(t)):
        lis.append(list(t.iloc[i].values))

    return lis

#================================= Bowler Section ===============================================#

def get_bowler_innings_wk():
    t = df.groupby(['match_id','season','start_date', 'venue','bowling_team','batting_team','bowling_skill','bowler']).bowler_wk.sum().reset_index()
    n = (df.groupby(['match_id','season','start_date', 'venue','bowling_team','batting_team','bowling_skill','bowler']).is_ball.sum().reset_index()['is_ball'])
    t['balls'] = n
    t['over'] =  (n // 6) + ((n % 6)/10)
    t['total_runs'] = df.groupby(['match_id','season','start_date', 'venue','bowling_team','batting_team','bowling_skill','bowler']).total_runs.sum().reset_index()['total_runs']
    t['six'] = df.groupby(['match_id','season','start_date', 'venue','bowling_team','batting_team','bowling_skill','bowler']).six.sum().reset_index()['six']
    t['four'] = df.groupby(['match_id','season','start_date', 'venue','bowling_team','batting_team','bowling_skill','bowler']).four.sum().reset_index()['four']
    t['dot'] = df.groupby(['match_id','season','start_date', 'venue','bowling_team','batting_team','bowling_skill','bowler']).dot.sum().reset_index()['dot']

    t.drop(['match_id'],axis=1,inplace=True)
    t = t.sort_values(by=['bowler_wk','total_runs'],ascending=[False,True])

    api = []
    for i in range(len(t)):
        api.append(list(t.iloc[i].values))

    return api

def get_bowler_innings_wk_by_season(ssn):
    temp = df[df['season'] == ssn ]
    t = temp.groupby(['match_id','season','start_date', 'venue','bowling_team','batting_team','bowling_skill','bowler']).bowler_wk.sum().reset_index()
    n = (temp.groupby(['match_id','season','start_date', 'venue','bowling_team','batting_team','bowling_skill','bowler']).is_ball.sum().reset_index()['is_ball'])
    t['balls'] = n
    t['over'] =  (n // 6) + ((n % 6)/10)
    t['total_runs'] = temp.groupby(['match_id','season','start_date', 'venue','bowling_team','batting_team','bowling_skill','bowler']).total_runs.sum().reset_index()['total_runs']
    t['six'] = temp.groupby(['match_id','season','start_date', 'venue','bowling_team','batting_team','bowling_skill','bowler']).six.sum().reset_index()['six']
    t['four'] = temp.groupby(['match_id','season','start_date', 'venue','bowling_team','batting_team','bowling_skill','bowler']).four.sum().reset_index()['four']
    t['dot'] = temp.groupby(['match_id','season','start_date', 'venue','bowling_team','batting_team','bowling_skill','bowler']).dot.sum().reset_index()['dot']

    t.drop(['match_id'],axis=1,inplace=True)
    t = t.sort_values(by=['bowler_wk','total_runs'],ascending=[False,True])

    api = []
    for i in range(len(t)):
        api.append(list(t.iloc[i].values))

    return api