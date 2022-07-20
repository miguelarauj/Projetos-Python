from random import randint
p = int(input('Quantas pessoas vão jogar? '))
lista_nomes = []
for c in range(0, p):
    c = c+1
    j = input(f'Jogador {c}: ')
    lista_nomes.append(j)
print(f'''JOGADORES:
{lista_nomes}''')
cont = 0
while True:
    lista_pontos = []
    cont = cont+1
    if cont > p:
        break
    t = 0
    c = 0
    while True:
        pc = randint(1, 10)
        t = t+pc
        for c in range(0, p):
            lista_pontos.append(t)
        print(f'''
CARTA: {pc}''')
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
for c in range(0,p):
    print(f'Jogdor: {lista_nomes[c]}')
    print(lista_pontos)
