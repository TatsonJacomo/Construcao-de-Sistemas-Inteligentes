while True:
    print("\n=== MENU ===")
    print("1 - Dizer olá")
    print("2 - Calcular o dobro")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        print("Olá! Seja bem-vindo!")

    elif opcao == "2":
        numero = int(input("Digite um número: "))
        print("Dobro:", numero * 2)

    elif opcao == "0":
        print("Encerrando...")
        break

    else:
        print("Opção inválida!")