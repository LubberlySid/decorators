from time import time


def timeit(function):
    def wrapper():
        start = time()
        function()
        end = time()
        print(f"Час виконання функції: {end - start}")
    return wrapper


@timeit
def summarize():
    num1, num2 = 4, 5
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")


summarize()
