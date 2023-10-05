letter = input()
symbol = ""
step = ""
for i in range(len(letter)):
    if letter[i] == ",":
        symbol = letter[:i]
        step = letter[i+1:]
        break
n = int(step)
if n >= 0:
    result = chr((ord(symbol) - 97 + n) % 26 + 97)
else:
    result = chr((ord(symbol) - 97 + n) % 26 + 97)
print(result)