#https://leetcode.com/problems/customer-placing-the-largest-number-of-orders/

import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    if orders.empty:
        return pd.DataFrame({'customer_number': []})
    df = orders.groupby('customer_number').size().reset_index(name = 'count')
    df.sort_values(by = 'count', ascending = False, inplace = True)
    return df[['customer_number']][0:1]

#https://leetcode.com/problems/customer-placing-the-largest-number-of-orders/

import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    if orders.empty:
        return pd.DataFrame({'customer_number': []})
    df = orders.groupby('customer_number').size().reset_index(name = 'count')
    ret_df = df[df['count'] == df['count'].max()][['customer_number']]
    return ret_df

#https://leetcode.com/problems/customer-placing-the-largest-number-of-orders/

import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    return orders['customer_number'].mode().to_frame()