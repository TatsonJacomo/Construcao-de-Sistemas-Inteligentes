# 13 — Cadastro de uma oficina
# Arquivo: 13_cadastro_oficina.py

# Uma escola oferece uma oficina de robótica. Crie variáveis para armazenar:

# nome da oficina: "Robótica para iniciantes";
# sala: "Laboratório 2";
# quantidade de vagas: 24;
# duração em horas: 2.5;
# inscrições abertas: True.
# Mostre uma ficha com um título e uma informação por linha. Em seguida, mostre o tipo de cada
# variável com type() e escreva comentários explicando o que str, int, float e bool representam nesse cadastro.

nomeOficina = "Robótica para iniciantes"
sala = "Laboratório 2"
vagas = 24
horas = 2.5
inscricao = True


print("========================")
print("Oficina de Robótica")
print("========================")
print(type(nomeOficina))  # str
print(type(sala))         # str
print(type(vagas))        # int
print(type(horas))        # float
print(type(inscricao))    # bool
print("========================")