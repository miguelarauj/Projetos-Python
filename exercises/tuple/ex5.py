tabel=(input('DIGITE UM PRODUTO: '),int(input('DIGITE O VALOR: R$')),input('DIGITE UM PRODUTO: '),int(input('DIGITE O VALOR: R$')),
       input('DIGITE UM PRODUTO: '),int(input('DIGITE O VALOR: R$')),input('DIGITE UM PRODUTO: '),int(input('DIGITE O VALOR: R$')))
print()
for c in range(0,(len(tabel))):
    if c%2==0:
        print(f'{tabel[c]:.<30}',end='')
    if c %2!=0:
        print('R$',(tabel[c]))
