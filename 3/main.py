a = 12
b = 34

# Поменять значения переменных друг с другом
a, b = b, a

# Создание списков
d = []
e = [1, 2, 3, 4, 5]
for i in range(5):
    d.append(i + 1)
# for i in range(1, 6):
#     d.append(i)
f = [i for i in range(1, 6)]
d = [i for i in range(1000) if i % 2 != 0]
g = [i for i in d if i % 3 == 0]
e = [i for i in range(1000) if i % 2 != 0 and i % 3 == 0]

print(g)

r = [[x, x] for x in range(3)]
print(r)

r = [[x, y] for x in range(3) for y in range(3)]
print(r)

r = [[x, y] for x in range(3) for y in range(3) if x + y != 1]
print(r)

d = {x: y for x in range(3) for y in range(3)}
print(d)

t = g
t[0] = 150
print(t[0], g[0])

t = g[:]
t[0] = 160
print(t[0], g[0])
t.sort(reverse=True)
print(t)
r.sort(key=lambda x: x[1])
# def my_func(x):
#     return x[1]
print(r)

# Задание №1:
# Дан отсортированный список (list), удалить дубликаты
# [1, 1, 1, 2, 3, 3, 4, 4, 4, 5] => [1, 2, 3, 4, 5]
# [13, 13, 43, 55, 55] => [13, 43, 55]

# Удаление по индексу
a = [1, 1, 1, 2, 3, 3, 4, 4, 4, 5]
i = 0
while i < len(a) - 1:
    if a[i] == a[i+1]:
        del a[i]
    else:
        i += 1

print(a)

# while i < len(a) - 1:
#     if a[i] == a[i+1]:
#         del a[i]
#         continue
#     i += 1

# Задание №2
# Дан список чисел от 1 до n, кроме одного числа в массиве длиной n-1.
# Найти недостающее.
# [3, 4, 2, 1, 7, 8, 5] => 6
a = [3, 4, 2, 1, 7, 6, 5]
print((len(a) + 2) * (len(a) + 1) // 2 - sum(a))

# Задание №3
# Дан массив (list) любых чисел.
# Передвинуть все нули в конец массива, сохранив порядок
# [1, 2, 2, 1, 0, 0, 1, 43, 0, 2, 1, 0, 0, 1]
# => [1, 2, 2, 1, 1, 43, 2, 1, 1, 0, 0, 0, 0, 0]

a = [1, 2, 2, 1, 0, 0, 1, 43, 0, 2, 1, 0, 0, 1]
#   [1, 2, 2, 1, 1, 43, 2, 1, 0, 2, 1, 0, 0, 1]
# k  0  0  0  0  1  2  2   2   3  3  3
k = 0
for i in range(len(a)):
    if a[i] == 0:
        k += 1
    else:
        a[i - k] = a[i]

for i in range(k):
    a[len(a) - 1 - i] = 0

print(a)
