# Объявление переменных
a = 1
print(a, a, 2, 3)
a = 2
print(a)
b = 3
c = a + b
d = b - a
print(c, d)
c = a * b
d = b / a
# Деление нацело
e = b // a
print(c, d, e)
# Возведение в степень
c = a ** b
print(c)
# Остаток от деления
e = b % a
print(e)
# Boolean
t = True
t = False
# Операции сравнения
g = a < b
print(a, b, "a < b", g)
g = a <= b
print(a, b, "a <= b", g)
g = a > b
print(a, b, "a > b", g)
g = a >= b
print(a, b, "a >= b", g)
a = 3
g = a == b
print(a, b, "a == b", g)
g = a != b
print(a, b, "a != b", g)

# Strings
a = "First"
b = 'Second'
print(a, b)
c = a + " " + b
print(c)
# Длина строки
print(len(c))
# Доступ по индексу
print(c[2])
print(c[2:4])
print(c[:4])
print(c[4:])

print(c + " " + str(e) + " " + str(t))

# Условный оператор
# Простой
if t:
    print('if')

# С else
if t:
    print('if')
else:
    print('else')

# С elif
if t:
    print('if')
elif g:
    print('elif')
else:
    print('else')

# С несколькими elif
if t:
    print('if')
elif g:
    print('elif')
elif g or t:
    print('elif never')
else:
    print('else')

# Логические
t = True
g = False
con = t and g
dis = t or g
print(t, g, con, dis)
condis = t or g and t  # == t or (g and t)
dif = (t or g) and t  # == (t and t) or (g and t) == t or g and t == t
h = not t
h_not = not (t or g)  # == not t and not g

n = 0
while n < 10:
    print(n)
    n += 2

# List
a = []
print("len(a)", len(a))
a.append(1)
a.append(2)
a.append(22)
print("len(a)", len(a))
print(a)
i = 0
s = 0
while i < len(a):
    s += a[i]
    i += 1
print('sum(a)', s)

# Бесконечный цикл
#i = 0
while i < len(a):
    s += a[i]

print(sum(a))

for i in range(len(a)):
    print(i, a[i])

for i in range(len(a)-1, 0, -1):
    print(i, a[i])

if 22 in a:
    print("22 in a")

# Empty list
a = []
# Empty dict
b = {}
b = {1: 1, 12: 2, 200: -1}
print(b)
print(b[200])
b[250] = 100
b[1] = "Ы"
b["1"] = "e"
del b[12]
print(b)
# Empty set
c = set()
c = {1, 2, 3, 4, 5, 50, 100, 1040}
c.add(51)
c.add(1)
print(c)
