from datetime import date
nas = int(input('Ano do seu nascimento: '))
idade = (date.today().year-nas)
if idade > 18:
    print('''ATRASO NO ALISTAMENTO
{} anos fora do prazo!'''.format(idade-18))
elif idade < 18:
    print('''AGUARDE
{} anos para o seu alistamento!'''.format(18-idade))
else:
    print('''CHEGOU A HORA DE SE ALISTAR
0 anos para o seu alistamento!''')
