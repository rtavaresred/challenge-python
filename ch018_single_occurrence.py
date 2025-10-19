"""
Write a function named single_occurrence that identifies a letter that appears only once in a given string.

The function should return the letter or an empty string "" if the input is empty.

The function should be case sensitive.

Examples:

single_occurrence("EFFEAABbc") ➞ "c"
single_occurrence("AAAAVNNNNSS") ➞ "V"
single_occurrence("S") ➞ "S"

Assume the given string contains exactly one letter that occurs only once.
"""

def single_occurrence(txt: str) -> str:
    """
    DOCSTRING:
    Retorna o primeiro caractere que aparece apenas uma vez em uma string.
    Se nenhum caractere for único, retorna uma string vazia.

    EXEMPLO:
    >>> single_occurrence("minimum")
    'n'
    >>> single_occurrence("aabbcc")
    ''
    >>> single_occurrence("abcabcde")
    'd'
    """
    if not txt:
        return ""
    
    for ch in txt:
        if txt.count(ch) == 1:
            return ch

    return ""


if __name__ == "__main__":
    print("---------- Single Occurrence ----------")
    print("Digite uma palavra ou frase para encontrar o primeiro caractere único.")
    print("Escreva 'sair' para encerrar ou 'help' para ajuda.\n")

    while True:
        texto = input("> ").strip()

        if texto.lower() == "sair":
            print("\nEncerrando...\n")
            break
        elif texto.lower() == "help":
            print(single_occurrence.__doc__)
            continue

        if not texto:
            print("❌ Digite uma palavra ou frase válida.\n")
            continue

        resultado = single_occurrence(texto)
        if resultado:
            print(f"O primeiro caractere único é: '{resultado}'\n")
        else:
            print("Nenhum caractere único encontrado.\n")
