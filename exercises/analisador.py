id_media = 0
for c in range(1, 5):
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    sexo = input('Sexo: ').upper()
    if sexo == 'm':
        m_velho = nome
    id_media = id_media+idade
print(id_media/4)
print(f'Homem mais velho: {m_velho}')
