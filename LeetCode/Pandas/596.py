#https://leetcode.com/problems/classes-more-than-5-students/
import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    df = courses.groupby('class').size().reset_index(name = 'count')
    return df[df['count']>=5][['class']]