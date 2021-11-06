def simple_generator():
    yield 1
    yield 2
    yield 3

print(simple_generator())
for item in simple_generator():
    print(item)

print("!!!!!!!!!!!!!!")


def power_of_generator(n, limit):
    current = 1
    while current < limit:
        yield current
        current *= n


for val in power_of_generator(2, 2000):
    print(val)