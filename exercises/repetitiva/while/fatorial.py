fat=1
num=int(input('Digite um número: '))
print(f'Calculando {num}! ',end='')
while num>=2:
    print(num ,end=' x ')
    fat*=num
    num-=1
print(f'1 = {fat}')
