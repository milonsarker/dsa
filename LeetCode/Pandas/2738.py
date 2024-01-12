#https://leetcode.com/problems/count-occurrences-in-text/

import pandas as pd
import re

def count_occurrences(files: pd.DataFrame) -> pd.DataFrame:
    bear_cnt = files[files["content"].str.contains(r"(\s+bear\s+)", regex=True, case=False)]["file_name"].nunique()
    bull_cnt = files[files["content"].str.contains(r"(\s+bull\s+)", regex=True, case=False)]["file_name"].nunique()
    
    df = pd.DataFrame({'word': ['bull', 'bear'], 'count': [bull_cnt, bear_cnt]})
    return df