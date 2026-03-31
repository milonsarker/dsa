#https://leetcode.com/problems/second-highest-salary/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata

import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    N = 2
    uniq_sal = employee['salary'].drop_duplicates()
    sorted_sal = uniq_sal.sort_values(ascending= False)
    if N > len(sorted_sal) or N < 1:
        return pd.DataFrame({f'SecondHighestSalary': [None]})
    nth_hi = sorted_sal.iloc[N-1]
    return pd.DataFrame({f'SecondHighestSalary': [nth_hi]})