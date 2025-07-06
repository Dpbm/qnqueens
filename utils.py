from typing import List, Dict, Tuple

Cell = Tuple[int, int]
Mapping = Dict[Cell, int]

def get_diagonal_attacks(cell:Cell, n:int) -> List[Cell]:
    """
    params:
        cell : Cell - the especific board position (i,j)
        n : int - the board side

    Check the attacks for each queen position in the diagonal.
    """

    current_row, current_col = cell

    attacks = []

    # top left
    current_i = current_row
    current_j = current_col
    while current_i > 0 and current_j > 0:
        current_i -= 1
        current_j -= 1
        attacks.append((current_i, current_j))

    # bottom right
    current_i = current_row
    current_j = current_col
    while current_i < n-1 and current_j < n-1:
        current_i += 1
        current_j += 1
        attacks.append((current_i, current_j))

    # top right 
    current_i = current_row
    current_j = current_col
    while current_i > 0 and current_j < n-1:
        current_i -= 1
        current_j += 1
        attacks.append((current_i, current_j))

    # bottom left 
    current_i = current_row
    current_j = current_col
    while current_i < n-1 and current_j > 0:
        current_i += 1
        current_j -= 1
        attacks.append((current_i, current_j))

    return attacks


def get_attacks_for_each_cell(cell:Cell, n:int) -> List[Cell]:
    """
    params:
        cell : Cell - the especific board position (i,j)
        n : int - the board side

    Check the attacks for each queen position.
    """

    current_row, current_col = cell

    attacks = []


    for k in range(n):
        current_mapped_col = (k, current_col)
        current_mapped_row = (current_row, k)

        if current_mapped_row != cell:
            attacks.append(current_mapped_row)
        
        if current_mapped_col != cell:
            attacks.append(current_mapped_col)

    attacks = [*attacks, *get_diagonal_attacks(cell, n)]

    

    return attacks



def get_pos_mapping(n:int) -> Mapping:
    """
    params:
        n: int - the side of the board

    Get the variable relative to that
    especific cell position (for qubo).
    """

    mapping = {}
    k = 0

    for i in range(n):
        for j in range(n):
            mapping[(i,j)] = k
            k += 1

    return mapping

def get_pos_mapping_qubit(n:int) -> Mapping:
    """
    params:
        n: int - the side of the board

    Get the qubit relative to that
    especific cell position (for circuits).
    """

    mapping = {}
    k = n

    for i in range(n):
        for j in range(n):
            k -= 1
            mapping[(i,j)] = k

        k = (i+2)*n
        

    return mapping
