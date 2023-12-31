from pickle import APPEND
import os
cardapio = []
produto =''
bebidas = []
pratos = []

#-----------------------------------------------Menu Cardápio---------------------------------------------
#--------------------------------------Adicionar no Menu do Restaurante-----------------------------------

#def cadastrar_cardapio(restaurante, cardapio):
#    menu_por_restaurante[restaurante] = cardapio
    
#def acessar_cardapio(restaurante):
#    if restaurante in menu_por_restaurante:
#        return menu_por_restaurante[restaurante]
restaurantes = ['cozinha', 'pratobom', 'fomenao']
crestaurante = ''
cardapiobebida =[]
cardapiocompleto = []
cardapiopratos = []

  
def menu_cardapio():
  limpa_tela()

  #consulta_restaurante()
  
  print("*"*30)
  print('* Escolha uma opção: '+' '*8 + '*')
  print('* 1. Exibir Cardápio.'+' '*8 + '*')
  print('* 2. Cadastrar novos itens.  *')
  print('* 3. Sair '+' '*19 + '*')
  print("*"*30)
  opcao = input(' ')
  if opcao == '1':
    imprime_cardapio()
  elif opcao == '2':
    cadastra_item()
    
  elif opcao == '3':
  #menuprincipal
    print('Obrigada por sua visita!')
  else:
    print('\nOpção Inválida! Tente novamente!\n')
    menu_cardapio()

def cadastra_item():
  
  indice = consulta_restaurante()
    
  print("*"*30)
  print('* Escolha uma opção: '+' '*8 + '*')
  print('* 1. Cadastrar Bebidas'+' '*7 + '*')
  print('* 2. Cadastrar Pratos'+' '*8+'*')
  print('* 3. Sair '+' '*19 + '*')
  print("*"*30)
  
  opcao = input(' ')
  if opcao == '1':
    limpa_tela()
    print("*"*30)
    print('*'*5+' Cadastro de Bebidas '+'*'*4)
    print("*"*30)
  
    informa_dados_item(bebidas)
    #for bebida in bebidas:
     # cardapiobebida.append(bebida)
  
    #cardapiocompleto.append(cardapiobebida)
    cardapiocompleto.append(bebidas)
    print(cardapiocompleto)   
            
  elif opcao == '2':
    if len(cardapiocompleto) < indice:
      print('Cadastre bebidas antes de cadastrar os pratos desse restaurante!\n')
      cadastra_item()
    limpa_tela()
    print("*"*30)
    print('*'*5+' Cardastro de Pratos '+'*'*5)
    print("*"*30)
    informa_dados_item(pratos)
    #for prato in range(len(pratos)):
    cardapiocompleto.append(pratos)   
  elif opcao == '3':
    menu_cardapio()
    #estabelecimento
  
  return cardapiocompleto


      #-------------------------testes---------------------------------
      
      #produto = ['1','coca','20','2','guarana','30']; prato = ['camarao','pudim','torta']
 

#print(cardapiorestaurante)
#print(crestaurante)
#print(f'{cardapiocompleto[indice*2:(indice*2)+2]}')

#------------------------------------------------------------------------------


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
      menu_cardapio()
    else:
      preco = input('* Digite o valor do produto. R$')
      cardapio.append( item )
      cardapio.append( produto )
      cardapio.append( preco )
      item += 1
      print('\nProduto cadastrado com sucesso!\n')
      outroProduto = input('Deseja cadastrar outro produto? S/N \n')
      if outroProduto.lower() != 's':
        menu_cardapio()          
  return cardapio

def imprime_cardapio():
    indice = consulta_restaurante()
    limpa_tela()
   
    print("*"*50); print(' '*5 + '* Escolha a opção para exibir o cardápio: ' + '*')
    print('     *     1. Cardápio de Bebidas'+' '*14 + '*')
    print('     *     2. Cardápio de Pratos'+' '*15+'*')
    print('     *     3. Cardápio Completo '+' '*15+'*')
    print('     *     4. Voltar ao Menu Anterior '+' '*9+'*')
    print('     *     5. Sair '+' '*28 + '*'); print("*"*50)
    pagina = input(' ')
    if pagina == '1':
      if len(cardapiocompleto) > 0: #(indice*2):
        print(" "*10 + "*"*30); print(" "*10 + '*'*5+' Cardápio de Bebidas '+'*'*4); print(" "*10 + "*"*30)
        print(' '*10 + f'{cardapiocompleto[indice*2]} - {cardapiocompleto[indice*2+1]}: R${cardapiocompleto[indice*2+2]}\n')
      else:
        print(f'Não existe cardápio cadastrado para o restaurante: {crestaurante}\n')  
    elif pagina == '2':
      if len(cardapiocompleto) >= (indice*2):
        print(" "*10 + "*"*30); print(" "*10 + '*'*5+' Cardápio de Pratos '+'*'*5); print(" "*10 + "*"*30)
        print(' '*10 + f'{pratos[i]} - {pratos[i+1]}: R${pratos[i+2]}')
    elif pagina == '3':
      if len(cardapiocompleto) >= (indice*2):
        print(f'{cardapiocompleto[indice*2:(indice*2)+2]}')
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
      
def consulta_restaurante():
  crestaurante = input('Informe o nome do restaurante: ')
  if crestaurante in restaurantes:
    indice = restaurantes.index(crestaurante)
    print(indice)  
  else:
    restaurantes.append(crestaurante)
    indice = -1
    print(indice)
  return indice

#-----------------------------------------------Pedido---------------------------------------------------
#----------------------------------Adicionar no Menu do Cliente-------------------------------------------

carrinho = []
itemCarrinho = []
totalDaCompra = 0
def menu_pedido():
    #--------CarregarRestaurante
  print("*"*30); print('* Escolha uma opção: '+' '*8 + '*');
  print('* 1. Exibir Cardápio.'+' '*8 + '*'); print('* 2. Novo pedido.'+' '*10 + '  *');
  print('* 3. Montar Combo.'+' '*11 + '*')
  print('* 4. Consultar Carrinho'+' '*6 + '*')
  print('* 5. Sair '+' '*19 + '*'); print("*"*30)
  opcao = input(' ')
  if opcao == '1':
    imprime_cardapio()
    menu_pedido()
  elif opcao == '2':
    escolhe_produto()
  #elif opcao == '3':
    #monta_combo()
  elif opcao == '4':
    print(carrinho)
    print(totalDaCompra)
  elif opcao == '5':
    print('Obrigada pela sua visita!')

def escolhe_produto():
  carrinho = []
  novoProduto = ''
  bebida_prato = input('Gostaria de adicionar uma bebida[b] ou prato[p]? ')
  if bebida_prato.lower() == 'b':
    print(" "*10 + "*"*30); print(" "*10 + '*'*5+' Cardápio de Bebidas '+'*'*4); print(" "*10 + "*"*30)
    for i in range(0,len(bebidas),3):
      print(' '*10 + f'{bebidas[i]} - {bebidas[i+1]}: R${bebidas[i+2]}')
    print("*"*30); print('*'*5+' Escolhendo Bebidas '+'*'*4); print("*"*30)
    informa_dados_carrinho(bebidas)
    for items in range(len(itemCarrinho)):
      carrinho.append(items) 
    while novoProduto.lower() == 's':
      escolha = int(input('Adicione uma bebida ao carrinho: '))
      item=()
      carrinho.append( bebidas[(escolha-1)*3] )
      novoProduto = input('Deseja inserir outro produto? S/N ')
    print('Item adicionado ao carrinho com sucesso!')
    escolhe_produto()  
  elif bebida_prato.lower() == 'p':
    print(" "*10 + "*"*30); print(" "*10 + '*'*5+' Cardápio de Pratos '+'*'*5); print(" "*10 + "*"*30)
    for i in range(0,len(pratos),3):
      print(' '*10 + f'{pratos[i]} - {pratos[i+1]}: R${pratos[i+2]}')
    print("*"*30); print('*'*5+' Escolhendo Bebidas '+'*'*4); print("*"*30)
    informa_dados_carrinho(pratos)
    for items in range(len(itemCarrinho)):
      carrinho.append(items) 
    while novoProduto.lower() == 's':
      escolha = int(input('Adicione um prato ao carrinho: '))
      item=()
      carrinho.append( pratos[(escolha-1)*3])
      novoProduto = input('Deseja inserir outro produto? S/N ')    
    print('Item adicionado ao carrinho com sucesso!')
    escolhe_produto()
  for i in range(3,len(carrinho),3):
      totalDaCompra += i          
  print(carrinho)
  print(totalDaCompra) 

def informa_dados_carrinho(item):
  print("*"*50); print('* Insira o numero do item ou digite # para sair  *'); print("*"*50)
  produtoEscolhido = (input('* Digite o número do item: '))  
  if produtoEscolhido == '#':      
    menu_pedido()
  else:
    produtoEscolhido = int(produtoEscolhido)      
    itemCarrinho.append( item[((produtoEscolhido-1)*3)] )
    itemCarrinho.append( item[(((produtoEscolhido-1)*3)+1)] )
    itemCarrinho.append( item[(((produtoEscolhido-1)*3)+2)] )
    
    print('\nProduto adicionado com sucesso!\n')
    novoProduto = input('Deseja inserir outro produto? S/N ')
    if novoProduto.lower() != 's':
      print(itemCarrinho)          
  return itemCarrinho

############################################

def limpa_tela():
  return os.system('cls' if os.name == 'nt' else 'clear')

#########################################
menu_cardapio()
menu_pedido()    


#############Corrigido###################

from pickle import APPEND
import os

#-----------------------------------------------Menu Cardápio---------------------------------------------
#--------------------------------------Adicionado no Menu do Restaurante-----------------------------------

restaurantes = ['cozinha', 'pratobom', 'fomenao']  

#Define a função para chamar o menu de gerenciamento do cardápio
def menu_cardapio():
  limpa_tela()
  indice = consulta_restaurante()
  
  print("*"*30)
  print('* Escolha uma opção: '+' '*8 + '*')
  print('* 1. Exibir Cardápio.'+' '*8 + '*')
  print('* 2. Cadastrar novos itens.  *')
  print('* 3. Sair '+' '*19 + '*')
  print("*"*30)
  
  opcao = input(' ')
  if opcao == '1':
    imprime_cardapio()
  elif opcao == '2':
    cadastra_item()
  elif opcao == '3':
    #menuprincipal
    print('Obrigada por sua visita!')
  else:
    print('\nOpção Inválida! Tente novamente!\n')
    menu_cardapio()

def cadastra_item():
  indice = consulta_restaurante()
  cardapio = []
    
  print("*"*30); print('* Escolha uma opção: '+' '*8 + '*')
  print('* 1. Cadastrar Bebidas'+' '*7 + '*')
  print('* 2. Cadastrar Pratos'+' '*8+'*')
  print('* 3. Sair '+' '*19 + '*'); print("*"*30)
  opcao = input(' ')
  
  if opcao == '1':
    limpa_tela()
    print("*"*30); print('*'*5+' Cadastro de Bebidas '+'*'*4); print("*"*30)
    cardapiobebidas = informa_dados_item(bebidas)
    cardapiocompleto.append(cardapiobebidas) 
  
  elif opcao == '2':
    if len(cardapiocompleto) < indice:
      print('Cadastre bebidas antes de cadastrar os pratos desse restaurante!\n')
      cadastra_item()
    limpa_tela()
    print("*"*30); print('*'*5+' Cardastro de Pratos '+'*'*5); print("*"*30)
    cardapiopratos = informa_dados_item(pratos)
    cardapiocompleto.append(pratos)   
  
  elif opcao == '3':
    menu_cardapio()
  
  return

def informa_dados_item(cardapio):
  produto =''; item = 1; outroProduto = 's'  
  while produto != '#' and outroProduto.lower() == 's':
    print("*"*40); print('* Insira o dado ou digite # para sair  *')
    print("*"*40); produto = input('* Digite o nome do item: ')
    
    if produto == '#':    
      menu_cardapio()
    elif produto in cardapio:
      print('Produto informado já existe no cardápio, informe outro item!')
      informa_dados_item(bebidas)
    else:
      preco = input('* Digite o valor do produto. R$')
      cardapio.append( item )
      cardapio.append( produto )
      cardapio.append( preco )
      item += 1
      print('\nProduto cadastrado com sucesso!\n')
      outroProduto = input('Deseja cadastrar outro produto? S/N \n')
      if outroProduto.lower() != 's':
        menu_cardapio()          
  
  return cardapio

def imprime_cardapio():
    indice = consulta_restaurante()
    limpa_tela()
   
    print("*"*50); print(' '*5 + '* Escolha a opção para exibir o cardápio: ' + '*')
    print('     *     1. Cardápio de Bebidas'+' '*14 + '*')
    print('     *     2. Cardápio de Pratos'+' '*15+'*')
    print('     *     3. Cardápio Completo '+' '*15+'*')
    print('     *     4. Voltar ao Menu Anterior '+' '*9+'*')
    print('     *     5. Sair '+' '*28 + '*'); print("*"*50)
    pagina = input(' ')
    if pagina == '1':
      if len(cardapiocompleto) > (indice*2):
        print(" "*10 + "*"*30); print(" "*10 + '*'*5+' Cardápio de Bebidas '+'*'*4); print(" "*10 + "*"*30)
        restaurant = (cardapiocompleto[indice*2])
        for beverage in range(0,len(restaurant),3):
          print(' '*10 + f'{restaurant[beverage]} - {restaurant[beverage+1]}: R${restaurant[beverage+2]}\n')
      else:
        print(f'Não existe cardápio cadastrado para o restaurante: {crestaurante}\n')  
    
    elif pagina == '2':
      if len(cardapiocompleto) > (indice*2):
        print(" "*10 + "*"*30); print(" "*10 + '*'*5+' Cardápio de Pratos '+'*'*5); print(" "*10 + "*"*30)
        restaurant = (cardapiocompleto[indice+1])
        for dish in range(0,len(restaurant),3):
          print(' '*10 + f'{restaurant[dish]} - {restaurant[dish+1]}: R${restaurant[dish+2]}\n')
    
    elif pagina == '3':
      if len(cardapiocompleto) > (indice*2):
        print(" "*10 + "*"*30); print(" "*10 + '*'*5+' Cardápio de Bebidas '+'*'*4); print(" "*10 + "*"*30)
        restaurant = (cardapiocompleto[indice*2])
        for beverage in range(0,len(restaurant),3):
          print(' '*10 + f'{restaurant[beverage]} - {restaurant[beverage+1]}: R${restaurant[beverage+2]}\n')

        print(" "*10 + "*"*30); print(" "*10 + '*'*5+' Cardápio de Pratos '+'*'*5); print(" "*10 + "*"*30)
        restaurant = (cardapiocompleto[indice+1])
        for dish in range(0,len(restaurant),3):
          print(' '*10 + f'{restaurant[dish]} - {restaurant[dish+1]}: R${restaurant[dish+2]}\n')           
    
    elif pagina == '4':
      menu_cardapio()
    
    elif pagina == '5':
      print(" "*10 + 'Fique mais um pouco!')
    
    else:
      print(" "*5 + '\nOpção inválida, escolha uma opção do menu.\n')
      imprime_cardapio()
    
    nova_consulta = input('Gostaria de efetuar nova consulta? S/N ')
    if nova_consulta.lower() == 's':
      imprime_cardapio()
    else:
      print(" "*10 + '\nObrigada pela sua visita!\n')
      
def consulta_restaurante():
  crestaurante = input('Informe o nome do restaurante: ')
  if crestaurante in restaurantes:
    indice = restaurantes.index(crestaurante)
  else:
    restaurantes.append(crestaurante)
    indice = -1
  return indice

#-----------------------------------------------Pedido----------------------------------------------------
#----------------------------------Adicionar no Menu do Cliente-------------------------------------------
#-----------------------Funcionalidade em desenvolvimento, ainda não implementada-------------------------

carrinho = []
itemCarrinho = []
totalDaCompra = 0
def menu_pedido():
    #--------CarregarRestaurante
  print("*"*30); print('* Escolha uma opção: '+' '*8 + '*');
  print('* 1. Exibir Cardápio.'+' '*8 + '*'); print('* 2. Novo pedido.'+' '*10 + '  *');
  print('* 3. Montar Combo.'+' '*11 + '*')
  print('* 4. Consultar Carrinho'+' '*6 + '*')
  print('* 5. Sair '+' '*19 + '*'); print("*"*30)
  opcao = input(' ')
  if opcao == '1':
    imprime_cardapio()
    menu_pedido()
  elif opcao == '2':
    escolhe_produto()
  #elif opcao == '3':
    #monta_combo()
  elif opcao == '4':
    print(carrinho)
    print(totalDaCompra)
  elif opcao == '5':
    print('Obrigada pela sua visita!')

def escolhe_produto():
  carrinho = []
  novoProduto = ''
  bebida_prato = input('Gostaria de adicionar uma bebida[b] ou prato[p]? ')
  if bebida_prato.lower() == 'b':
    print(" "*10 + "*"*30); print(" "*10 + '*'*5+' Cardápio de Bebidas '+'*'*4); print(" "*10 + "*"*30)
    for i in range(0,len(bebidas),3):
      print(' '*10 + f'{bebidas[i]} - {bebidas[i+1]}: R${bebidas[i+2]}')
    print("*"*30); print('*'*5+' Escolhendo Bebidas '+'*'*4); print("*"*30)
    informa_dados_carrinho(bebidas)
    for items in range(len(itemCarrinho)):
      carrinho.append(items) 
    while novoProduto.lower() == 's':
      escolha = int(input('Adicione uma bebida ao carrinho: '))
      item=()
      carrinho.append( bebidas[(escolha-1)*3] )
      novoProduto = input('Deseja inserir outro produto? S/N ')
    print('Item adicionado ao carrinho com sucesso!')
    escolhe_produto()  
  elif bebida_prato.lower() == 'p':
    print(" "*10 + "*"*30); print(" "*10 + '*'*5+' Cardápio de Pratos '+'*'*5); print(" "*10 + "*"*30)
    for i in range(0,len(pratos),3):
      print(' '*10 + f'{pratos[i]} - {pratos[i+1]}: R${pratos[i+2]}')
    print("*"*30); print('*'*5+' Escolhendo Bebidas '+'*'*4); print("*"*30)
    informa_dados_carrinho(pratos)
    for items in range(len(itemCarrinho)):
      carrinho.append(items) 
    while novoProduto.lower() == 's':
      escolha = int(input('Adicione um prato ao carrinho: '))
      item=()
      carrinho.append( pratos[(escolha-1)*3])
      novoProduto = input('Deseja inserir outro produto? S/N ')    
    print('Item adicionado ao carrinho com sucesso!')
    escolhe_produto()
  for i in range(3,len(carrinho),3):
      totalDaCompra += i          
  print(carrinho)
  print(totalDaCompra) 

def informa_dados_carrinho(item):
  print("*"*50); print('* Insira o numero do item ou digite # para sair  *'); print("*"*50)
  produtoEscolhido = (input('* Digite o número do item: '))  
  if produtoEscolhido == '#':      
    menu_pedido()
  else:
    produtoEscolhido = int(produtoEscolhido)      
    itemCarrinho.append( item[((produtoEscolhido-1)*3)] )
    itemCarrinho.append( item[(((produtoEscolhido-1)*3)+1)] )
    itemCarrinho.append( item[(((produtoEscolhido-1)*3)+2)] )
    
    print('\nProduto adicionado com sucesso!\n')
    novoProduto = input('Deseja inserir outro produto? S/N ')
    if novoProduto.lower() != 's':
      print(itemCarrinho)          
  return itemCarrinho

##############################################################

def limpa_tela():
  return os.system('cls' if os.name == 'nt' else 'clear')

##############################################################
menu_cardapio()
menu_pedido()     
