words = input("Введите список слов через пробел: ")
new_word = ""
for i in range(len(words)):
    if words[i].isalpha():
        if i == len(words) - 1 or not words[i+1].isalpha():
            new_word += words[i]
print(new_word)