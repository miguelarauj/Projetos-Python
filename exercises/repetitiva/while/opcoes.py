op = int
num1 = int(input('Digite um número: '))
num2 = int(input('Digite um número: '))
while op != 5:
    print(f'O que você deseja fazer com {num1} e {num2}?')
    op = int(input('''[1] SOMAR
[2] MULTIPLICAR
[3] MAIOR
[4] NOVOS NÚMEROS
[5] SAIR DO PROGRAMA
OPÇÃO: '''))
    if op == 1:
        print(num1+num2)
    elif op == 2:
        print(num1*num2)
    elif op == 3:
        if num1 > num2:
            print(num1)
        else:
            print(num2)
    elif op == 4:
        num1 = int(input('Digite um número: '))
        num2 = int(input('Digite um número: '))
    elif op == 5:
        print('(FINALIZANDO)')
    else:
        print('NÚMERO INVÁLIDO')
print('SAINDO...')
