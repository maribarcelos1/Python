def existe_contato(lista,telefone):
    if len(lista)>0: #verifica se tem algo na lista
        for contato in lista:
            if contato ['telefone'] == telefone:
                return True
        return False

def adicionar(lista):
    while True:
        telefone = int(input("Digite o telefone:\n"))

        if not existe_contato(lista, telefone):
            break
        else:
            print('Esse telefone ja foi atualizado!')
            print('Cadastre Outro')

    contato = {
        "telefone": telefone,
        "nome": input("Digite o nome\n"),
        "email": input("Digite o email\n")
    }
    lista.append(contato)
    print(" o contato {} foi cadastrado com sucesso:\n".format(contato["nome"]))


def alterar():
    pass
def excluir():
    pass
def buscar():
    pass
def listar():
    pass

def principal():
    lista = [] # inicia com a lista vazia

    while True:
        print('''            === AGENDA ===
        [1] Adicionar contato
        [2] Alterar Contato
        [3] Excluir Contato
        [4] Buscar Contato
        [5] Listar contatos
        [6] Sair ''')
        opcao = int(input("> "))

        if opcao == 1:
            adicionar(lista)
        elif opcao == 2:
            alterar()
        elif opcao == 3:
            excluir()
        elif opcao == 4:
            buscar()
        elif opcao == 5:
            listar()
        elif opcao == 6:
            print("Saindo do programa...")
            break
        else:
            print("Opção Invalida!")

principal()