from random import randint

n = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(n)
maior = menor = 0

for c in n:
    print(c)
    if c>=maior:
        maior=c
    if c <= maior:
        menor=c
print(maior,'\n',menor)
