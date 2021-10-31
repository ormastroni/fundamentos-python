# Projeto de um sistema de e-commerce

A figura a seguir apresenta o diagrama de classes projetado para um sistema de ecommerce. O objetivo da sua equipe de desenvolvimento é implementar todas as classes em Python, incluindo pelo menos dois novos membros privados e seus métodos públicos de acesso para cada classe (use a criatividade). Além disso, implemente também todos os métodos que já estão definidos na interface das classes:

<img src='https://drive.google.com/uc?id=1FzBSYtWSA7CSe4ZQbvhRoOmMND4Eb3k_'>

## Cliente
- adicionarCartao(p1: string): **p1** é uma string que representa o número do cartão e este método cria um novo objeto CartaoCredito e o guarda na coleção de cartões do cliente (lista cartoes)

## CartaoCredito
- debitar(v: integer): debita o valor **v** do limite do cartão
- estornar(v: integer): estorna o valor **v** do limite do cartão

## Pedido
- faturar(c: CartaoCredito): fatura o valor do pedido no cartão **c**
- cancelar(): cancela o pedido

## Carrinho
- finalizarCompra(): gera o pedido e tenta faturá-lo
- insereProduto(p: Produto, quant: integer): insere o produto **p** na lista de produtos no carrinho em **quant** unidades
- removeProduto(p: Produto, quant: integer): remove **quant** unidade do produto **p** na lista de produtos no carrinho
- esvazia(): esvazia os produtos do carrinho, isto é, remove todos os produtos

### Observações
- O trabalho pode ser feito individualmente. Neste caso, o trabalho vai render um bônus na sua avaliação do AT
- A turma pode também se dividir em grupos para a implementação do projeto como um time de desenvolvimento. Neste caso, sugiro a seguinte configuração:

| Grupos              | Escopo de trabalho      |
|---------------------|-------------------------|
| Grupo cliente       | Cliente e Carrinho      |
| Grupo produto       | Produto, Livro e Game   |
| Grupo pagamento     | Pedido e CartaoCredito  |
| Grupo de integração | Testar tudo funcionando |

- Os grupos devem se comunicar para combinarem as interfaces públicas de cada classe
- A responsabilidade de cada grupo é deixar a sua parte (escopo de trabalho) funcionando
- A responsabilidade do grupo de integração é garantir que as partes de todos os grupos funcionem corretamente juntas
- O grupo de integração deve mostrar um programa que reutilize o código dos outros grupos para a seguinte sequencia de operações:
  - Criação de 3 clientes onde um deles tem 2 cartões de crédito, enquanto os demais apenas um. Os limites dos 4 cartões devem ser diferentes
  - Criação de 4 produtos: 2 livros e 2 games
  - O cliente com dois cartões faz 2 pedidos: um com um livro e um game, e outro com 2 livros
  - Os outros clientes devem fazer 1 pedido cada com 1 livro ou 1 game
  - Mostre um cenário onde o pedido de um dos clientes não é efetivado por falta de limite no cartão
  - Mostre um cenário onde o pedido de um dos clientes não é efetivado por falta do produto no estoque
- Caso você precise de algum ajuste no modelo, solicite ao professor a mudança

## Prazo: 06/12



