a = input()

i = 0
j = len(a) - 1

while i < j:
    if not a[i].isalnum():
        i += 1
        continue
    if not a[j].isalnum():
        j -= 1
        continue
    if a[i] != a[j]:
        print(False)
        exit()
    i += 1
    j -= 1
print(True)

#  as aasa
# i,j = 4, 3

