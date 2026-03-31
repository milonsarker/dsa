#https://leetcode.com/problems/find-total-time-spent-by-each-employee/
import pandas as pd

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    employees['duration'] = employees['out_time'] - employees['in_time']
    return employees.groupby(['event_day', 'emp_id']).sum().reset_index().rename(columns={'duration': 'total_time', 'event_day':'day'})[['day','emp_id','total_time']]