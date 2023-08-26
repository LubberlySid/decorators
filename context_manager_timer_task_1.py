from time import time
from contextlib import contextmanager


class MyContext:
    def __init__(self, result):
        self.result = result

    def __enter__(self):
        self.start = time()
        print("Hello, Ostap")

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = time()
        print("The end")
        self.result[0] = self.end - self.start


result_holder = [0]
with MyContext(result_holder):
    print("We said hello to the user")
print(f"Function time: {result_holder}")


@contextmanager
def my_context():
    print("\nEntering the context")
    yield

    print("Exiting the context")


with my_context():
    start = time()
    print(100 * "#")
    print("How are you?")
    print(100 * "#")
    end = time()
    print(f"Function time: {end - start}")
