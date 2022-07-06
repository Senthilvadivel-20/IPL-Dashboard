from django.conf import settings
from django.conf.urls.static import static
from unicodedata import name
from django import views
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name="Home"),
    path('player_home',views.player_home,name="player_home"),
    path('player_feature',views.batsman,name="player_feature"),
    path('summary_table',views.result,name="summary_table"),
    path('Runs_against_teams_chart',views.Runs_against_teams_chart,name="Runs_against_teams_chart"),
    path('Wicket_chart',views.Wicket_chart,name="Wicket_chart"),
    path('player/<name>',views.batsman_url,name="player_details"),
    #Comparing players
    path('Comparing_player_home',views.comparing_player_home,name="Comparing_player_home"),
    path('Comparison_of_players',views.comparing_player,name="Comparison_of_players"),

    #Teams
    path('enter_team',views.enter_team,name="enter_team"),
    path('team_home',views.team_home,name="team_home"),
    path('team_stats',views.team_stats,name="team_stats"),

    #head2head
    path('h2h_home',views.h2h_home,name="head_to_head_home"),
    path('h2h',views.h2h,name="h2h"),
    path('h2h/<name>',views.h2h_team_target,name="h2h_target"),

    #Stats
    path('stats_overall_highscore',views.get_overall_batsman_high_score,name='stats_overall_highscore'),
    path('stats_season_highscore',views.get_by_season_batsman_high_score,name='stats_season_highscore'),
    path('stats_overall_bowler_wk',views.get_overall_bowler_stats,name="stats_overall_bowler_wk"),
    path('stats_season_bowler_wk',views.get_season_bowler__stats,name="stats_season_bowler_wk"),

    #Score prediction
    path('score_prediction_home',views.score_prediction_home,name="score_prediction_home"),
    path('score_prediction_result',views.score_prediction, name = "score_prediction_result")

    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
