import PySimpleGUI as sg 

sg.theme('DarkTeal6') #Tema da calculadora 

layout = [[sg.Input('0',size = (15,3), font= ('consolas', 20), key = '-CHAVE-', readonly=True)],#Linha de texto, com a KEY = CHAVE, também adicionado o 'readonly=True', para não permitir que o usuario digite pelo teclado.       
    [sg.Button('C',size = (12,2), button_color = ('black', 'lightpink')),
    sg.Button('⌫',size = (5,2), button_color = ('black', 'lightgray')),
    sg.Button('*',size = (5,2), button_color = ('black', 'lightgray'))],

    [sg.Button('7',size = (5,2)),
    sg.Button('8',size = (5,2)),
    sg.Button('9',size = (5,2)),
    sg.Button('-',size = (5,2), button_color = ('black', 'lightgray'))],
    
    [sg.Button('4',size = (5,2)),
    sg.Button('5',size = (5,2)),
    sg.Button('6',size = (5,2)),
    sg.Button('+',size = (5,2), button_color = ('black', 'lightgray'))],

    [sg.Button('1',size = (5,2)),
    sg.Button('2',size = (5,2)),
    sg.Button('3',size = (5,2)),
    sg.Button('/',size = (5,2), button_color = ('black', 'lightgray'))],

    [sg.Button('.',size = (5,2)),
    sg.Button('0',size = (5,2)),
    sg.Button('=',size = (12,2), button_color = ('black', 'orange'))]]

janela = sg.Window('PyCalculator', layout, size=(250,290), return_keyboard_events=False)#janela criada, também usando um comando bem legal para não aparecer nada no terminal e deixar o ambiente mais limpo, por assim dizer

valor_atual = '' #variavel vazia, armazendando o valor na calculadora
igual_pressionado = False #variavel criada, para reconhecer o click do '=', e quando for apertado outro evento, o texto na tela seja apagado e so apareça o novo texto, no caso o valor aqui é falso

while True:
    event, values = janela.read(timeout=1)
    if event == sg.WIN_CLOSED:
        break   # fechando da calculadora

    if event == 'C':
        valor_atual = '0'
        janela['-CHAVE-'].update(valor_atual)
        igual_pressionado = False


    elif event == '⌫':
        if valor_atual == 'ERROR': #caso retornar erro, ele apaga completamente a str
            valor_atual = '0'
        else:
            valor_atual = valor_atual[:-1]
        janela['-CHAVE-'].update(valor_atual)


    elif event == '=':#try e except, colocados para não deixar dar erros
        try:
            result = eval(valor_atual)#verifica a str e faz como se fosse um comando de matematica
            valor_atual = str(result)#retorna como uma str de novo
            janela['-CHAVE-'].update(valor_atual) 
            igual_pressionado = True #o evento '=' foi apertado, retornando um valor verdadeiro 
        except:
            valor_atual = 'ERROR'#caso dê erro, retorna essa msg
            janela['-CHAVE-'].update(valor_atual)
            igual_pressionado = False


    elif event in ['+', '-', '/', '*']:#parte dos operadores
        valor_atual += event
        janela['-CHAVE-'].update(valor_atual)
        igual_pressionado = False  


    elif event in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']:#parte dos valores
        if igual_pressionado:#depois do '=', o valor 'zera' e começa uma nova expressão,caso eu coloque um novo numero
            valor_atual = ''
            igual_pressionado = False
        # Verifica se o valor atual é 0 e se o evento não é o ponto decimal
        if valor_atual == '0' and event != '.':
            valor_atual = event
        else:
            valor_atual += event
        janela['-CHAVE-'].update(valor_atual)

janela.close()