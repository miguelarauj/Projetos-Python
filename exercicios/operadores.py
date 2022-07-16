"""calclo basico
"""
# soma = int(input('escreva 2 + 2'))

# sub = int(input('escreva 2 - 2:'))

# mult = int(input('escreva 2 * 2:'))

# div = int(input('escreva 5 / 2:'))

# pot = int(input('escreva 2 ** 2:'))

# divint = int(input('escreva 5 // 2:'))

# rest = int(input('escreva 3 % 9:'))

# print((5 + 3) * 2)
# print(5//2)
# print(5%2)

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
