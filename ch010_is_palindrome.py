def is_palindrome(text: str) -> bool:
    """
    DOCSTRING:
    Verifica se uma string é um palíndromo (lida igual de frente para trás e de trás para frente).
    Ignora espaços e diferenciação entre maiúsculas/minúsculas.

    EXEMPLO:
    >>> is_palindrome("arara")
    True
    >>> is_palindrome("Python")
    False
    >>> is_palindrome("Ame a ema")
    True
    """
    normalized = "".join(c.lower() for c in text if c.isalnum())
    return normalized == normalized[::-1]


if __name__ == "__main__":
    print("---------- Palindrome Checker ----------")
    print("Digite uma palavra ou frase para verificar se é palíndromo.")
    print("Escreva 'sair' para encerrar ou 'help' para ajuda.\n")

    while True:
        texto = input("> ").strip()

        if texto.lower() == "sair":
            print("\nEncerrando...\n")
            break
        elif texto.lower() == "help":
            print(is_palindrome.__doc__)
            continue

        if not texto:
            print("❌ Digite uma palavra ou frase válida.\n")
            continue

        resultado = is_palindrome(texto)
        print("Resultado:", resultado, "\n")
