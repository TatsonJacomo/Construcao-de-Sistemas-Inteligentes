# Desenvolva um menu para registrar as pontuações das missões de um robô:

# 1 - Registrar pontuação
# 2 - Mostrar relatório
# 3 - Desfazer o último registro
# 0 - Sair

# 1. Comece com uma lista vazia de pontuações.
# 2. Na opção 1, leia um inteiro de 0 a 100. Repita a leitura enquanto estiver fora da faixa e adicione apenas o valor válido.
# 3. Na opção 2, mostre as pontuações na ordem de registro, a quantidade, o total, a média e a maior pontuação. Mostre também quantas missões tiveram pelo menos 70 pontos.
# 4. Se a lista estiver vazia, o relatório deve informar que não há missões registradas, sem calcular média ou maior pontuação.
# 5. Na opção 3, remova e mostre a última pontuação com pop(). Se a lista estiver vazia, informe que não há registro para desfazer.
# 6. A opção 0 encerra o programa. Outras opções mostram uma mensagem de erro.

# Teste de mesa: registre 80, 60 e 100.
# O relatório deve mostrar três missões, total 240, média 80.0, maior pontuação 100 e duas missões com pelo menos 70 pontos.
# Desfaça o último registro: restarão [80, 60], com média 70.0 e uma missão com pelo menos 70 pontos.

# Desafio adicional: crie outra lista contendo somente as pontuações a partir de 70, sem modificar a lista original.

pontuacoes = []

while True:
    print("\n=== Central de Missões ===")
    print("1 - Registrar pontuação")
    print("2 - Mostrar relatório")
    print("3 - Desfazer o último registro")
    print("0 - Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        while True:
            try:
                valor = int(input("Digite a pontuação da missão (0 a 100): "))
            except ValueError:
                print("Entrada inválida. Digite um número inteiro.")
                continue

            if 0 <= valor <= 100:
                pontuacoes.append(valor)
                print(f"Pontuação registrada: {valor}")
                break

            print("Pontuação fora da faixa permitida. Digite um número de 0 a 100.")

    elif opcao == "2":
        if not pontuacoes:
            print("Não há missões registradas.")
        else:
            total = sum(pontuacoes)
            media = total / len(pontuacoes)
            maior = max(pontuacoes)
            missões_70 = sum(1 for valor in pontuacoes if valor >= 70)
            pontuacoes_acima_70 = [valor for valor in pontuacoes if valor >= 70]

            print(f"Pontuações registradas: {pontuacoes}")
            print(f"Quantidade de missões: {len(pontuacoes)}")
            print(f"Total: {total}")
            print(f"Média: {media:.1f}")
            print(f"Maior pontuação: {maior}")
            print(f"Missões com pelo menos 70 pontos: {missões_70}")
            print(f"Pontuações a partir de 70: {pontuacoes_acima_70}")

    elif opcao == "3":
        if not pontuacoes:
            print("Não há registro para desfazer.")
        else:
            removida = pontuacoes.pop()
            print(f"Última pontuação removida: {removida}")

    elif opcao == "0":
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida. Tente novamente.")


