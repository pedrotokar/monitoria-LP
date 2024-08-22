# Lista 1 - Linguagens de programação

Objetivos: revisar laços de repetição, condicionais e funções.

## Exercício 1

Seja $p$ o perimetro de um triângulo retângulo com lados $\\{a, b, c\\}$
($a, b, c$ são números naturais). Se definimos $p = 120$, teremos três possíveis
triângulos retângulos com perímetro $p$: $\\{20, 48, 52\\}, \\{24, 45, 51\\}, \\{30, 40, 50\\}$.

Escreva uma função que receba um inteiro $n$ e retorne um inteiro representando
qual valor de $p \leq n$ temos o maior número de triângulos possível. Se mais de
um valor de $p$ for adequado, a função deve retornar o menor deles.

Se a entrada da função não for um número inteiro, ela deverá imprimir uma mensagem
avisando que só recebe inteiros e retornar `None`.

## Exercício 2

Escreva uma função que receba dois números naturais não nulos $m, n$, que seguem
duas restrições: $m < n$ e $m$ e $n$ devem ser primos entre si. A função deve
retornar uma matriz $n \times n$ preenchida com os números naturais de 1 a $n^2$.

O preenchimento deve ser realizado no sentido horizontal, mas seguindo uma regra
especial: a inserção dos números deve ser feita em passos de $m$ em $m$ casas.
Caso $m$ e $n$ não atendam os requisitos, a função deve imprimir uma mensagem avisando
do problema e retornar `None`.

Exemplo de retorno para $m = 2$ e $n = 3$:
```python
[[1 6 2],
 [7 3 8],
 [4 9 5]]
```

Exemplo de retorno para $m = 3$ e $n = 5$:
```python
[[1  18 10 2  19],
 [11 3  20 12 4 ],
 [21 13 5  22 14],
 [6  23 15 7  24],
 [16 8  25 17 9 ]]
```

## Exercício 3

Construa uma função que receba dois retângulos e retorne um booleano indicando
se eles colidem. Um retângulo é representado como uma tupla de 4 elementos, cada
um sendo um dos vértices do retângulo, iniciando do superior esquerdo e
avançando em sentido horário. Cada vértice é representado como uma tupla, contendo
coordenadas x e y do plano cartesiano.

Considere que os retângulos não são rotacionados (isto é, as arestas são
paralelas aos eixos) e que dois retângulos colidem se um dos vértices de um
deles está contido no conjunto **fechado** delimitado pelo outro retângulo.

Se um dos retẫngulos estiver representado incorretamente, a função deverá retornar
`None` e mostrar uma mensagem indicando o problema com o input.

## Exercício 4

Agora generalize o problema, com uma função que receba um número qualquer de
retângulos, por meio de argumentos nomeados `(**kwargs)`, e retorne uma lista com
tuplas. Cada tupla deve ter dois elementos, que equivalem a um par de retângulos que
colidem (os nomes dos argumentos devem ser usados para representar um retângulo).
A ordenação dos retângulos de uma tupla deve seguir a ordenação passada na função.

Se nenhum retângulo colidir, ou se nenhum ou apenas um retângulo for passado
para a função, ela devera retornar uma lista vazia.
