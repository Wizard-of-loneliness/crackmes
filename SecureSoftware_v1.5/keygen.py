import platform

computer_name = platform.node().upper()
key = ""
for letter in computer_name:
    value = ord(letter) & 0xF
    if value > 9:
        value = value + 7
    
    hexstring = hex(value + 0x30)[2:]
    key += bytes.fromhex(hexstring).decode('utf-8')
print("key:", key)
