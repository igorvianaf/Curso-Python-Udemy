class Foo:
    def __init__(self):
        self.public = 'Isso é publico'
        self._protected = 'Isso é protegido'
        self.__private = 'Isso é privado'

    def metodo_publico(self):
        return self.public

    def _metodo_protected(self):
        print('Método protected')
        return 'metodo_protected'

    def __metodo_private(self):
        print('__metodo_private')
        return '__metodo_private'
classe1 = Foo()
print(classe1.metodo_publico())
print(classe1._metodo_protected())
print(classe1.__private())

