def group_by_length(palavras: list[str]) -> dict[int, list[str]]:
    """
    Agrupa as palavras por comprimento em um dicionário.

    Args:
        palavras (list[str]): Lista de palavras.

    Returns:
        dict[int, list[str]]: Dicionário onde as chaves são os tamanhos
        das palavras e os valores são listas com palavras desse tamanho.

    Exemplos:
        >>> group_by_length(["sol", "lua", "estrela"])
        {3: ["sol", "lua"], 7: ["estrela"]}
    """
    grupos = {}
    for palavra in palavras:
        tamanho = len(palavra)
        if tamanho not in grupos:
            grupos[tamanho] = []
        grupos[tamanho].append(palavra)
    return grupos


if __name__ == "__main__":
    palavras = ["sol", "lua", "estrela", "cro", "crowex", "rodrigo", "cacau", "nunu", "lulu"]
    resultado = group_by_length(palavras)
    print(resultado)
