import openpyxl
import pandas as pd

lista_pesquisa = []
lar = (len(lista_pesquisa)+2)
while True:
    c = 2
    i = 0
    print(c, i, lar)
    print(lista_pesquisa)
    while True:
        pesquisa = str(input('Pesquisa: '))
        lista_pesquisa.append(pesquisa)
        if pesquisa == 'F':
            lista_pesquisa.remove('F')
            break
    for resultado in range(len(lista_pesquisa)):
        print(lista_pesquisa[resultado])
        planilha = openpyxl.load_workbook(
            r"D:\ADS\Projetos\Repositório\ProjetosPython\projetos-python\miniprojects\project.analise-excel\arq.xlsx")
        aba_planilha = planilha.active
        aba_planilha['A'+str(c)].value = lista_pesquisa[i]
        i = i+1
        c = c+1
        planilha.save(
            r"D:\ADS\Projetos\Repositório\ProjetosPython\projetos-python\miniprojects\project.analise-excel\arq.xlsx")
        ler_ = pd.read_excel(
            r"D:\ADS\Projetos\Repositório\ProjetosPython\projetos-python\miniprojects\project.analise-excel\arq.xlsx")
    print(ler_)
