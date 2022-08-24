total = int(input('QUANTO DESEJA SACAR: R$'))
qtced=0
while True:
    if total>=50:
        ced=50
    elif total>=20:
        ced=20
    elif total>=10:
        ced=10
    elif total>=1:
        ced=1
    while total>=ced:
        total-=ced
        qtced+=1
    print('='*15)
    print(qtced,'- R$',ced,',00')
    print('='*15)
    qtced=0
    if total==0:
        break
