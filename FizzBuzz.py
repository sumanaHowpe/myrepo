def fizz_buzz(number):
    if number % 5 == 0 and number % 3 == 0:
        return 'fizz-buzz'
    if number % 3 == 0:
        return 'fizz'
    if number % 5 == 0:
        return 'buzz'
    return number

print(fizz_buzz(34))