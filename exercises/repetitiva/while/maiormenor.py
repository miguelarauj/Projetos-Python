s = c = 0
per = 'S'
while per == 'S':
    num = int(input('Digite um número: '))
    s += num
    c += 1
    if c == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    per = input('Deseja continuar? ').upper()
print(f'A soma é: {s}')
print(f'Quantidade de numeros: {c}')
media = s/c
print(f'A média é: {media:.2f}')
print(f'O maior é: {maior}')
print(f'O menor é: {menor}')
