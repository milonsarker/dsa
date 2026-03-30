#https://leetcode.com/problems/replace-employee-id-with-the-unique-identifier/

import pandas as pd

def replace_employee_id(employees: pd.DataFrame, employee_uni: pd.DataFrame) -> pd.DataFrame:
    return employee_uni.merge(employees, on = 'id', how = 'right')[['unique_id', 'name']]