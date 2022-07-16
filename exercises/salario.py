si = int(input('Qual o seu salário atual? R$'))
au: int
resp: str
resp = input(f'Confirma que o salário é de R${si:.2f}? (S/N) ')
while resp == 'N' or resp == 'n':
    si = int(input('Qual o seu salário atual? R$'))
    au: int
    resp = input(f'Confirma que o salário é de R${si:.2f}? (S/N) ')
if si > 1250:
    au = si + si * 10 / 100
    print(f'R${au:.2f}')
else:
    au = si + si * 15 / 100
    print(f'R${au:.2f}')
