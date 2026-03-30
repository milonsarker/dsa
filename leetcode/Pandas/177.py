#https://leetcode.com/problems/nth-highest-salary/description/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata

import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    uniq_sal = employee['salary'].drop_duplicates()
    sorted_sal = uniq_sal.sort_values(ascending= False)
    if N > len(sorted_sal) or N < 1:
        return pd.DataFrame({f'getNthHighestSalary({N})': [None]})
    nth_hi = sorted_sal.iloc[N-1]
    return pd.DataFrame({f'getNthHighestSalary({N})': [nth_hi]})