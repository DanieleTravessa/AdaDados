from pickle import APPEND
cardapio=[]
produto =''
item = 1

def menu_cardapio():
    print("Escolha uma opção: ")
    print('1. Exibir Cardápio.')
    print('2. Cadastrar novos itens: ')
    opcao = input(' ')
    if opcao == '1':
        imprime_cardapio()
    elif opcao == '2':
        cadastra_item()

def cadastra_item():
    while produto != 'fim':
        produto = input('Digite o nome do item: ')
    if produto!='fim':
        preco = input('Digite o valor do produto. R$')
        cardapio.append( item )
        cardapio.append( produto)
        cardapio.append( preco )
        item += 1

def imprime_cardapio():
    for i in range(0,len(cardapio),3):
        print(f'{cardapio[i]} - {cardapio[i+1]}: R${cardapio[i+2]}')

menu_cardapio()