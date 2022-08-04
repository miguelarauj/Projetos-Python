import random
num_random = random.randint(1, 5)
print()
adiv = int(input('''De 1 a 4, tente adivinhar qual número estou pensando. 
'''))
print()
while adiv != num_random:
    if adiv>num_random:
        adiv = int(input('''Menos do que isso. Tente novamente. 
'''))
        print()
    elif adiv<num_random:
        adiv = int(input('''Mais do que isso. Tente novamente. 
'''))
        print()
print('PARABÉNS, VOCÊ ACERTOU!')
