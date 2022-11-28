import PySimpleGUI as sg

layout = [
    [sg.Text('Usuario.')],
    [sg.Input(key='usuario')],
    [sg.Text('Senha')],
    [sg.Input(key='senha')],
    [sg.Button('Login')],
    [sg.Text('',key='mensagem')],
]

janela = sg.Window('login', layout= layout)

while True:
    event, values = janela.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'Login':
        usuario_correto = 'Lucas'
        senha_correta = '12345'
        usuario = values['usuario']
        senha = values['senha']
        if usuario == usuario_correto and senha == senha_correta:
            janela['mensagem'].update('Login realizado com sucesso.')
        else:
            janela['mensagem'].update('Usuario ou Senha Incorreto.')
            

        