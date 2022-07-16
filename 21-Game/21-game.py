"""_21_
    """
import random
t = 0
r = input('continuar? ')
while r == 's':
    if t > 21:
        print('PERDEU')
    if t == 21:
        print('GANHOU')
    num = random.randint(1, 10)
    t = t+num
    print(f'carta: {num}')
    print(f'total: {t}')
    print('')
    r = input('continuar? ')
