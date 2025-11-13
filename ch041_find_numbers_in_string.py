import re

def find_numbers_in_string(texto: str) -> list[int]:
    """
    Extrai todos os números inteiros presentes em uma string.

    Args:
        texto (str): Texto que pode conter números misturados com palavras.

    Returns:
        list[int]: Lista de números inteiros encontrados no texto.

    Exemplos:
        >>> find_numbers_in_string("Eu tenho 2 gatos e 14 peixes")
        [2, 14]
        >>> find_numbers_in_string("Nenhum número aqui!")
        []
        >>> find_numbers_in_string("Hoje é dia 12 e são 23 horas")
        [12, 23]
    """
    return [int(n) for n in re.findall(r'\d+', texto)]


if __name__ == "__main__":
    print("---------- Find Numbers in String ----------")
    print("Extrai todos os números inteiros presentes em um texto.")
    print("Digite qualquer frase contendo números.")
    print("Escreva 'sair' ou pressione Enter para encerrar.\n")

    # Exemplo inicial
    exemplo = "Eu tenho 2 gatos e 14 peixes"
    print(f"Exemplo: {exemplo}")
    print("Resultado:", find_numbers_in_string(exemplo))
    print("-" * 40)

    # Loop interativo
    while True:
        texto = input("> ").strip()
        if not texto or texto.lower() == "sair":
            print("\nEncerrando o programa...\n")
            break

        numeros = find_numbers_in_string(texto)
        print("Números encontrados:", numeros if numeros else 'nenhum número.')
        print("-" * 40)