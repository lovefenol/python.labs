def split_text(text):
    words = []
    current_word = ""
    for symbol in text.lower():
        if symbol.isalpha() or symbol.isdigit():
            current_word += symbol
        else:
            if current_word != "":
                words.append(current_word)
                current_word = ""
    if current_word != "":
        words.append(current_word)
    return words


def analyze(words):
    if len(words) == 0:
        print("слов нет")
        return

    print(f"слова: {words}")
    print(f"общее количество слов: {len(words)}")

    frequency = {}
    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    print(f"частота слов: {frequency}")

    most_word = words[0]
    most_count = frequency[most_word]
    for word in frequency:
        if frequency[word] > most_count:
            most_word = word
            most_count = frequency[word]
    print(f"самое частое слово: '{most_word}' (встречается {most_count} раз)")

    shortest = words[0]
    longest = words[0]
    for word in words:
        if len(word) < len(shortest):
            shortest = word
        if len(word) > len(longest):
            longest = word
    print(f"самое короткое слово: '{shortest}'")
    print(f"самое длинное слово: '{longest}'")


text = input("введите текст: ")
words = split_text(text)

print()
print("анализ всех слов")
analyze(words)

long_words = []
for word in words:
    if len(word) >= 3:
        long_words.append(word)

print()
print("анализ слов длиной от 3 символов")
analyze(long_words)
