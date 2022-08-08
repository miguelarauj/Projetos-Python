from os import system as sy
from time import sleep as sl
mi = im = m = 0
while True:
    print('_'*25,'\n')
    idade = int(input('INFORME A SUA IDADE: '))
    sexo = input('SEXO [M/F]: ').upper()
    while sexo not in 'MF':
        sexo = input('SEXO [M/F]: ').upper()
    if idade >= 18:
        mi += 1
    if sexo == 'M':
        m += 1
    if sexo == 'F' and idade < 20:
        im += 1
    per = input('DESEJA CONTINUAR? [S/N] ').upper()
    if per == 'N':
        sl(5)
        sy('cls')
        break
    sl(5)
    sy('cls')
print(
    f'Quantas pessoas tem mais de 18 anos: {mi}\nHomens cadastrados: {m}\nMulheres com menos de 20 anos: {im}')
