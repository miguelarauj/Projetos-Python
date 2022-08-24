num = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinzo','seis','sete','oito','nove','dez')
change_num = int(input('Escolha um número de 0 a 10: '))

while change_num>10 or change_num<0:
    change_num = int(input('Escolha um número de 0 a 10: '))

print(num[change_num])
