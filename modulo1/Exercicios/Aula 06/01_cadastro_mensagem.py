# Arquivo: 01_cadastro_mensagem.py

# Antes de investigar uma mensagem, a equipe precisa organizar os dados disponíveis.

# Recebam pelo teclado:

# o nome ou apelido do analista;
# a identificação da mensagem, como texto, por exemplo MSG-007;
# a quantidade de grupos de símbolos, como inteiro;
# o tempo estimado para analisar cada grupo, em minutos, como decimal.

# Regras:

# 1. A quantidade de grupos e o tempo por grupo devem ser maiores que zero.
# 2. Se qualquer um desses valores for inválido, mostrem Dados inválidos e não calculem o tempo total.
# 3. Se os dados forem válidos, calculem o tempo total estimado: quantidade de grupos multiplicada pelo tempo por grupo.
# 4. Apresentem uma ficha com o analista, a identificação, a quantidade de grupos e o tempo total em minutos.
# 5. Se o total for menor ou igual a 60 minutos, mostrem Análise dentro do prazo; caso contrário, mostrem Reorganizar o trabalho.

# Para explicar: por que a identificação é texto mesmo quando contém algarismos? Por que é adequado usar float() para o tempo por grupo?


analista = input("Qual nome do analista? ")
credencial = input("Qual sua credencial (ex: MSG-007)? ")
quantidade_grupo = int(input("Qual a quantidade de grupo de símbolos? "))
tempo_grupo = float(input("Qual a quantidade de tempo estimado (em minutos)? "))

print("\n--------- DADOS DO ANALISTA ---------")

if quantidade_grupo <= 0 or tempo_grupo <= 0:
    print("Dados Inválidos")
else:
    # CALCULO DO TEMPO TOTAL
    tempo_total = quantidade_grupo * tempo_grupo

    print(f"Analista responsável: {analista}")
    print(f"Identificação da mensagem: {credencial}")
    print(f"Quantidade de grupos: {quantidade_grupo}")
    print(f"Tempo total estimado: {tempo_total: .1f} minutos")

    if tempo_total <= 60.0:
        print("Status: Análise dentro do prazo")
    else:
        print("Status: Reorganizar o trabalho")

print("----------------------------------------")
