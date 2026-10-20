text = input("введите строку: ")

clean_text = ""
for letter in text.lower():
    if letter != " ":
        clean_text += letter

is_palindrome = True
left = 0
right = len(clean_text) - 1
while left < right:
    if clean_text[left] != clean_text[right]:
        is_palindrome = False
        break
    left += 1
    right -= 1

if is_palindrome:
    print(f"строка '{text}' является палиндромом")
else:
    print(f"строка '{text}' не является палиндромом")
