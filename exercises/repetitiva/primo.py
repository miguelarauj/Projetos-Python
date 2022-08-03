num = int(input('Digite um numero: '))
cont=0
for c in range(1, num+1):
    if num % c == 0:
        print('\033[34m', end=" ")
        cont+=1    
    else:
        print('\033[m', end=" ")
    print(c, end=" ")
if cont>2:
    print('NÃO É PRIMO')
else:
    print('É PRIMO')