# Crie uma lista vazia e um menu com as opções:
# 1 - Adicionar pessoa ao final da fila
# 2 - Atender a primeira pessoa
# 3 - Mostrar a fila e sua quantidade de pessoas
# 0 - Sair

# Utilize append() para adicionar e pop(0) para atender. Antes de atender, verifique se há alguém na fila.
# Opções desconhecidas devem apresentar uma mensagem de erro.

# Teste atender com a fila vazia e adicionar Ana e Bruno para conferir a ordem dos atendimentos.

fila = []

while True:
    print("\n=== Fila de Atendimento ===")
    print("1 - Adicionar pessoa ao final da fila")
    print("2 - Atender a primeira pessoa")
    print("3 - Mostrar a fila e sua quantidade de pessoas")
    print("0 - Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        pessoa = input("Digite o nome da pessoa: ")
        fila.append(pessoa)
        print(f"{pessoa} entrou na fila.")

    elif opcao == "2":
        if not fila:
            print("Não há ninguém na fila para atender.")
        else:
            atendida = fila.pop(0)
            print(f"Atendendo: {atendida}")

    elif opcao == "3":
        print(f"Fila atual: {fila}")
        print(f"Quantidade de pessoas: {len(fila)}")

    elif opcao == "0":
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida. Tente novamente.")