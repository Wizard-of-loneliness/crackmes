import math

secret_list = ["00", "01", "1A", "12", "13", "01", "00", "00", "14", "05", "08", "05", "00", "06", "16"]
valid_magic_list = secret_list[::-1]
bin_data = ""
for magic_hex in valid_magic_list:
    bin_data += "{0:05b}".format(int(magic_hex, 16))
key = ""
for i in range(len(bin_data)):
    if bin_data[i] == "1":
        hexstring = str(hex(0x30 + i))[2:]
        key += bytes.fromhex(hexstring).decode('utf-8')
print("Key:", key)
