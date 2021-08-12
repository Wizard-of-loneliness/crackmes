number = ord(input("Enter a character : "))
check0x80 = 0
if number > 128:
    check0x80 = 1
check1 = check0x80 + ~((number & 0xF) ^ ((~number) & 0xF0))
if check1:
    password = (number & (number * (2 ** (number & 1))))
else:
    password = ~(number // 2 ** (number & 0xF))
print("Password could be", password)
