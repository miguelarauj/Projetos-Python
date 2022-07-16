n = int(input('Digite um numero para ser convertido: '))
op = input('''Escolha uma opção de conversão:
( 1 ) BINÁRIO
( 2 ) OCTAL
( 3 ) HEXADECIMAL
''')
print()
if op == '1':
    print('BINÁRIO')
    print('{} fica como: {}'.format(n, bin(n)[2:]))
elif op == '2':
    print('OCTAL')
    print('{} fica como: {}'.format(n, oct(n)[2:]))
elif op == '3':
    print('HEXADECIMAL')
    print('{} fica como: {}'.format(n, hex(n)[2:]))
else:
    print('TENTE NOVAMENTE')
