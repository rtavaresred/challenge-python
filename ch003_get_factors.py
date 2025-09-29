"""
Write a function named get_factors that takes an integer and 
returns a list of all its factors in ascending order.

A factor is a number that divides another number without leaving a remainder.
"""

def get_factors(n: int) -> list[int]:
    """
    DOCSTRING:
    Retorna uma lista com todos os divisores (fatores) de um número inteiro positivo.

    EXEMPLO:
    >>> get_factors(12)
    [1, 2, 3, 4, 6, 12]
    """
    return [num for num in range(1, n + 1) if n % num == 0]

if __name__ == "__main__":
    print("---------- Get Factors ----------")
    print("Digite um número inteiro positivo para ver seus divisores.")
    print("Escreva 'sair' para encerrar ou 'help' para ajuda.\n")

    while True:
        texto = input("> ").strip().lower()

        if texto == "sair":
            print("\nEncerrando...\n")
            break
        elif texto == "help":
            print(get_factors.__doc__)
            continue

        # Verificar se é um número inteiro positivo
        try:
            numero = int(texto)
            if numero <= 0:
                print("Por favor, digite um número inteiro positivo.\n")
                continue
        except ValueError:
            print("Entrada inválida! Digite apenas um número inteiro positivo.\n")
            continue

        # Chamar a função
        resultado = get_factors(numero)
        print("Resultado:", resultado, "\n")
