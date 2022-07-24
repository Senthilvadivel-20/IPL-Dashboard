import pandas as pd
import numpy as np

file="https://raw.githubusercontent.com/Senthilvadivel-20/Data/data/IPL.csv"
df=pd.read_csv(file,dtype={'season':np.object})

def runs_by_team(name):
    temp=df[df["striker"]==name]
    temp=temp.groupby('bowling_team').runs_off_bat.sum()
    temp=temp.reset_index()
    label=temp['bowling_team']
    value=temp['runs_off_bat']
    return label,value

def bowling_runs(name):
    temp=df[df["bowler"]==name]
    temp=temp.groupby('batting_team').total_runs.sum()
    temp=temp.reset_index()
    label=temp['batting_team']
    value=temp['total_runs']
    return label,value
    
def season_runs(name):
    temp=df[df["striker"]==name]
    temp=temp.groupby('season').runs_off_bat.sum()
    temp=temp.reset_index()
    label=temp['season'].to_list()
    value=temp['runs_off_bat'].to_list()
    return label,value


def Wicket_against_team(name):
    temp = df[df['bowler'] == name]
    temp = temp.groupby('batting_team').bowler_wk.sum().reset_index()
    return temp['batting_team'].to_list(),temp['bowler_wk'].to_list()

def Wicket_by_season(name):
    temp = df[df['bowler'] == name]
    temp = temp.groupby('season').bowler_wk.sum().reset_index()
    return temp['season'].to_list(),temp['bowler_wk'].to_list()
