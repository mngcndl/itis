# Числа фибоначи
# fib(n) = fib(n-1) + fib(n-2)
# fib(1) = fib(2) = 1
# 1 1 2 3 5 8 13 21 34 55

def fib_recursive(n):
    if n == 1 or n == 2:
        return 1
    return fib_recursive(n - 1) + fib_recursive(n-2)


def fib_recursive_with_memory(n):
    memory = [None] * (n + 1)
    return __fib_recursive_with_memory_internal(n, memory)


def __fib_recursive_with_memory_internal(n, memory):
    if memory[n] is not None:
        return memory[n]

    if n == 1 or n == 2:
        result = 1
    else:
        result = __fib_recursive_with_memory_internal(n - 1, memory)\
                 + __fib_recursive_with_memory_internal(n-2, memory)
    memory[n] = result
    return result


def fib_with_memory(n):
    if n == 1 or n == 2:
        return 1
    memory = [None] * (n + 1)
    memory[1] = memory[2] = 1
    for i in range(3, n + 1):
        memory[i] = memory[i - 1] + memory[i - 2]
    return memory[n]


def fib(n):
    if n == 1 or n == 2:
        return 1
    a = 1
    b = 1
    for i in range(2, n):
        c = a + b
        a = b
        b = c
    return b


print(fib(3))
