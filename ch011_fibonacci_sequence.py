"""
Write a function fibonacci_sequence(n) that takes an integer n as input and 
returns a list of the first n numbers in the Fibonacci sequence.
"""

def fibonacci_sequence(n: int) -> list[int]:
    """
    DOCSTRING:
    Gera a sequência de Fibonacci até o enésimo termo (n).
    A sequência começa em 0 e 1, e cada número seguinte é a soma dos dois anteriores.

    EXEMPLO:
    >>> fibonacci_sequence(5)
    [0, 1, 1, 2, 3]
    >>> fibonacci_sequence(1)
    [0]
    >>> fibonacci_sequence(0)
    []
    """
    if n <= 0:
        return []

    if n == 1:
        return [0]

    sequence = [0, 1]

    for i in range(2, n):
        next_num = sequence[i - 1] + sequence[i - 2]
        sequence.append(next_num)

    return sequence


if __name__ == "__main__":
    print("---------- Fibonacci Sequence ----------")
    print("Digite um número inteiro positivo para ver a sequência de Fibonacci.")
    print("Escreva 'sair' para encerrar ou 'help' para ajuda.\n")

    while True:
        texto = input("> ").strip().lower()

        if texto == "sair":
            print("\nEncerrando...\n")
            break
        elif texto == "help":
            print(fibonacci_sequence.__doc__)
            continue

        # Verificar se o valor é inteiro
        try:
            numero = int(texto)
            if numero < 0:
                print("❌ Digite apenas números inteiros positivos.\n")
                continue
        except ValueError:
            print("❌ Digite apenas números inteiros válidos.\n")
            continue

        resultado = fibonacci_sequence(numero)
        print("Resultado:", resultado, "\n")