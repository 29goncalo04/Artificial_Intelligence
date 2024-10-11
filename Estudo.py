frutas = ["maçãs", "laranjas", "pêras", "bananas"]
for fruta in frutas:
    print(fruta)

print()

precosFruta = {"maçãs":2.00, "laranjas":1.50, "pêras":1.75}
for fruta, preco in precosFruta.items():
    if preco<2.00:
        print("As " + fruta + " custam %f o kg" %(preco))
    else:
        print("As " + fruta + " são demasiado caras")

print()

print(list(map(lambda x : x*x, [1,2,3])))

print()

print(list(filter(lambda x : x<4, [1,2,3,4,5,4,3,2,1])))

#####################
class Pessoa:
    populacao = 0

    def __init__(self, minhaIdade):
        self.idade = minhaIdade
        Pessoa.populacao += 1

    def get_populacao(self):
        return Pessoa.populacao

    def get_idade(self):
        return self.idade