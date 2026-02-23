#Nesta atividade, você vai aprofundar seu entendimento sobre como os atributos e métodos interagem dentro de uma classe, focando na distinção entre eles e no uso de self. Vamos criar uma classe chamada Pessoa para representar informações de uma pessoa. Crie a classe Pessoa com um construtor __init__ que recebe e inicializa dois atributos de instância: nome (string) e idade (inteiro). Adicione à classe Pessoa um método de instância chamado apresentar(). Este método deve imprimir uma saudação, como "Olá, meu nome é [nome] e tenho [idade] anos.", usando os atributos do próprio objeto. Crie um segundo método de instância chamado fazer_aniversario(). Este método deve aumentar o atributo idade do objeto em 1 e, em seguida, imprimir uma mensagem como "Parabéns, [nome]! Agora você tem [nova idade] anos!". Após definir a classe, crie um objeto chamado joao com o nome "João" e 25 anos de idade. Em seguida, chame o método apresentar() para ver a saudação inicial. Depois, chame o método fazer_aniversario() e, por fim, chame apresentar() novamente para confirmar que a idade foi atualizada. Dica: Lembre-se que self é essencial para acessar e modificar os atributos do objeto dentro dos métodos. O método fazer_aniversario() deve usar self.idade += 1 para atualizar o atributo.

class Pessoa:
    def __init__(self, nome:str, idade:int):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")

    def fazer_aniversario(self):
        self.idade += 1
        print(f"Parabéns, {self.nome}! Agora você tem {self.idade} anos!")

apres = Pessoa("Xonas", 87)
apres.apresentar()
apres.fazer_aniversario()
apres.apresentar()
