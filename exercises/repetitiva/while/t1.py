import os
from time import sleep

s = 0
m = 0
h = 0
while True:
    if s < 10:
        print(f'{m}:0{s}')
    else:
        print(f'{m}:{s}')
    s += 1
    sleep(1)
    if s >= 59:
        s = 0
        m += 1
    os.system('cls')
