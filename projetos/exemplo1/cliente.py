class Cliente:
  def __init__(self, nome, cpf, idade):
    self._nome = nome
    self._cpf = cpf
    self._idade = idade
    self._vip = False

  def getNome(self):
    return self._nome

  def getCPF(self):
    return self._cpf

  def getIdade(self):
    return self._idade

  def eh_vip(self):
    return self._vip

  def ganha_vip(self):
    self._vip = True

  def perde_vip(self):
    self._vip = False