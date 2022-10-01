import PySimpleGUI as sg
import json

file = open("stock.json", "r")
stock = json.load(file)
file.close()

file = open("stock1.json", "r")
stock1 = json.load(file)
file.close()

layout = [
    [sg.Text("Bem vindo -usuario-!")],
    [sg.Text("Escolha um produto.")],
    [sg.Combo(values=[stock["1"][0], stock["2"][0], stock["3"][0], stock["4"][0], stock["5"][0]], key='product')],
    [sg.Button('Ver disponibilidade')],
    [sg.Text("Qual a quantidade desejada?"), sg.Input(key='amount', size=(6, 1))],
    [sg.Button('Adicionar ao carrinho')]

]

window = sg.Window("Minhas compras", layout)
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == 'Ver disponibilidade':
        product_name = values['product']
        sg.Popup(product_name, f'Quantidade no estoque: {stock1[product_name][0]}', f'Preço: R${stock1[product_name][1]}')
    if event == 'Adicionar ao carrinho':
        cart = []
        user = (values['product'], values['amount'])
        cart.append(user)
        print(cart)

