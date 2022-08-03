id_media = 0
cont_h = 0
cont_m = 0
for c in range(1, 5):
    print(f'PESSOA {c}:')
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    sexo = input('Sexo: ').upper()
    print()
    if sexo == 'M':
        cont_h += 1
        if cont_h == 1:
            nome_velho = nome
            idade_velho = idade
        elif idade > idade_velho:
            idade_velho = idade
            nome_velho = nome
    elif idade < 20:
        cont_m += 1
    id_media = id_media+idade
print(f'Média de idade: {id_media/4}')
print(f'Homem mais velho: {nome_velho} tem {idade_velho}')
if cont_m > 1:
    print(f'Mulheres com menos de 20: {cont_m}')
elif cont_m == 1:
    print('Uma mulher com menos de 20')
