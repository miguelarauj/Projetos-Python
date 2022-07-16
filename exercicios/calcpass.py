k=int(input('Quantos km? '))
if k<=200:
    pre=k*0.50
    print(f'VALOR DA PASSAGEM \nR${pre:.2f}')
else:
    pre=k*0.45
    print(f'VALOR DA PASSAGEM \nR${pre:.2f}')