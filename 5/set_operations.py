a = set()
b = {1, 2, 4}  # set
c = {}  # dict
d = {1: 2, 3: 4}  # dict

a.add(4)
a.add(5)
print(a)
a.add(5)
print(a)

if 5 in a:  # O(1)
    print("5 in a!")

union = a | b
intersection = a & b
e = a ^ b  # (a | b) - (a & b)
print(union)
print(intersection)
print(e)
f = a - b
print(f)
f.remove(5)
print(f)
