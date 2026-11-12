# Crie a classe Conta, recebendo apenas titular. O saldo inicial deve ser zero.

# Implemente:

# depositar(valor): aceita somente valores positivos;
# sacar(valor): aceita somente valores positivos e menores ou iguais ao saldo;
# ambos os métodos retornam True quando realizam a operação e False quando a recusam, preservando o saldo em caso de recusa.

# Crie duas contas independentes. Na primeira, deposite 50, saque 20, tente sacar 40 e tente depositar -10. A segunda deve permanecer com saldo zero.

# Conferência: saldo final da primeira conta 30; retornos True, True, False, False.


# class Conta:
#     def __init__(self, titular):
#         self.titular = titular
#         self.saldo = 0

#     def depositar(self, valor):
#         if valor <= 0:
#             return False
#         self.saldo += valor
#         return True

#     def sacar(self, valor):
#         if valor <= 0 or valor > self.saldo:
#             return False
#         self.saldo -= valor
#         return True


# conta1 = Conta("Ana")
# conta2 = Conta("Bruno")

# resultado = conta1.depositar(50)
# print(f"\nDepósito 1: retorno = {resultado}, saldo = {conta1.saldo}, saldo2 = {conta2.saldo}\n")

# resultado = conta1.sacar(20)
# print(f"Saque 1: retorno = {resultado}, saldo = {conta1.saldo}, saldo2 = {conta2.saldo}")

# resultado = conta1.sacar(40)
# print(f"Saque 2: retorno = {resultado}, saldo = {conta1.saldo}, saldo2 = {conta2.saldo}\n")

# resultado = conta1.depositar(-10)
# print(f"Depósito 2: retorno = {resultado}, saldo = {conta1.saldo}, saldo2 = {conta2.saldo}\n")

# print(f"Saldo final da conta 1: {conta1.saldo}")
# print(f"Saldo final da conta 2: {conta2.saldo}\n")



class Conta:
    def __init__(self, titular):
        self.titular = titular
        self.saldo = 0

    def depositar(self, valor):
        if valor <= 0:
            return False

        self.saldo = self.saldo + valor
        return True

    def sacar(self, valor):
        if valor <= 0 or valor > self.saldo:
            return False

        self.saldo = self.saldo - valor
        return True


conta1 = Conta("Ana")
conta2 = Conta("Carlos")

# Operações na primeira conta
resultado1 = conta1.depositar(50)
resultado2 = conta1.sacar(20)
resultado3 = conta1.sacar(40)
resultado4 = conta1.depositar(-10)

print("RESULTADO DAS OPERAÇÕES")
print("------------------------")

print("Depósito de 50:", resultado1)
print("Saque de 20:", resultado2)
print("Saque de 40:", resultado3)
print("Depósito de -10:", resultado4)

print("\nSALDOS FINAIS")
print("Conta de", conta1.titular, ":", conta1.saldo)
print("Conta de", conta2.titular, ":", conta2.saldo)