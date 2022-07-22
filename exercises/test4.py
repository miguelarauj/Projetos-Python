import openpyxl
import pandas as pd

lista_pesquisa = []
planilha = openpyxl.load_workbook(
            r"D:\ADS\Projetos\Repositório\ProjetosPython\projetos-python\miniprojects\project.analise-excel\arq.xlsx")
aba_planilha = planilha.active
aba_planilha['A3' [0]].value
print(aba_planilha)
