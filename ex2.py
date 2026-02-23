#Nesta atividade, vamos aprofundar a manipulação de atributos e métodos. Você criará uma classe para representar uma lâmpada. Uma lâmpada pode estar ligada ou desligada. Crie uma classe chamada Lampada. No construtor __init__, defina um atributo de instância chamado ligada. Inicialize-o com o valor False, pois a lâmpada começa desligada por padrão. Crie um método chamado ligar() que altera o atributo ligada para True e imprime a mensagem "Lâmpada ligada!". Crie um método chamado desligar() que altera o atributo ligada para False e imprime a mensagem "Lâmpada desligada!". Crie um método chamado verificar_estado() que imprime "A lâmpada está ligada." ou "A lâmpada está desligada.", dependendo do valor do atributo ligada. Após definir a classe, crie um objeto minha_lampada. Chame o método verificar_estado() para ver o estado inicial. Em seguida, chame o método ligar(), e depois chame novamente verificar_estado(). Por fim, chame o método desligar() e verificar_estado() mais uma vez. Dica: Lembre-se que self.ligada dentro de um método se refere ao atributo da instância. Você pode usar uma estrutura condicional (if/else) para verificar o estado no método verificar_estado().

class Lampada:
    def __init__(self, ligada:bool):
        self.ligada = ligada

    def Ligar(self):
        self.ligada = True
     


    def Desligar(self):
        self.ligada = False
       

    def verificar_estado(self):
        if self.ligada == True:
            print("Lâmpada ligada!")
        else:
            print("Lâmpada desligada!")

lamp1 = Lampada (False)
lamp1.Ligar()

lamp1.verificar_estado()

