telephone_number = input()
result = ""
for char in telephone_number:
    if char.isdigit() or char == "+":
        result += char
print(result)