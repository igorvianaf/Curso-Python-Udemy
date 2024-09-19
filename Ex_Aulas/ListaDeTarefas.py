def mostrar_lista(lista):
    for item in lista:
            print(item)


tarefas = []


while True:
    print('Comandos: listar, desfazer e refazer')
    entrada_usuario = input('Digite uma tarefa ou comando: ').lower().strip()
    if entrada_usuario == 'listar':
        mostrar_lista(tarefas)
    elif entrada_usuario == 'desfazer':
        ...
    elif entrada_usuario == 'refazer':
        ...
    elif entrada_usuario == 'sair':
        break
    else:
        tarefas.append(entrada_usuario)