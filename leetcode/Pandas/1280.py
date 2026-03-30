#https://leetcode.com/problems/students-and-examinations/

import pandas as pd

def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:
    m_ss = students.merge(subjects, how = 'cross')
    df = examinations.groupby(['student_id','subject_name']).size().reset_index(name='attended_exams')
    m_fin = m_ss.merge(df, left_on = ['student_id', 'subject_name'], right_on = ['student_id', 'subject_name'], how = 'left')
    m_fin['attended_exams'] = m_fin['attended_exams'].fillna(0).astype(int)
    return m_fin.sort_values(by = ['student_id','subject_name'])[['student_id', 'student_name', 'subject_name', 'attended_exams']]   