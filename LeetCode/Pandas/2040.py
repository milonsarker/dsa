#https://leetcode.com/problems/accepted-candidates-from-the-interviews/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata

import pandas as pd

def accepted_candidates(candidates: pd.DataFrame, rounds: pd.DataFrame) -> pd.DataFrame:
    merged = candidates.merge(rounds, on = 'interview_id')
    grouped = merged.groupby(['candidate_id', 'years_of_exp']).sum().reset_index()
    result = grouped[(grouped['years_of_exp'] >= 2) & (grouped['score']>15)][['candidate_id']]
    return result
    