# manter estados dentro de classes
class Camera:
    def __init__(self, nome, filmando=False):
        self.nome = nome
        self.filmando = filmando

    def filmar(self):
        if self.filmando:
            print(f'{self.nome} Já está filmando!!')
            return
        print(f'{self.nome} está filmando...' )
        self.filmando = True

    def fotografar(self):
        if self.filmando:
            print('Não posso fotografar e filmar ao mesmo tempo')
            return
        print(f'{self.nome} está fotografando...')

    def parar_filmar(self):
        if not self.filmando:
            print('Não esta filmando...')
            return
        print(f'{self.nome} está parando de filmar...')
        self.filmando = False

c1 = Camera('Cannon')
c2 = Camera('Sony')

print(c1.nome)
c1.filmar()
c1.fotografar()
c1.parar_filmar()
c1.fotografar()
