# Leia a idade e pergunte se a pessoa possui inscrição (sim/nao).
#  Considere idade não negativa e uma das duas respostas indicadas.
#  A entrada só será permitida para quem tiver pelo menos 14 anos e inscrição confirmada.

# Use and. 
# Teste uma pessoa que atende aos dois critérios,
#  outra que atende a apenas um e outra que não atende a nenhum.


idade = int(input("Digite sua idade: "))
inscricao = str(input("Possui inscriçrão? (sim/nao) "))

if idade >= 14 and inscricao == "sim":
    print("Incrição Confirmada")
else:
    print("Incrição não permitida!")
