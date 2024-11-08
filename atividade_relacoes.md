# Atividade - 09/11

Objetivo: implementar classes que modelem um dado problema. Implementar herança entre
classes. Implementar três tipos de relacionamentos entre classes: Associação,
Composição e Agregação. Se não se lembrar o que são essas relações,
[consulte essa explicação.](https://github.com/matwerner/fgv-lp/blob/master/aulas/Semana%2011%20-%20Classes/35_classes_associacao_agregacao_composicao.md).

Entrega: deverá ser criado um repositório no GitHub contendo os arquivos resultantes
da atividade, na conta do aluno. Enviar o link do repositório, nome e matrícula
para pedrotokar2004@gmail.com com o assunto "Atividade LP 0911". **Prazo: 10/11 23h59**

OBS: não é necessário fazer documentação, mas é importante comentar o motivo das
suas escolhas para implementação. É necessário ter pelo menos um driver code que
teste as funcionalidades implementadas.

## Enunciado

Você deve modelar um sistema para uma franquia de loja de instrumentos que vende
três tipos de instrumentos: baixos, guitarras e violões. Esse sistema será feito
em Python e usará classes para representar as principais entidades relacionadas
à empresa.

A primeira entidade são as lojas. Como se espera de uma franquia, existem várias
filiais diferentes espalhadas pelo mundo. O sistema deve ser capaz de manter
registro de todas as filiais existentes, e das seguintes infomações sobre elas:

- Localização;
- Quadro de funcionários (quais funcionários tem na loja);
- Estoque (quantos e quais instrumentos estão no estoque da loja).

Além de registrar essas informações, é preciso que um usuário do sistema possa:

- Mudar o quadro de funcionarios (colocar ou tirar um funcionario);
- Mudar o estoque (colocar ou retirar um instrumento);
- Consultar quantos instrumentos de cada tipo tem disponíveis na loja;
- Consultar quantos funcionários de cada cargo estão alocados na loja.

(Para o quadro de funcionários e estoque, não necessariamente precisa ser capaz
de remover um objeto especifico. Pode remover qualquer um arbitrariamente, para
simplificar)
Por último, as lojas podem armazenar qual a outra loja que é mais perto delas.

A segunda entidade são os funcionários. O sistema precisa manter registro das
seguintes informações deles:

- Nome completo;
- Documento (CPF);
- Salário;
- Cargo;
- Loja atual.

É importante ter em mente que os funcionários podem ser remanejados entre as lojas,
ou seja, continuam existindo independente da loja. Além disso, é importante notar
que existe uma hierarquia fixa de cargos na franquia, ou seja, existe um conjunto
fixo de cargos que um funcionário pode ter (e cada funcionário tem apenas um cargo)

A última entidade são os instrumentos. Como dito acima, as lojas vendem três tipos de
instrumentos: guitarras, baixos e violões. O sistema precisa manter as seguintes
informações para todos os instrumentos:

- Marca;
- Modelo;
- Preço;
- Número de cordas.

Além disso, instrumentos diferentes podem ter peculiaridades e informações a
serem armazenadas diferentes (use sua criatividade e conhecimento de música).

É importante ter em mente que os instrumentos nunca são remanejados: um instrumento
existe exclusivamente em uma loja, e não é transferido para outra. Devido a essa
natureza, não existem instrumentos que não são associados a nenhuma loja. Logo,
se uma loja deixa de existir, os instrumentos também deixam (são doados para caridade).

Agora, você tem informações o suficiente para implementar o sistema da loja. Antes
de começar, pense bem nos tipos de relação que existem entre cada classe.
