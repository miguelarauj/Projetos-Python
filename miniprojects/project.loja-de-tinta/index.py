"""Calculadora de tinta"""
lar = float(input('Largura: '))
alt = float(input('Altura: '))
a = alt*lar
L = a*4
gp = 150.00
gg = 620.00
print(f'Área: {a:.1f}m²')
print(f'Litros: {L:.1f}L')
print('')
if L <= 3.5:
    print(f'Um galão de 3.5L necessário para a sua pintura \nValor: R${gp}')
else:
    if L > 3.5 and L <= 7:
        print(
            f'Dois galões de 3.5L são necessários para a pintura \nValor: R${gp*2}')
    else:
        if L > 7 and L <= 10.5:
            print(
                f'Três galões de 3.5L são necessários para a pintura \nValor: R${gp*3}')
        else:
            if L > 10.5 and L <= 14:
                print(
                    f'Um galões de 3.5L são necessários para a pintura \nValor: R${gg}')
            else:
                if L > 14 and L <= 28:
                    print(
                        f'Dois galões de 14L necessários para a pintura \nValor: R${gg*2}')
                else:
                    if L > 28 and L <= 42:
                        print(
                            f'Três galões de 14L são necessários para a pintura \nValor: R${gg*3}')
                    else:
                        if L > 42 and L <= 56:
                            print(
                                f'Quatro galões de 14L são necessários para a pintura \nValor: R${gg*4}')
