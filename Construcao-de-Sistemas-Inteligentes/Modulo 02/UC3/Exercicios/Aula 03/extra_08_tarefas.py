# Crie a classe Tarefa, recebendo descricao e iniciando concluida com False.

# concluir() muda o estado para True se a tarefa estiver pendente.
# reabrir() muda o estado para False se a tarefa estiver concluída.
# Os dois métodos retornam True quando alteram o estado e False caso contrário.


# Mantenha uma lista de objetos Tarefa e implemente o menu:

# 1 - Cadastrar tarefa
# 2 - Listar tarefas
# 3 - Concluir tarefa
# 4 - Reabrir tarefa
# 5 - Mostrar resumo
# 0 - Sair


# Regras:

# 1. Inicie com uma lista vazia.
# 2. No cadastro, recuse descrição vazia ou exatamente igual à de uma tarefa existente.
# 3. Na listagem, mostre descrição e situação de cada tarefa. Se não houver tarefas, informe isso.
# 4. Nas opções 3 e 4, procure a descrição exata com um for. Informe quando não encontrar a tarefa; quando encontrar, apresente uma mensagem de acordo com o retorno do método.
# 5. No resumo, mostre o total de tarefas, quantas estão pendentes e quantas estão concluídas. Percorra os objetos para calcular as contagens.
# 6. Informe opções desconhecidas e repita o menu até receber 0.



# O menu recebe entradas, procura objetos e apresenta resultados.
# As mudanças entre pendente e concluída ficam nos métodos da classe.


# Roteiro de conferência: liste e consulte o resumo antes de cadastrar qualquer tarefa; 
# cadastre Estudar POO e Revisar listas; tente repetir o primeiro cadastro; 
# conclua Estudar POO duas vezes; procure uma descrição inexistente; 
# reabra a primeira tarefa duas vezes; tente cadastrar "" pressionando apenas Enter; 
# informe uma opção desconhecida e encerre.


# Resultados de referência: após concluir a primeira tarefa, o resumo deve indicar 2 tarefas, 1 pendente e 1 concluída.
# Após reabri-la, deve indicar 2 pendentes e 0 concluídas. 
# Tentativas recusadas não alteram esses totais.

