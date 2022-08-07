u = 0
pc = 0
while True:
    from emoji import emojize
    from random import randint
    print(emojize(':raised_fist: :hand_with_fingers_splayed:  :victory_hand:'))
    ppt = ['Pedra', (emojize(':raised_fist:'))], ['Papel', (emojize(
        ':hand_with_fingers_splayed:'))], ['Tesoura', (emojize(
            ':victory_hand:'))]
    print(emojize('''
    [0] Pedra :raised_fist:
    [1] Papel :hand_with_fingers_splayed:
    [2] Tesoura :victory_hand:
    '''))
    h = int(input('>> '))
    pc = randint(0, 2)
    print(f'>> {pc}')
    print()
    print(f'Usuário: {ppt[h][0]}{ppt[h][1]}')
    print(f'BOT: {ppt[pc][0]}{ppt[pc][1]}')
    print()
    if pc == h:
        print('''EMPATE
            ''')
    elif pc == 0:
        if h == 1:
            print('USUÁRIO GANHOU')
            u += 1
        elif h == 2:
            print('BOT GANHOU')
            pc += 1
    elif pc == 1:
        if h == 0:
            print('BOT GANHOU')
            pc += 1
        elif h == 2:
            print('USUÁRIO GANHOU')
            u += 1
    elif pc == 2:
        if h == 0:
            print('USUÁRIO GANHOU')
            u += 1
        elif h == 1:
            print('BOT GANHOU')
            pc += 1
    per = input('DESEJA CONTINUAR? ').upper()
    if per == 'N':
        break
print(f'Suas vitórias: {u}')
print(f'Vitórias PC: {pc}')
