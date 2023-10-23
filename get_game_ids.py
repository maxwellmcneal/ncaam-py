import requests
import json
import pandas as pd
from datetime import datetime

def get_game_ids(team = "26", season = "2022-23"):
    
    season_formatted = season[:2] + season[-2:]
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'}
    url = "https://www.espn.com/mens-college-basketball/team/schedule/_/id/" + str(team) + str("/season/") + str(season_formatted)
    r = requests.get(url, headers=headers)
    
    if str(r).find("<Response [403]>") > 0:
        print("403 Error")
    
    text = str(r.content)

    first_trigger = "[],\"teamSchedule\":"
    second_trigger = ",\"noData\":\"No Data Available\"}"

    text = text.split(first_trigger)
    text = text[1].split(second_trigger)
    text = text[0].replace("\\", "")

    postseason = None

    if text.find("Postseason") > 0:
        text = text.replace("}}]}},{", "}}]}}~{")
        text = text.split("~")
        postseason = text[0]
        regseason = text[1]
        
        postseason = postseason.replace("\"post\":[{", "~{")
        postseason = postseason.split("~")
        postseason = postseason[1]
        postseason = postseason[:-4]  
        postseason = postseason.replace("},{", "}~{")
        postseason = postseason.split("~")
        postseason_games = []
        for game in postseason:
            if game.find("date") > 0:
                postseason_games.append(game)
        postseason_games[-1] = postseason_games[-1] + "}"
    else:
        regseason = text
        
    regseason = regseason.replace("\"post\":[{", "~{")
    regseason = regseason.split("~")
    regseason = regseason[1]
    regseason = regseason[:-4]  
    regseason = regseason.replace("},{", "}~{")
    regseason = regseason.split("~")

    if postseason is not None:
        season = regseason + postseason_games
    else:
        season = regseason

    game_id = []
    date = []
    opponent = []
    win_loss_symbol = []
    team_score = []
    opponent_score = []
    location = []
    season_type = []

    for game in season:
        game = json.loads(game)
        
        game_id.append(game["result"]["link"].split("/")[-1])
        date.append(datetime.strptime(game["date"]["date"][:10], '%Y-%m-%d').date())
        opponent.append(game["opponent"]["shortDisplayName"])
        win_loss_symbol.append(game["result"]["winLossSymbol"])
        team_score.append(game["result"]["currentTeamScore"])
        opponent_score.append(game["result"]["opponentTeamScore"])
        season_type.append(game["seasonType"]["name"])

        neutralsite = game["opponent"]["neutralSite"]
        if neutralsite:
            location.append("Neutral Site")
        elif game["opponent"]["homeAwaySymbol"] == "vs":
            location.append('Home')
        elif game["opponent"]["homeAwaySymbol"] == "@":
            location.append("Away")
        else:
            location.append("N/A")

    season_df = pd.DataFrame({
        "Game ID":game_id,
        "Date":date,
        "Opponent":opponent,
        "Win/Loss":win_loss_symbol,
        "Team Score":team_score,
        "Opponent Score":opponent_score,
        "Location":location,
        "Type of Game":season_type
    })
    return(season_df)