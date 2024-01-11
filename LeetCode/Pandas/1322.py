#https://leetcode.com/problems/ads-performance/

import pandas as pd

def ads_performance(ads: pd.DataFrame) -> pd.DataFrame:
    df = ads.groupby('ad_id')['action'].apply(lambda x: round((sum(x == 'Clicked')/(sum(x=='Clicked') + sum( x == 'Viewed')) * 100) if (sum(x=='Clicked') + sum( x == 'Viewed')) > 0 else 0.00 ,2)).reset_index().rename(columns = {'action':'ctr'}) 
    return df.sort_values(by = ['ctr','ad_id'], ascending = [False, True])