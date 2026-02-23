#Nesta primeira atividade, nosso objetivo é usar a POO para modelar um objeto do dia a dia. Você vai criar uma classe chamada Cachorro. Pense no que um cachorro é e o que ele pode fazer. Sua classe Cachorro deve ter: Um construtor __init__ que inicializa o objeto com três atributos de instância: nome (uma string), idade (um número inteiro) e raca (uma string). Um método de instância chamado latir() que não recebe nenhum parâmetro além de self e imprime a frase "Au au!". Outro método de instância chamado aniversario() que aumenta a idade do cachorro em 1 e imprime a mensagem: "Parabéns, [nome do cachorro]! Você completou [nova idade] anos!". Depois de definir a classe, crie um objeto (uma instância) chamado meu_cachorro a partir dela, passando os dados que você quiser. Em seguida, chame o método latir() e, por fim, chame o método aniversario() para ver a mágica acontecer. Dica: Lembre-se de usar self para se referir aos atributos e métodos dentro da classe. O construtor __init__ é o local perfeito para atribuir os valores iniciais.

class Cachorro:
    def __init__(self,nome:str, idade:int, raça:str):
        self.nome = nome
        self.idade = idade
        self.raça = raça

    def latir(self):
        print("Au au!")

    def aniversario(self):
        print(f"Parabéns,{self.nome}!Você completou {self.idade + 1} anos!")
    
meu_cachorro = Cachorro("Laika", 3, "salsicha")

meu_cachorro.aniversario()
