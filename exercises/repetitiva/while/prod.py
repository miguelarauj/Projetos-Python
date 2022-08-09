caro = total = maior = menor = c = 0
n_maior = n_menor = ' '
while True:
    c = +1
    nome = input('Produto: ')
    valor = int(input('Valor: R$'))
    if c == 1:
        menor = maior = valor
    else:
        if valor < menor:
            menor = valor
            n_menor = nome
        if valor > maior:
            maior = valor
            n_maior = nome
    total += valor
    if valor > 1000:
        caro += 1
    per = input('\nDESEJA CONTINUAR? ').upper()
    while per!='S' and per!='N':
        per = input('\nDESEJA CONTINUAR? ').upper()
    if per == 'N':
        break
print(
    f'\nTOTAL: {total}\n{caro} produtos custam mais de R$1000,00\nMAIS BARATO: {n_menor} R${menor}')
