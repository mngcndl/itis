first, second = 'тыгы', 'т'
counts_first = {}

for letter in first:
    if letter in counts_first:
        counts_first[letter] += 1
    else:
        counts_first[letter] = 1
for letter in second:
    if letter not in counts_first:
        print(False)
        exit()
    counts_first[letter] -= 1
    if counts_first[letter] == 0:
        del counts_first[letter]
print(len(counts_first) == 0)

# O(n) + O(m)
# memory usage: O(n)

a = list(map(str,input()))
b = list(map(str,input()))
print(a.sort() == b.sort())

# O(n*log(n)) + O(m*log(m)) + O(min(n + m))
# O(n*log(n)) + O(m*log(m))
