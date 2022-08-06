num = int(input('Digite um número: '))
s = num
while num != 999:
    print(num, end=' - ')
    print('CONTINUE')
    num = int(input('Digite um número: '))
    s += num
print(f'A SOMA DOS VALORES É: {(s-999)}')
