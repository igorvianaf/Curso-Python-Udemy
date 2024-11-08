class Carrinho:

# Lista para receber os produtos da classe produto
    def __init__(self):
        # Atributo para armazenar os produtos.
        self._produtos = []
# Método para calcular o total da compra
    def total(self):
        return sum([p.preco for p in self._produtos])

# Método para inserir um ou mais objetos da classe produto, dentro da lista de _produtos
    def inserir_produtos(self, *produtos):
        for produto in produtos:
            self._produtos.append(produto)

# Método para listar os produtos da classe carrinho
    def listar_produtos(self):
        print()
        for produto in self._produtos:
            print(produto.nome, produto.preco)
        print()

# Classe para receber diversos produtos
class Produto:
    def __init__(self, nome, preco):
        # Atributos para definir os itens da classe produto
        self.nome = nome
        self.preco = preco

carrinho = Carrinho()
p1, p2 = Produto('Caneta', 1.20), Produto('Camiseta', 25)
carrinho.inserir_produtos(p1, p2)
carrinho.listar_produtos()
print(carrinho.total())
