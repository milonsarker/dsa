import pandas as pd

data = [[1, 'Electrical Engineering'], [7, 'Computer Engineering'], [13, 'Bussiness Administration']]
departments = pd.DataFrame(data, columns=['id', 'name']).astype({'id':'Int64', 'name':'object'})
data = [[23, 'Alice', 1], [1, 'Bob', 7], [5, 'Jennifer', 13], [2, 'John', 14], [4, 'Jasmine', 77], [3, 'Steve', 74], [6, 'Luis', 1], [8, 'Jonathan', 7], [7, 'Daiana', 33], [11, 'Madelynn', 1]]
students = pd.DataFrame(data, columns=['id', 'name', 'department_id']).astype({'id':'Int64', 'name':'object', 'department_id':'Int64'})

students_with_no_department = students.merge(departments, how='left', left_on='department_id', right_on='id', suffixes=('_student', '_department'))
print(students_with_no_department[students_with_no_department['id_department'].isnull()])