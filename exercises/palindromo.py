frase = input('DIGITE UMA FRASE:').upper().strip(".,;").split()
junto=''.join(frase)
inverso=''
for c in range (len(junto)-1,-1,-1):
    inverso+=junto[c]
print(inverso, junto)
if inverso==junto:
    print('É IGUAL')
else:
    print('É DIFERENTE')