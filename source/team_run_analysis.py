import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')

df=pd.read_csv("https://raw.githubusercontent.com/Senthilvadivel-20/Data/data/IPL.csv",dtype={'season':np.object})
dt=pd.read_json('https://raw.githubusercontent.com/Senthilvadivel-20/Data/data/Match.json')

#-----------------------------------------------#
#               Functions                       #
#-----------------------------------------------#
class Team_Batting:
    def __init__(self,name):
        self.name = name
        
    #No of matchs played
    def total_matches(self):
        n=len(dt[(dt['team_1']==self.name) | (dt['team_2']==self.name)])
        return n
    
    def total_runs(self):
        temp = df[df['batting_team']==self.name]
        scr = temp['total_runs'].sum()
        return scr
    
    def total_runs_off_bat(self):
        temp = df[df['batting_team']==self.name]
        scr = temp['runs_off_bat'].sum()
        return scr
    
    def total_extra_runs(self):
        temp = df[df['batting_team']==self.name]
        scr = temp['extras'].sum()
        return scr
    
    def total_wk(self):
        temp = df[df['batting_team']==self.name]
        wk = temp['wk'].sum()
        return wk
    
    def total_dot(self):
        temp = df[df['batting_team']==self.name]
        scr = temp['dot'].sum()
        return scr
    
    
    def total_one(self):
        temp = df[df['batting_team']==self.name]
        scr = temp['one'].sum()
        return scr
    
    def total_two(self):
        temp = df[df['batting_team']==self.name]
        scr = temp['two'].sum()
        return scr
    
    def total_three(self):
        temp = df[df['batting_team']==self.name]
        scr = temp['three'].sum()
        return scr
    
    def total_four(self):
        temp = df[df['batting_team']==self.name]
        scr = temp['four'].sum()
        return scr
    
    def total_five(self):
        temp = df[df['batting_team']==self.name]
        scr = temp['five'].sum()
        return scr
    
    def total_six(self):
        temp = df[df['batting_team']==self.name]
        scr = temp['six'].sum()
        return scr
    
    
    #!!!!!!!!!!!!!! SEASON !!!!!!!!!!!!!!!!!!!
    
    def ssn_matches(self,ssn):
        n=len(dt[((dt['team_1']==self.name) | (dt['team_2']==self.name)) & (dt['season'] == ssn)])
        return n
    
    def ssn_runs(self,ssn):
        temp = df[(df['batting_team']==self.name) & (df['season'] == ssn)]
        scr = temp['total_runs'].sum()
        return scr
    
    def ssn_runs_off_bat(self,ssn):
        temp = df[(df['batting_team']==self.name) & (df['season'] == ssn)]
        scr = temp['runs_off_bat'].sum()
        return scr
    
    def ssn_extra_runs(self,ssn):
        temp = df[(df['batting_team']==self.name) & (df['season'] == ssn)]
        scr = temp['extras'].sum()
        return scr
    
    def ssn_wk(self,ssn):
        temp = df[(df['batting_team']==self.name) & (df['season'] == ssn)]
        wk = temp['wk'].sum()
        return wk
    
    def ssn_dot(self,ssn):
        temp = df[(df['batting_team']==self.name) & (df['season'] == ssn)]
        scr = temp['dot'].sum()
        return scr
    
    
    def ssn_one(self,ssn):
        temp = df[(df['batting_team']==self.name) & (df['season'] == ssn)]
        scr = temp['one'].sum()
        return scr
    
    def ssn_two(self,ssn):
        temp = df[(df['batting_team']==self.name) & (df['season'] == ssn)]
        scr = temp['two'].sum()
        return scr
    
    def ssn_three(self,ssn):
        temp = df[(df['batting_team']==self.name) & (df['season'] == ssn)]
        scr = temp['three'].sum()
        return scr
    
    def ssn_four(self,ssn):
        temp = df[(df['batting_team']==self.name) & (df['season'] == ssn)]
        scr = temp['four'].sum()
        return scr
    
    def ssn_five(self,ssn):
        temp = df[(df['batting_team']==self.name) & (df['season'] == ssn)]
        scr = temp['five'].sum()
        return scr
    
    def ssn_six(self,ssn):
        temp = df[(df['batting_team']==self.name) & (df['season'] == ssn)]
        scr = temp['six'].sum()
        return scr
        


#=================================================================================#
#                                    BOWLING                                      #
#=================================================================================#

#TEAM BOWLING
class Team_Bowling:
    
    def __init__(self,name):
        self.name = name
    
    def total_matches(self):
        n=len(dt[(dt['team_1']==self.name) | (dt['team_2']==self.name)])
        return n
    
    def total_runs(self):
        temp = df[df['bowling_team']==self.name]
        scr = temp['total_runs'].sum()
        return scr
    
    def total_runs_off_bat(self):
        temp = df[df['bowling_team']==self.name]
        scr = temp['runs_off_bat'].sum()
        return scr
    
    def total_extra_runs(self):
        temp = df[df['bowling_team']==self.name]
        scr = temp['extras'].sum()
        return scr
    
    def total_wk(self):
        temp = df[df['bowling_team']==self.name]
        wk = temp['wk'].sum()
        return wk
    
    def total_bowled_wk(self):
        temp = df[df['bowling_team']==self.name]
        wk = temp['bowled'].sum()
        return wk
    
    
    def total_caught_wk(self):
        temp = df[df['bowling_team']==self.name]
        wk = temp['caught'].sum()
        return wk
    
    def total_caught_and_bowled_wk(self):
        temp = df[df['bowling_team']==self.name]
        wk = temp['caught and bowled'].sum()
        return wk
    
    def total_hit_wicket_wk(self):
        temp = df[df['bowling_team']==self.name]
        wk = temp['hit wicket'].sum()
        return wk
    
    def total_lbw_wk(self):
        temp = df[df['bowling_team']==self.name]
        wk = temp['lbw'].sum()
        return wk
    
    def total_obstructing_the_field_wk(self):
        temp = df[df['bowling_team']==self.name]
        wk = temp['obstructing the field'].sum()
        return wk
    
    def total_retired_hurt_wk(self):
        temp = df[df['bowling_team']==self.name]
        wk = temp['retired hurt'].sum()
        return wk
    
    def total_run_out_wk(self):
        temp = df[df['bowling_team']==self.name]
        wk = temp['run out'].sum()
        return wk
    
    def total_stumped_wk(self):
        temp = df[df['bowling_team']==self.name]
        wk = temp['stumped'].sum()
        return wk
    
    
    
    #!!!!!!!!!!!!!! SEASON !!!!!!!!!!!!!!!!!!!
    
    def ssn_matches(self,ssn):
        n=len(dt[((dt['team_1']==self.name) | (dt['team_2']==self.name)) & (dt['season'] == ssn)])
        return n
    
    def ssn_runs(self,ssn):
        temp = df[(df['bowling_team']==self.name) & (df['season'] == ssn)]
        scr = temp['total_runs'].sum()
        return scr
    
    def ssn_runs_off_bat(self,ssn):
        temp = df[(df['bowling_team']==self.name) & (df['season'] == ssn)]
        scr = temp['runs_off_bat'].sum()
        return scr
    
    def ssn_extra_runs(self,ssn):
        temp = df[(df['bowling_team']==self.name) & (df['season'] == ssn)]
        scr = temp['extras'].sum()
        return scr
    
    def ssn_wk(self,ssn):
        temp = df[(df['bowling_team']==self.name) & (df['season'] == ssn)]
        wk = temp['wk'].sum()
        return wk
    
    def ssn_bowled_wk(self,ssn):
        temp = df[(df['bowling_team']==self.name) & (df['season'] == ssn)]
        wk = temp['bowled'].sum()
        return wk
    
    
    def ssn_caught_wk(self,ssn):
        temp = df[(df['bowling_team']==self.name) & (df['season'] == ssn)]
        wk = temp['caught'].sum()
        return wk
    
    def ssn_caught_and_bowled_wk(self,ssn):
        temp = df[(df['bowling_team']==self.name) & (df['season'] == ssn)]
        wk = temp['caught and bowled'].sum()
        return wk
    
    def ssn_hit_wicket_wk(self,ssn):
        temp = df[(df['bowling_team']==self.name) & (df['season'] == ssn)]
        wk = temp['hit wicket'].sum()
        return wk
    
    def ssn_lbw_wk(self,ssn):
        temp = df[(df['bowling_team']==self.name) & (df['season'] == ssn)]
        wk = temp['lbw'].sum()
        return wk
    
    def ssn_obstructing_the_field_wk(self,ssn):
        temp = df[(df['bowling_team']==self.name) & (df['season'] == ssn)]
        wk = temp['obstructing the field'].sum()
        return wk
    
    def ssn_retired_hurt_wk(self,ssn):
        temp = df[(df['bowling_team']==self.name) & (df['season'] == ssn)]
        wk = temp['retired hurt'].sum()
        return wk
    
    def ssn_run_out_wk(self,ssn):
        temp = df[(df['bowling_team']==self.name) & (df['season'] == ssn)]
        wk = temp['run out'].sum()
        return wk
    
    def ssn_stumped_wk(self,ssn):
        temp = df[(df['bowling_team']==self.name) & (df['season'] == ssn)]
        wk = temp['stumped'].sum()
        return wk


#===========================================================================

def season_list(team):
    t = df[(df['batting_team']==team)]
    return list(t['season'].unique())