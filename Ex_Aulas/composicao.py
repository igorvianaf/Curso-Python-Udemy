class Clientes:
    def __init__(self, nome):
        # Atributos da class Clientes
        self.nome = nome
        self.endereco = []

    def inserir_endereco(self, rua, numero):
        """Usando a composição para criar a instancia de endereço, dentro da classe Clientes. Para que quando a classe cliente não existir, a classe endereco não seja usada também."""
        self.endereco.append((Endereco(rua, numero)))
    
    def listar_enderecos(self):
        # Método para listar o endereço, com nome de rua e número.
        for endereco in self.endereco:
            print(endereco.rua, endereco.numero)

class Endereco:
    def __init__(self, rua, numero):
        # Atributos da class Endereco
        self.rua = rua
        self.numero = numero

cliente1 = Clientes('Igor')
cliente1.inserir_endereco('Avenida Brasil', 5000)
cliente1.inserir_endereco('Rua I', 93)

cliente1.listar_enderecos()
