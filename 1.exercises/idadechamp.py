from datetime import date
nas = int(input('Digite o ano do seu nascimento: '))
idade = date.today().year-nas
if 4 <= idade <= 9:
    print('MIRIM')
elif idade <= 14:
    print('INFANTIL')
elif idade <= 19:
    print('JUNIOR')
elif idade <= 25:
    print('SÊNIOR')
elif idade < 4:
    print('AINDA NÃO TEM IDADE SUFICIENTE')
else:
    print('MASTER')
