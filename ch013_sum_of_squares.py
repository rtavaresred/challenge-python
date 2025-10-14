"""
Develop a program that accepts a number n from input and calculates the sum of all square numbers up to and including n.
"""

def sum_of_squares(n: int) -> int:
    """
    DOCSTRING:
    Calcula a soma dos quadrados de todos os números inteiros de 1 até n.

    EXEMPLO:
    >>> sum_of_squares(3)
    14
    >>> sum_of_squares(5)
    55
    """
    res = 0
    for i in range(1, n + 1):
        res += i * i
    return res


if __name__ == "__main__":
    print("---------- Sum of Squares ----------")
    print("Digite um número inteiro positivo para calcular a soma dos quadrados.")
    print("Escreva 'sair' para encerrar ou 'help' para ajuda.\n")

    while True:
        texto = input("> ").strip()

        if texto.lower() == "sair":
            print("\nEncerrando...\n")
            break
        elif texto.lower() == "help":
            print(sum_of_squares.__doc__)
            continue

        try:
            n = int(texto)
            if n < 1:
                print("❌ Digite um número inteiro positivo.\n")
                continue
        except ValueError:
            print("❌ Digite apenas números inteiros.\n")
            continue

        resultado = sum_of_squares(n)
        print(f"Resultado: {resultado}\n")