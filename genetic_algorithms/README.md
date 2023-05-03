# Atividade Algoritmos Genéticos

Os códigos foram criados se baseando no [código criado em sala](./algoritmo_exemplo.ipynb).

## Problemas

### Problema das N-rainhas

O problema das N-rainhas consiste em encontrar todas as combinações possíveis de N rainhas num tabuleiro de dimensão N por N tal que nenhuma das rainhas ataque qualquer outra. Duas rainhas atacam-se uma à outra quando estão na mesma linha, na mesma coluna ou na mesma diagonal do tabuleiro. Nesta tarefa você solucionar o problema das n-rainhas utilizando um algoritmo genético.

[Resposta](./n_rainhas.py)

### Problema da Mochila 0-1

No problema da mochila 0-1, recebemos um conjunto de itens, cada um com um peso e um valor, e precisamos determinar o número de cada item a ser incluído em uma coleção de modo que o peso total seja menor ou igual a um determinado limite e o valor total é o maior possível. Nesta tarefa você deve solucionar este problema utilizando um algoritmo genético.

Para ilustrar este problema, imagine a situação hipotética. Um ladrão entra em uma loja carregando uma mochila (bolsa) que pode carregar 35 kg de peso. A loja possui 10 itens, cada um com peso e preço específicos. Agora, o dilema do ladrão é fazer uma seleção de itens que maximize o valor (ou seja, o preço total) sem exceder o peso da mochila. Temos que ajudar o ladrão a fazer a seleção.

> Como eu não ajudo ladrão, no código o cenário foi mudado para um rapaz que participa de um leilão e precisa pegar os itens de maior valor que não ultrapassem o peso da sua mochila.

Utilize os seguintes itens para colocar na mochila:

| Item  | Peso  | Valor |
| :---: | :---: | :---: |
|   1   |   3   |  266  |
|   2   |  13   |  442  |
|   3   |  10   |  671  |
|   4   |   9   |  526  |
|   5   |   7   |  388  |
|   6   |   1   |  245  |
|   7   |   8   |  210  |
|   8   |   8   |  145  |
|   9   |   2   |  126  |
|  10   |   9   |  322  |

[Resposta](./mochila_1_0.py)

## Referências