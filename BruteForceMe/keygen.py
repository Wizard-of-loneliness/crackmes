import subprocess
import random
 
 
def CheckforWin(key):
    binary_path = "C:/path/to/BruteForceMe.exe"
    proc_run = subprocess.run(binary_path, capture_output=True, text=True, input=key)
    return ("win" in proc_run.stdout)
 
 
chars_used = "abcdefghijklmnopqrstuvwxyz"
chars_list = list(chars_used)
while True:
    guess_key = "".join(random.choices(chars_list, k=4))
    if CheckforWin(guess_key):
        print("valid key is :", guess_key)
        break
