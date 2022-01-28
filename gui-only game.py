from platform import win32_is_iot
import PySimpleGUI as sg

 
sg.ChangeLookAndFeel('GreenTan')

columnsub1 = [
    [sg.Text('LEVEL', size=(8, 1)), sg.Text('1', justification = 'right', key='LVL_val', size=(5, 1))],
    [sg.Text('Strength', size=(8, 1)), sg.Text('1', justification = 'right', key='STR_val', size=(5, 1))],
    [sg.Text('Perception', size=(8, 1)), sg.Text('1', justification = 'right', key='PER_val', size=(5, 1))],
    [sg.Text('Charisma', size=(8, 1)), sg.Text('1', justification = 'right', key='CHA_val', size=(5, 1))],
    [sg.Text('Dexterity', size=(8, 1)), sg.Text('1', justification = 'right', key='DEX_val', size=(5, 1))],
    [sg.Text('Intelligence', size=(8, 1)), sg.Text('1', justification = 'right', key='INT_val', size=(5, 1))],
    [sg.Text('Luck', size=(8, 1)), sg.Text('1', justification = 'right', key='LUK_val', size=(5, 1))],
]

column1 = [
    [sg.Text('savename', key='savename', size=(35, 2), relief='raised', border_width= 2)],
    [sg.Canvas(background_color='black', size=(140, 185)), sg.Column(columnsub1)]
    
           ]

def win1_layout():
    layout = [
        [sg.Text('Select save file', size=(40, 2), font=("Helvetica", 15))],
        [sg.Radio('Save slot 1    ', "RADIO1", default=True), sg.Radio('Save slot 2    ', "RADIO1"), sg.Radio('Save slot 3 ', "RADIO1")],
        [sg.Button('Select'), sg.Button('Exit')]
            ]

    return layout

def win2_layout():
    layout2 = [
    [sg.InputText('Name the save file', key='saveid')],
    [sg.Button('Start game'), sg.Cancel()]
    ]

    return layout2

def win3_layout():
    layout3 = [
        
            [sg.Canvas(background_color='gray', size=(300, 500)),
             sg.vtop(sg.Column(column1))
             ]
            
            ]
    
    return layout3

win1 = sg.Window('GUI-only game', win1_layout())

win2_active = False
win3_active = False
while True:
    ev1, vals1 = win1.read(timeout=100)
    if ev1 == sg.WIN_CLOSED or ev1 == 'Exit':
        break

    if not win2_active and ev1 == 'Select':
        win2_active = True
        win2 = sg.Window('GUI-only game', win2_layout())

    if win2_active:
        ev2, vals2 = win2.read(timeout=100)
        if ev2 == sg.WIN_CLOSED or ev2 == 'Cancel':
            win2_active  = False
            win2.close()
            
        if not win3_active and ev2 == 'Start game':
            win3_active = True
            win3 = sg.Window('GUI-only game', win3_layout())
    
    if win3_active:
        ev3, vals3 = win3.read(timeout=100)
        win3['savename'].update(vals2['saveid'])
        win1.Hide()
        win2.Hide()
        if ev3 == sg.WIN_CLOSED:
            win3_active = False
            win2_active = False
            win3.close()
            win2.close()
            win1.close()
            break
