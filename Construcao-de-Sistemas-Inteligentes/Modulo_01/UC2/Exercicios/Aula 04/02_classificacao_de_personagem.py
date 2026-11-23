# Um jogo de RPG classifica seus aventureiros de acordo com o nível alcançado.

# Solicite o nome e o nível de um personagem e determine sua classificação:

# Nível           Classificação
# 1 a 5 	        Aprendiz
# 6 a 15	        Guerreiro
# 16 a 30	        Veterano
# 31 ou superior	Lendário


# Requisitos:

# Não permita níveis menores que 1.
# Mostre o nome do personagem e sua classificação.
# Utilize if, elif e else.

nome = input("Qual nome do seu personagem? ")
nivel = int(input("Qual seu nível? "))

if nivel > 1 and nivel < 5:
    print("Apendriz")
elif nivel > 6 and nivel < 15:
    print("Guerreiro")
elif nivel > 16 and nivel < 30:
    print("Veterano")
elif nivel >= 31:
    print("Lendário")
else:
    print("Sem Classificação")
    