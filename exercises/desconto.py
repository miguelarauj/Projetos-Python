val = float(input('Informe o valor do produto: R$'))
print()
op = int(input('''[ 1 ] À vista dinheiro/cheque: 10% de desconto
[ 2 ] À vista no cartão: 5% de desconto
[ 3 ] Em até 2x no cartão: preço formal
[ 4 ] 3x ou mais no cartão: 20% de juros

-> '''))
print()
if op == 1:
    vf = val-val * 10 / 100
    print(f'À vista dinheiro/cheque: R${vf:.2f}')
elif op == 2:
    vf = val-val * 5 / 100
    print(f'À vista no cartão: R${vf:.2f}')
elif op == 3:
    vf = val
    op2 = int(input('Quantidade de parcelas: '))
    if op2 > 2 and op2 <= 0:
        print('OPÇÃO INVÁLIDA')
    else:
        print(f'{op2}X no cartão: R${vf/op2:.2f}')
elif op == 4:
    vf = val+val * 20 / 100
    op2 = int(input('Quantidade de parcelas: '))
    if op2 < 3:
        print('OPÇÃO INVÁLIDA')
    else:
        print(f'{op2}X no cartão: R${vf/op2:.2f}')
else:
    print('OPÇÃO INVÁLIDA')
