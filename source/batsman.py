# from sys import exec_prefixs
import pandas as pd
import numpy as np

df=pd.read_csv('./Files/IPL.csv',dtype={'season':np.object})
dt=pd.read_json('./Files/people.json')
dt['season'] = dt['season'].astype('str')

#create a class for the staticsticss

def batted_season(name):
    temp=df[df['striker']==name]
    return (temp['season'].unique())

def bowled_season(name):
    temp=df[df['bowler']==name]
    return (temp['season'].unique())

#Batting Part !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
class runs:
    # df=pd.read_csv('D:/PROJECT/IPL Dashboard/Code/Data/IPL_2021.csv',dtype={'season':np.object})
    # dt=pd.read_json('D:/PROJECT/IPL Dashboard/Code/Data/people.json')

    def __init__(self,name):
        self.name=name
        
    #tatal part
    def total_match(self):
        no=0
        for i in range(len(dt)):
            if self.name in dt['people'][i]:
                    no+=1
        if no == 0:
            return 0
        else:
            return no+1
    
    def batted_match(self):
        temp=df[df['striker']==self.name]
        n=len(temp['match_id'].unique())
        return n

    def total_out(self):
        try :
            temp=df['player_dismissed'].value_counts().reset_index()
            obj=temp[temp['index']==self.name]
            v=obj['player_dismissed'].to_list()
            return v[0]
        except:
            return "NaN"

        
    
    def total_runs(self):
        temp=df[df['striker']==self.name]
        runs=temp['runs_off_bat'].sum()
        return runs
    
    def total_hs(self):
        temp=df[df['striker']==self.name]
        temp=temp.groupby('match_id').runs_off_bat.sum().sort_values(ascending=False)
        #use max and min
        return temp.max()
    
    def total_ball_faced(self):
        temp=df[df['striker']==self.name]
        bf=len(temp)-(temp['w'].sum())
        return bf

    def total_avg(self):
        try:
            temp=df[df['striker']==self.name]
    #         total_match=runs.total_match(self)
            total_runs=runs.total_runs(self)
            out=runs.total_out(self)
            avg=total_runs/out
            return round(avg,2)
        except:
            return 'NaN'
    
    def total_strike_rate(self):
        total_runs=runs.total_runs(self)
        total_ball_faced=runs.total_ball_faced(self)
        sr=(total_runs/total_ball_faced)*100
        return round(sr,2)
    
    def all_match_score(self):
        temp=df[(df['striker']==self.name)]
        temp=temp.groupby('match_id').runs_off_bat.sum().reset_index()
        return temp
    
    def total_100(self):
        temp=runs.all_match_score(self)
        return sum(temp['runs_off_bat']>100)
        
    def total_50(self):
        temp=runs.all_match_score(self)
        return sum(temp['runs_off_bat']>50)
    
    def total_30(self):
        temp=runs.all_match_score(self)
        return sum(temp['runs_off_bat']>30)
    
    def total_6(self):
        temp=df[df['striker']==self.name]
        return temp['six'].sum()
    
    def total_5(self):
        temp=df[df['striker']==self.name]
        return temp['five'].sum()
    
    def total_4(self):
        temp=df[df['striker']==self.name]
        return temp['four'].sum()
    
    def total_3(self):
        temp=df[df['striker']==self.name]
        return temp['three'].sum()
    
    def total_2(self):
        temp=df[df['striker']==self.name]
        return temp['two'].sum()
    
    def total_1(self):
        temp=df[df['striker']==self.name]
        return temp['one'].sum()
    
    def total_dot(self):
        temp=df[df['striker']==self.name]
        return temp['dot'].sum()
    
#     ----------------------Season part--------------------------

    def ssn_match(self,ssn):
        temp=dt[dt['season']==ssn]
        no=0
        pl_list=temp['people'].to_list()
        for i in range(len(pl_list)):
            if self.name in pl_list[i]:
                    no+=1
        if no == 0:
            return 0
        else:
            return no+1
    
    def ssn_batted_match(self,ssn):
        temp=df[(df['striker']==self.name)&(df['season']==ssn)]
        n=len(temp['match_id'].unique())
        return n

    def ssn_out(self,ssn):
        temp=df[df['season']==ssn]
        temp=temp['player_dismissed'].value_counts().reset_index()
        obj=temp[temp['index']==self.name]
        try:
            out=obj['player_dismissed'].to_list()[0]
        except:
            out=0
        # print(obj)
        return out
        
    
    def ssn_runs(self,ssn):
        temp=df[(df['striker']==self.name)&(df['season']==ssn)]
        runs=temp['runs_off_bat'].sum()
        return runs

    
    def ssn_hs(self,ssn):
        temp=df[(df['striker']==self.name)&(df['season']==ssn)]
        temp=temp.groupby('match_id').runs_off_bat.sum().sort_values(ascending=False)
        #use max and min
        return temp.max()
    
    def ssn_ball_faced(self,ssn):
        temp=df[(df['striker']==self.name)&(df['season']==ssn)]
        bf=len(temp)-(temp['w'].sum())
        return bf

    def ssn_avg(self,ssn):
        temp=df[(df['striker']==self.name)&(df['season']==ssn)]
#         total_match=runs.total_match(self)
        total_runs=runs.ssn_runs(self,ssn)
        total_out=runs.ssn_out(self,ssn)
        avg = total_runs/total_out
        return round(avg,2)
    
    def ssn_strike_rate(self,ssn):
        ssn_runs=runs.ssn_runs(self,ssn)
        ssn_ball_faced=runs.ssn_ball_faced(self,ssn)    
        sr=(ssn_runs/ssn_ball_faced)*100
        return round(sr,2)
        
    def ssn_match_score(self,ssn):
        temp=df[(df['striker']==self.name)&(df['season']==ssn)]
        temp=temp.groupby('match_id').runs_off_bat.sum().reset_index()
        return temp
    
    def ssn_100(self,ssn):
        temp=runs.ssn_match_score(self,ssn)
        return sum(temp['runs_off_bat']>100)
        
    def ssn_50(self,ssn):
        temp=runs.ssn_match_score(self,ssn)
        return sum(temp['runs_off_bat']>50)
    
    def ssn_30(self,ssn):
        temp=runs.ssn_match_score(self,ssn)
        return sum(temp['runs_off_bat']>30)
    
    def ssn_6(self,ssn):
        temp=df[(df['striker']==self.name)&(df['season']==ssn)]
        return temp['six'].sum()
    
    def ssn_5(self,ssn):
        temp=df[(df['striker']==self.name)&(df['season']==ssn)]
        return temp['five'].sum()
    
    def ssn_4(self,ssn):
        temp=df[(df['striker']==self.name)&(df['season']==ssn)]
        return temp['four'].sum()
    
    def ssn_3(self,ssn):
        temp=df[(df['striker']==self.name)&(df['season']==ssn)]
        return temp['three'].sum()
    
    def ssn_2(self,ssn):
        temp=df[(df['striker']==self.name)&(df['season']==ssn)]
        return temp['two'].sum()
    
    def ssn_1(self,ssn):
        temp=df[(df['striker']==self.name)&(df['season']==ssn)]
        return temp['one'].sum()

    def ssn_dot(self,ssn):
        temp=df[(df['striker']==self.name)&(df['season']==ssn)]
        return temp['dot'].sum()
    

    def runs_in_season(self,season):
        temp=df[(df['striker']==self.name) & (df['season']==season)]
        runs=temp['runs_off_bat'].sum()
        return runs


#Bowling Part !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

class bowling:
    
    def __init__(self,name):
        self.name=name
        
    def table(self):
        temp=df[df['bowler']==self.name]
        return temp
    
    def ssn_table(self,ssn):
        temp=df[(df['bowler']==self.name)&(df['season']==ssn)]
        return temp
        
    #total part
    def total_match(self):
        no=0
        for i in range(len(dt)):
            if self.name in dt['people'][i]:
                    no+=1
                    
        return no+1
    
    def bowled_match(self):
        temp=df[df['bowler']==self.name]
        n=len(temp['match_id'].unique())
        return n
    
    def total_balls(self):
        temp=df[df['bowler']==self.name]
        n=len(temp)-(temp['w'].sum())
        return n
    
    def total_runs(self):
        temp=df[df['bowler']==self.name]
        n=temp['bowler_runs'].sum()
        return n
        
    def total_wicket(self):
        temp=df[df['bowler']==self.name]
        n=temp['bowler_wk'].sum()
        return n
    
    def total_bbw(self):
        temp=df[df['bowler']==self.name]
        d1=temp.groupby('match_id').bowler_wk.sum().reset_index()
        d2=temp.groupby('match_id').bowler_runs.sum().reset_index()
        d=pd.merge(d1,d2,how="inner").sort_values(by=['bowler_wk','bowler_runs'],ascending=[False,True]).reset_index(drop=True)
        try:
            w=d['bowler_wk'][0]
            r=d['bowler_runs'][0]
            return f'{w}/{r}'
        except:
            return 0
    
    def total_avg(self):
        runs=bowling.total_runs(self)
        wk=bowling.total_wicket(self)
        return round(runs/wk,2)
    
    def total_eco(self):
        runs=bowling.total_runs(self)
        ovr=bowling.total_balls(self)/6
        return round(runs/ovr,2)
    
    def total_sr(self):
        balls=bowling.total_balls(self)
        wk=bowling.total_wicket(self)
        return round(balls/wk,2)
    
    def total_6(self):
        temp=bowling.table(self)
        return temp['six'].sum()
    
    def total_4(self):
        temp=bowling.table(self)
        return temp['four'].sum()
    
    #Season part ::::::::::::::::::::::::::::    
    
    
    def ssn_match(self,ssn):
        temp=dt[dt['season']==ssn]
        no=0
        pl_list=temp['people'].to_list()
        for i in range(len(pl_list)):
            if self.name in pl_list[i]:
                    no+=1
                    
        return no
    
    def ssn_bowled_match(self,ssn):
        temp=bowling.ssn_table(self,ssn)
        n=len(temp['match_id'].unique())
        return n
    
    def ssn_balls(self,ssn):
        temp=bowling.ssn_table(self,ssn)
        n=len(temp)-(temp['w'].sum())
        return n
    
    def ssn_runs(self,ssn):
        temp=bowling.ssn_table(self,ssn)
        n=temp['bowler_runs'].sum()
        return n
    
    def ssn_wicket(self,ssn):
        temp=bowling.ssn_table(self,ssn)
        n=temp['bowler_wk'].sum()
        return n
    
    def ssn_bbw(self,ssn):
        temp=bowling.ssn_table(self,ssn)
        d1=temp.groupby('match_id').bowler_wk.sum().reset_index()
        d2=temp.groupby('match_id').bowler_runs.sum().reset_index()
        d=pd.merge(d1,d2,how="inner").sort_values(by=['bowler_wk','bowler_runs'],ascending=[False,True]).reset_index(drop=True)
        w=d['bowler_wk'].to_list()[0]
        r=d['bowler_runs'].to_list()[0]
        return f'{w}/{r}'
    
    
    def ssn_avg(self,ssn):
        runs=bowling.ssn_runs(self,ssn)
        wk=bowling.ssn_wicket(self,ssn)
        if wk == 0:
            return "Nan"
        else:
            val=round(runs/wk,2)
            return val
            
    
    def ssn_eco(self,ssn):
        runs=bowling.ssn_runs(self,ssn)
        ovr=bowling.ssn_balls(self,ssn)/6
        eco=runs/ovr
        return round(eco,2)
    
    def ssn_sr(self,ssn):
        balls=bowling.ssn_balls(self,ssn)
        wk=bowling.ssn_wicket(self,ssn)
        if wk == 0:
            return "Nan"
        else:
            return round(balls/wk,2)
    
    def ssn_6(self,ssn):
        temp=bowling.ssn_table(self,ssn)
        return temp['six'].sum()
    
    def ssn_4(self,ssn):
        temp=bowling.ssn_table(self,ssn)
        return temp['four'].sum()
    
    
    
    