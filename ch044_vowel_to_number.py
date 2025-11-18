# ch044_vowel_to_number.py
# Programa: Converte vogais para números semelhantes

def converter_vogais_para_numeros(texto: str) -> str:
    """
    Substitui apenas as vogais (a, e, i, o, u) por números semelhantes.

    Tabela usada:
    a -> 4
    e -> 3
    i -> 1
    o -> 0
    u -> 7

    Args:
        texto (str): Texto que será convertido.

    Returns:
        str: Texto convertido com vogais substituídas.

    Exemplos:
        >>> converter_vogais_para_numeros("casa")
        'c4s4'
        >>> converter_vogais_para_numeros("Eu estou bem")
        '3u 3st0u b3m'
        >>> converter_vogais_para_numeros("programar é divertido")
        'pr0gr4m4r é d1v3rt1d0'
    """

    mapa = {
        "a": "4", "A": "4",
        "e": "3", "E": "3",
        "i": "1", "I": "1",
        "o": "0", "O": "0",
        "u": "7", "U": "7"
    }

    novo_texto = ""
    for char in texto:
        novo_texto += mapa.get(char, char)

    return novo_texto


if __name__ == "__main__":
    print("Conversor de vogais para números (tipo c4s4, 3st0u, d1v3rt1d0)")
    print("Digite 'sair' ou vazio para encerrar.\n")

    while True:
        frase = input("Digite uma frase: ").strip()

        if frase.lower() in ["sair", ""]:
            print("Encerrando...")
            break

        print("Convertido:", converter_vogais_para_numeros(frase))
        print("-" * 40)
