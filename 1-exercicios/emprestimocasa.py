casa = float(input('Valor da casa: R$'))
a = int(input('Parcelamento em quantos anos? '))
sal = float(input('Seu salário: R$'))
vpar = casa / (a * 12)
print(f'R${vpar:.2f}')
if vpar <= sal * 30 / 100:
    print('EMPRÉSTIMO ACEITO')
else:
    print('EMPRÉSTIMO CONCEDIDO')
