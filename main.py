import pandas as pd

data = pd.read_excel("lab_pi_101.xlsx")

last_row = data.shape[0]

skore = data['Группа'].str.contains('ПИ101').sum()

student_PI101 = len(data[data['Группа'] == 'ПИ101']['Личный номер студента'].unique())

pi101 = data.loc[data['Группа']== 'ПИ101' , 'Личный номер студента'].unique()

control = data['Уровень контроля'].unique()

years = sorted(data['Год'].unique())

print("В исходном датасете содержалось" , last_row, "оценок, из них ", skore, " относятся к группе ПИ101.", 
      '\n', "В датасете находятся оценки" , student_PI101, 'студентов со следующими личными номерами:', ', '.join(map(str, pi101)),
      '\n', "Используемые формы контроля:", ', '.join(map(str, control)), 
      '\n', 'Данные представлены по следующим учебным годам: ', ', '.join(map(str, years)))