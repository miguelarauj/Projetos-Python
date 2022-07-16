import re
from PySimpleGUI import PySimpleGUI as sg

sg.theme('Reddit')
layout = [
    [sg.Text('Largura'), sg.Input(key='largura')],
    [sg.Text('Altura'), sg.Input(key='altura')],
    [sg.Button('Calcular')],
]

janela = sg.Window('tela de calculo', layout)

while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Calcular':
        if valores['largura'] == int and valores['altura'] == int:
            print('48')
