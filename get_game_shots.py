import requests
import json
import pandas as pd

def get_game_shots(gameid):
    url = "https://www.espn.com/mens-college-basketball/playbyplay?gameId=" + str(gameid)
    r = requests.get(url)
    
    text = str(r.content)
    text = text.split('shtChrt')
    text = text[1].split('plays')
    data = text[1]
    data = data[3:]

    data = data.split('],"tms')
    data = data[0]

    shots = data.replace("},{", "}~{")
    shots = shots.split("~")
    
    id = []
    half = []
    text = []
    home_away = []
    athlete_id = []
    athlete_name = []
    x_coord = []
    y_coord = []
    shot_type_id = []
    shot_type_text = []
    scoring_play = []
    assisted = []
    three_pointer = []
    free_throw = []

    for shot in shots:
        shot = json.loads(shot)
        
        id.append(shot['id'])
        half.append(shot['period']['number'])
        text.append(shot['text'])
        home_away.append(shot['homeAway'])
        athlete_id.append(shot['athlete']['id'])
        athlete_name.append(shot['athlete']['name'])
        x_coord.append(shot['coordinate']['x'])
        y_coord.append(shot['coordinate']['y'])
        shot_type_id.append(shot['type']['id'])
        shot_type_text.append(shot['type']['txt'])
        
        if shot['text'].find('made') > 0:
            made = True
        else:
            made = False
        scoring_play.append(made)
        
        if shot['text'].find('Assist') > 0:
            assist = True
        else:
            assist = False
        assisted.append(assist)
        
        if shot['text'].find('Three') > 0:
            three = True
        else:
            three = False
        three_pointer.append(three)
        
        if shot['text'].find('Free') > 0:
            ft = True
        else:
            ft = False
        free_throw.append(ft)
        

    result = pd.DataFrame({
        "ID":id,
        "Half":half,
        "Description":text,
        "Home/Away":home_away,
        "Athlete ID":athlete_id,
        "Athlete Name":athlete_name,
        "X coordinate":x_coord,
        "Y coordinate":y_coord,
        "Shot Type ID":shot_type_id,
        "Shot Type Description":shot_type_text,
        "Scoring Play":scoring_play,
        "Assisted":assisted,
        "Three Pointer":three_pointer,
        "Free Throw":free_throw
    })
    
    return(result)

# get_game_shots(401490418)