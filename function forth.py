def even(number):
    if number % 2 == 0:
        return True
    else:
        return False

number = 10
if even(number):
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")
