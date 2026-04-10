#https://leetcode.com/problems/all-the-matches-of-the-league/

import pandas as pd

def find_all_matches(teams: pd.DataFrame) -> pd.DataFrame:
    joined_df = teams.merge(teams,  how='cross').rename(columns={'team_name_x': 'home_team', 'team_name_y': 'away_team'})
    return joined_df[joined_df['home_team'] != joined_df['away_team']]
