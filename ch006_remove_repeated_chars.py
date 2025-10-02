"""
Write a function remove_repeated_chars(s) that takes a string s as input
and returns a new string with repeated characters removed.
"""

def remove_repeated_chars(text: str) -> str:
    """
    DOCSTRING:
    Recebe uma string e retorna outra string sem caracteres repetidos,
    mantendo apenas a primeira ocorrência de cada caractere.

    EXEMPLO:
    >>> remove_repeated_chars("banana")
    'ban'
    >>> remove_repeated_chars("abracadabra")
    'abrcd'
    """
    sem_repeticao = []

    for char in text:
        if char not in sem_repeticao:
            sem_repeticao.append(char)

    return "".join(sem_repeticao)


if __name__ == "__main__":
    print("---------- Remove Repeated Chars ----------")
    print("Digite um texto para remover caracteres repetidos.")
    print("Escreva 'sair' para encerrar ou 'help' para ajuda.\n")

    while True:
        texto = input("> ").strip()

        if texto.lower() == "sair":
            print("\nEncerrando...\n")
            break
        elif texto.lower() == "help":
            print(remove_repeated_chars.__doc__)
            continue

        if not texto:
            print("❌ Digite um texto válido.\n")
            continue

        # Chamar a função
        resultado = remove_repeated_chars(texto)
        print("Resultado:", resultado, "\n")
