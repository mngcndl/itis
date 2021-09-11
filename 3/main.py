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
