from contextlib import contextmanager


class DividerContext:
    def __enter__(self):
        print(100*"*")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(100*"*", "\n")


with DividerContext():
    print("It's our text")


@contextmanager
def my_context():
    print(100 * "#")
    yield

    print(100 * "#")


with my_context():
    print("Today is sunny")
