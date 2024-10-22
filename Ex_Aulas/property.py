class Caneta:
    def __init__(self, cor, tampa):
        self._cor_tinta = cor
        self.tampa = tampa


    """Usado para acessar um atributo preservando o seu valor inicial e dando a possibilidade de estabelecer novos valores ao atributo com o setter. Também cria a possibilidade de acessar o método como atributo"""
    @property
    def cor(self):
        return self._cor_tinta

    @property
    def cor_tampa(self):
        return self.tampa


caneta = Caneta('Azul', 'Preta')

print(caneta.cor)
print(caneta.tampa)
