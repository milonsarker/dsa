#https://leetcode.com/problems/immediate-food-delivery-i/

import pandas as pd

def food_delivery(delivery: pd.DataFrame) -> pd.DataFrame:
    percentage = round(sum( delivery['order_date'] == delivery['customer_pref_delivery_date'] ) * 100/len(delivery), 2)
    return pd.DataFrame({'immediate_percentage':[percentage]})