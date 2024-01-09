#https://leetcode.com/problems/rearrange-products-table/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata

import pandas as pd

def rearrange_products_table(products: pd.DataFrame) -> pd.DataFrame:
    return pd.melt(products, id_vars = 'product_id', var_name = 'store', value_name = 'price').dropna()