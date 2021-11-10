class Pedido:

  def __init__(self, cliente, livro, quantidade=1):
    self._cliente = cliente
    self._livro = livro
    self._quant = quantidade

  def quemFez(self):
    return self._cliente

  def livro(self):
    return self._livro

  def total(self):
    preco_livro = self.livro().getPreco()
    return self._quant*preco_livro

  def efetiva(self):
    # Este método validar se o pedido pode ser efetivado ou não
    # Testar se a quantidade do pedido é inferior ao estoque do Livro

    if (self._quant <= self.livro().getEstoque()):
      resto = self.livro().getEstoque() - self._quant
      self.livro().atualizaEstoque(resto)
      return True
    return False