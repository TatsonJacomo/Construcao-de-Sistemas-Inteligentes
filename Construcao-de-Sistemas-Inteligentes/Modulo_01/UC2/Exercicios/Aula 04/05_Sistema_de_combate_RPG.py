# Exercício 05 — Sistema de combate RPG

# Intermediário

# Durante uma aventura, um personagem encontra um inimigo e precisa decidir se consegue derrotá-lo.

# Solicite:
# Nome do personagem.
# Vida atual.
# Pontos de ataque.
# Vida do inimigo.
# Pontos de defesa do inimigo.

# Calcule o dano causado:
# dano = ataque - defesa

# Considere as seguintes regras:
# Se a vida do personagem for menor ou igual a zero, ele não poderá atacar.
# Se o dano for menor ou igual a zero, o ataque não causará dano.
# Se o dano for maior ou igual à vida do inimigo, o inimigo será derrotado.
# Caso contrário, o inimigo sobreviverá. Exiba a vida restante dele.

# Desafio: Impedir que a vida restante do inimigo fique negativa.

nome = input("Digite o nome do personagem: ")
vida_personagem = float(input("Digite a vida atual do personagem: "))
ataque = float(input("Digite os pontos de ataque: "))
vida_inimigo = float(input("Digite a vida do inimigo: "))
defesa_inimigo = float(input("Digite os pontos de defesa do inimigo: "))

dano = ataque - defesa_inimigo

if vida_personagem <= 0:
    print(f"{nome} não pode atacar porque está sem vida.")
elif dano <= 0:
    print(f"{nome} não causou dano ao inimigo.")
elif dano >= vida_inimigo:
    print(f"{nome} derrotou o inimigo!")
else:
    vida_restante = vida_inimigo - dano
    if vida_restante < 0:
        vida_restante = 0
    print(f"{nome} causou {dano} de dano.")
    print(f"Vida restante do inimigo: {vida_restante}")

