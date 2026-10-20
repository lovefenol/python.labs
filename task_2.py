password = input("введите пароль: ")

if len(password) < 16:
    print("слишком короткий")
elif password.isalpha() or password.isdigit():
    print("слабый пароль")
else:
    print("надежный пароль")
