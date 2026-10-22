# Exercício 06 — Controle de acesso a um laboratório

# Intermediário

# Um laboratório de tecnologia possui equipamentos que só podem ser utilizados por pessoas autorizadas.

# Solicite:
# Idade.
# Se a pessoa é aluno matriculado (sim ou nao).
# Se possui autorização do professor (sim ou nao).
# Se o laboratório está disponível (sim ou nao).

# O acesso será permitido quando:
# O laboratório estiver disponível.
# A pessoa tiver pelo menos 16 anos.
# A pessoa for matriculada ou possuir autorização do professor.

# Requisitos: Utilize and e or e apresente uma mensagem indicando se o acesso foi permitido ou negado.

idade = int(input("Digite a idade: "))
aluno_matriculado = input("É aluno matriculado? (sim/nao): ").strip().lower()
autorizacao_professor = input("Possui autorização do professor? (sim/nao): ").strip().lower()
laboratorio_disponivel = input("O laboratório está disponível? (sim/nao): ").strip().lower()

permitido = (
    laboratorio_disponivel == "sim"
    and idade >= 16
    and (aluno_matriculado == "sim" or autorizacao_professor == "sim")
)

if permitido:
    print("Acesso permitido.")
else:
    print("Acesso negado.")


