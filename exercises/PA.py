termo_inicial = int(input('Termo: '))
cont_termo = int(input('Quantidade de termos: '))
razao = int(input('Razão: '))
decimo = termo_inicial+cont_termo*razao
for c in range(termo_inicial, decimo, razao):
    if c == razao*cont_termo+termo_inicial-razao:
        print(c)
    else:
        print(c, ' - ', end=' ')
