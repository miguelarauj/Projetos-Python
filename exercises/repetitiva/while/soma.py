num = int(input('Digite um número: '))
s = num
while num != 999:
    print(num, end=' - ')
    print('CONTINUE')
    s += num
    num = int(input('Digite um número: '))
print(f'A SOMA DOS VALORES É: {(s)}')
