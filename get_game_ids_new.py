from pydantic import BaseModel, ValidationError
from datetime import datetime
from zoneinfo import ZoneInfo
from typing import List
import requests
import json
import pandas as pd

def get_game_ids_new(team = "26", season = "2022-23"):
    # Change season into year
    ### DOESNT WORK FOR 1999-2000
    season_formatted = season[:2] + season[-2:]
    
    # Create web request
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'}
    url = "https://www.espn.com/mens-college-basketball/team/schedule/_/id/" + str(team) + str("/season/") + str(season_formatted)
    
    r = requests.get(url, headers=headers)

    # Web request error check
    if str(r).find("<Response [403]>") > 0:
        print("403 Error")

    text = str(r.content) # convert to string for preprocessing

    # Triggers that bookend the json we are interested in within the page contents
    first_trigger = "\"scheduleData\":"
    second_trigger = "},\"subType"

    # Extract the json data we care about with these triggers
    text = text.split(first_trigger)
    text = text[1].split(second_trigger)

    text = text[0].replace("\\", "")

    # Convert json data into dict
    game_dict = json.loads(text)

    # Create pydantic models
    class Time(BaseModel):
        link: str | None = None
        time: datetime | None = None
        
    class Opponent(BaseModel):
        shortDisplayName: str | None = None
        homeAwaySymbol: str | None = None
        neutralSite: bool | None = None

    class Result(BaseModel):
        winLossSymbol: str | None = None
        currentTeamScore: int | None = None
        opponentTeamScore: int | None = None
        
    class SeasonType(BaseModel):
        name: str | None = None
        
    class Notes(BaseModel):
        headline: str | None = None

    class Game(BaseModel):
        time: Time | None
        opponent: Opponent | None
        result: Result | None
        seasonType: SeasonType | None
        notes: Notes | None
        
    class FlavorText(BaseModel):
        customText: str | None
        status: str | None
        
    class Events(BaseModel):
        pre: List[Game | FlavorText]
        post: List[Game | FlavorText]
        
    class TeamSchedule(BaseModel):
        events: Events
        
    class FullData(BaseModel):
        teamSchedule: List[TeamSchedule]

    # Try to fit json dict to pydantic model
    try:
        data = FullData(**game_dict)
    # If it fails, throw error (something wrong with input data)
    except ValidationError as e:
        return(e)

    # VIEW READABLE JSON OUTPUT
    # pretty = json.dumps(data.model_dump(), indent = 4, default = str)
    # print(pretty)

    def parseGame(Game: Game) -> dict:
        gameDict = {}
        for item in Game:
            data = item[1].model_dump()
            gameDict = gameDict | data # dict merge
        return(gameDict)

    allGameDicts = []
    for item in data.teamSchedule: # regular and postseason
        for game in item.events.post: # all games that already occurred (.post)
            if type(game) == Game:
                gameDict = parseGame(game)
                allGameDicts.append(gameDict)

    season_df = pd.DataFrame(allGameDicts)
    
    # CLEAN DATA
    
    
    return(season_df)