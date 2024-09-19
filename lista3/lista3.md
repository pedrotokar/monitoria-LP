# Lista de Exercícios 3 - Tratamento de Erros

Objetivo: Revisar testes unitários e assertivas.

Data para entrega: 25/09 23h59.

## Exercício 1 (primeiro e último)
Escrever testes para as funções `len()` e `sorted()` (funções padrão do Python). Os testes devem cobrir cenários com entradas válidas e inválidas.

### 1. Função [`len()`](https://docs.python.org/3/library/functions.html#len) (padrão do Python)

- Escreva testes que verifiquem o comportamento da função `len()` com diferentes tipos de entradas, como listas, strings e dicionários.
- Crie testes para entradas inválidas, como passar um número ou outro tipo que não seja iterável.

### 2. Função [`sorted()`](https://docs.python.org/3/library/functions.html#sorted) (padrão do Python)

- Escreva testes que verifiquem o comportamento da função sorted() com diferentes tipos de listas e strings.
- Teste também se o parâmetro `reverse=True` funciona corretamente.
- Crie testes para entradas inválidas, como passar `None` ou objetos não iteráveis.

## Instruções de entrega:

1. Use um arquivo de teste para cada função:
   - Para a função `len()`, use o arquivo `test_len.py`.
   - Para a função `sorted()`, use o arquivo `test_sorted.py`.

2. Cada arquivo deve conter:
   - *Testes válidos*: Casos em que a função retorna o valor esperado (pelo menos 3).
   - *Testes inválidos*: Casos em que a função lança uma exceção apropriada (pelo menos 2 excessões diferentes).
   - *Teste de exceção*: Valide se a exceção está sendo lançada com a mensagem correta (quando aplicável).

3. Nomeie os testes de forma clara, como `test_len_with_list` ou `test_sorted_with_strings`.
   - Importante: a biblioteca pytest, por padrão, busca apenas por funções com nomes iniciados em `test_`. Por isso, suas funções devem sempre iniciar com esse prefixo.

4. Utilize assert para verificar as saídas dos testes.

---

## Exemplos de Testes:

### Testando a função len():

```python
# test_len.py

def test_len_with_list():
    assert len([1, 2, 3]) == 3

def test_len_with_string():
    assert len("hello") == 5

def test_len_with_invalid_input():
    try:
        len(42)
    except TypeError:
        assert True
    else:
        assert False
