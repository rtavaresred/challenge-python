def sort_string_by_case(text: str) -> str:
    """
    DOCSTRING:
    Move todas as letras minúsculas para o início e as maiúsculas para o final da string,
    preservando a ordem relativa entre elas.

    EXEMPLO:
    >>> sort_string_by_case("RoDRiGo")
    'oioRDRG'
    """
    lower = []
    upper = []

    for char in text:
        if char.islower():
            lower.append(char)
        else:
            upper.append(char)

    sorted_str = ''.join(lower + upper)
    return sorted_str


if __name__ == "__main__":
    print("---------- Sort String by Case ----------")
    print("Move todas as letras minúsculas para o início e maiúsculas para o final.")
    print("Exemplo: RoDRiGo → oioRDRG")
    print("Escreva 'sair' para encerrar ou 'help' para ajuda.\n")

    while True:
        entrada = input("> ").strip()

        if entrada.lower() == "sair":
            print("\nEncerrando...\n")
            break
        elif entrada.lower() == "help":
            print(sort_string_by_case.__doc__)
            continue

        if not entrada:
            print("❌ Digite algum texto para organizar.\n")
            continue

        resultado = sort_string_by_case(entrada)
        print(f"Resultado: {resultado}\n")
