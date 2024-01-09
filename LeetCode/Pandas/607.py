#https://leetcode.com/problems/sales-person/description/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata

import pandas as pd

def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    merged_df = company.merge(orders.merge(sales_person, on='sales_id'), on = 'com_id')
    df = merged_df[merged_df['name_x'] == 'RED'][['name_y']]
    return sales_person[~sales_person['name'].isin(df.values.ravel())][['name']]