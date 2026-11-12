
# Leia duas notas de mesmo peso.
#  Se alguma nota estiver fora da faixa de 0 a 10, mostre Nota inválida e não calcule a média.
#  Caso ambas sejam válidas, calcule e mostre a média e a situação:

# média a partir de 7: aprovado;
# média a partir de 5 e abaixo de 7: recuperação;
# média abaixo de 5: reprovado.

nota1 = float(input("Digite uma nota entre 0 e 10:"))
nota2 = float(input("Digite outra nota entre 0 e 10:"))

if nota1 < 0 or nota1 > 10 or nota2 < 0 and nota2 > 10:
    print("Nota Inválida")
else: 
    media = (nota1 + nota2) / 2
    print(f"Media: {media}")
    if media >= 7:
        print("Aprovado")
    elif media >= 5:
        print("Recuperação")
    else:
        print("Reprovado")
