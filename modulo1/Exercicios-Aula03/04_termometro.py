# Leia uma temperatura e mostre apenas uma classificação:

# abaixo de 18: Ambiente frio;
# a partir de 18 e abaixo de 26: Ambiente agradável;
# a partir de 26: Ambiente quente.
# Teste especialmente os valores 18 e 26.

temperatura = float(input("Digite a temperatura: "))

if temperatura <= 18:
    print("Ambiente frio")
elif temperatura >= 18 and temperatura <= 26:
    print("Ambiente Agradável")
else:
    print("Ambiente Quente!")
