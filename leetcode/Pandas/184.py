#https://leetcode.com/problems/department-highest-salary/

import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    df = employee.merge(department, left_on= 'departmentId', right_on = 'id', suffixes=('_emp', '_dept'))
    df_max = df.groupby('id_dept')['salary'].max().reset_index()
    df_result = pd.merge(df, df_max,  how='inner', left_on=['id_dept','salary'], right_on = ['id_dept','salary'])
    df_result.rename(columns = {'name_dept':'Department', 'name_emp':'Employee', 'salary':'Salary'}, inplace = True)
    return df_result[['Department','Employee', 'Salary']]