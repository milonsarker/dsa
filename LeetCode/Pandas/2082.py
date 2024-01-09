#https://leetcode.com/problems/the-number-of-rich-customers/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata

import pandas as pd

def count_rich_customers(store: pd.DataFrame) -> pd.DataFrame:
    df_filtered = store[store['amount']>500]
    rich_count = df_filtered['customer_id'].nunique()
    return pd.DataFrame({'rich_count':[rich_count]})