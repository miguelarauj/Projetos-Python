vel = int(input('VELOCIDADE: '))
if vel > 80:
    print('MULTADO POR EXCESSO DE VELOCIDADE')
    print('valor R${}'.format((vel-80)*7))
