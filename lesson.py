def check_even(number:int) -> bool:
    if number % 2 == 0:
        return True
    else:
        return False
number = int(input('Enter number: '))
print(check_even(number))