print('Calculo basico')
x = int(input('X= '))
o = str(input('+, -, *, /: '))
y = int(input('Y= '))
cal = int
if o == '+':
    cal = (x + y)
else:
    if o == '-':
        cal = (x - y)
    else:
        if o == '*':
            cal = (x * y)
        else:
            if o == '/':
                cal = (x / y)
print(f'{x} {o} {y} = {cal:.1f}')
print('Dobro, Triplo e Raiz Quadrada')
d = (x * 2)
t = (x * 3)
print(f'Dobro: {d} \n Triplo: {t}')
print('Média')
m = ((x + y) / 2)
print(f'Média: {m}')
