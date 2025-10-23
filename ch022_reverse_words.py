def reverse_words(sentence: str) -> str:
    """
    DOCSTRING:
    Inverte a ordem das palavras em uma frase.
    As palavras permanecem intactas, apenas a sequência muda.

    EXEMPLO:
    >>> reverse_words("hello world")
    'world hello'
    >>> reverse_words("Python is fun")
    'fun is Python'
    """
    return " ".join(sentence.split()[::-1])


if __name__ == "__main__":
    print("---------- Word Reversal ----------")
    print("Digite uma frase para inverter a ordem das palavras.")
    print("Exemplo: 'Python is awesome'")
    print("Escreva 'sair' para encerrar ou 'help' para ajuda.\n")

    while True:
        texto = input("> ").strip()

        if texto.lower() == "sair":
            print("\nEncerrando...\n")
            break
        elif texto.lower() == "help":
            print(reverse_words.__doc__)
            continue

        if not texto:
            print("❌ Digite uma frase válida.\n")
            continue

        resultado = reverse_words(texto)
        print(f"Resultado: {resultado}\n")
