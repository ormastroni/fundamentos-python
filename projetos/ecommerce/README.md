# Projeto de um sistema de e-commerce

A figura a seguir apresenta as classes parcialmente projetadas para um sistema de ecommerce. O objetivo da sua equipe de desenvolvimento é implementar todas as classes em Python, incluindo pelo menos dois novos membros privados e seus métodos públicos de acesso para cada classe. Além disso, implemente todos os métodos que já foram definidos na interface das classes:

<img src='https://drive.google.com/uc?id=1FzBSYtWSA7CSe4ZQbvhRoOmMND4Eb3k_'>

- Cliente
> adicionarCartao(p1: string): **p1** é uma string que representa o número do cartão e este método cria um novo objeto CartaoCredito e o guarda na coleção de cartões do cliente (lista cartoes)

- CartaoCredito
> debitar(v: integer): debita o valor **v** do limite do cartão
> estornar(v: integer): estorna o valor **v** do limite do cartão

- Pedido
> faturar(c: CartaoCredito): fatura o valor do pedido no cartão **c**
> cancelar(): cancela o pedido

- Carrinho
> finalizarCompra(): gera o pedido e tenta faturá-lo
> insereProduto(p: Produto, quant: integer): insere o produto **p** na lista de produtos no carrinho em **quant** unidades
> removeProduto(p: Produto, quant: integer): remove **quant** unidade do produto **p** na lista de produtos no carrinho
> esvazia(): esvazia os produtos do carrinho, isto é, remove todos os produtos



