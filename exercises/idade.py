from datetime import date

cont_maior=0
cont_menor=0
for c in range (1,8):
    ano=int(input('Digite seu ano de nascimento: '))
    idade=(date.today().year)-ano
    print(idade)
    if idade>=18:
        cont_maior+=1
    else:
        cont_menor+=1
print(f'''
Maiores de idade: {cont_maior}
Menores de idade: {cont_menor}''')
