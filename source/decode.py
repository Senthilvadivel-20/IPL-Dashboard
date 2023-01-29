import pandas as pd
from sklearn.preprocessing import LabelEncoder

venue_encoder=LabelEncoder()
team_encoder=LabelEncoder()

df = pd.read_csv('./Files/IPL.csv')

df['venue']=venue_encoder.fit_transform(df['venue'])
df['batting_team']=team_encoder.fit_transform(df['batting_team'])
df['bowling_team']=team_encoder.fit_transform(df['bowling_team'])

def encoding(venue,t1,t2):
    venue=venue_encoder.transform([venue])[0]
    batting_team=team_encoder.transform([t1])[0]
    bowling_team=team_encoder.transform([t2])[0]
    return venue,batting_team,bowling_team
