#https://leetcode.com/problems/game-play-analysis-i/
import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    return activity.groupby('player_id').min().reset_index().rename(columns = {'event_date':'first_login'})[['player_id','first_login']]