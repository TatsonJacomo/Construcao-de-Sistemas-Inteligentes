# Um robô pode realizar até cinco missões.
#  Ele começa com 100 pontos de energia, e cada missão custa 25 pontos.

# Utilize for para percorrer as missões de 1 até 5.

# Antes de pedir o resultado da missão, verifique se existe energia suficiente.
# Se não houver, mostre Energia insuficiente e encerre o laço com break.

# Para cada missão que puder ser realizada, solicite uma pontuação inteira entre 0 e 100. 
# Utilize while para repetir a leitura enquanto a pontuação estiver fora da faixa.

# Após receber uma pontuação válida, desconte a energia, acumule os pontos e conte a missão realizada.

# Ao final, mostre a quantidade de missões realizadas, a pontuação total, a média de pontos por missão realizada e a energia restante.
#  Só calcule a média se houver pelo menos uma missão realizada.

# Teste de mesa: com pontuações 80, 60, 100 e 40, o robô deve completar quatro missões, somar 280 pontos, obter média 70.0 e terminar com energia 0.
# A quinta missão não deve solicitar pontuação.

# Desafio adicional: altere a energia inicial para 20. O programa deve encerrar sem realizar missões e sem tentar dividir por zero.

energia = 100
pontuacao_total = 0
missoes_realizadas = 0

for missao in range(1, 6):
    if energia < 25:
        print("Energia insuficiente")
        break

    pontuacao = -1
    while pontuacao < 0 or pontuacao > 100:
        try:
            pontuacao = int(input(f"Digite a pontuação da missão {missao} (0 a 100): "))
        except ValueError:
            print("Pontuação inválida. Digite um número inteiro entre 0 e 100.")
            pontuacao = -1

    energia -= 25
    pontuacao_total += pontuacao
    missoes_realizadas += 1

print(f"Missões realizadas: {missoes_realizadas}")
print(f"Pontuação total: {pontuacao_total}")
if missoes_realizadas > 0:
    print(f"Média de pontos por missão: {pontuacao_total / missoes_realizadas:.1f}")
else:
    print("Média de pontos por missão: 0.0")
print(f"Energia restante: {energia}")

