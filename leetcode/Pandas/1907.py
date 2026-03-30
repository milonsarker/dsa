#https://leetcode.com/problems/count-salary-categories/

import pandas as pd

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    low = sum(accounts['income']<20000)
    hi = sum(accounts['income'] > 50000)
    avg = sum((accounts['income']>=20000) & (accounts['income']<=50000))
    return pd.DataFrame({'category':['Low Salary', 'Average Salary', 'High Salary'], 'accounts_count':[low,avg,hi]})
    