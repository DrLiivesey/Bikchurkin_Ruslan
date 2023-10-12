words = input("Введите список слов через пробел: ")
print("".join([words[i] for i in range(len(words)) if words[i].isalpha() and (i == len(words) - 1 or not words[i+1].isalpha())]))





