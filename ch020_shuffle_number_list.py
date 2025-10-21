import random

def shuffle_number_list(n: int) -> list[int]:
    """
    DOCSTRING:
    Cria uma lista de inteiros de 1 até n e a embaralha de forma aleatória.

    EXEMPLO:
    >>> shuffle_number_list(5)
    [3, 1, 5, 2, 4]
    """
    numeros = list(range(1, n + 1))
    random.shuffle(numeros)
    return numeros


if __name__ == "__main__":
    print("---------- Shuffle Number List ----------")
    print("Digite um número inteiro positivo para gerar e embaralhar a lista.")
    print("Escreva 'sair' para encerrar ou 'help' para ajuda.\n")

    while True:
        texto = input("> ").strip()

        if texto.lower() == "sair":
            print("\nEncerrando...\n")
            break
        elif texto.lower() == "help":
            print(shuffle_number_list.__doc__)
            continue

        try:
            n = int(texto)
            if n <= 0:
                print("❌ Digite um número inteiro positivo.\n")
                continue
        except ValueError:
            print("❌ Digite apenas números inteiros.\n")
            continue

        resultado = shuffle_number_list(n)
        print("Lista embaralhada:", resultado, "\n")
