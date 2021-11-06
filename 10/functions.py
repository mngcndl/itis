# def some_function():
#     print(1)
#     return "Something"
#
# another_function = some_function
# del some_function
# # some_function()  # NameError: name 'some_function' is not defined
# print(another_function)
# another_function()
#
#
# def one_more_function(arg_func):
#     print("Inside one more")
#     return arg_func()
#
# print(one_more_function)
# print(one_more_function(another_function))
#

def printing(func):
    print(321)

    def wrap():
        print("Start")
        res = func()
        print("End")
        return res
    return wrap


@printing
def example():
    print("Middle")
    return 123


print(example())
