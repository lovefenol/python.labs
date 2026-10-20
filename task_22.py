import functools

def type_check(*types):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(len(types)):
                if not isinstance(args[i], types[i]):
                    raise TypeError(
                        f"аргумент №{i + 1} ({args[i]!r}) должен быть типа "
                        f"{types[i].__name__}, а передан {type(args[i]).__name__}"
                    )
            return func(*args, **kwargs)
        return wrapper
    return decorator

@type_check(int, int)
def add(a, b):
    return a + b

print(f"add(2, 3) = {add(2, 3)}")

try:
    print(add(2, "3"))
except TypeError as error:
    print(f"ошибка TypeError: {error}")

try:
    print(add(2.5, 3))
except TypeError as error:
    print(f"ошибка TypeError: {error}")
