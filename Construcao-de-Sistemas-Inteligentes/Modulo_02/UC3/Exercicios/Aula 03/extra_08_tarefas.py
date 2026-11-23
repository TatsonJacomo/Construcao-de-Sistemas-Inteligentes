class Tarefa:
    def __init__(self, descricao):
        self.descricao = descricao
        self.concluida = False

    def concluir(self):
        if self.concluida:
            return False
        self.concluida = True
        return True

    def reabrir(self):
        if not self.concluida:
            return False
        self.concluida = False
        return True


tarefas = []

while True:
    print("\n1 - Cadastrar tarefa")
    print("2 - Listar tarefas")
    print("3 - Concluir tarefa")
    print("4 - Reabrir tarefa")
    print("5 - Mostrar resumo")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        descricao = input("Descrição da tarefa: ")
        if descricao == "":
            print("Descrição vazia não é permitida.")
        elif any(tarefa.descricao == descricao for tarefa in tarefas):
            print("Já existe uma tarefa com essa descrição.")
        else:
            tarefas.append(Tarefa(descricao))
            print("Tarefa cadastrada.")

    elif opcao == "2":
        if len(tarefas) == 0:
            print("Não há tarefas cadastradas.")
        else:
            for tarefa in tarefas:
                situacao = "concluída" if tarefa.concluida else "pendente"
                print(tarefa.descricao, "-", situacao)

    elif opcao == "3":
        descricao = input("Descrição da tarefa: ")
        encontrada = None
        for tarefa in tarefas:
            if tarefa.descricao == descricao:
                encontrada = tarefa
                break

        if encontrada is None:
            print("Tarefa não encontrada.")
        elif encontrada.concluir():
            print("Tarefa concluída.")
        else:
            print("A tarefa já estava concluída.")

    elif opcao == "4":
        descricao = input("Descrição da tarefa: ")
        encontrada = None
        for tarefa in tarefas:
            if tarefa.descricao == descricao:
                encontrada = tarefa
                break

        if encontrada is None:
            print("Tarefa não encontrada.")
        elif encontrada.reabrir():
            print("Tarefa reaberta.")
        else:
            print("A tarefa já estava pendente.")

    elif opcao == "5":
        pendentes = 0
        concluidas = 0
        for tarefa in tarefas:
            if tarefa.concluida:
                concluidas += 1
            else:
                pendentes += 1

        print("Total:", len(tarefas))
        print("Pendentes:", pendentes)
        print("Concluídas:", concluidas)

    elif opcao == "0":
        print("Encerrando...")
        break

    else:
        print("Opção desconhecida.")

 