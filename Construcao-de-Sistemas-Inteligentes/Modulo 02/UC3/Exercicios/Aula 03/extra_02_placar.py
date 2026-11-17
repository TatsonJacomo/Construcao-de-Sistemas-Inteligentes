# O código abaixo deveria registrar os pontos de um jogador, mas contém erros:

# class Placar:
#     def __init__(self, jogador):
#         jogador = jogador
#         pontos = 0

#     def marcar(quantidade):
#         pontos = pontos + quantidade


# placar = Placar("Lia")
# placar.marcar(3)
# print(placar.jogador, placar.pontos)


# 1. Corrija a inicialização dos atributos e a definição do método.
# 2. Faça marcar(quantidade) aceitar apenas inteiros positivos, retornando True quando somar os pontos e False quando recusar o valor. Considere que o argumento já é inteiro.
# 3. Acrescente consultar_pontos(), que retorna a pontuação sem alterá-la.
# 4. Execute marcar(3), marcar(2), marcar(0) e marcar(-1).
# 5. Guarde o retorno de consultar_pontos() em uma variável e mostre seu dobro.


# Conferência: os retornos das marcações são True, True, False e False. A pontuação final é 5, e seu dobro é 10.


# Para explicar: por que escrever apenas pontos = 0 em __init__ não cria um atributo do objeto?


