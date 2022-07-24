from base64 import encode
from django.shortcuts import render
from regex import match
from source.runs import *
from source.batsman import runs,bowling,batted_season,bowled_season
from source.team_run_analysis import Team_Batting, Team_Bowling, season_list
from source.h2h import *
from source import stats
from source import decode
#Web Scrap
import requests 
import bs4 

#Score prediction
from sklearn.preprocessing import LabelEncoder
import joblib

def home(request):
    return render(request,'Home.html',locals())

def player_home(request):
    return render(request,'player_home.html',locals())

def batsman(request):
    global Name
    name=request.POST['Name']
    Name = name
    return render(request,'player_feature.html',locals())

def batsman_url(request,name):
    global Name
    # name=request.POST['Name']
    Name = name
    return render(request,'player_feature.html',locals())

def Runs_against_teams_chart(request):

    # name=request.POST['Name']
    name=Name

    # Batsman
    bat_res=runs_by_team(name)
    bat_labels=list(bat_res[0])
    bat_values=list(bat_res[1])

    # Bowling
    bowl_res=bowling_runs(name)
    bowl_labels=list(bowl_res[0])
    bowl_values=list(bowl_res[1])

    #Season run
    ssn_res=season_runs(name)
    ssn_labels=ssn_res[0]
    ssn_values=ssn_res[1]

    # print(ssn_labels)
    return render(request,'player_runs_chart.html',locals())

#Bowling part
def Wicket_chart(request):
    
    name = Name

    wicket_against_team = Wicket_against_team(name)
    wicket_against_team_labels = wicket_against_team[0]
    wicket_against_team_values = wicket_against_team[1]

    wicket_by_season = Wicket_by_season(name)
    wicket_by_season_labels = wicket_by_season[0]
    wicket_by_season_values = wicket_by_season[1]

    return render(request,'player_wicket_chart.html',locals())

def result(request):
    # name=request.POST["Name"]
    name=Name
    obj=runs(name)

    total=[obj.total_match(),obj.batted_match(), obj.total_out(),obj.total_runs(),obj.total_hs(),obj.total_ball_faced(), obj.total_avg(), obj.total_strike_rate(), obj.total_100(), obj.total_50(), obj.total_30(), obj.total_6(), obj.total_5(), obj.total_4(), obj.total_3(), obj.total_2(), obj.total_1(), obj.total_dot()]

    bat_ssn=batted_season(name)

    ssn_list=[]
    for i in bat_ssn:
        y=i
        s1=obj.ssn_match(i)
        s2=obj.ssn_batted_match(i)
        s3=obj.ssn_out(i)
        s4=obj.ssn_runs(i)
        s5=obj.ssn_hs(i)
        s6=obj.ssn_ball_faced(i)
        s7=obj.ssn_avg(i)
        s8=obj.ssn_strike_rate(i)
        s9=obj.ssn_100(i)
        s10=obj.ssn_50(i)
        s11=obj.ssn_30(i)
        s12=obj.ssn_6(i)
        s13=obj.ssn_5(i)
        s14=obj.ssn_4(i)
        s15=obj.ssn_3(i)
        s16=obj.ssn_2(i)
        s17=obj.ssn_1(i)
        s18=obj.ssn_dot(i)
        lis=[y,s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14,s15,s16,s17,s18]
        ssn_list.append(lis)

    ssn_list.reverse() 

    #boling part

    bwl_ssn= bowled_season(name)

    bwl=bowling(name)
    ttl=[ bwl.total_match(), bwl.bowled_match(), bwl.total_balls(), bwl.total_runs(), bwl.total_wicket(), bwl.total_bbw(), bwl.total_avg(), bwl.total_eco(), bwl.total_sr(), bwl.total_6(), bwl.total_4() ]

    ssn_bowl_list=[]
    for i in bwl_ssn:
        v1=i
        v2=bwl.ssn_match(i)
        v3=bwl.ssn_bowled_match(i)
        v4=bwl.ssn_balls(i)
        v5=bwl.ssn_runs(i)
        v6=bwl.ssn_wicket(i)
        v7=bwl.ssn_bbw(i)
        v8=bwl.ssn_avg(i)
        v9=bwl.ssn_eco(i)
        v10=bwl.ssn_sr(i)
        v11=bwl.ssn_6(i)
        v12=bwl.ssn_4(i)
        lis=[v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12]
        ssn_bowl_list.append(lis)

    ssn_bowl_list.reverse()

    return render(request,'table.html',locals())



#_________________________________________________________________________________
########################### Player Comparison ###################################
#_________________________________________________________________________________

def comparing_player_home(request):
    return render(request,'comparing_player_home.html')

def comparing_player(request):

    player_1 = request.GET['player_1']
    player_2 = request.GET['player_2']

    labels = ['Total Match', 'Batted Match', 'out', 'Total runs', 'High Score', 'Ball faced', 'Average', 'Strike rate', '100+', '50+', '30+', '6', '5', '4', '3', '2', '1', '0', 'No.of.Match', 'Bowled match', 'Balls', 'Runs', 'Wickets', 'BBM', 'Average', 'Economy', 'Strike Rate', '6', '4']

    #For player 1
    obj = runs(player_1)
    bwl=bowling(player_1)
    player_1_value=[obj.total_match(),obj.batted_match(), obj.total_out(),obj.total_runs(),obj.total_hs(),obj.total_ball_faced(), obj.total_avg(), obj.total_strike_rate(), obj.total_100(), obj.total_50(), obj.total_30(), obj.total_6(), obj.total_5(), obj.total_4(), obj.total_3(), obj.total_2(), obj.total_1(), obj.total_dot(),
                        bwl.total_match(), bwl.bowled_match(), bwl.total_balls(), bwl.total_runs(), bwl.total_wicket(), bwl.total_bbw(), bwl.total_avg(), bwl.total_eco(), bwl.total_sr(), bwl.total_6(), bwl.total_4()
                            ]

    #For player 2
    obj = runs(player_2)
    bwl=bowling(player_2)
    player_2_value=[obj.total_match(),obj.batted_match(), obj.total_out(),obj.total_runs(),obj.total_hs(),obj.total_ball_faced(), obj.total_avg(), obj.total_strike_rate(), obj.total_100(), obj.total_50(), obj.total_30(), obj.total_6(), obj.total_5(), obj.total_4(), obj.total_3(), obj.total_2(), obj.total_1(), obj.total_dot(),
                        bwl.total_match(), bwl.bowled_match(), bwl.total_balls(), bwl.total_runs(), bwl.total_wicket(), bwl.total_bbw(), bwl.total_avg(), bwl.total_eco(), bwl.total_sr(), bwl.total_6(), bwl.total_4()
                            ]

    data = []
    for i in range(len(labels)):
        temp = [labels[i], player_1_value[i], player_2_value[i]]
        data.append(temp)    


    return render(request,'comparison_of_players.html',locals())

#--------------------------------------------------------------------#
#                   Support function                                 #
#--------------------------------------------------------------------#

def team_info(team):
    team = team.lower().replace(" ","-")
    try:
        url = "https://www.iplt20.com/teams/"+team
        request_result = requests.get( url )
        soup = bs4.BeautifulSoup( request_result.text , "html.parser" )
        temp = soup.find( "div" , class_='vn-teamdesc col-100 floatLft text-left' )
        info = []
        for i in temp.find_all('p'):
            info.append(i.text)
        
        try:
            temp2 = soup.find( "div" , class_='vn-trophyBtn' ).text
            year = [int(i) for i in temp2.split(',')]
        except:
            year = None
        
        url1 = "https://www.iplt20.com/teams/"+team+"/squad"
        request_result1 = requests.get( url1 )
        soup1 = bs4.BeautifulSoup( request_result1.text , "html.parser" )
        temp1 = soup1.find( "div" , class_='ih-pcard-wrap' )
        player_list = []
        for i in temp1.find_all('h2'):
            player_list.append(i.text)

        return info,player_list,year
    except:
        info = ['Owner : No Data', 'Coach : No Data', 'Venue : No data', 'Captain : No Data']
        player_list = ['no Data']
        year = None
        return info,player_list,year
    

#################### TEAM ####################################

def enter_team(request):
    return render(request,'team_enter.html')

def team_home(request):

    global team_name

    team_name = request.GET['team_name']

    val = team_info(team_name)

    info = val[0]
    player_list = val[1]
    year = val[2]


    return render(request,'team_home.html',locals())

def team_stats(request):
    name = team_name    
    sl = season_list(team_name)

    bat = Team_Batting(team_name)

    batting_total = ['Over all',bat.total_matches(), bat.total_runs(), bat.total_runs_off_bat(), bat.total_extra_runs(), bat.total_wk(), bat.total_dot(), bat.total_one(), bat.total_two(), bat.total_three(), bat.total_four(), bat.total_five(), bat.total_six()]

    ssn_bat_list = []
    for i in sl:
        t = [i,bat.ssn_matches(i), bat.ssn_runs(i), bat.ssn_runs_off_bat(i), bat.ssn_extra_runs(i), bat.ssn_wk(i), bat.ssn_dot(i), bat.ssn_one(i), bat.ssn_two(i), bat.ssn_three(i), bat.ssn_four(i), bat.ssn_five(i), bat.ssn_six(i)]
        ssn_bat_list.append(t)

    bow = Team_Bowling(team_name)

    bowling_total = ['Over all', bow.total_matches(), bow.total_runs(), bow.total_runs_off_bat(), bow.total_extra_runs(),bow.total_wk(),bow.total_bowled_wk(),bow.total_caught_wk(),bow.total_caught_and_bowled_wk(),bow.total_hit_wicket_wk(),bow.total_lbw_wk(),bow.total_obstructing_the_field_wk(), bow.total_retired_hurt_wk(), bow.total_run_out_wk(), bow.total_stumped_wk() ]

    ssn_bowl_list = []

    for i in sl:
        t = [i,bow.ssn_matches(i), bow.ssn_runs(i), bow.ssn_runs_off_bat(i), bow.ssn_extra_runs(i),bow.ssn_wk(i),bow.ssn_bowled_wk(i),bow.ssn_caught_wk(i),bow.ssn_caught_and_bowled_wk(i),bow.ssn_hit_wicket_wk(i),bow.ssn_lbw_wk(i),bow.ssn_obstructing_the_field_wk(i), bow.ssn_retired_hurt_wk(i), bow.ssn_run_out_wk(i), bow.ssn_stumped_wk(i) ]
        ssn_bowl_list.append(t)

    return render(request, 'team_stats.html',locals())


#=========================================================================#
#                             Head to Head                                #
#=========================================================================#

def h2h_home(request):
    return render(request,'h2h_home.html')

def h2h(request):

    t1 = request.GET['team_1']
    t2 = request.GET['team_2']

    team_1_win = head2head_win(t1,t2)
    team_2_win = head2head_win(t2,t1)

    team_1_lose = team_2_win
    team_2_lose = team_1_win

    tie = is_any_tie(t1,t2)

    team_1_hs = match_high_score(t1,t2)
    team_2_hs = match_high_score(t2,t1)

    team_1_ls = match_low_score(t1,t2)
    team_2_ls = match_low_score(t2,t1)

    team_1_url = t1 + "and" + t2
    team_2_url = t2 + "and" + t1

    return render(request,'h2h.html',locals())

def h2h_team_target(request,name):
    
    teams = name.split("and")
    t1 = teams[0]
    t2 = teams[1]

    val = target(t1,t2)

    team_labels = val[0]
    team_values = val[1]


    return render(request,'h2h_team_target_chart.html',locals())

def get_overall_batsman_high_score(request):
    lis = stats.get_batsman_high_score()
    return render(request,'stats_overall_batsman_high_score.html',locals())

def get_by_season_batsman_high_score(request):
    ssn = request.GET['season']
    lis = stats.get_season_batsman_high_score(ssn)
    print(lis[0])
    return render(request,'stats_overall_batsman_high_score.html',locals())

def get_overall_bowler_stats(request):
    lis = stats.get_bowler_innings_wk()
    return render(request,'stats_bowler_wk.html',locals())

def get_season_bowler__stats(request):
    ssn = request.GET['season']
    lis = stats.get_bowler_innings_wk_by_season(ssn)
    return render(request,'stats_bowler_wk.html',locals())


# ------------------------Score Prediction-----------------------------
def score_prediction_home(request):
    return render(request,'score_prediction_home.html')

def score_prediction(request):

    venue = request.GET['venue']
    team_1 = request.GET['batting_team']
    team_2 = request.GET['bowling_team']
    encode = decode.encoding(venue,team_1,team_2)

    bowled=str(request.GET['over'])+'.'+str(request.GET['balls'])

    venue = encode[0]
    innings=int(request.GET['innings'])
    batting_team = encode[1]
    bowling_team = encode[2]
    ball=float(bowled)
    run=int(request.GET['run'])
    wicket=int(request.GET['wicket'])

    predictor=[[venue,innings,batting_team,bowling_team,ball,run,wicket]]

    lr = joblib.load('./Files/predicted_score.sav')

    print(predictor)

    score = int(lr.predict(predictor)[0])

    return render(request,'score_prediction_result.html',locals())
