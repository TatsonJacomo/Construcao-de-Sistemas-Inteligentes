# A equipe dispõe de tempo limitado para analisar uma mensagem. As prioridades abaixo são regras fictícias para praticar decisões em Python.

# Recebam pelo teclado:

# a identificação da mensagem;
# o tempo disponível, em minutos, como decimal;
# o tempo necessário, em minutos, como decimal;
# a resposta à pergunta A mensagem indica risco imediato? (sim/nao):;
# a resposta à pergunta A mensagem contém uma pista recorrente? (sim/nao):.

# Regras de validação:

# Os dois tempos devem ser maiores que zero. Usem or para detectar um tempo inválido e mostrem Tempo inválido.
# As duas respostas devem ser exatamente sim ou nao. Se alguma não for, mostrem Resposta inválida.
# Não classifiquem a mensagem quando houver dados inválidos. Se houver erro nos tempos e nas respostas ao mesmo tempo, a mensagem de tempo inválido tem prioridade.


#  Com dados válidos, escolham apenas um resultado, nesta ordem:

#|         Condição	                                                        |       Resultado                       |
#| Tempo necessário maior que o disponível	                                |   Solicitar apoio: tempo insuficiente |
#| Há tempo suficiente e existe risco imediato                              |   Prioridade máxima                   |
#| Há tempo suficiente, não existe risco imediato e existe pista recorrente	|   Prioridade alta                     |
#| Há tempo suficiente e nenhuma das duas indicações está presente          |	Prioridade normal                   |

# Mostrem a identificação da mensagem e o resultado. Quando houver tempo suficiente, calculem e mostrem também quantos minutos restarão depois da análise.

# Atenção ao limite: se o tempo necessário for igual ao disponível, a análise cabe no prazo e o tempo restante será zero.

# Para explicar: se há risco imediato, mas falta tempo, qual resultado aparece? Justifiquem com a ordem das condições e discutam por que um programa real precisaria de regras definidas por pessoas responsáveis por esse contexto.


# Parte 2 — Teste de mesa e execução

# Antes de executar, preencham o resultado esperado para cada caso.
# Depois executem o programa, registrem a saída obtida e indiquem se ela corresponde à previsão. 
# Se houver diferença, expliquem a correção feita.


# Casos obrigatórios da missão 1


# Usem um nome e uma identificação de sua escolha.


# Analista escolhido: Ana; identificação: MSG-TESTE.
#| Grupos | Minutos por grupo | Resultado esperado       | Saída obtida             |
#| 10     | 5.0               | Análise dentro do prazo  | Análise dentro do prazo  |
#| 12     | 5.0               | Análise dentro do prazo  | Análise dentro do prazo  |
#| 13     | 5.0               | Reorganizar o trabalho   | Reorganizar o trabalho   |
#| 0      | 5.0               | Dados inválidos          | Dados inválidos          |
#| 10     | -1.0              | Dados inválidos          | Dados inválidos          |
#| 8      | 7.5               | Análise dentro do prazo  | Análise dentro do prazo  |
#
# Caso criado: 8 grupos a 7.5 minutos verificam o limite de 60 minutos
# com um tempo por grupo decimal.



# Casos obrigatórios da missão 2


# Usem uma identificação de sua escolha.

#| Disponível | Necessário | Risco  | Pista | Resultado esperado                      | Saída obtida                             |
#| 60         | 60         | sim    | sim   | Prioridade máxima; restam 0 min         | Prioridade máxima; restam 0 min          |
#| 60         | 61         | sim    | sim   | Solicitar apoio: tempo insuficiente     | Solicitar apoio: tempo insuficiente      |
#| 60         | 30         | nao    | sim   | Prioridade alta; restam 30 min          | Prioridade alta; restam 30 min           |
#| 60         | 30         | nao    | nao   | Prioridade normal; restam 30 min        | Prioridade normal; restam 30 min         |
#| 60         | 30         | sim    | nao   | Prioridade máxima; restam 30 min        | Prioridade máxima; restam 30 min         |
#| 0          | 30         | nao    | nao   | Tempo inválido                          | Tempo inválido                           |
#| 60         | 30         | talvez | nao   | Resposta inválida                       | Resposta inválida                        |
#| -1         | 30         | talvez | nao   | Tempo inválido                          | Tempo inválido                           |
#| 45         | 45         | nao    | sim   | Prioridade alta; restam 0 min           | Prioridade alta; restam 0 min            |
#
# Caso criado: 45 minutos disponíveis e necessários verificam igualdade
# entre os tempos, restante zero e a classificação por pista recorrente.


# Acrescentem pelo menos um caso criado pela dupla para cada missão e expliquem o que ele verifica.


# Parte 3 — Reflexão individual

# Cada integrante deve escrever um parágrafo de 5 a 8 linhas respondendo:

# Como o filme e os programas desta atividade ajudam a compreender a relação entre regras, testes e decisões humanas? 
# Cite uma condição do seu código e explique um limite da simulação.

# Reflexão individual:
# As atividades mostram que um programa transforma regras definidas por pessoas
# em decisões que podem ser repetidas de maneira consistente. No código, a
# condição tempo_necessario > tempo_disponivel leva a solicitar apoio antes de
# verificar risco ou pista recorrente. Os testes ajudam a conferir essa ordem,
# inclusive nos limites em que os tempos são iguais ou inválidos. Porém, a
# simulação não compreende o contexto nem avalia a gravidade real de uma mensagem.
# Por isso, as regras devem ser definidas e revisadas por pessoas responsáveis.

identificacao = input("Identificação da mensagem: ")

try:
    tempo_disponivel = float(input("Tempo disponível (em minutos): "))
except ValueError:
    tempo_disponivel = None

try:
    tempo_necessario = float(input("Tempo necessário (em minutos): "))
except ValueError:
    tempo_necessario = None

risco_imediato = input("A mensagem indica risco imediato? (sim/nao): ")
pista_recorrente = input("A mensagem contém uma pista recorrente? (sim/nao): ")

print(f"\nIdentificação da mensagem: {identificacao}")

if (tempo_disponivel is None
    or tempo_necessario is None
    or tempo_disponivel <= 0
    or tempo_necessario <= 0
):
    print("Resultado: Tempo inválido")
elif risco_imediato not in ("sim", "nao") or pista_recorrente not in ("sim", "nao"):
    print("Resultado: Resposta inválida")
else:
    if tempo_necessario > tempo_disponivel:
        resultado = "Solicitar apoio: tempo insuficiente"
    elif risco_imediato == "sim":
        resultado = "Prioridade máxima"
    elif pista_recorrente == "sim":
        resultado = "Prioridade alta"
    else:
        resultado = "Prioridade normal"

    print(f"Resultado: {resultado}")

    if tempo_necessario <= tempo_disponivel:
        tempo_restante = tempo_disponivel - tempo_necessario
        print(f"Tempo restante: {tempo_restante:.1f} minutos")

# Se há risco imediato, mas falta tempo, aparece "Solicitar apoio: tempo
# insuficiente". Essa condição é verificada primeiro e encerra a classificação,
# portanto o risco não substitui a necessidade de apoio. Em um sistema real,
# a ordem das regras deve ser definida e revisada pelas pessoas responsáveis,
# considerando o contexto, os objetivos e as consequências das decisões.