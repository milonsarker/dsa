#https://leetcode.com/problems/group-sold-products-by-the-date/

import pandas as pd

def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
    groups = activities.groupby('sell_date')
    df = groups.agg(
        num_sold = ('product','nunique'),
        products = ('product', lambda x: ','.join(sorted(set(x))))
    ).reset_index()
    df.sort_values(by = 'sell_date', inplace = True)
    return df
    