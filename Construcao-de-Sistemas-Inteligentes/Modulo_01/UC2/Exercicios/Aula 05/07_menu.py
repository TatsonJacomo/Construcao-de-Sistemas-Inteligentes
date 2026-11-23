# Crie um menu com as seguintes opções:
# === MENU ===
# 1 - Somar dois números
# 2 - Verificar maioridade
# 0 - Sair
# O menu deverá continuar aparecendo até o usuário escolher a opção 0.
# Utilize while True, condicionais e break.

while True:
    print("\n=== MENU ===")
    print("1 - Somar dois números")
    print("2 - Verificar maioridade")
    print("0 - Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        print(f"A soma é: {num1 + num2}")

    elif opcao == 2:
        idade = int(input("Digite a idade: "))
        if idade >= 18:
            print("É maior de idade.")
        else:
            print("É menor de idade.")

    elif opcao == 0:
        print("Saindo do sistema...")
        break

    else:
        print("Opção inválida! Escolha 1, 2 ou 0.")