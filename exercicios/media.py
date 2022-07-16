n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1+n2)/2
print(f'MÉDIA: {m:.1f}')
if m < 5:
    print('REPROVADO')
elif 7 <= m <= 10:
    print('APROVADO')
elif m > 10:
    print('MÉDIA INCORRETA, CONFIRA AS NOTAS')
else:
    print('RECUPERAÇÃO')
