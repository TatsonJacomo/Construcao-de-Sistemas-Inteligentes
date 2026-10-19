# Leia o preço de um lanche e a quantidade comprada. Calcule o total. 
# Considere preço e quantidade positivos. 
# Se o total for a partir de R$ 50.00, aplique 10% de desconto; caso contrário, mantenha o valor original.
# Mostre o total antes do desconto, o desconto e o valor final. Para calcular 10%, multiplique o total por 0.10.
#  Teste totais abaixo de 50, iguais a 50 e acima de 50.


preco = float(input("Qual preço do lanche? "))
quantidade = int(input("Você comprou quantos? "))
total = preco * quantidade

print("Total da compra: ", total)

if total >= 50.00:
    desconto = total * 0.10
else:
    desconto = 0.00

valorFinal = total - desconto


valorfinal = total - desconto

print(f"\nTotal antes do desconto: R$ {total:.2f}")
print(f"Desconto: R$ {desconto:.2f}")
print(f"Valor final: R$ {valorFinal:.2f}")