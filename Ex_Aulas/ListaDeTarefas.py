def mostrar_lista(lista):
    for item in lista:
            print(item)

def opcoes(entrada_usuario):
    if entrada_usuario == 'listar':
        mostrar_lista(tarefas)
    elif entrada_usuario == 'desfazer':
        ...
    elif entrada_usuario == 'refazer':
        ...
    elif entrada_usuario == 'sair':
        return False
    else:
        tarefas.append(entrada_usuario)


tarefas = []


while True:
    print('Comandos: listar, desfazer e refazer')
    menu = opcoes(input('Digite uma tarefa ou comando: ').lower().strip())
    if menu == False:
        break