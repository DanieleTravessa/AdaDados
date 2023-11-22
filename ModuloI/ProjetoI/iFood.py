#from manipulate_data import load_json_file, save_json_file

# Inicialização das listas de clientes e restaurantes
#clientes = load_json_file("cadastro", "cliente")
#if clientes is None:
#    clientes = []

#restaurantes = load_json_file("cadastro", "restaurante")
#if restaurantes is None:
#    restaurantes = []

def validar_nome_cliente():
    while True:
        nome_do_cliente = input("Digite o seu nome completo: ")
        if nome_do_cliente.replace(" ", "").isalpha():
            return nome_do_cliente
        print("Nome inválido. O nome deve conter apenas letras e não pode estar em branco.")

def validar_cpf():
    while True:
        cpf = input("Digite o seu CPF: ")
        cpf = ''.join(filter(str.isdigit, cpf))
        if len(cpf) == 11:
            return cpf
        print("CPF inválido. Deve conter exatamente 11 dígitos e ser composto exclusivamente por números.")

def validar_telefone():
    while True:
        numero_telefone = input("Digite o seu número de telefone: ")
        numero_telefone = ''.join(filter(str.isdigit, numero_telefone))
        if len(numero_telefone) == 12:
            numero_formatado = f"({numero_telefone[:3]}) {numero_telefone[3:8]}-{numero_telefone[8:]}"
            return numero_formatado
        print("Número de telefone inválido. Deve conter exatamente 12 dígitos e ser composto exclusivamente por números.")

def validar_email_cliente():
    while True:
        email_cliente = input("Digite o seu e-mail: ")
        if "@" in email_cliente and "." in email_cliente:
            return email_cliente
        print("E-mail inválido. Deve estar no formato 'usuario@dominio.com'.")

def validar_latitude_cliente():
    while True:
        latitude_cliente = input("Digite a latitude do seu endereço: ")
        try:
            latitude_cliente = float(latitude_cliente)
            if -90 <= latitude_cliente <= 90:
                return latitude_cliente
            else:
                print("Latitude fora do intervalo válido. Deve estar entre -90 e 90.")
        except ValueError:
            print("Latitude fora do intervalo válido. Deve estar entre -90 e 90.")

def validar_longitude_cliente():
    while True:
        longitude_cliente = input("Digite a longitude do seu endereço: ")
        try:
            longitude_cliente = float(longitude_cliente)
            if -180 <= longitude_cliente <= 180:
                return longitude_cliente
            else:
                print("Longitude fora do intervalo válido. Deve estar entre -180 e 180.")
        except ValueError:
            print("Longitude fora do intervalo válido. Deve estar entre -180 e 180.")

def exibir_perfil_cliente():
    cpf_digitado = input("Digite o seu CPF: ")
    cpf_digitado = ''.join(filter(str.isdigit, cpf_digitado))  # Remove caracteres não numéricos do CPF digitado
    for cliente in clientes:
        cpf_armazenado = ''.join(filter(str.isdigit, cliente[1]))  # Remove caracteres não numéricos do CPF armazenado
        if cpf_armazenado == cpf_digitado:
            print("\nPerfil do Cliente:")
            print("Nome:", cliente[0])
            print("CPF:", cliente[1])
            print("Número de Telefone:", cliente[2])
            print("E-mail:", cliente[3])
            print("Endereço em (latitude e longitude):", cliente[4])
            return
    print("Cliente não encontrado.")

def cadastrar_cliente():
    nome_do_cliente = validar_nome_cliente()
    cpf_armazenado = validar_cpf()
    numero_telefone = validar_telefone()
    email_cliente = validar_email_cliente()
    latitude_cliente = validar_latitude_cliente()
    longitude_cliente = validar_longitude_cliente()

    cliente = [nome_do_cliente, cpf_armazenado, numero_telefone, email_cliente, [latitude_cliente, longitude_cliente]]
    clientes.append(cliente)

    # Salva a lista de clientes no arquivo JSON
    nome_colunas = ["Nome do Cliente", "CPF", "Numero de Telefone", "E-mail", "Localizacao Cliente"]
    save_json_file("cadastro", "cliente", clientes, nome_colunas)

    print("\nCliente cadastrado com sucesso!")

# Função para o Menu de Gerenciamento do Cliente
def menu_gerenciar_clientes():
    while True:
        print("\nMenu Ifood Cliente:")
        print("1. Cadastro de Cliente")
        print("2. Exibir meu Perfil")
        print("3. Localizar os restaurantes mais próximos")
        print("4. Voltar ao Menu Principal")
        opcao = input("Selecione uma opção: ")

        if opcao == '1':
            cadastrar_cliente()
        elif opcao == '2':
            exibir_perfil_cliente()
        elif opcao == '3':
            pass
        elif opcao == '4':
            print("Voltando ao Menu Principal...")
            break
        else:
            print("Opção inválida. Tente novamente.")

###########################################################################################################################################################################

# Inicialização da lista de restaurantes
#restaurantes = load_json_file("cadastro", "restaurante")
#if restaurantes is None:
#    restaurantes = []

def validar_nome_proprietario():
    while True:
        nome_do_proprietario = input("Digite o nome completo do Proprietário: ")
        if nome_do_proprietario.replace(" ", "").isalpha():
            return nome_do_proprietario
        print("Nome inválido. O nome deve conter apenas letras e não pode estar em branco.")

def validar_nome_restaurante():
    while True:
        nome_do_restaurante = input("Digite o nome do Restaurante: ")
        if nome_do_restaurante.replace(" ", "").isalpha():
            return nome_do_restaurante
        print("Nome inválido. O nome deve conter apenas letras e não pode estar em branco.")

def validar_cnpj():
    while True:
        cnpj = input("Digite o CNPJ: ")
        cnpj = ''.join(filter(str.isdigit, cnpj))
        if len(cnpj) == 14:
            cnpj_formatado = f"{cnpj[:2]}.{cnpj[2:5]}.{cnpj[5:8]}/{cnpj[8:12]}-{cnpj[12:]}"
            return cnpj_formatado
        print("CNPJ inválido. Deve conter exatamente 14 dígitos e ser composto exclusivamente por números.")

def validar_telefone():
    while True:
        numero_telefone = input("Digite o número de telefone no formato (DDD) XXXXX-XXXX: ")
        numero_telefone = ''.join(filter(str.isdigit, numero_telefone))
        if len(numero_telefone) == 12:
            numero_formatado = f"({numero_telefone[:3]}) {numero_telefone[3:8]}-{numero_telefone[8:]}"
            return numero_formatado
        print("Número de telefone inválido. Deve conter exatamente 12 dígitos e ser composto exclusivamente por números.")

def validar_email_restaurante():
    while True:
        email = input("Digite o e-mail do restaurante: ")
        if "@" in email and "." in email:
            return email
        print("E-mail inválido. Deve estar no formato 'usuario@dominio.com'.")

def validar_numero_funcionarios():
    while True:
        numero_funcionarios = input("Digite o número de funcionários: ")
        if numero_funcionarios.isdigit() and int(numero_funcionarios) >= 0:
            return numero_funcionarios
        print("Número de funcionários inválido. O valor deve ser maior ou igual a 0.")

def validar_latitude_restaurante():
    while True:
        latitude = input("Digite a latitude do endereço do restaurante: ")
        try:
            latitude = float(latitude)
            if -90 <= latitude <= 90:
                return latitude
            else:
                print("Latitude fora do intervalo válido. Deve estar entre -90 e 90.")
        except ValueError:
            print("Latitude fora do intervalo válido. Deve estar entre -90 e 90.")

def validar_longitude_restaurante():
    while True:
        longitude = input("Digite a longitude do endereço do restaurante: ")
        try:
            longitude = float(longitude)
            if -180 <= longitude <= 180:
                return longitude
            else:
                print("Longitude fora do intervalo válido. Deve estar entre -180 e 180.")
        except ValueError:
            print("Longitude fora do intervalo válido. Deve estar entre -180 e 180.")

def cadastrar_restaurante():
    nome_do_proprietario = validar_nome_proprietario()
    nome_do_restaurante = validar_nome_restaurante()
    cnpj = validar_cnpj()
    numero_telefone = validar_telefone()
    email = validar_email_restaurante()
    numero_funcionarios = validar_numero_funcionarios()
    latitude = validar_latitude_restaurante()
    longitude = validar_longitude_restaurante()

    restaurante = [nome_do_proprietario, nome_do_restaurante, cnpj, numero_telefone, email, numero_funcionarios, [latitude, longitude]]

    restaurantes.append(restaurante)

    # Salva a lista de restaurantes no arquivo JSON
    nome_colunas = ["Nome do Proprietario", "Nome do Restaurante", "CNPJ", "Numero de Telefone", "E-mail", "Numero de Funcionarios", "Localizacao do Restaurante"]
    save_json_file("cadastro", "restaurante", restaurantes, nome_colunas)

    print("\nRestaurante cadastrado com sucesso!")

# Função para exibir o perfil do restaurante
def perfil_restaurante():
    nome_restaurante = input("Digite o nome do Restaurante: ")
    for restaurante in restaurantes:
        if restaurante[1] == nome_restaurante:
            print("\nPerfil do Restaurante:")
            print("Nome do Proprietário:", restaurante[0])
            print("Nome do Restaurante:", restaurante[1])
            print("CNPJ:", restaurante[2])
            print("Número de Telefone:", restaurante[3])
            print("E-mail:", restaurante[4])
            print("Número de Funcionários:", restaurante[5])
            print("Endereço do Restaurante (Latitude, Longitude):", restaurante[6])
            #cardapio acessarCardapio = input('Acesse o Menu de Cardápio digitando 1 !')
            #if acessarCardapio == '1': menu_cardapio(restaurante[1])
            return
    print("Restaurante não encontrado.")


def menu_gerenciar_restaurantes():
    while True:
        print("\nMenu Ifood Restaurantes:")
        print("1. Cadastrar Restaurante")
        print("2. Perfil do Restaurante")
        print("3. Cardápio")
        print("4. Histórico de Vendas")
        print("5. Voltar ao Menu Principal")

        opcao = input("Selecione uma opção: ")

        if opcao == '1':
            cadastrar_restaurante()
        elif opcao == '2':
            perfil_restaurante()
        elif opcao == '3':        
            menu_cardapio()
        elif opcao == '4':
            pass
        elif opcao == '5':
            print("Voltando ao Menu Principal...")
            break
        else:
            print("Opção inválida. Tente novamente.")
                     
###########################################################################################################################################################################

cardapio = []
produto =''
bebidas = []
pratos = []

#-----------------------------------------------Menu Cardápio---------------------------------------------
#--------------------------------------Adicionar no Menu do Restaurante-----------------------------------

def menu_cardapio():
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

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  


# Função para o menu principal
def menu_principal():
    while True:
        print("\nMenu Principal:")
        print("1. Ifood Restaurantes")
        print("2. Ifood Clientes")
        print("3. Sair")

        opcao = input("Selecione uma opção: ")

        if opcao == "1":
            menu_gerenciar_restaurantes()
        elif opcao == "2":
            menu_gerenciar_clientes()
        elif opcao == "3":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Execução do programa
menu_principal()