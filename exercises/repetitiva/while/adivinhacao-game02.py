import random
num_random = random.randint(1, 5)
adiv = int(input('''De 1 a 5, tente adivinhar qual número estou pensando. 
'''))
print()
tent = 1
while adiv != num_random:
    tent += 1
    if adiv > num_random:
        adiv = int(input('''Menos do que isso. Tente novamente. 
'''))
        print()
    elif adiv < num_random:
        adiv = int(input('''Mais do que isso. Tente novamente. 
'''))
        print()
print(f'PARABÉNS, VOCÊ ACERTOU DEPOIS DE {tent} TENTATIVAS!')
