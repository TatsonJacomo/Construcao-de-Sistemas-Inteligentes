# Crie a classe Conta, recebendo apenas titular. O saldo inicial deve ser zero.

# Implemente:

# depositar(valor): aceita somente valores positivos;
# sacar(valor): aceita somente valores positivos e menores ou iguais ao saldo;
# ambos os métodos retornam True quando realizam a operação e False quando a recusam, preservando o saldo em caso de recusa.

# Crie duas contas independentes. Na primeira, deposite 50, saque 20, tente sacar 40 e tente depositar -10. A segunda deve permanecer com saldo zero.

# Conferência: saldo final da primeira conta 30; retornos True, True, False, False.


class Conta:
    def __init__(self, titular):
        self.titular = titular
        self.saldo = 0

        def depositar(self, valor):
            if valor <= 0:
                return False
            self.saldo += valor
            return True
        