def character_frequency(text: str) -> str:
    """
    DOCSTRING:
    Analisa uma string e retorna o caractere mais frequente e o menos frequente.

    EXEMPLO:
    >>> character_frequency("banana")
    "Most: 'a' (3x), Least: 'b' (1x)"
    >>> character_frequency("abracadabra")
    "Most: 'a' (5x), Least: 'c' (1x)"
    """
    if not text:
        return "Empty string provided."

    frequency = {}
    for char in text:
        frequency[char] = frequency.get(char, 0) + 1

    most_char = max(frequency, key=frequency.get)
    least_char = min(frequency, key=frequency.get)

    return f"Most: '{most_char}' ({frequency[most_char]}x), Least: '{least_char}' ({frequency[least_char]}x)"


if __name__ == "__main__":
    print("---------- Character Frequency ----------")
    print("Digite uma string para analisar os caracteres mais e menos frequentes.")
    print("Exemplo: 'banana'")
    print("Escreva 'sair' para encerrar ou 'help' para ajuda.\n")

    while True:
        texto = input("> ").strip()

        if texto.lower() == "sair":
            print("\nEncerrando...\n")
            break
        elif texto.lower() == "help":
            print(character_frequency.__doc__)
            continue

        if not texto:
            print("❌ Digite uma string válida.\n")
            continue

        resultado = character_frequency(texto)
        print(f"Resultado: {resultado}\n")
