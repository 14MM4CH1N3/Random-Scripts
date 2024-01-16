def sqandmult(number, exponent, modnumber):
    original_number = number
    binary_exponent = bin(exponent)
    for i in range(3, len(binary_exponent)):
        if binary_exponent[i:i + 1] == "1":
            number = ((number * number) * original_number) % modnumber
        else:
            number = (number * number) % modnumber
    return number

print(sqandmult(1234567, 23456789, 3333337))