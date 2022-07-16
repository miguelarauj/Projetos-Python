from random import randint
ran = randint(0, 5)
print('Bem vindo ao jogo de adivinhação')
print()
pen = int(input('De 0 a 5, que numero estou pensando? '))
print()
print(f'Estava pensando em {ran}')
while pen != ran:
    print('Sinto informar mas você é um trouxa!')
    ran = randint(0, 5)
    print()
    pen = int(input('De 0 a 5, que numero estou pensando? '))
    print()
    print(f'Estava pensando em {ran}')
if pen == ran:
    print()
    print('Hmm, um bruxo por aqui!')
