# Lista 2 - Linguagens de programação

Objetivos: revisar tratamento de erros.

Entrega: crie um arquivo `respostas.py` na pasta raiz do repositório, contendo as
funções relativas aos dois primeiros exercícios. A função relativa ao exercício
um deverá se chamar `exercicio1` e a relativa ao exercício dois deverá se chamar
`exercicio2`. O arquivo criado para o exercício 3 deverá estar na raiz do
respositório. O prazo de entrega é dia ??/??, 23h59.

## Exercício 1: Validação de Entrada e Cálculo de Norma Vetorial

Implemente uma função em Python que receba como entrada um vetor (tupla de
números) e calcule a norma Euclidiana desse vetor. A função deve realizar
validações básicas de entrada para garantir que o vetor contém apenas números.
Se a entrada for inválida, a função deve levantar uma exceção apropriada.

### Passos:
1. *Função para cálculo da norma:*
    - Implemente uma função chamada exercicio1(vetor) que calcule e retorne
    a norma Euclidiana do vetor, definida como
    $ \| \mathbf{v} \| = \sqrt{\sum_{i=1}^n v_i^2} $.

2. *Validação da entrada:*
    - A função deve verificar se a entrada é uma lista de números (int ou float).
    - Se a entrada não for uma lista, ou se algum elemento da lista não for
    numérico, a função deve levantar uma exceção do tipo TypeError ou
    ValueError com uma mensagem apropriada.

## *Exercício 2: Determinação da Equação da Reta*

Dado dois pontos $ P_1 = (x_1, y_1) $ e $ P_2 = (x_2, y_2) $ no plano
cartesiano, implemente uma função em Python que calcule e retorne a equação da
reta que passa por esses dois pontos na forma geral $ y = ax + b $.

### *Passos:*
1. *Entrada dos Pontos:*
    - A função exercicio2(ponto1, ponto2) deve receber dois parâmetros, ponto1 e
    ponto2, que são tuplas representando as coordenadas dos pontos $ P_1 $ e
    $ P_2 $, respectivamente.

2. *Validação da entrada:*
    - A função deve verificar se os pontos de entrada são tuplas de tamanho 2,
    contendo números (int ou float).
    - Se a entrada não for válida, a função deve levantar uma exceção do tipo
    TypeError ou ValueError com uma mensagem apropriada.
    - Existem outros erros a serem tratados? Se sim, trate-os!

3. *Saída da função:*
   - A função deve retornar uma tupla (a, b) contendo os coeficientes da equação
   da reta.

## *Exercício 3: Tratamento de erros em função externa*

Você está desenvolvendo uma interface em terminal para ler arquivos JSON, com a
ajuda de um módulo externo que implementa uma função para ler um arquivo JSON
(que vida fácil!). Na sua interface, um usuário deverá inserir de input o nome
de um arquivo, e eses input é usado pela função para retornar um dicionário
com os conteúdos do arquivo.

Como é de conhecimento geral, usuários costumam usar os programas da pior forma
possível, e você sabe que a função pode dar alguns erros. Então, você deve tratar
esses erros, usando `try`, `except` e `else`, e exibindo mensagens pertinentes
para os possíveis erros que um usuário pode cometer.

### *Passos:*
1. *Elaboração inicial do script:*
    - Crie um arquivo `leitor_json.py`, que deve importar o arquivo `modulo.py`,
    coletar um input do usuário e usá-lo na função `carrega_conteudos_json`, que
    retorna um dicionário.
    - Esse dicionário deverá ser exibido ao usuário (opcionalmente com o módulo
    `pprint`).

2. *Tratamento de exceções:*
    - Com a ajuda de um bloco `try` `except`, o seu código deverá ser capaz de
    mostrar mensagens informativas ao usuário para caso a entrada dele faça a
    função levantar uma exceção. A documentação da função lista quais exceções
    ela pode levantar.
    - O script deverá pedir outro input depois de mostrar a mensagem de erro,
    até ter sucesso ou ser interrompido (por um ctrl+C)
