"""
Write a function remove_duplicates(in_list) that takes a list of integers in_list and returns a new list with duplicates removed. 
The order of elements should remain the same as in the input list.
"""

def remove_duplicates(in_list: list) -> list:
    """
    DOCSTRING:
    Remove elementos duplicados de uma lista, preservando a ordem original.

    EXEMPLO:
    >>> remove_duplicates([1, 2, 2, 3, 1, 4])
    [1, 2, 3, 4]
    """
    no_duplicates = []
    for item in in_list:
        if item not in no_duplicates:
            no_duplicates.append(item)
    return no_duplicates


if __name__ == "__main__":
    print("---------- Remove Duplicates ----------")
    print("Digite elementos separados por vírgula ou espaço.")
    print("Escreva 'sair' para encerrar ou 'help' para ajuda.\n")

    while True:
        texto = input("> ").strip()

        if texto.lower() == "sair":
            print("\nEncerrando...\n")
            break
        elif texto.lower() == "help":
            print(remove_duplicates.__doc__)
            continue

        try:
            # Aceitar vírgula ou espaço
            if "," in texto:
                partes = [p.strip() for p in texto.split(",")]
            else:
                partes = [p.strip() for p in texto.split()]

            resultado = remove_duplicates(partes)
            print("Resultado:", resultado, "\n")

        except Exception as e:
            print("❌ Digite apenas uma lista de elementos separados por vírgula ou espaço.\n")
