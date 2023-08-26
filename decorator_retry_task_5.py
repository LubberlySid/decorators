def retry(num=3):

    def decorator(func):

        def wrapper(*args, **kwargs):
            print("Start")
            print(100 * "#")

            for i in range(num):
                try:
                    func(*args, **kwargs)
                    break
                except TypeError:
                    print("Sorry, error")

            print(100 * "#")
            print("End")

        return wrapper

    return decorator


@retry(3)
def some_func():
    print(3 + "x")


some_func()
