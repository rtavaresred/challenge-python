def get_middle_char(s: str) -> str:
    """
    DOCSTRING:
    Retorna o caractere central de uma string.  
    Se o comprimento for par, retorna uma string vazia.

    EXEMPLO:
    >>> get_middle_char("abc")
    'b'
    >>> get_middle_char("abcd")
    ''
    >>> get_middle_char("x")
    'x'
    """
    if len(s) == 1:
        return s

    if len(s) % 2 == 0:
        return ""
    else:
        middle = len(s) // 2
        return s[middle]


if __name__ == "__main__":
    print("---------- Return the Middle Character of a String ----------")
    print("Digite uma palavra ou frase para descobrir o caractere central.")
    print("Se a string tiver número par de caracteres, retorna vazio ('').")
    print("Escreva 'sair' para encerrar ou 'help' para ajuda.\n")

    while True:
        texto = input("> ").strip()

        if texto.lower() == "sair":
            print("\nEncerrando...\n")
            break
        elif texto.lower() == "help":
            print(get_middle_char.__doc__)
            continue

        if not texto:
            print("❌ Digite uma palavra ou frase válida.\n")
            continue

        resultado = get_middle_char(texto)
        print(f"Resultado: '{resultado}'\n")
