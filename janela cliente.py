import PySimpleGUI as sg
import json

file = open("stock.json", "r")
stock = json.load(file)
file.close()

file = open("stock1.json", "r")
stock1 = json.load(file)
file.close()

item1 = [stock["1"][0], stock["1"][1]]
print(item1)

layout = [
    [sg.Text("Bem vindo -usuario-!")],
    [sg.Combo(values=[item1, stock["2"][0], stock["3"][0], stock["4"][0], stock["5"][0]], key='product')],
    [sg.Button('OK')]

]

window = sg.Window("Minhas compras", layout)
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == 'OK':
        print(values)
        sg.Popup(values['product'],)