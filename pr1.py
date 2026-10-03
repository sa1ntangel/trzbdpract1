import numpy as np

data_grades = np.array([
    68, 72, 55, 80, 91, 64, 77, 83, 59, 70,
    88, 62, 75, 95, 60, 100, 100, 100, 100, 100,
    67, 73, 58, 81, 90, 65, 78, 84, 61, 71,
    87, 63, 76, 94, 66, 100, 100, 100, 100, 100,
    69, 74, 56, 82, 92, 64, 79, 85, 60, 72,
    0, 0, 0, 0, 0, 65, 77, 83, 58, 70
])

A = np.array([68, 72, 55, 80, 91, 64, 77, 83, 59, 70, 88, 62, 75, 95, 60])

print("задание 1")
print("Массив data_grades:")
print(data_grades)
print("")

srednee = np.mean(data_grades)
print("Среднее значение:", srednee)

mediana = np.median(data_grades)
print("Медиана:", mediana)

otklonenie = np.std(data_grades)
print("Стандартное отклонение:", otklonenie)

dispersia = np.var(data_grades)
print("Дисперсия:", dispersia)

maksimum = np.max(data_grades)
print("Максимальное значение:", maksimum)

minimum = np.min(data_grades)
print("Минимальное значение:", minimum)

razmah = maksimum - minimum
print("Размах данных:", razmah)

p25 = np.percentile(data_grades, 25)
p50 = np.percentile(data_grades, 50)
p75 = np.percentile(data_grades, 75)
p90 = np.percentile(data_grades, 90)
p99 = np.percentile(data_grades, 99)

print("25 перцентиль:", p25)
print("50 перцентиль:", p50)
print("75 перцентиль:", p75)
print("90 перцентиль:", p90)
print("99 перцентиль:", p99)

q1 = np.percentile(data_grades, 25)
q3 = np.percentile(data_grades, 75)
print("Первый квартиль (Q1):", q1)
print("Третий квартиль (Q3):", q3)

iqr = q3 - q1
print("Межквартильный размах (IQR):", iqr)

nizhnyaya = q1 - 1.5 * iqr
verhnyaya = q3 + 1.5 * iqr
print("Нижняя граница:", nizhnyaya)
print("Верхняя граница:", verhnyaya)

vybrosy = data_grades[(data_grades < nizhnyaya) | (data_grades > verhnyaya)]
print("Выбросы:", vybrosy)

print("")
print("Почему появились выбросы:")
print("Выбросы это 5 нулей. Они могли появиться потому, что эти студенты не сдали работу, отсутствовали или не выполнили задание. Это связано с пропусками и неуспеваемостью")
print("")
print("Что с ними делать:")
print("Удалять нули нельзя, тогда мы потеряем инфу о неуспевающих. Заменять на медиану тоже не стоит - это исказит реальную картину.Правильнее оставить нули как есть, чтобы видеть настоящую успеваемость")
print("")

print("задание 2")
print("Массив A:")
print(A)
print("")

matrica = A.reshape(3, 5)
print("Матрица 3x5:")
print(matrica)

razmernost = matrica.shape
print("Размерность матрицы (shape):", razmernost)

kolvo = matrica.size
print("Общее количество элементов:", kolvo)

summa_strok = np.sum(matrica, axis=1)
summa_stolbcov = np.sum(matrica, axis=0)
print("Сумма по строкам:", summa_strok)
print("Сумма по столбцам:", summa_stolbcov)

transponirovannaya = matrica.T
print("Транспонированная матрица:")
print(transponirovannaya)

srednee_m = np.mean(matrica)
otklonenie_m = np.std(matrica)
dispersia_m = np.var(matrica)
q1_m = np.percentile(matrica, 25)
q2_m = np.percentile(matrica, 50)
q3_m = np.percentile(matrica, 75)

print("Среднее значение матрицы:", srednee_m)
print("Стандартное отклонение матрицы:", otklonenie_m)
print("Дисперсия матрицы:", dispersia_m)
print("Первый квартиль (Q1):", q1_m)
print("Второй квартиль (Q2):", q2_m)
print("Третий квартиль (Q3):", q3_m)
print("")



studenty = data_grades[(data_grades >= 60) & (data_grades <= 80)]
print("Студентов с оценками от 60 до 80:", len(studenty))
print("Их оценки:", studenty)

print("")
print("Что значат нули в наборе данных:")
print("Нули означают, что студенты не сдали работу или отсутствовали. Это пропущенные данные, которые показывают неуспеваемость. Их оставляют , чтобы видеть реальную картину")