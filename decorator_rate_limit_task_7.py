import datetime
import time


def rate_limit(max_calls, period):
    def decorator(func):
        call_times = []

        def wrapper(*args, **kwargs):
            now = datetime.datetime.now()
            call_times.append(now)

            call_times[:] = [call_time for call_time in call_times
                             if now - call_time <= datetime.timedelta(seconds=period)]

            if len(call_times) > max_calls:
                time_to_wait = (call_times[0] + datetime.timedelta(seconds=period)) - now
                print(f"Rate limit exceeded. Please wait {time_to_wait.total_seconds()} seconds.")
                return

            return func(*args, **kwargs)

        return wrapper
    return decorator


@rate_limit(max_calls=5, period=10)
def my_function():
    print("Function called")


for _ in range(7):
    my_function()


