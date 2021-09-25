arr = [1, 2, 3, 4, 9, -3]
b = 3

visited_items = set()

for item in arr:
    if b - item in visited_items:
        print(item, b-item)
        exit()
    visited_items.add(item)
print("Not found")
