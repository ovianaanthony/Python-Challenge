#class PlanoTelefone:
#    def __init__(self, nome, saldo):
#        self.nome = nome
#        self.saldo = saldo
#
#    def verificar_saldo(self):
#        return self.saldo
#
#    def mensagem_personalizada(self, valor):
#        if(valor < 10):
#          return "Seu saldo está baixo. Recarregue e use os serviços do seu plano."
#        elif(valor >= 50):
#          return "Parabéns! Continue aproveitando seu plano sem preocupações."
#        else:
#          return "Seu saldo está razoável. Aproveite o uso moderado do seu plano."
#
#class UsuarioTelefone:
#    def __init__(self, nome, plano):
#        self.nome = nome
#        self.plano = plano
#
#    def verificar_saldo(self, plano_usuario):
#        valor = plano_usuario.verificar_saldo()
#        return plano_usuario.mensagem_personalizada(valor)
#
#plano_usuario = PlanoTelefone("nome_plano", 50) 
#usuario = UsuarioTelefone("nome_usuario", "plano_usuario")
#print(usuario.verificar_saldo(plano_usuario))

# Classe UsuarioTelefone e o encapsulamento dos atributos nome, numero e plano:



class UsuarioTelefone:
    def __init__(self, nome, numero, plano):
        self.nome = nome
        self.numero = numero
        self.plano = plano

#  Crie um método fazer_chamada para permitir que um usuário faça uma chamada telefônica:
    def fazer_chamada(self, destinatario, duracao):
        custo = self.calcular_custo(duracao)
        return self.verificar_saldo(custo, destinatario)
#  Calcule o custo da chamada usando o método 'custo_chamada' do objeto 'plano':
    def calcular_custo(self, duracao):
        return self.plano.calcular_custo(duracao)
# Verifique se o saldo do plano é suficiente para a chamada.
    def verificar_saldo(self, custo, destinatario):
        if(custo>self.plano.verificar_saldo()):
            return False
        else:
            return f"Sucesso ao ligar para {destinatario}, seu saldo restante é {self.plano.deduzir_saldo(custo)}"

class Plano:
    def __init__(self, saldo_inicial):
        self.saldo = saldo_inicial

#  Crie um método para verificar_saldo e retorne o saldo atual:
    def verificar_saldo(self):
      return self.saldo
#  Crie um método custo_chamada para calcular o custo de uma chamada supondo o custo de $0.10 por minuto:
    def calcular_custo(self, duracao, custo=0.10):
      return duracao*custo

#  Crie um método deduzir_saldo para deduz o valor do saldo do plano:
    def deduzir_saldo(self, valor):
      saldo = self.verificar_saldo()
      saldo -= valor
      return saldo

# Classe UsuarioPrePago, aqui vemos a herança onde UsuarioPrePago herda os atributos e métodos da classe UsuarioTelefone:
class UsuarioPrePago(UsuarioTelefone):
    def __init__(self, nome, numero, saldo_inicial):
        super().__init__(nome, numero, Plano(saldo_inicial))


# Objeto de UsuarioPrePago com os dados fornecidos:
usuario_pre_pago = UsuarioPrePago("nome", "numero", 10)

# Chama o método fazer_chamada do objeto usuario_pre_pago e imprime o resultado:
print(usuario_pre_pago.fazer_chamada("destinatario", 40))