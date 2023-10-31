def get_armstrong_numbers():
    num = 1
    while True:
        digits = [int(digit) for digit in str(num)]
        power = len(digits)
        armstrong_sum = sum(digit ** power for digit in digits)
        if armstrong_sum == num:
            yield num
        num += 1


armstrong_gen = get_armstrong_numbers()
for i in range(8):
    print(next(armstrong_gen), end=' ')
