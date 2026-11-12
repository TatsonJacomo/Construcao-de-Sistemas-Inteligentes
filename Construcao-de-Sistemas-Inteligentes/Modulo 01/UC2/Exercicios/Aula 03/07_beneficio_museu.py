# Leia uma idade não negativa. 
# Neste museu fictício, pessoas com menos de 12 anos ou a partir de 60 anos têm entrada gratuita.
#  As demais pagam R$ 20.00.

# Use or e teste as idades 11, 12, 59 e 60.

idade = int(input("Digite sua idade: "))

if idade < 12 or idade > 60:
    print("Entrada Gratuita!")
else:
    print("Entrada R$20.00")