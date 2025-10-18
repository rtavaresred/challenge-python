"""
Write a Python function named check_alphabet_order that takes a string as input and returns True
 if the letters are in alphabetical order, and False otherwise.

For example, "abc" is in alphabetical order, but "cfabh" is not because 'f' 
comes between 'c' and 'a'.
"""

def check_alphabet_order(a: str) -> bool:
    """
    DOCSTRING:
    Verifica se os caracteres de uma string estão em ordem alfabética crescente.

    EXEMPLO:
    >>> check_alphabet_order("abc")
    True
    >>> check_alphabet_order("acb")
    False
    >>> check_alphabet_order("xyz")
    True
    """
    for i in range(1, len(a)):
        if a[i - 1] >= a[i]:
            return False
    return True


if __name__ == "__main__":
    print("---------- Alphabetical Order Challenge ----------")
    print("Digite uma palavra para verificar se está em ordem alfabética.")
    print("Exemplo: 'abc' → True, 'acb' → False")
    print("Escreva 'sair' para encerrar ou 'help' para ajuda.\n")

    while True:
        texto = input("> ").strip()

        if texto.lower() == "sair":
            print("\nEncerrando...\n")
            break
        elif texto.lower() == "help":
            print(check_alphabet_order.__doc__)
            continue

        if not texto.isalpha():
            print("❌ Digite apenas letras (sem números ou símbolos).\n")
            continue

        resultado = check_alphabet_order(texto.lower())
        print(f"Resultado: {resultado}\n")
