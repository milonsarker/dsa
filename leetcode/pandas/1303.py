#https://leetcode.com/problems/find-the-team-size/

import pandas as pd

def team_size(employee: pd.DataFrame) -> pd.DataFrame:
    emp_group_by = employee.groupby('team_id').agg({'employee_id': 'count'}).reset_index().rename(columns={'employee_id': 'team_size'})
    return employee.merge(emp_group_by, on='team_id', how='left')[['employee_id', 'team_size']]
