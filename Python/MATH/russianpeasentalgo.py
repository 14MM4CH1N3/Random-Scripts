#i dont think this is right but lol
def multiply_polynomials(x, y):
    rc08 = int('0b00011011', 2)
    rc09 = int('0b00110110', 2)
    rc10 = int('0b01101100', 2)
    rc11 = int('0b11011000', 2)
    rc12 = int('0b10110000', 2)
    rc13 = int('0b01100000', 2)
    rc14 = int('0b11000000', 2)
    leftlist = []
    if y % 2 != 0:
        leftlist.append(x)
    while y >= 1:
        x = x * 2
        y = y // 2
        if y % 2 == 0:
            continue
        else:
            if x > int(0xFF):
                tempx = int("0b" + bin(x)[-8:], 2)
                bruh = [*bin(x)[2:-8:][::-1]]
                counter = 8
                for i in bruh:
                    if i == '1' and counter == 8:
                        tempx = tempx ^ rc08
                    if i == '1' and counter == 9:
                        tempx = tempx ^ rc09
                    if i == '1' and counter == 10:
                        tempx = tempx ^ rc10
                    if i == '1' and counter == 11:
                        tempx = tempx ^ rc11
                    if i == '1' and counter == 12:
                        tempx = tempx ^ rc12 ^ rc08
                    if i == '1' and counter == 13:
                        tempx = tempx ^ rc13 ^ rc09 ^ rc08
                    if i == '1' and counter == 14:
                        tempx = tempx ^ rc14 ^ rc10 ^ rc09
                    counter += 1
                leftlist.append(tempx)
            else:
                leftlist.append(x)
    xored = 0
    for i in leftlist:
        xored = xored ^ i
    return int(hex(xored), 16)

poly1 = '0x71'
poly2 = '0x0B'
a = multiply_polynomials(int(poly1, 16), int(poly2, 16))
poly1 = '0x37'
poly2 = '0x0D'
b = multiply_polynomials(int(poly1, 16), int(poly2, 16))
poly1 = '0x94'
poly2 = '0x09'
c = multiply_polynomials(int(poly1, 16), int(poly2, 16))
poly1 = '0xED'
poly2 = '0x0E'
d = multiply_polynomials(int(poly1, 16), int(poly2, 16))
print(hex(a ^ b ^ c ^ d))