import matplotlib.pyplot as plt
from draw_court import draw_court
from get_game_shots import get_game_shots

def draw_shot_chart(gameid, team = 'home'):
    shots = get_game_shots(gameid)
    
    ax = draw_court()
    
    
    home_shots = shots.loc[shots['Home/Away'] == team]
    home_makes = home_shots.loc[home_shots['Scoring Play'] == True]
    home_misses = home_shots.loc[home_shots['Scoring Play'] == False]
    
    ax.scatter(y = home_makes['X coordinate']*12, x = home_makes['Y coordinate']*12 + 63, marker = 'o', color='#1f77b4', s = 5)
    ax.scatter(y = home_misses['X coordinate']*12, x = home_misses['Y coordinate']*12 + 63, facecolors='none', edgecolors='#1f77b4', linewidths= 0.7, s = 8)
    plt.show()