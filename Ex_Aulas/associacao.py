# Associação - Usada para criar uma ligação da classe Escritor ao atributo e método da classe Ferramentas

class Escritor:
    def __init__(self, nome):
        self.nome = nome
        self._ferramenta = None

# property para criar um método que pode ser usado como atributo.
    @property
    def ferramenta(self):
        return self._ferramenta

#usando o setter para modificar o valor do atributo _ferramentas da classe escritor.
    @ ferramenta.setter
    def ferramenta(self, ferramenta):
        self._ferramenta = ferramenta

class Ferramentas:
    def __init__(self, nome):
        self.nome = nome

    def escrever(self):
        return f'{self.nome} está escrevendo'
    

escritor = Escritor('Igor')
caneta = Ferramentas('Caneta Bic')
maquina_escrever = Ferramentas('Máquina de escrever')
#atribuido dentro da classe Escritor o valor da ferramenta
escritor.ferramenta = maquina_escrever
print(caneta.escrever())
print(maquina_escrever.escrever())
print(escritor.ferramenta.escrever())