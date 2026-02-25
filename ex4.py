#Agora, vamos aplicar todos os conceitos em um pequeno projeto: um sistema simples de gestão de contas bancárias. Você vai criar uma classe que representa uma conta e outra para gerenciar um cliente. Parte 1: A Classe ContaBancaria Crie uma classe chamada ContaBancaria. Ela deve ter: Um construtor __init__ que inicializa os atributos de instância numero_conta (string) e saldo (número). O saldo inicial deve ser 0. Um método depositar(valor) que adiciona o valor ao saldo. Ele deve verificar se o valor é positivo. Um método sacar(valor) que retira o valor do saldo. Ele deve verificar se o valor é positivo e se há saldo suficiente para o saque. Um método verificar_saldo() que retorna o saldo atual. Parte 2: A Classe Cliente Crie uma classe chamada Cliente. Ela deve ter: Um construtor __init__ que inicializa os atributos de instância nome (string) e conta (que será um objeto da classe ContaBancaria). Parte 3: Interagindo com as Classes Crie um objeto da classe ContaBancaria com um número de conta de sua escolha. Crie um objeto da classe Cliente, passando um nome e o objeto da conta que você acabou de criar. Use o objeto do cliente para interagir com sua conta: Deposite 1000 reais. Verifique e imprima o saldo. Tente sacar 200 reais. Verifique e imprima o novo saldo. Tente sacar 900 reais para ver a validação de saldo insuficiente. Dica: No construtor da classe Cliente, você não deve criar uma nova conta, mas sim receber um objeto de ContaBancaria já existente. Isso demonstra como objetos podem conter outros objetos como atributos, uma característica poderosa da POO.



class ContaBancaria:
    def __init__(self, numero_conta:str, saldo:float = 0.0 ):
        self.numero_conta = numero_conta
        self.saldo = saldo
    
    def depositar(self, valor:float):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso")
        else:
            print("Valor inválido")

    def sacar(self,valor:float):
        if valor <= 0:
            print("Valor inválido para saque.")
        elif valor > self.saldo:
            print("Saldo insuficiente.")
        else:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado com sucesso.")
    
    def verificar_saldo(self):
        print(f"Saldo atual: R${self.saldo:.2f}")

           
class Cliente:
    def __init__(self, nome: str, conta: ContaBancaria):
        self.nome = nome
        self.conta = conta
    
    def hora_da_verdade(self):
        print(f"Cliente: {self.nome}")
        print(f"Número da conta: {self.conta.numero_conta}")
        self.conta.verificar_saldo()


# Criando objetos
conta1 = ContaBancaria("16356", 1000)
cliente1 = Cliente("João", conta1)

# Testando
cliente1.hora_da_verdade()
cliente1.conta.depositar(500)
cliente1.conta.sacar(200)
cliente1.conta.verificar_saldo()

    