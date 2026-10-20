import functools
import time

def timing(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        elapsed_ms = (end - start) * 1000
        print(f"функция {func.__name__} выполнилась за {elapsed_ms:.3f} мс")
        return result
    return wrapper

@timing
def sum_numbers(n):
    total = 0
    for i in range(n):
        total += i
    return total

@timing
def wait_a_bit():
    time.sleep(0.2)

print(f"сумма: {sum_numbers(1000000)}")
wait_a_bit()
