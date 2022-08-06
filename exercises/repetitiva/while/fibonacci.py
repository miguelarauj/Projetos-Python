n = int(input('Quantidade de termos: '))
t1 = 0
t2 = 1
if n == 2:
    print(t1, end=' - ')
    print(t2, end=' - FIM')
elif n == 1:
    print(t1, end=' -  FIM')
elif n == 0:
    print('FIM')
else:
    c = 3
    print(t1, end=' - ')
    print(t2, end=' - ')
    while c <= n:
        t3 = t1+t2
        print(t3, end=' - ')
        t1 = t2
        t2 = t3
        c += 1
    print('FIM')
