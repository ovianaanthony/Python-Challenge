from abc import ABC, abstractclassmethod, abstractproperty

class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self._contas = []

    @property
    def contas(self):
        return self._contas
    
    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self._contas.append(conta)

class PessoaFisica(Cliente):
    def __init__(self, endereco, nome, cpf, data_nascimento):
        super().__init__(endereco)
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento

    @property
    def pegar_cpf(self):
        return self.cpf
    
    def __str__(self):
        return f'Cliente: {self.nome} - cpf: {self.cpf}'

class Conta:
    def __init__(self, cliente, numero):
        self._saldo = 0
        self.numero = numero
        self.agencia = "0001"
        self.cliente = cliente
        self._historico = Historico()

    @property
    def saldo(self):
        return self._saldo

    @property
    def clientela(self):
        return self.cliente

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(cliente, numero)

    @abstractclassmethod
    def sacar(self, value):
        pass
        
    @property
    def historico(self):
        return self._historico 
 
    def depositar(self, valor):
        self._saldo += valor/2
        return True
    
class ContaCorrente(Conta):
    def __init__(self, cliente, numero):
        super().__init__(cliente, numero)
        self.limite = 500
        self.limite_saques = 3

    def sacar(self, value):
        if(self.limite<value):  
            print("Valor ultrapassa o limite de saque disponível.")
            return False
        elif(self.limite_saques==0):
            print("Você já atingiu o limite de saques") 
            return False 
        else:
            if(self.saldo < value):
                print("Valor de saque inválido.")
                return False
            else:
                self._saldo -= value/2
                self.limite_saques-=1
                print("Saque realizado com sucesso.")
                return True

    def __str__(self):
        return f'Dados da minha conta...\nAgência: {self.agencia} - Número: {self.numero}\n{self.cliente}.'
    
class Transacao(ABC):
    @abstractclassmethod
    def registrar(self, conta):
        pass

class Deposito(Transacao):
    def __init__(self, valor):
        super().__init__()
        self.valor = valor
    
    def registrar(self, conta):
        valor = conta.depositar(self.valor)
        if(valor):
            conta.historico.adicionar_transacao(self)


class Saque(Transacao):
    def __init__(self, valor):
        super().__init__()
        self.valor = valor

    def registrar(self, conta):
        valor = conta.sacar(self.valor)
        if(valor):
            conta.historico.adicionar_transacao(self)


class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao):
        self._transacoes.append({"tipo": transacao.__class__.__name__,
                                "valor": transacao.valor,})

def criar_usuario(cpfs, clientes):
    cpf = input("Digite o seu cpf: ")
    busca_cpf = filtrar_cpf(cpf, cpfs)
    if(busca_cpf):
        nome = input("Digite seu nome: ")
        data_nascimento = input("Digite a sua data de nascimento: ")
        endereco = input("Digite o seu endereço: ")
        cliente = PessoaFisica(nome=nome, cpf=cpf,endereco=endereco, data_nascimento=data_nascimento)
        clientes.append(cliente)
        return True
    else:
        print("Operação não realizada, já existe esse cpf na base de dados.")
        return False

def filtrar_cpf(cpf, cpfs):
    for documento in cpfs:
        if(documento == cpf):
            return False    
    cpfs.append(cpf)
    return True

def filtrar_clientes(clientes, cpf):
    for cliente in clientes:
        if(cpf == cliente.cpf):
            return cliente
    print("Não existe cliente cadastrado.")
    return False
    
        
def depositar(valor, contas, cpfs):
    if(valor<=0):
        print("Valor de depósito inválido.")
        return False
    else:
        cpf = input("Digite o cpf: ")
        if not(filtrar_cpf(cpf, cpfs)):
            print("Cpf ainda não cadastrado.")
            return False
        conta_1 = ''
        for count in contas:
            if(count.clientela.pegar_cpf == cpf):
                conta_1 = count
                transacao = Deposito(valor)
                conta_1.clientela.realizar_transacao(conta=conta_1, transacao=transacao)
                return True    
        print(f"Cliente não encontrado para efetuar a operação.")
        return False
        

def sacar(value, contas, cpfs):
    cpf = input("Digite o cpf: ")
    if not(filtrar_cpf(cpf, cpfs)):
        print("Cpf ainda não cadastrado.")
        return False
    conta_1 = ''
    for count in contas:
        if(count.clientela.pegar_cpf == cpf):
            conta_1 = count
            transacao = Saque(value)
            conta_1.clientela.realizar_transacao(conta=conta_1, transacao=transacao)
            return True
    print(f"Cliente não encontrado para efetuar a operação.")
    return False
    

def tirar_extrato(contas, cpfs):
    cpf = input("Digite o seu cpf: ")
    index = 0
    for cpfs in contas[index].clientela.cpf:
        if(cpfs == cpf):
            print("===================EXTRATO===================")
            transacoes = contas[index].historico.transacoes
            extrato = ""
            if not transacoes:
                print("Ainda não foram realizadas operações.")
            else:
                for transacao in transacoes:
                    extrato += f"\n{transacao["tipo"]}:\n R$ {transacao["valor"]:.2f}" 
                print(extrato) 
                print("============================================")
                return True
        index+=1
    print("Não foi possível tirar o extrato, não existe conta relacionada ao cpf informado.")
    return False

def criar_conta(contas, clientes):
    numero = len(contas)
    if(numero==0):
        numero+=1
    cpf = input("Insira seu cpf: ")
    cliente = filtrar_clientes(clientes, cpf)
    if(cliente):
            nova_conta = ContaCorrente.nova_conta(filtrar_clientes(clientes, cpf), numero)
            contas.append(nova_conta)
            cliente.contas.append(nova_conta)
            return True
    else:
        print("Erro ao criar conta, usuário não cadastrado.")
        return False

#veerificar o print da listagem de contas desta função ******** AINDA FALTA ******
def listar_contas(contas, clientes):
    cpf = input("Digite o seu cpf: ")
    cliente = filtrar_clientes(clientes, cpf)
    if(len(contas)==0):
        print("Ainda não existe contas no banco de dados...")
    index = 0
    while index < len(cliente.contas):
        print(str(cliente.contas[index]))
        index+=1
    
        

def visualizar_saldo(contas, clientes):
    cpf = input("Digite o seu cpf: ")
    if(filtrar_clientes(clientes, cpf)):
        index = 0
        for cpfs in contas[index].clientela.cpf:
            if(cpfs == cpf):
                print(f"Seu saldo disponível é: {contas[index].saldo}")
                return True
    print("Cliente não encontrado na base de dados.")
    return False

def menu(cpfs, clientes, contas):
    print(" ================ MENU =============== \n"
          "       NU -   Novo Usuário             \n"
          "       D  -    Depositar               \n" 
          "       S  -      Sacar                 \n"
          "       E  -     Extrato                \n"
          "       NC -    Nova Conta              \n"
          "       LC -   Listar Contas            \n"
          "       SD -      Saldo                 \n"
          "       0  -       Sair                 \n"
          " ===================================== \n")

    operacao = input("Insira a operação desejada: ").upper()
    match(operacao):
        case "NU":
            user = criar_usuario(cpfs, clientes)
            if(user):
                print("Usuário criado com sucesso!")
        case "D":
            valor = int(input("Digite um valor: "))
            dep = depositar(valor, contas, cpfs)
            if(dep):
                print("Depósito realizado com sucesso!")
        case "S":
            value = int(input("Digite o valor: "))
            sacar(value, contas, cpfs)
        case "E":
            tirar_extrato(contas, cpfs)
        case "NC":
            count = criar_conta(contas, clientes)
            if(count):
                print("Conta criada com sucesso!")
        case "SD":
            visualizar_saldo(contas, clientes)
        case "LC":
            print("Listando contas...")
            listar_contas(contas, clientes)
        case "0":
            return  
    
    menu(cpfs, clientes, contas)

def main():
    cpfs = []
    contas = []
    clientes = []

    menu(cpfs, clientes, contas)

main()






