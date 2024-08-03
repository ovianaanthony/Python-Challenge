conta = {
    'saldo': 0,
    'limit': 0,
}

relatorio = {
    'extract': []
}

def depositar(valor):
    if(valor>0):
        conta['saldo']+=valor
        print("Depósito realizado!")
        relatorio['extract'].append(f'Depósito:  R${valor:.2f}')
        menu()
    else:
        print("Valor negativo não reconhecido.")
        menu()
    

def sacar(quantidade):
    if(quantidade>500):
        print("Excede o limite de Saque permitido.")
        menu()
    elif(quantidade>conta['saldo']):
        print("Saque indisponível")
        menu()
    else:
        conta['limit']+=1
        if(conta['limit']==4):
            print("Limite de saques diários alcançado.")
            menu()
        else:
            conta['saldo'] -= quantidade
            relatorio['extract'].append(f'Saque:  R${quantidade:.2f}')
            menu()

def tirar_extrato():
    a = list(relatorio.values())
    for item in a:
        print(f'{item}\n')

    print(f'O saldo da sua conta é R${conta['saldo']:.2f}.')
    menu()

def menu():
    print("""
    ================ MENU ================
      
    Informe o número da operação desejada:

    1 - Depósito
    2 - Saque 
    3 - Extrato
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
        quantidade = input("Digite o valor do saque: ")
        quantidade = float(quantidade)
        sacar(quantidade)
    elif(escolha == "3"):
        tirar_extrato()
    else:
        print("Opção inválida tente novamente.")
        menu()


menu()

