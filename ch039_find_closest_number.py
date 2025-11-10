def find_closest_number(numeros: list[int], alvo: int) -> int:
    """
    Encontra o número mais próximo de um valor alvo em uma lista.

    Args:
        numeros (list[int]): Lista de números.
        alvo (int): Valor alvo a ser comparado.

    Returns:
        int: Número da lista mais próximo do valor alvo.

    Exemplos:
        >>> find_closest_number([10, 22, 14, 26], 20)
        22
        >>> find_closest_number([5, 8, 12], 9)
        8
    """
    if not numeros:
        raise ValueError("A lista não pode estar vazia.")
    return min(numeros, key=lambda n: abs(n - alvo))


if __name__ == "__main__":
    print("---------- Find Closest Number ----------")
    print("Encontra o número mais próximo de um valor alvo em uma lista.")
    print("Formato: lista de números e valor alvo.")
    print("Exemplo: [10, 22, 14, 26] alvo 20 → 22\n")

    while True:
        entrada = input("Lista de números (ex: 10, 22, 14, 26): ").strip()
        if not entrada or entrada.lower() == "sair":
            print("\nEncerrando...\n")
            break

        try:
            numeros = [int(x) for x in entrada.replace(",", " ").split()]
        except ValueError:
            print("Entrada inválida. Use apenas números inteiros separados por espaço ou vírgula.")
            continue

        try:
            alvo = int(input("Número alvo: ").strip())
        except ValueError:
            print("Valor alvo inválido.")
            continue

        resultado = find_closest_number(numeros, alvo)
        print(f"✅ Número mais próximo de {alvo}: {resultado}\n")
