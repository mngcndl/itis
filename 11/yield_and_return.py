def usage_of_return(number_of_values):
    # result = [[i, i**2, i**3] for i in range(number_of_values)]
    result = []
    for i in range(number_of_values):
        result.append([i, i**2, i**3])

    return result


def usage_of_yield(number_of_values):
    for i in range(number_of_values):
        yield [i, i**2, i**3]

# print("Yield:")
# for i in usage_of_yield(5):
#     print(i)
gen = usage_of_yield(5)
print(gen.__next__())
print(gen.__next__())
print(gen.__next__())
print(gen.__next__())
print(gen.__next__())
print(gen.__next__())

# print("Return:")
# for i in usage_of_return(5):
#     print(i)
# print(usage_of_return(5))
