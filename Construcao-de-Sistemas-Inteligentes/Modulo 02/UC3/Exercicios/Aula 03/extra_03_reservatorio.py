# Crie a classe Reservatorio, recebendo capacidade e iniciando nivel com zero.
# Considere a capacidade positiva e todas as medidas em litros inteiros.

# Implemente:

# adicionar(litros): aceita uma quantidade positiva apenas se ela couber integralmente no reservatório;
# retirar(litros): aceita uma quantidade positiva apenas se houver água suficiente;
# espaco_disponivel(): retorna a diferença entre a capacidade e o nível atual.


# Os dois primeiros métodos devem retornar booleanos. Não aceite uma operação parcialmente: se alguém tentar adicionar mais água do que cabe, recuse toda a quantidade.

# Crie um reservatório de capacidade 100 e execute as operações abaixo em sequência. Complete a tabela antes de rodar o programa.


#|  Operação	    |    Retorno previsto	|  Nível depois |
#| adicionar(60)	|	                    |               |
#| adicionar(50)	|	                    |               |
#| retirar(20)		|                       |               |
#| adicionar(60)	|	                    |               |
#| retirar(100)		|                       |               |
#| retirar(1)		|                       |               |
#| adicionar(0)		|                       |               |


# Conferência final: nível 0 e espaço disponível 100. Teste também uma retirada negativa e a adição exata da capacidade em um reservatório vazio.

