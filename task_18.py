import functools
from datetime import datetime

def log_calls(filename):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            line = f"{now} | функция: {func.__name__} | args: {args} | kwargs: {kwargs}\n"
            with open(filename, "a", encoding="utf-8") as file:
                file.write(line)
            return func(*args, **kwargs)
        return wrapper
    return decorator

@log_calls("calls.log")
def add(a, b):
    return a + b

@log_calls("calls.log")
def greet(name, greeting="привет"):
    return f"{greeting}, {name}!"

print(f"add(2, 3) = {add(2, 3)}")
print(f"greet('Маша') = {greet('Маша')}")
print(f"greet('Петя', greeting='здравствуй') = {greet('Петя', greeting='здравствуй')}")

print()
print("содержимое файла calls.log:")
with open("calls.log", "r", encoding="utf-8") as file:
    print(file.read())
