import PySimpleGUI as sg
import json

file = open("stock.json", "r")
stock = json.load(file)
file.close()

file = open("stock1.json", "r")
stock1 = json.load(file)
file.close()

layout = [
    [sg.Text(f'Bem vindo -usuario-!')],
    [sg.Text("Escolha um produto.")],
    [sg.Combo(values=[stock["1"][0], stock["2"][0], stock["3"][0], stock["4"][0], stock["5"][0]], key='product', size=(27, 1))],
    [sg.Button('Ver disponibilidade')],
    [sg.Text("Qual a quantidade desejada?"), sg.Input(key='amount', size=(3, 1))],
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
        list_stock = stock1[values['product']]
        amount_in_stock = list_stock[0]
        request = values['amount']
        if int(request) > int(amount_in_stock):
            sg.Popup('Nao temos essa quantidade no estoque')
        else:
            sg.Popup('Items adicionados ao carrinho!')
            eq = int(amount_in_stock) - int(request)
            previous_amount = stock1[values['product']][0]
            print(previous_amount)
            stock1[values['product']][0] = eq
            print(stock1[values['product']])

            #cart = {}
            #user_cart = (values['product'], values['amount'])
            #cart.update({1})
            #file = open('cart.json', 'w')




