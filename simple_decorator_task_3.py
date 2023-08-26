def log_func(function):
    def wrapper():
        print("Text before function call")
        function()
        print("Text after function call")

    return wrapper


@log_func
def greeting():
    print("Hi, Ostap")


greeting()
