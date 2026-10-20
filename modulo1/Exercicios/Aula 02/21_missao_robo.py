# Você vai simular uma missão utilizando apenas variáveis e operações sequenciais.

# Crie o estado inicial do robô:

#         Informação            	Valor inicial
#          Nome                     	"Atlas"
#          Energia	                       100
#     Distância percorrida, em metros   	0
#      Amostras coletadas                  	0
#       Missão em andamento	               True

# Mostre uma ficha inicial. Depois simule os acontecimentos nesta ordem:

# O robô percorre 120 metros e consome 20 pontos de energia.
# Coleta 3 amostras e consome 15 pontos de energia.
# Recarrega 10 pontos de energia.
# Percorre mais 80 metros e consome 25 pontos de energia.
# Coleta mais 2 amostras e consome 10 pontos de energia.
# Encerra a missão: atribua False à variável que indica se a missão está em andamento.
# Atualize as variáveis correspondentes em cada etapa. Mostre uma mensagem após cada acontecimento e, no final, apresente uma ficha com todos os valores atualizados.

# Parte extra: considerando que a missão durou 4 minutos, calcule a distância média percorrida por minuto e mostre o resultado com a unidade metros por minuto.


nome = "Atlas"
energia = 100
distancia_percorrida = 0
amostras_coletadas = 0
missao_em_andamento = True

print("-------- Meu Robô ---------")
print("Nome", nome)
print("Energia", energia)
print("Distância Percorrida", distancia_percorrida)
print("Amostras Coletadas", amostras_coletadas)
print("Missão em Andamento", missao_em_andamento)
print("----------------------------")
print()
print("1 - O robô percorreu 120 metros e consome 20 pontos de energia.")
distancia_percorrida += 120
energia -= 20
print()
print("2 - Coleta 3 amostras e consome 15 pontos de energia.")
amostras_coletadas += 3
energia -= 15
print()
print("3 - Recarrega 10 pontos de energia.")
energia += 10
print()
print("4 - Percorre mais 80 metros e consome 25 pontos de energia.")
distancia_percorrida += 80
energia -= 25
print("5 -  Coleta mais 2 amostras e consome 10 pontos de energia.")
amostras_coletadas = 2
energia -= 10
print("")
print("6 - Encerra a missão: atribua False à variável que indica se a missão está em andamento.")
missao_em_andamento = False
print("")


tempo_total_minutos = 4
distancia_media = distancia_percorrida / tempo_total_minutos

print("-------- Ficha Final --------")
print("Nome:", nome)
print("Energia Final:", energia)
print("Distância Total Percorrida:", distancia_percorrida, "metros")
print("Amostras Totais Coletadas:", amostras_coletadas)
print("Missão em Andamento:", missao_em_andamento)
print("-----------------------------")

print("Distância Média Percorrida: ${distancia_media} metros por minuto")