from math import ceil, comb
from itertools import product

def tribonacci(n):
    a, b, c = 1, 1, 2 

    for _ in range(3, n + 1):
        a, b, c = b, c, a + b + c

    return c


def optimal_probability(board_size, minimum_turns):
    soma = 0

    for k in range((board_size - minimum_turns) // 2 + 1):
        soma += comb(minimum_turns, k) * comb(minimum_turns - k, board_size - minimum_turns - 2*k)

    return soma / (3 ** minimum_turns)


def analyze_board_game(board_size):
    if board_size < 3: 
        raise ValueError("Tabuleiro deve ter no minimo 3 casas")
    
    minimum_turns = ceil(board_size/3)
    optimal_path_probability = optimal_probability(board_size, minimum_turns)
    combinations_without_loop = tribonacci(board_size)

    return {
        "Quantidade minima de turnos": minimum_turns,
        "Possibilidade de um usuário conseguir executar o caminho ótimo" : optimal_path_probability,
        "Combinações sem loop": combinations_without_loop
        }

