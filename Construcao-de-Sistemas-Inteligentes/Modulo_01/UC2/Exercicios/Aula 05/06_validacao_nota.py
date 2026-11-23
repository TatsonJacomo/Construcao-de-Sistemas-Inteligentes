# Solicite uma nota entre 0 e 10.
# Enquanto o usuário informar um valor fora desse intervalo, apresente Nota inválida e solicite novamente.
# Quando uma nota válida for informada, mostre Nota registrada com sucesso!.

nota = float(input("Digite uma nota entre 0 e 10: "))

while nota < 0 or nota > 10:
    print("Nota inválida!")
    nota = float(input("Digite uma nota entre 0 e 10: "))

print("Nota registrada com sucesso!")