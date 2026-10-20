# Crie uma loja com atendimento de uma única compra por execução.

# Leia o nome do aventureiro e sua quantidade de ouro, como número inteiro.
# Se o ouro for negativo, mostre Quantidade de ouro inválida e não prossiga com a compra.
# Caso contrário, mostre um menu: 1 para poção de vida (25 moedas), 2 para escudo (60 moedas) e 3 para espada (100 moedas).
# Leia a opção como texto e verifique se ela existe.
# Para uma opção válida, verifique se o ouro é suficiente. Se for, desconte o preço e mostre o item adquirido e o saldo restante. Caso contrário, informe quantas moedas faltam.
# Se a opção não existir, mostre Item inválido.
# O ouro só pode ser descontado quando a compra for confirmada. Teste uma compra com sobra de ouro, uma com o valor exato, outra com saldo insuficiente, uma opção inválida e um saldo inicial negativo.


nome = input("Digite o nome do aventureiro: ")
ouro = int(input("Digite a quantidade de ouro: "))

if ouro < 0:
    print("Quantidade de ouro inválida.")
else:
    print(f"\nSeja bem-vindo à loja, {nome}!")
    print("--- MENU DA LOJA ---")
    print("1 - Poção de vida (25 moedas)")
    print("2 - Escudo (60 moedas)")
    print("3 - Espada (100 moedas)")
    
    opcao = input("Escolha o item desejado (1, 2 ou 3): ")
    
    preco = 0
    nome_item = ""
    opcao_valida = True
    
    if opcao == "1":
        preco = 25
        nome_item = "Poção de vida"
    elif opcao == "2":
        preco = 60
        nome_item = "Escudo"
    elif opcao == "3":
        preco = 100
        nome_item = "Espada"
    else:
        opcao_valida = False
        print("Item inválido.")

        
    if opcao_valida:
        if ouro >= preco:
            ouro -= preco
            print(f"Compra confirmada! Você adquiriu: {nome_item}.")
            print(f"Saldo restante de ouro: {ouro} moedas.")
        else:
            faltam = preco - ouro
            print(f"Saldo insuficiente. Faltam {faltam} moedas para comprar {nome_item}.")