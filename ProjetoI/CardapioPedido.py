from pickle import APPEND
import os
cardapio = []
produto =''
bebidas = []
pratos = []


def menu_cardapio():
  print("*"*30)
  print('* Escolha uma opção: '+' '*8 + '*')
  print('* 1. Exibir Cardápio.'+' '*8 + '*')
  print('* 2. Cadastrar novos itens:  *')
  print('* 3. Sair '+' '*19 + '*')
  print("*"*30)
  opcao = input(' ')
  if opcao == '1':
    imprime_cardapio()
  elif opcao == '2':
    cadastra_item()
  #elif opcao == '3':
  #menuprincipal
  else:
    print('\nOpção Inválida! Tente novamente!\n')
    menu_cardapio()

def cadastra_item():
  
  print("*"*30)
  print('* Escolha uma opção: '+' '*8 + '*')
  print('* 1. Cadastrar Bebidas'+' '*7 + '*')
  print('* 2. Cadastrar Pratos'+' '*8+'*')
  print('* 3. Sair '+' '*19 + '*')
  print("*"*30)
  opcao = input(' ')
  if opcao == '1':
    print("*"*30)
    print('*'*5+' Cadastro de Bebidas '+'*'*4)
    print("*"*30)
    informa_dados_item(bebidas)
    for items in range(len(cardapio)):
      bebidas.append(items)    
  elif opcao == '2':
    print("*"*30)
    print('*'*5+' Cardastro de Pratos '+'*'*5)
    print("*"*30)
    informa_dados_item(pratos)
    for items in range(len(cardapio)):
      pratos.append(items)  
  elif opcao == '3':
    menu_cardapio()
  return

def informa_dados_item(cardapio):
  produto =''
  item = 1
  outroProduto = 's'
  
  while produto != '#' and outroProduto.lower() == 's':
    print("*"*40)
    print('* Insira o dado ou digite # para sair  *')
    print("*"*40)
    produto = input('* Digite o nome do item: ')
    if produto == '#':
      os.system('cls')
      menu_cardapio()
    else:
      preco = input('Digite o valor do produto. R$')
      cardapio.append( item )
      cardapio.append( produto )
      cardapio.append( preco )
      item += 1
      print('Produto cadastrado com sucesso!')
      outroProduto = input('Deseja cadastrar outro produto? S/N ')
      if outroProduto.lower() != 's':
        menu_cardapio()          
  return cardapio

def imprime_cardapio():
 
    print("*"*50); print(' '*5 + '* Escolha a opção para exibir o cardápio: ' + '*')
    print('     *     1. Cardápio de Bebidas'+' '*14 + '*')
    print('     *     2. Cardápio de Pratos'+' '*15+'*')
    print('     *     3. Cardápio Completo '+' '*15+'*')
    print('     *     4. Voltar ao Menu Anterior '+' '*9+'*')
    print('     *     5. Sair '+' '*28 + '*'); print("*"*50)
    pagina = input(' ')
    if pagina == '1':
      print(" "*10 + "*"*30); print(" "*10 + '*'*5+' Cardápio de Bebidas '+'*'*4); print(" "*10 + "*"*30)
      for i in range(0,len(bebidas),3):
        print(' '*10 + f'{bebidas[i]} - {bebidas[i+1]}: R${bebidas[i+2]}\n')
    elif pagina == '2':
      print(" "*10 + "*"*30); print(" "*10 + '*'*5+' Cardápio de Pratos '+'*'*5); print(" "*10 + "*"*30)
      for i in range(0,len(pratos),3):
        print(' '*10 + f'{pratos[i]} - {pratos[i+1]}: R${pratos[i+2]}')
    elif pagina == '3':
      print(" "*10 + "*"*30); print(" "*10 + '*'*5+' Cardápio de Bebidas '+'*'*4); print(" "*10 + "*"*30)
      for i in range(0,len(bebidas),3):
        print(' '*10 + f'{bebidas[i]} - {bebidas[i+1]}: R${bebidas[i+2]}')
      print(" "*10 + "*"*30); print(" "*10 + '*'*5+' Cardápio de Pratos '+'*'*5); print(" "*10 + "*"*30)
      for i in range(0,len(pratos),3):
        print(' '*10 + f'{pratos[i]} - {pratos[i+1]}: R${pratos[i+2]}')           
    elif pagina == '4':
      menu_cardapio()
    elif pagina == '5':
      print(" "*10 + 'Certeza que quer sair?')
    else:
      print(" "*5 + '\nOpção inválida, escolha uma opção do menu.\n')
      imprime_cardapio()
    
    nova_consulta = input('Gostaria de efetuar nova consulta? S/N ')
    if nova_consulta.lower() == 's':
      imprime_cardapio()
    else:
      print(" "*10 + '\nObrigada pela sua visita!\n')

menu_cardapio()