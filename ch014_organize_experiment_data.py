def organize_experiment_data(raw_data: list[int]) -> list:
    """
    DOCSTRING:
    Recebe uma lista de inteiros representando dados experimentais.
    Retorna uma lista com três elementos:
    1. Lista de valores únicos em ordem crescente
    2. Quantidade de valores únicos
    3. Média (arredondada para 2 casas) dos valores únicos

    EXEMPLO:
    >>> organize_experiment_data([4, 2, 4, 6])
    [[2, 4, 6], 3, 4.0]
    >>> organize_experiment_data([10, 10, 20])
    [[10, 20], 2, 15.0]
    """
    sorted_unique = sorted(set(raw_data))
    count_unique = len(sorted_unique)
    average_unique = round(sum(sorted_unique) / count_unique, 2)
    return [sorted_unique, count_unique, average_unique]


if __name__ == "__main__":
    print("---------- Organize Experiment Data ----------")
    print("Digite inteiros separados por espaço ou vírgula para organizar os dados.")
    print("Escreva 'sair' para encerrar ou 'help' para ajuda.\n")

    while True:
        texto = input("> ").strip()

        if texto.lower() == "sair":
            print("\nEncerrando...\n")
            break
        elif texto.lower() == "help":
            print(organize_experiment_data.__doc__)
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

        if not numeros:
            print("❌ Digite ao menos um número.\n")
            continue

        resultado = organize_experiment_data(numeros)
        print("Resultado:", resultado, "\n")