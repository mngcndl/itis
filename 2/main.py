# https://www.hackerrank.com/challenges/nested-list/problem
# Вводные данные
records = [
    ['Bob', 10],
    ['Ivan', 20],
    ['Peter', 15],
    ['Anna', 25],
    ['Dave', 10],
    ['Kate', 15]
]
# expected = ['Kate', 'Peter']

# Преобразовываем вводные данные в dict,
# где ключ это балл, а значение это список имен
grades = {}
# item это запись из records, например ['Bob', 10]
for item in records:
    # item[1] это балл, например 10
    # проверяем был ли этот балл в словаре
    if item[1] in grades.keys():
        # Добавляем в список имен по соответствующему баллу
        grades[item[1]].append(item[0])
    else:
        # Создаем началный список с одним именем по новому баллу
        grades[item[1]] = [item[0]]
    # print(grades)
print(grades)

# Сортируем ключи (баллы) по возрастанию, переведя в список
grades_keys = sorted(list(grades.keys()))
print(grades_keys)
# Corner case
if len(grades_keys) < 2:
    print("Not possible")
    exit()

# Достаем нужный нам список Имен
result = grades[grades_keys[1]]
print(result)

# Сортируем по алфавиту
result.sort()
print(result)
