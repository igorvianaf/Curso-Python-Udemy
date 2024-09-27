class Escritor:
    def __init__(self, nome):
        self.nome = nome
        self._ferramenta = None

    @property
    def ferramenta(self):
        return self._ferramenta

    @ferramenta.setter
    def ferramenta(self, ferramenta):
        self._ferramenta = ferramenta



class FerramentaDeEscrever:
    def __init__(self, nome):
        self.nome = nome

    def escrever(self):
        return f'{self.nome} está escrevendo'


escritor = Escritor('João')
caneta = FerramentaDeEscrever('Caneta Azul')
maquina_escrever = FerramentaDeEscrever('Maquina de escrever')
escritor.ferramenta = caneta
escritor.ferramenta = maquina_escrever

print(caneta.escrever())
print(maquina_escrever.escrever())