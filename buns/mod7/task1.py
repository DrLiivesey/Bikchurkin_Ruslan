def validate_args(func):
    def wrapper(*args):
        if len(args) != 1:
            return "Not enough arguments" if len(args) < 1 else "Too many arguments"
        elif not isinstance(args[0], int):
            return "Wrong types"
        elif args[0] < 0:
            return "Negative argument"
        else:
            return func(*args)
    return wrapper

@validate_args
def calculate_square(n):
    return n ** 2

print(calculate_square(5))  # Output: 25
print(calculate_square())   # Output: Not enough arguments
print(calculate_square(2, 3))  # Output: Too many arguments
print(calculate_square("hello"))  # Output: Wrong types
print(calculate_square(-4))  # Output: Negative argument
