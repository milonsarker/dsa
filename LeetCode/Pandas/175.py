#https://leetcode.com/problems/combine-two-tables/

import pandas as pd

def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
    df = person.merge(address, how = 'left', on = 'personId')
    return df[['firstName', 'lastName', 'city', 'state']]