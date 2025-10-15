"""
Write a function has_unique_chars(s) that takes a non-empty string s and 
returns True if the string contains only unique characters, and False otherwise.
"""

def has_unique_chars(s: str) -> bool:
    """
    DOCSTRING:
    Verifica se uma string contém apenas caracteres únicos
    (sem repetições).

    EXEMPLO:
    >>> has_unique_chars("abcde")
    True
    >>> has_unique_chars("hello")
    False
    """
    return len(s) == len(set(s))


if __name__ == "__main__":
    print("---------- Check Unique Characters ----------")
    print("Digite uma palavra ou frase para verificar se possui apenas caracteres únicos.")
    print("Escreva 'sair' para encerrar ou 'help' para ajuda.\n")

    while True:
        texto = input("> ").strip()

        if texto.lower() == "sair":
            print("\nEncerrando...\n")
            break
        elif texto.lower() == "help":
            print(has_unique_chars.__doc__)
            continue

        if not texto:
            print("❌ Digite uma palavra ou frase válida.\n")
            continue

        resultado = has_unique_chars(texto)
        print(f"Resultado: {resultado}\n")
