def t(c):
    c = False


a = True
print(a)
t(a)
print(a)


def f(arr):
    # arr = []
    arr.append(12)


b = [1]
f(b)
print(b)


def generator(limit):
    for i in range(limit):
        yield i


def filter_elements(gen, filter_func):
    for item in gen:
        if filter_func(item):
            yield item


def even_filter(item):
    return item % 3 == 0


for item in generator(10):
    print(item)

for item in filter_elements(generator(20), even_filter):
    print(item)


a = True
print(a)
t(a)
print(a)