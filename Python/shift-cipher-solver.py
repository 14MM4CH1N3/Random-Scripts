#yeahhhhhhhhhh
ciphertext = list("<insert ciphertext>")
z = list()
for i in ciphertext:
    a = ord(i)+1 #manually increment every time the file is ran
    if a > 122:
        x = 96 + (a - 122)
        z += chr(x)
    else:
        z += chr(a)
print(' '.join(z))
h = list()
for i in z:
    a = ord(i)+5
    if a > 122:
        x = 96 + (a - 122)
        h += chr(x)
    else:
        h += chr(a)
print(' '.join(h))
print(' '.join(ciphertext))