# Defina o código fictício "ROBO123".
# Dê ao usuário no máximo três tentativas para acertá-lo.

# Mostre o número da tentativa antes de cada leitura. 
# Se acertar, encerre o laço com break e informe o sucesso. 
# Se errar todas, informe que as tentativas acabaram.

# Teste um acerto na primeira tentativa, um acerto na terceira e três erros.

codigo_correto = "ROBO123"

for tentativa in range(1, 4):
    codigo = input(f"Tentativa {tentativa}: Digite o código: ")

    if codigo == codigo_correto:
        print("Código correto! Acesso liberado.")
        break
else:
    print("Tentativas acabaram. Código incorreto.")


