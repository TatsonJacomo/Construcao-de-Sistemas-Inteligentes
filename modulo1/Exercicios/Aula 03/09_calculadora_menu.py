num1 = int(input("Digite um numero: "))
num2 = int(input("Digite outro numero: "))

 
print("====== Calculadora ======")
print(" Opção 1 - SOMAR")
print(" Opção 2 - SUBTRAIR")
print(" Opção 3 - MULTIPLICAR")
print(" Opção 4 - DIVIDIR")
print("=========================")

opcao = int(input("digite sua opção (1 a 4): "))

if opcao == 1:
    resultado = num1 + num2
    print(f"O resultado da soma e: {resultado}")
elif opcao == 2:
    resultado = num1 - num2
    print(f"O resultado da subtração e: {resultado}")
elif opcao == 3:
    resultado = num1 * num2 
    print(f"O resultado da multiplicação e: {resultado}")
elif opcao == 4:
    if num2 == 0:
        print("Não é possível dividir por zero.")
    else:
        resultado = num1 / num2
        print(f"O resultado da Subtração e: {resultado}")
else:
    print("Opção inválida.")