def are_anagrams(a: str, b: str) -> bool:
    """
    DOCSTRING:
    Verifica se duas strings são anagramas (contêm as mesmas letras, em qualquer ordem).
    A verificação não diferencia maiúsculas de minúsculas.

    EXEMPLO:
    >>> are_anagrams("listen", "silent")
    True
    >>> are_anagrams("hello", "world")
    False
    """
    return sorted(a.lower()) == sorted(b.lower())


if __name__ == "__main__":
    print("---------- Anagram Check ----------")
    print("Digite duas palavras separadas por vírgula para verificar se são anagramas.")
    print("Exemplo: 'listen,silent'")
    print("Escreva 'sair' para encerrar ou 'help' para ajuda.\n")

    while True:
        texto = input("> ").strip()

        if texto.lower() == "sair":
            print("\nEncerrando...\n")
            break
        elif texto.lower() == "help":
            print(are_anagrams.__doc__)
            continue

        if "," not in texto:
            print("❌ Digite duas palavras separadas por vírgula.\n")
            continue

        a, b = [p.strip() for p in texto.split(",", 1)]
        if not a or not b:
            print("❌ Ambas as palavras devem ser fornecidas.\n")
            continue

        resultado = are_anagrams(a, b)
        print(f"Resultado: {resultado}\n")
