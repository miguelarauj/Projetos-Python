pri_term = int(input('Primeiro termo: '))
raz = int(input('Razão: '))
c = 1
con = 10
total=0
while con != 0:
    total+=con
    while c < total:
        print(pri_term, end=' -> ')
        pri_term += raz
        c += 1
    print('PAUSA')
    con = int(input('Quantas razões voce quer mostrar a mais? '))
print('FIM')
