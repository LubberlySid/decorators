def memorize(func):
    cache = {}

    def wrapper(*args):
        if args in cache:
            return cache[args]

        result = func(*args)
        cache[args] = result

        return result

    return wrapper


@memorize
def summarize(number1, number2):
    return number1 + number2


result1 = summarize(3, 6)
print(result1)

result2 = summarize(5, 3)
print(result2)

result3 = summarize(3, 6)
print(result3)
