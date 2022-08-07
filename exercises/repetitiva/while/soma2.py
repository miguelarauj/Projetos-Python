s = c = 0
while True:
    num = int(input('Digite um múmero: '))
    if num == 999:
        break
    c+=1
    s+=num
print(f'Quantidade: {c}')
print(f'Soma: {s}')
