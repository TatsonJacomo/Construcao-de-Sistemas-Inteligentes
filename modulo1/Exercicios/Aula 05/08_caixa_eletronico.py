# Desenvolva um caixa eletrônico simples com saldo inicial de R$ 500.00.

# O programa deverá apresentar o seguinte menu:

# === CAIXA ELETRÔNICO ===
# 1 - Consultar saldo
# 2 - Depositar dinheiro
# 3 - Sacar dinheiro
# 0 - Sair


# Regras:

# O menu deverá continuar funcionando até que o usuário escolha sair.
# Depósitos e saques devem possuir valores maiores que zero.
# Não será permitido sacar mais dinheiro do que existe na conta.
# O saldo deverá ser atualizado após depósitos e saques válidos.
# Opções inválidas devem apresentar uma mensagem de erro.

# Desafio adicional: conte quantos depósitos e saques foram realizados durante a execução.

saldo = 500.00
quantidade_depositos = 0
quantidade_saques = 0

while True:
    print("\n=== CAIXA ELETRÔNICO ===")
    print("1 - Consultar saldo")
    print("2 - Depositar dinheiro")
    print("3 - Sacar dinheiro")
    print("0 - Sair")

    try:
        opcao = int(input("Escolha uma opção: "))
    except ValueError:
        print("Erro: opção inválida.")
        continue

    if opcao == 1:
        print(f"Saldo atual: R$ {saldo:.2f}")

    elif opcao == 2:
        try:
            valor = float(input("Digite o valor do depósito: "))
        except ValueError:
            print("Erro: valor inválido.")
            continue

        if valor <= 0:
            print("Erro: o valor do depósito deve ser maior que zero.")
        else:
            saldo += valor
            quantidade_depositos += 1
            print(f"Depósito realizado com sucesso. Saldo atual: R$ {saldo:.2f}")

    elif opcao == 3:
        try:
            valor = float(input("Digite o valor do saque: "))
        except ValueError:
            print("Erro: valor inválido.")
            continue

        if valor <= 0:
            print("Erro: o valor do saque deve ser maior que zero.")
        elif valor > saldo:
            print("Erro: saldo insuficiente para realizar o saque.")
        else:
            saldo -= valor
            quantidade_saques += 1
            print(f"Saque realizado com sucesso. Saldo atual: R$ {saldo:.2f}")

    elif opcao == 0:
        print(f"Total de depósitos: {quantidade_depositos}")
        print(f"Total de saques: {quantidade_saques}")
        print("Obrigado por usar o caixa eletrônico!")
        break

    else:
        print("Erro: opção inválida.")