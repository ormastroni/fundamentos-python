class Agencia:
    def __init__(self, banco, numero, nome):
        self._numero = numero
        self._nome = nome
        self._banco = banco
        self._contas = []

    def getNumero(self):
        return self._numero
    
    def getNome(self):
        return self._nome

    def getBanco(self):
        return self._banco

    def abreConta(self, cliente, numero):
        conta = Conta(numero, cliente, self)
        self._contas.append(conta)
        return conta

class Conta:
    def __init__(self, numero, cliente, agencia):
        self._agencia = agencia
        self._cliente = cliente
        self._numero = numero
        self._saldo = 0

    def getAgencia(self):
        return self._agencia

    def getCliente(self):
        return self._cliente

    def deposita(self, valor):
        self._saldo += valor

    def saca(self, valor):
        self._saldo -= valor

    def getSaldo(self):
        return self._saldo

class Banco:
    def __init__(self, nome):
        self._nome = nome
        self._agencias = []

    def criaAgencia(self, numero, nome):
        ag = Agencia(self, numero, nome)
        self._agencias.append(ag)

    def getNome(self):
        return self._nome

    def getAgencias(self):
        return self._agencias

    def getAgencia(self, numero):
        for ag in self._agencias:
            if numero == ag.getNumero():
                return ag
        return None

class Cliente:

    def __init__(self, nome, cpf, email):
        self._nome = nome
        self._cpf = cpf
        self._email = email
    
    def getNome(self):
        return self._nome