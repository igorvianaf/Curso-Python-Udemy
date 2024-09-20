import os


lista = []
lista_refazer = []


def listar_tarefas(lista):
    if not lista:
        print('Sua lista de tarefas está vazia!')
        return
    for item in lista:
        print(item)

def desfazer_lista(lista, lista_desfazer):
    if not lista:
        print('Não temos tarefas para desfazer na sua lista')
        return
    ultima_tarefa = lista.pop()
    lista_desfazer.append(ultima_tarefa)
    print(f'{ultima_tarefa} foi removido da sua lista')

def refazer_lista(lista, lista_refazer):
    if not lista_refazer:
        print('Não temos tarefas para refazer na sua lista')
        return
    ultima_tarefa = lista_refazer.pop()
    lista.append(ultima_tarefa)
    print(f'{ultima_tarefa} voltou a sua lista')

def adicionar(tarefa, lista):
    lista.append(tarefa)
    print(f'{tarefa} adicionado a sua lista')

def opcoes(entrada_usuario):
    var_checar = entrada_usuario.strip().lower()

    if var_checar == 'listar':
        listar_tarefas(lista)

    elif var_checar == 'desfazer':
        desfazer_lista(lista, lista_refazer)

    elif var_checar == 'refazer':
        refazer_lista(lista, lista_refazer)

    elif var_checar == 'clear':
        os.system('cls')

    elif var_checar == 'sair':
        return False

    else:
        adicionar(entrada_usuario, lista)


print('Bem vindo a sua lista!!')
while True:
    print('Digite um dos comandos (Listar, Desfazer, Refazer) ou adicione algo a sua lista: ')
    menu = opcoes(input('Digite uma tarefa ou comando: '))
    if menu == False:
        break