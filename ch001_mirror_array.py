"""
Write a function named mirror_array that transforms an integer list into a mirror by adding the list in reverse order to the end of the original list, excluding the last item.

For example:

[0, 2, 4, 6] becomes [0, 2, 4, 6, 4, 2, 0]
[1, 2, 3, 4, 5] becomes [1, 2, 3, 4, 5, 4, 3, 2, 1]
[3, 5, 6, 7, 8] becomes [3, 5, 6, 7, 8, 7, 6, 5, 3]

Note: The last item of the original list should not be repeated in the mirrored list.
"""

# Antes eu tinha feito return a, a[-2::-1] e saiu um resultado que eu não esperava, e eu não consegui pensar na hora… 
# mas descobri agora que é só colocar a + a[-2::-1] e pronto, resolvido!

def mirror_array(a):
    """
    DOCSTRING:
    Recebe uma lista de inteiros e devolve a mesma lista
    seguida da sua versão invertida, sem repetir o último item.

    EXEMPLO:
    >>> mirror_array([0, 2, 4, 6])
    [0, 2, 4, 6, 4, 2, 0]

    """
    return a + a[-2::-1]


if __name__ == "__main__":
    print("---------- Mirror Array ----------")
    print("Digite inteiros separados por espaço ou vírgula.")
    print("Escreva 'sair' para encerrar ou 'help' para ajuda.\n")

    while True:
        texto = input("> ").strip().lower()
        
        if texto == "sair":
            print("\nEncerrando...\n")
            break
        if texto == "help":
            print(mirror_array.__doc__)
            continue
        if not texto:
            continue

        # remove colchetes, espaços extras e divide por espaço ou vírgula
        texto = texto.replace("[", "").replace("]", "")
        partes = [x.strip() for x in texto.replace(",", " ").split()]

        try:
            numeros = [int(x) for x in partes]
        except ValueError:
            print("❌ Digite apenas números inteiros, 'help' ou 'sair'.\n")
            continue

        resultado = mirror_array(numeros)
        print("Resultado:", resultado, "\n")