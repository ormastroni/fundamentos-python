# Projetos de desenvolvimento

Os projetos a seguir devem ser desenvolvidos como parte da avaliação do curso

## Projetos coletivos
- Este projeto deve ser feito em grupo para estimular o desenvolvimento em equipe
    - [Bach-end de sistema e-commerce](https://github.com/ormastroni/fundamentos-python/tree/main/projetos/ecommerce)

## Projetos individuais
- Cada aluno deve escolher um dos projetos listados abaixo e implementar as classes sugeridas que abstraem um conjunto mínimo de operações. Faz parte do exercício a definição da classe adequada onde cada operação (método) deve ser implementada.

### Back-end IFood
- Simule a operação do IFood implementando pelo menos 4 membros públicos e privados para as seguintes classes do domínio:
    - Cliente
    - Restaurante
    - Prato
    - Pedido
    - Entregador
- Operações que devem ser implementadas:
    - Cliente faz pedido de pratos a um restaurante
    - Restaurante prepara pedido
    - Restaurante finaliza pedido e chama entregador
    - Entregador faz a entrega do pedido para o cliente

### Back-end Uber
- Simule a operação do Uber implementando pelo menos 4 membros públicos e privados para as seguintes classes do domínio:
    - Passageiro
    - Motorista
    - Viagem
    - MetodoPagamento
        - CartaoCredito
        - Paypal
        - Pix
- Operações que devem ser implementadas:
    - Passageiro define seus métodos de pagamento e escolhe um como default
    - Passageiro solicita uma viagem de um local A para o local B com um método de pagamento
    - Motorista aceita a viagem de um cliente
    - Motorista inicia a viagem de um cliente
    - Motorista finaliza a viagem de um cliente
    - Passageiro avalia motorista na viagem

### Back-end de sistema acadêmico (Moodle)
- Simule a operação do Moodle implementando pelo menos 4 membros públicos e privados para as seguintes classes do domínio:
    - Turma
    - Disciplina
    - Aluno
    - Professor
- Operações que devem ser implementadas:
    - Alunos matriculam-se em turmas
    - Uma turma está associada a uma disciplina lecionada por um professor
    - Professores avaliam AT de alunos nas turmas das disciplinas que lecionam
    - Aluno escolhe um professor orientador
    - CR de um aluno é a média da nota desse aluno em todas as turmas que ele cursou