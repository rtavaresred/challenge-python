def sum_minimums(mat: list[list[int]]) -> int:
    """
    DOCSTRING:
    Calcula a soma dos menores valores de cada linha em uma matriz.

    EXEMPLOS:
    >>> sum_minimums([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    12
    >>> sum_minimums([[3, 5, 2], [1, 6, 4]])
    3
    """
    res = 0
    for row in mat:
        res += min(row)
    return res


if __name__ == "__main__":
    print("---------- Sum of Minimums ----------")
    print("Calcula a soma dos menores valores de cada linha em uma matriz de números inteiros.")
    print("Formato: [[números], [números], ...]")
    print("Exemplo: [[3, 5, 2], [1, 6, 4]]")
    print("Escreva 'sair' para encerrar ou 'help' para ajuda.\n")

    while True:
        entrada = input("> ").strip()

        if entrada.lower() == "sair":
            print("\nEncerrando...\n")
            break
        elif entrada.lower() == "help":
            print(sum_minimums.__doc__)
            continue

        try:
            matriz = eval(entrada)
            if not isinstance(matriz, list) or not all(isinstance(linha, list) for linha in matriz):
                print("❌ Digite uma matriz válida no formato [[1,2,3],[4,5,6]]\n")
                continue

            resultado = sum_minimums(matriz)
            print(f"Resultado: {resultado}\n")

        except Exception:
            print("❌ Erro ao processar entrada. Certifique-se de usar o formato correto, como [[1,2,3],[4,5,6]]\n")
