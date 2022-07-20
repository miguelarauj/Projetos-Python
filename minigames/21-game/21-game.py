from random import randint
from sre_constants import BRANCH
t = 0
c = 0
while True:
    pc = randint(1, 10)
    t = t+pc
    c = c+1
    print(f'''
CARTA: {pc}
''')
    if c > 1:
        print(f'''TOTAL: {t}
''')
    if t > 21:
        print('''PERDEU
''')
        break
    elif t == 21:
        print('''GANHOU
''')
        break
    resp = input('Deseja continuar? [ENTER/N]')
    if resp == 'n' or resp == 'N':
        break
