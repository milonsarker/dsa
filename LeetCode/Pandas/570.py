#https://leetcode.com/problems/managers-with-at-least-5-direct-reports/

import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    cnt_df = employee.groupby('managerId').size().reset_index(name='count')
    cnt_df = cnt_df[cnt_df['count']>=5]
    df = employee.merge(cnt_df, left_on = 'id', right_on = 'managerId')[['name']]
    return df