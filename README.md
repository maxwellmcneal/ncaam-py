# ncaam-py

This repo contains helper functions for analyzing NCAAM basketball data in Python.


### draw_court.py
This is a function to draw an image of a properly scaled NCAAM basketball court. It is used as follows:
```python
from draw_court import draw_court

draw_court()
```
![image](https://github.com/maxwellmcneal/ncaam-py/assets/135375736/eda8d142-bc0e-4492-bf66-1432dce6022c)

### draw_shot_chart.py
This is a function to plot the shotchart from a specific game on an image of the court to better show where teams were scoring from.
A filled in dot indicates a make, and a hollow dot indicates a miss.
The game is selected using the gameid argument, which is a 9 digit number that appears at the end of the URL for the game on ESPN.com.
For example, the ESPN page for the Arizona vs. UCLA matchup on March 4th, 2023 is found at https://www.espn.com/mens-college-basketball/game/_/gameId/401490418.
Looking in the URL, it ends with the number 401490418, thus the gameid for this game is 401490418.
The other argument, team, is used to select if the shotchart for the home team or the away team will be shown.
The default team displayed is the home team, but it can easily be changed to the away team by adding ```team = 'away'```.

```python
from draw_shot_chart import draw_shot_chart

draw_shot_chart(gameid = 401490418, team = 'home')
```
![image](https://github.com/maxwellmcneal/ncaam-py/assets/135375736/2a5785e8-5be8-453b-a760-31902b61b27e)


### get_game_shots.py
This function returns a Pandas DataFrame containing information about all the shots taken in a game, such as the player who took the shot, which team they are on, the X and Y coordinate of the shot on the floor, if the shot was a 3 pointer, if the shot was assisted, etc.
The game is selected using the gameid argument, which is a 9 digit number that appears at the end of the URL for the game on ESPN.com.
For example, the ESPN page for the Arizona vs. UCLA matchup on March 4th, 2023 is found at https://www.espn.com/mens-college-basketball/game/_/gameId/401490418.
Looking in the URL, it ends with the number 401490418, thus the gameid for this game is 401490418.
```python
from get_game_shots import get_game_shots

data = get_game_shots(gameid = 401490418)
data.head()
```
![image](https://github.com/maxwellmcneal/ncaam-py/assets/135375736/5096e27f-50cb-4ef6-a153-179a09c58d1c)
