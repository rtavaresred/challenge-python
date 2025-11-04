def create_mixed_string(s1: str, s2: str) -> str:
    """
    DOCSTRING:
    Cria uma nova string combinando duas strings conforme as regras:
    - Pega o primeiro caractere de s1, depois o último de s2;
    - Em seguida o segundo de s1, e o penúltimo de s2, e assim por diante.
    - Qualquer caractere restante é adicionado ao final.

    EXEMPLO:
    >>> create_mixed_string("Cro", "Wex")
    'Cxreow'
    >>> create_mixed_string("Abc", "Xyz")
    'Azbycx'
    """
    s1_length = len(s1)
    s2_length = len(s2)
    length = max(s1_length, s2_length)
    result = ""

    # inverte s2
    s2 = s2[::-1]

    # combina caracteres conforme regras
    for i in range(length):
        if i < s1_length:
            result += s1[i]
        if i < s2_length:
            result += s2[i]

    return result


if __name__ == "__main__":
    print("---------- Mixed String Creator ----------")
    print("Cria uma string combinando duas outras (primeiro de s1 + último de s2).")
    print("Exemplo: Cro Wex → Cxreow")
    print("Escreva 'sair' para encerrar ou 'help' para ajuda.\n")

    while True:
        entrada = input("> ").strip()

        if entrada.lower() == "sair":
            print("\nEncerrando...\n")
            break
        elif entrada.lower() == "help":
            print(create_mixed_string.__doc__)
            continue

        try:
            parts = entrada.split()
            if len(parts) != 2:
                print("❌ Digite duas palavras separadas por espaço (ex: Cro Wex)\n")
                continue

            s1, s2 = parts
            resultado = create_mixed_string(s1, s2)
            print(f"Resultado: {resultado}\n")

        except Exception as e:
            print(f"❌ Erro: {e}\n")
