def find_missing_number(arr: list[int]) -> int:
    """
    DOCSTRING:
    Dada uma lista de inteiros, encontra o menor número faltante na sequência.
    Se não houver número faltante, retorna o próximo inteiro após o maior valor.

    EXEMPLO:
    >>> find_missing_number([0, 1, 2, 4, 5])
    3
    >>> find_missing_number([1, 2, 3])
    0
    >>> find_missing_number([0, 1, 2, 3])
    4
    """
    for num in range(max(arr) + 1):
        if num not in arr:
            return num
    return max(arr) + 1


if __name__ == "__main__":
    print("---------- Find Missing Number ----------")
    print("Digite inteiros separados por espaço ou vírgula.")
    print("Escreva 'sair' para encerrar ou 'help' para ajuda.\n")

    while True:
        texto = input("> ").strip().lower()

        if texto == "sair":
            print("\nEncerrando...\n")
            break
        elif texto == "help":
            print(find_missing_number.__doc__)
            continue

        # Converter entrada em lista de inteiros
        try:
            if "," in texto:
                numeros = [int(x.strip()) for x in texto.split(",")]
            else:
                numeros = [int(x) for x in texto.split()]
        except ValueError:
            print("❌ Digite apenas números inteiros separados por espaço ou vírgula.\n")
            continue

        # Garantir que lista não esteja vazia
        if not numeros:
            print("❌ Digite ao menos um número.\n")
            continue

        # Chamar a função
        resultado = find_missing_number(numeros)
        print("Resultado:", resultado, "\n")