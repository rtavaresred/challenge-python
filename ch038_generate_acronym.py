def generate_acronym(frase: str) -> str:
    """
    Gera um acrônimo (sigla) a partir das palavras de uma frase.

    Args:
        frase (str): Frase de onde será gerado o acrônimo.

    Returns:
        str: Acrônimo formado pelas letras iniciais das palavras.

    Exemplos:
        >>> generate_acronym("São Paulo Futebol Clube")
        'SPFC'
    """
    # Palavras comuns que geralmente não entram em siglas
    ignorar = {"de", "da", "do", "das", "dos", "e"}
    palavras = frase.split()
    letras = [p[0].upper() for p in palavras if p.lower() not in ignorar]
    return "".join(letras)


if __name__ == "__main__":
    print("\nExemplo: São Paulo Futebol Clube")
    print(f"Resultado será: {generate_acronym('São Paulo Futebol Clube')}\n")
    print("Digite frases para gerar acrônimo (pressione Enter para sair).")
    while True:
        frase = input("\nFrase: ").strip()
        if not frase:
            print("Encerrando...")
            break
        resultado = generate_acronym(frase)
        print(f"Acrônimo: {resultado}")
