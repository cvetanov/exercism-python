def get_digits(number, digits):
    if number == 0:
        return digits
    digits.append(number % 10)
    return get_digits(number / 10, digits)

def is_armstrong_number(number):
    if number == 0:
        return True
    digits = get_digits(number, [])
    num_digits = len(digits)
    return number == sum([i ** num_digits for i in digits])
    
