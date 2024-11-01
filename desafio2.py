usuarios = []      # nome, data de nascença, cpf, endereco
conta = []         # numero de conta, agencia, usuarios
AGENCIA = "0001"

controle = {
    'saldo': 0,
    'limit': 0,
    'acoes': 0
}

relatorio = {
    'extract': []
}

def depositar(valor, /):
    if(valor>0):
        controle['saldo']+=valor
        print("Depósito realizado!")
        relatorio['extract'].append(f'Depósito:  R${valor:.2f}.')
        controle['acoes']+=1
        menu()
    else:
        print("Valor negativo não reconhecido.")
        menu()
    

def sacar(*, quantidade):
    if(quantidade>500):
        print("Excede o limite de Saque permitido.")
        menu()
    elif(quantidade>controle['saldo']):
        print("Saque indisponível")
        menu()
    else:
        controle['limit']+=1
        if(controle['limit']==4):
            print("Limite de saques diários alcançado.")
            menu()
        else:
            controle['saldo'] -= quantidade
            relatorio['extract'].append(f'Saque:  R${quantidade:.2f}.')
            controle['acoes']+=1
            print("Saque realizado com sucesso!")
            menu()

def tirar_extrato():
    a = list(relatorio.values())

    index = 0  
    while index < controle['acoes']:
        print(a[0][index])
        index+=1

    print(f'\nO saldo da sua conta é R${controle['saldo']:.2f}.\n')
    menu()

def criar_usuario(usuarios):
    cpf = input("Digite o seu cpf: ")
    boleano = filtrar_user(cpf, usuarios)

    if (boleano):
        print("Usuário já existente no sistema")
        menu()

    nome = input("Digite seu nome: ")
    data_nascimento = input("Digite sua data de nascimento: ")
    endereco = input("Digite seu endereço: ")
    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print("\nUsuário criado com sucesso!")
    menu()


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Digite o seu cpf: ")
    boleano = filtrar_user(cpf, usuarios)

    if(boleano):
        print("Conta criada com sucesso!")
        return conta.append({"agencia": agencia, "numero_conta": numero_conta, "usuario": boleano})
    print("Usuário não encontrado!")
    menu()

def filtrar_user(cpf, usuarios):
    usuarios_filtrados = []
    for usuario in usuarios: 
        if (usuario["cpf"]==cpf):
            usuarios_filtrados.append(usuario)
    if(usuarios_filtrados):
        return usuarios_filtrados[0]
    else:
        return None

def menu():
    print("""
    ================ MENU ================
      
    Informe o número da operação desejada:

    1 - Depósito
    2 - Saque 
    3 - Extrato
    4 - Criar novo usuário
    5 - Criar nova conta
    0 - Encerrar movimentação
      
    ======================================    
    """)
    
    escolha = input()

    if(escolha == "0"):
        return
    if(escolha == "1"):
        valor = input("Digite o valor para depósito: ")
        valor = float(valor)
        depositar(valor)
    elif(escolha == "2"):
        quanti = input("Digite o valor do saque: ")
        quanti = float(quanti)
        sacar(quantidade=quanti)
    elif(escolha == "3"):
        tirar_extrato()
    elif(escolha == "4"):
        criar_usuario(usuarios)
    elif(escolha == "5"):
        numero_conta = len(conta)+1
        conta_var = criar_conta(AGENCIA, numero_conta, usuarios)
        if(conta_var):
            conta.append(conta_var)
    else:
        print("Opção inválida tente novamente.")
        menu()


menu()

