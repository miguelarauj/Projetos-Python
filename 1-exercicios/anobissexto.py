from datetime import date
a = int(input('Informe o ano: (tecle "0" para analisar o ano atual)'))
if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
    if a == 0:
        a = date.today().year
        print(a)
    print('É bissexto')
else:
    print('não é bissexto')
