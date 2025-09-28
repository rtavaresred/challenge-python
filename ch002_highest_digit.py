"""
Create a function named highest_digit that accepts a numerical argument and returns the highest digit in that number.

For instance,

highest_digit(379) should return 9
highest_digit(2) should return 2
highest_digit(377401) should return 7
"""

# Aprendi o novo comando max(...) 
# Corrigi o erro que ocorria ao usar `for x in n` sem converter n para string com str(n).

def highest_digit(n: int) -> int:
    """
    DOCSTRING:
    Retorna o maior dígito presente em um número inteiro positivo.

    EXEMPLO:
    >>> highest_digit(1654)
    6
    """
    return max(int(x) for x in str(n))


if __name__ == "__main__":
    print("---------- Highest Digit ----------")
    print("Digite um número inteiro positivo.")
    print("Escreva 'sair' para encerrar ou 'help' para ajuda.\n")

    while True:
        texto = input("> ").strip().lower()

        if texto == "sair":
            print("\nEncerrando...\n")
            break
        if texto == "help":
            print(highest_digit.__doc__)
            continue
        if not texto:
            continue

        # Verificar se é um número inteiro positivo
        try:
            numero = int(texto)
            if numero < 0:
                print("❌ Por favor, digite um número inteiro positivo.\n")
                continue
        except ValueError:
            print("❌ Digite apenas um número inteiro positivo, 'help' ou 'sair'.\n")
            continue

        resultado = highest_digit(numero)
        print("Resultado:", resultado, "\n")