def manage_inventory(inventory, to_remove, range_to_view):
    """
    DOCSTRING:
    Gerencia um inventário removendo um item específico e retornando
    uma parte (slice) da lista resultante com base em um intervalo dado.

    EXEMPLO:
    >>> manage_inventory(["sword", "shield", "potion", "bow"], "potion", (0, 2))
    ['sword', 'shield', 'bow']
    >>> manage_inventory(["apple", "banana", "orange"], "banana", (1, 2))
    ['orange']
    """
    items = inventory.copy()  # evita modificar a lista original

    if to_remove in items:
        items.remove(to_remove)

    start, end = range_to_view
    return items[start:end + 1]


if __name__ == "__main__":
    # Exemplo com 10 cores
    cores = [
        "amarelo", "vermelho", "amarelo", "azul", "amarelo", "verde", "roxo",
        "laranja","amarelo", "branco", "preto", "rosa", "cinza"
    ]

    print("---------- Inventory Management ----------")
    print("Inventário original:", cores)

    # Remove 'amarelo' e pega o slice (0, 3)
    resultado = manage_inventory(cores, "amarelo", (0, 4))
    print("Inventário após remover 'amarelo' e mostrar (0,4):", resultado)
