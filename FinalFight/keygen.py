import random

def CheckValueAtOffset(holder, value):
    edx = ((holder * 0x80808081) // 2**39)
    eax = 255 * edx
    return ((holder - eax) == value)

def CheckValueAtOffest14(key):
    sum = 0
    iplus1 = 0
    i = 0
    while ((len(key) -1) > iplus1):
        i = iplus1
        iplus1 = i + 1
        letter = ord(key[i])
        consecutive_letter = ord(key[i+1])
        sum += (letter * consecutive_letter) // iplus1
    return (CheckValueAtOffset(sum, 0xBF))

def CheckValueAtOffset37(key):
    product = 1
    for i in range(0, len(key)):
        try:
            eax = ord(key[len(key) - i])
        except IndexError:
            eax = 0
        edx = ord(key[len(key) - i -1])
        if  eax == edx:
            product = product + 1
        else:
            product = product * abs(eax - edx)
    return (CheckValueAtOffset(product, 0xA3))

def CheckValueAtOffset38(key):
    sum = 0
    i = 0
    while i < (len(key) - 2):
        rfl = ord(key[i])
        rsl = ord(key[i + 1])
        rtl = ord(key[i + 2])
        sum = sum + ((rfl * rsl) % rtl)
        i = i + 3
    return CheckValueAtOffset(sum, 0x43)

def CheckValueAtOffset39(key):
    sum = 0
    i = 0
    while i < (len(key) - 2):
        ebx = ord(key[i + 1])
        ebx = ebx - (10 * (((ebx * 0x67) // 2**10) - (ebx // 2**7)))
        eax = ord(key[i])
        ecx = ((eax * 0x67) // 2**10)
        eax = eax // 2**7
        ecx = ecx - eax
        if ebx > 0:
            edx = 0
            eax = 1
            while edx < ebx:
                eax = eax * ecx
                edx = edx + 1
        else:
            eax = 1
        eax = eax // ord(key[i + 2])
        sum = sum + eax
        i = i + 3
    return CheckValueAtOffset(sum, 0xAB)

def CheckValueAtOffset3A(key):
    i = 0
    sum = 1
    while i < (len(key) - 1):
        ecx = ord(key[i]) ** 2
        try:
            edx = ord(key[i + 1]) ** 2
        except IndexError:
            edx = 0
        if ecx > edx:
            sum = sum + (ecx % edx)
        if ecx < edx:
            sum = sum + (edx % ecx)
        i = i + 2
    return CheckValueAtOffset(sum, 0x99)

chars_used = "abcdefghijklmnopqrstuvwxyz"
chars_list = list(chars_used)
counter = 0
key_count = 1      #set number of keys you want
key_length = 8     #set key length, it should be greater than 2. It is easier to bruteforce values with lower key length.
print(f"Brute-forcing {key_count} valid key(s):")
while (counter < key_count):
    guess_key = "".join(random.choices(chars_list, k=key_length))
    if CheckValueAtOffest14(guess_key) and CheckValueAtOffset37(guess_key) and CheckValueAtOffset38(guess_key) and CheckValueAtOffset39(guess_key) and CheckValueAtOffset3A(guess_key):
    # if CheckValueAtOffset37(guess_key):
        counter = counter + 1
        print(guess_key)
