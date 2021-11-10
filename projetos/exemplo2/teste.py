from infnet_bank import Cliente, Conta, Agencia, Banco

b1 = Banco('Santander')
b1.criaAgencia(1, 'Centro')
b1.criaAgencia(2, 'Tijuca')

c1 = Cliente('Maria', '111', 'maria@')

ag_tijuca = b1.getAgencia(2)
print(ag_tijuca.getNome())
print(ag_tijuca.getNumero())
print(ag_tijuca.getBanco().getNome())
conta_c1 = ag_tijuca.abreConta(c1, 123)

print(conta_c1.getCliente().getNome())
print(conta_c1.getSaldo())

conta_c1.deposita(100)
print(conta_c1.getSaldo())
