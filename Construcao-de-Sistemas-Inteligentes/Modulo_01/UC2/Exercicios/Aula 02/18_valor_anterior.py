#Leia o programa sem executá-lo:

# saldo = 80
# saldo_anterior = saldo

# saldo = saldo - 25
# saldo = saldo + 10

# print("Saldo anterior:", saldo_anterior)
# print("Saldo atual:", saldo)


# Anote em comentários os valores que serão mostrados.
# Execute o código para conferir.
# Explique por que saldo_anterior mantém o valor que recebeu na atribuição, mesmo depois das mudanças em saldo.
# Acrescente uma despesa de 15 ao saldo atual e mostre novamente as duas variáveis.




saldo = 80
saldo_anterior = saldo  # saldo_anterior copia o valor atual de saldo (80)
saldo = saldo - 25      # saldo é atualizado para 55 (80 - 25)
saldo = saldo + 10      # saldo é atualizado para 65 (55 + 10)

print("Saldo anterior:", saldo_anterior)  # Mostra: Saldo anterior: 80
print("Saldo atual:", saldo)              # Mostra: Saldo atual: 65



# Adicionando uma despesa de 15 ao saldo atual
saldo = saldo - 15  # 65 - 15 = 50

print("--- Após a nova despesa ---")
print("Saldo anterior:", saldo_anterior)  # Continua sendo 80
print("Saldo atual:", saldo)              # Atualizado para 50