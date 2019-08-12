"""ValueError occurs when input is anything other than a number (letters, characters, etc.)
ZeroDivisionError occurs when a 0 is entered as input for the denominator."""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator <= 0:
        denominator = int(input("Enter a denominator greater than zero: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")
