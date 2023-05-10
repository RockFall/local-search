_____________________________________________________________________________________________________
                        TP01 -  Ordenação usando Busca em Espaço de Estados

-----------------------------------------------------------------------------------------------------
Autor: Caio Henrique Dias Rocha - 2023.1
Disciplina: Introdução a Inteligência Artificial - DCC642
Professor: Luiz Chaimowicz
Universidade Federal de Minas Gerais - UFMG
-----------------------------------------------------------------------------------------------------

Este programa implementa os algoritmos de busca em espaços de estados
* Breadth-first search (BFS),
* Iterative deepening search (IDS), 
* Uniform-cost search (UCS),
* A* search, 
* Greedy search (G)

Para executar o programa, execute o comando:
python3 TP1.py <ALGORITMO> <TAMANHO> <LISTA> [PRINT]
Onde:
    <ALGORITMO> é o algoritmo a ser executado (B, I, U, A, G)
    <TAMANHO> é o tamanho da lista
    <LISTA> é a lista de inteiros a ser ordenada
    [PRINT] é um parâmetro opcional que, se presente, imprime os estados intermediários

Exemplo:
    $ python3 TP1.py U 3 3 1 2 PRINT

O programa imprime a quantidade de estados expandidos, o custo da solução, a lista ordenada final e, 
se o parâmetro PRINT estiver presente, imprime os estados intermediários.
_____________________________________________________________________________________________________