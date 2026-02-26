def get_sequence_value(x):
    if x == 0:
        raise ValueError("Sequencia começa no indice 1")
    return (x*7)+4