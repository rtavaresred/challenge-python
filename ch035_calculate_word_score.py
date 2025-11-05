def calculate_word_score(word: str) -> int:
    """
    DOCSTRING:
    Calcula a pontuação de uma palavra somando os valores das letras.
    Cada letra vale conforme sua posição no alfabeto: A=1, B=2, ..., Z=26.
    Ignora caracteres que não são letras.

    EXEMPLO:
    >>> calculate_word_score("ABC")
    6
    >>> calculate_word_score("Rodrigo")
    90
    """
    word = word.upper()
    total = 0

    for ch in word:
        if ch.isalpha():
            total += ord(ch) - 64  # 'A' = 65 em ASCII

    return total


if __name__ == "__main__":
    print("---------- Word Score Calculator ----------")
    print("Calcula a pontuação de uma palavra (A=1, B=2, ..., Z=26).")
    print("Exemplo: Rodrigo → 90")
    print("Escreva 'sair' para encerrar ou 'help' para ajuda.\n")

    while True:
        entrada = input("> ").strip()

        if entrada.lower() == "sair":
            print("\nEncerrando...\n")
            break
        elif entrada.lower() == "help":
            print(calculate_word_score.__doc__)
            continue

        if not entrada.isalpha():
            print("❌ Digite apenas letras (sem números ou símbolos).\n")
            continue

        resultado = calculate_word_score(entrada)
        print(f"Pontuação da palavra '{entrada}': {resultado}\n")
