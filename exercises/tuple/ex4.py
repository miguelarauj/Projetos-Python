tuple_num=(int(input('DIGITE O PRIMEIRO NUMERO: ')),int(input('DIGITE O SEGUNDO NUMERO: ')),int(input('DIGITE O TERCEIRO NUMERO: '))
           ,int(input('DIGITE O QUARTO NUMERO: ')))
print(f'Voce digitou',end=' ')
pos=0
print(f'\nO 9 aparece {tuple_num.count(9)} vez(es)')
if '3' in tuple_num:
    print(f'\nO 3 aparece na {tuple_num.index(3)+1}ª posição')
else:
    print(f'\nO 3 não aparece')
print('Os valores pares digitados foram:',end=' ')
for c in tuple_num:
    if c%2==0:
        print(c, end=' ')
