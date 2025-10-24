def find_runner_up(arr: list[int]) -> int:
    """
    DOCSTRING:
    Encontra o segundo maior número (runner-up) em uma lista de inteiros.
    Se não houver um runner-up, retorna None.

    EXEMPLO:
    >>> find_runner_up([2, 3, 6, 6, 5])
    5
    >>> find_runner_up([10, 10, 10])
    None
    """
    if not arr or len(arr) < 2:
        return None

    max_score = max(arr)
    runner_up_candidates = [x for x in arr if x != max_score]

    if not runner_up_candidates:
        return None

    return max(runner_up_candidates)


if __name__ == "__main__":
    print("---------- Find the Runner-Up Score ----------")
    print("Digite uma lista de números separados por espaço para encontrar o segundo maior valor.")
    print("Exemplo: '2 3 6 6 5'")
    print("Escreva 'sair' para encerrar ou 'help' para ajuda.\n")

    while True:
        texto = input("> ").strip()

        if texto.lower() == "sair":
            print("\nEncerrando...\n")
            break
        elif texto.lower() == "help":
            print(find_runner_up.__doc__)
            continue

        try:
            arr = [int(x) for x in texto.split()]
            resultado = find_runner_up(arr)
            if resultado is None:
                print("❌ Não há um runner-up na lista.\n")
            else:
                print(f"Runner-up: {resultado}\n")
        except ValueError:
            print("❌ Digite apenas números inteiros separados por espaço.\n")
