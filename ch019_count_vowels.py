def count_vowels(texto: str) -> int:
    """
    DOCSTRING:
    Conta o número de vogais (a, e, i, o, u) presentes em uma string.
    A contagem não diferencia maiúsculas de minúsculas.

    EXEMPLO:
    >>> count_vowels("Rodrigo")
    3
    >>> count_vowels("Python")
    1
    >>> count_vowels("AEIOU")
    5
    """
    vogais = "aeiouAEIOU"
    return sum(1 for ch in texto if ch in vogais)


if __name__ == "__main__":
    print("---------- Count Vowels ----------")
    print("Digite uma palavra ou frase para contar quantas vogais ela possui.")
    print("Escreva 'sair' para encerrar ou 'help' para ajuda.\n")

    while True:
        texto = input("> ").strip()

        if texto.lower() == "sair":
            print("\nEncerrando...\n")
            break
        elif texto.lower() == "help":
            print(count_vowels.__doc__)
            continue

        if not texto:
            print("❌ Digite uma palavra ou frase válida.\n")
            continue

        resultado = count_vowels(texto)
        print(f"Número de vogais: {resultado}\n")
