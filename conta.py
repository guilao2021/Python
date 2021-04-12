class Conta:

    def __init__(self, numero, titular, saldo, limite):

        print("Construindo objeto...{}".format(self))

        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        self.__tarifa = 5.0

    def extrato(self):
        print("O saldo do {} é de R$ {} !".format(self.__titular, self.__saldo))

    def deposita(self, valor):
        self.__saldo += valor

    def __pode_sacar(self, valor):
        valor_disponivel = self.__saldo + self.__limite
        return valor <= valor_disponivel

    def saca(self, valor):
        if self.__pode_sacar(valor):
            self.__saldo -= valor
        else:
            print("O valor de R$ {} ultrapassa o seu limite máximo.".format(valor))

    def __pode_transferir(self, valor):
        total_transferencia = valor + self.__tarifa
        return self.__saldo >= total_transferencia

    def transfere(self, valor, destino):
        if self.__pode_transferir(valor):
            valor = valor + self.__tarifa
            self.saca(valor)
            destino.deposita(valor)
            print("Transferência de R$ {} realizada.".format(valor))
        else:
            print("Saldo insuficiente.")

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, novo_limite):
        self.__limite = novo_limite

    @staticmethod
    def codigo_banco():
        return '001'

    @staticmethod
    def codigos_bancos():
        return {'BB': '001', 'Caixa': '104', 'Bradesco': '237'}
