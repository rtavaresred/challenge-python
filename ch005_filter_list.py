def filter_list(a: list) -> list[int]:
    """
    DOCSTRING:
    Recebe uma lista contendo inteiros e strings.
    Retorna apenas os elementos inteiros, filtrando as strings.

    EXEMPLO:
    >>> filter_list([1, "a", "30", 0, 15])
    [1, 0, 15]
    """
    res = []
    for i in a:
        if type(i) == int:
            res.append(i)
    return res


if __name__ == "__main__":
    print("---------- Filter List ----------")
    print("Digite valores separados por espaço ou vírgula (ex: 1 a b 0 15).")
    print("Escreva 'sair' para encerrar ou 'help' para ajuda.\n")

    while True:
        texto = input("> ").strip().lower()

        if texto == "sair":
            print("\nEncerrando...\n")
            break
        elif texto == "help":
            print(filter_list.__doc__)
            continue

        # Transformar entrada em lista de inteiros e strings
        try:
            if "," in texto:
                partes = [x.strip() for x in texto.split(",")]
            else:
                partes = texto.split()

            lista = []
            for item in partes:
                if item.isdigit():
                    lista.append(int(item))
                else:
                    lista.append(item)
        except Exception:
            print("❌ Digite apenas inteiros e/ou strings separados por espaço ou vírgula.\n")
            continue

        # Chamar a função
        resultado = filter_list(lista)
        print("Resultado:", resultado, "\n")
