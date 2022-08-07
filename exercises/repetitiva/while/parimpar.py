from os import system
from time import sleep
import random
import sys
u = 0
while True:
    s = 0
    n_pc = random.randint(0, 5)
    ip_pc = random.randint(1, 2)
    if ip_pc == 2:
        ip_pc = str('PAR')
        ip_u = str('IMPAR')
    elif ip_pc == 1:
        ip_pc = str('IMPAR')
        ip_u = str('PAR')
    print()
    print(f'PC: {ip_pc}')
    print()
    print(f'USUÁRIO: {ip_u}')
    print()
    n_u = int(input('USUÁRIO: Número [0-5]: '))
    print()
    print(f'PC: Número [0-5]: {n_pc}')
    print()
    s = n_pc+n_u
    if s % 2 == 0:
        r = 'PAR'
    else:
        r = 'IMPAR'
    if r == ip_u:
        g = 'USUÁRIO'
        u += 1
    elif r == ip_pc:
        g = 'PC'
    print(f'RESULTADO: {r}\n{g} GANHOU!')
    if g == 'PC':
        print('FIM DE JOGO')
        print(f'USUÁRIO GANHOU {u} VEZES!')
        for c in range(1, 11):
            sys.stdout.write("\r{}".format(c))
            sleep(1)
        system('cls')
        break
    print()
    print('FIM DA RODADA')
    for c in range(1, 16):
        sys.stdout.write("\r{}".format(c))
        sleep(1)
    system('cls')
