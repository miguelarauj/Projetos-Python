sexo = input('Sexo [M/F]: ').upper().strip()[0]
while sexo != 'M' and sexo != 'F':
    print('INVÁLIDO, TENTE NOVAMENTE')
    sexo = input('Sexo [M/F]: ').upper().strip()[0]
print('OBRIGADO')
