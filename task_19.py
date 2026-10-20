import functools

def cache(func):
    saved_results = {}

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        key = (args, tuple(kwargs.items()))
        if key in saved_results:
            print(f"  (результат для {args} взят из кэша)")
            return saved_results[key]
        result = func(*args, **kwargs)
        saved_results[key] = result
        return result
    return wrapper

@cache
def slow_square(number):
    print(f"  считаю квадрат числа {number}...")
    return number * number

print("первый вызов slow_square(5):")
print(f"результат: {slow_square(5)}")
print("второй вызов slow_square(5):")
print(f"результат: {slow_square(5)}")
print("вызов slow_square(7):")
print(f"результат: {slow_square(7)}")
