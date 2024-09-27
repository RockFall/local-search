"""
                            TP01 -  Ordenação usando Busca em Espaço de Estados
    
    ---------------------------------------------------------------------------------------------
    Autor: Caio Henrique Dias Rocha - 2023.1
    Disciplina: Introdução a Inteligência Artificial - DCC642
    Professor: Luiz Chaimowicz
    Universidade Federal de Minas Gerais - UFMG
    ---------------------------------------------------------------------------------------------

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
        python3 TP1.py U 3 3 1 2 PRINT

    O programa imprime a quantidade de estados expandidos, o custo da solução, a lista ordenada final e, 
    se o parâmetro PRINT estiver presente, imprime os estados intermediários.
"""

import sys
from queue import Queue
from queue import PriorityQueue


"""
Check if the list is sorted
"""
def check_sorted(state):
    # Check if list is sorted
    for i in range(len(state) - 1):
        if state[i] > state[i + 1]:
            return False
    return True


"""
Generate all possible successors by swapping two elements
Neighbor elements have cost 2, non-neighbor elements have cost 4
"""
def generate_successors(state, path):
    successors = []
    for i in range(len(state) - 1):
        for j in range(i + 1, len(state)):
            new_state = state.copy()
            new_state[i], new_state[j] = new_state[j], new_state[i]
            cost = 4
            if i+1 == j or i-1 == j:
                cost = 2
            if new_state not in path:
                successors.append((new_state, cost))
    return successors

"""
Heuristic function
    Returns the estimated cost from state to the goal
    
    Here, we count the number of misplaced elements
"""
def heuristic(state):
    misplaced = 0
    for i in range(len(state) - 1):
        if state[i] > state[i + 1]:
            misplaced += 1
    return misplaced

"""
_____________________________________________________________________________________________
Breadth-first search
"""
def bfs(initial_state):
    q = Queue()
    q.put((initial_state, [initial_state], 0, 0))
    
    while not q.empty():
        state, path, expanded_count, cost = q.get()
        if check_sorted(state):
            return path, expanded_count, cost
        successors = generate_successors(state, path)
        for successor, succ_cost in successors:
            q.put((successor, path + [successor], expanded_count + 1, cost + succ_cost))
"""
################################################################################################
"""


"""
_____________________________________________________________________________________________
Iterative deepening search
"""
def ids(initial_state):
    depth_limit = 0
    while True:
        result, expanded_count, cost = dls(initial_state, [], 0, 0, depth_limit)
        if result is not None:
            return result, expanded_count, cost
        depth_limit += 1

def dls(state, path, expanded_count, cost, depth_limit):
    # Depth-limited search
    if check_sorted(state):
        return path, expanded_count, cost
    elif depth_limit == 0:
        return None, expanded_count, cost
    else:
        successors = generate_successors(state, path)
        for successor, succ_cost in successors:
            result, expanded_count, new_cost = dls(successor, path + [successor], expanded_count + 1, cost + succ_cost, depth_limit - 1)
            if result is not None:
                return result, expanded_count, new_cost
        return None, expanded_count, new_cost
"""
################################################################################################
"""



"""
_____________________________________________________________________________________________
Uniform-cost search
"""
def ucs(initial_state):
    q = PriorityQueue()
    # Cost is the priority comparative value
    q.put((0, initial_state, [initial_state], 0))
    visited = []

    while not q.empty():
        cost, state, path, expanded_count = q.get()
        if check_sorted(state):
            return path, expanded_count, cost
        if state not in visited:
            visited.append(state)
            successors = generate_successors(state, path)
            for successor, succ_cost in successors:
                new_cost = cost + succ_cost
                new_path = path + [successor]
                q.put((new_cost, successor, new_path, expanded_count + 1))

    return None, 0, 0
"""
################################################################################################
"""


"""
_____________________________________________________________________________________________
A* search
"""
def a_star(initial_state):
    global aux_counter
    q = PriorityQueue()
    # Cost is the priority comparative value
    q.put((0 + heuristic(initial_state), 0, initial_state, [initial_state], 0))
    visited = []

    while not q.empty():
        _, g, state, path, expanded_count = q.get()
        if check_sorted(state):
            return path, expanded_count, g
        if state not in visited:
            visited.append(state)
            successors = generate_successors(state, path)
            aux_counter += 1
            for successor, succ_cost in successors:
                
                print("Auxiliar counter: ", aux_counter)
                new_g = g + succ_cost
                new_path = path + [successor]
                q.put((new_g + heuristic(successor), new_g, successor, new_path, expanded_count + 1))

    return None, 0, 0
"""
################################################################################################
"""

"""
_____________________________________________________________________________________________
Greedy search
"""
def greedy(initial_state):
    global aux_counter
    # Greedy search
    q = PriorityQueue()
    # Heuristic is the priority comparative value
    q.put((heuristic(initial_state), initial_state, [initial_state], 0, 0))
    visited = []

    while not q.empty():
        h_cost, state, path, expanded_count, path_cost = q.get()
        if check_sorted(state):
            return path, expanded_count, new_path_cost
        if state not in visited:
            visited.append(state)
            successors = generate_successors(state, path)
            aux_counter += 1
            for successor, succ_cost in successors:
                new_h = heuristic(successor)
                new_path = path + [successor]
                new_path_cost = path_cost + succ_cost
                q.put((new_h, successor, new_path, expanded_count + 1, new_path_cost))
    return None, 0, 0
"""
################################################################################################
"""

# Main
if __name__ == "__main__":
    # Get the parameters entered on terminal
    global aux_counter
    aux_counter = 0
    algorithm = "G"
    size = 10
    items = [8, 3, 1, 4, 6, 5, 8, 7, 2, 9, 10, 15, 12]

    # If param PRINT is given -> print intermediate states
    print_path = True

    path = []
    expanded_count = 0
    cost = 0
    
    # Run the algorithm (B, I, U, A, G),
    if algorithm == "B":
        path, expanded_count, cost = bfs(items)
    elif algorithm == "I":
        path, expanded_count, cost = ids(items)
    elif algorithm == "U":
        path, expanded_count, cost = ucs(items)
    elif algorithm == "A":
        path, expanded_count, cost = a_star(items)
    elif algorithm == "G":
        path, expanded_count, cost = greedy(items)

    # Print the results
    print(cost, expanded_count)
    if print_path:
        for state in path:
            output_str = " ".join(str(x) for x in state)
            print(output_str)
    else:
        output_str = " ".join(str(x) for x in path[-1])
        print(output_str)

    print("Auxiliar counter: ", aux_counter)