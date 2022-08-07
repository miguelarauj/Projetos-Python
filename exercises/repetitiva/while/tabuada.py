while True:
    tab = int(input('Digite o valor que deseja conferir: '))
    if tab < 0:
        break
    for c in range(1, 11):
        print(f'{tab}  x {c:2}= {tab*c:2}')
