maior = 0
menor = 0
for c in range(1, 6):
    peso = int(input('Peso (Kg): '))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso
print(maior, menor)
