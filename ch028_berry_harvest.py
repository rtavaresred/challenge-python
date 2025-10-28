def berry_harvest(berry_row: str, start: int, end: int) -> str:
    """
    DOCSTRING:
    Analisa uma linha de plantações e informa quantas frutas de cada tipo
    (Strawberry, Blueberry, Raspberry) foram colhidas em um intervalo específico.

    Cada caractere da string representa uma fruta:
    - 'S' → Strawberry
    - 'B' → Blueberry
    - 'R' → Raspberry

    EXEMPLO:
    >>> berry_harvest("SSSSSS", 0, 6)
    'Harvest results: 6 Strawberries'
    >>> berry_harvest("SBRSBBRSBR", 0, 3)
    'Harvest results: 1 Strawberry, 1 Blueberry, 1 Raspberry'
    """
    harvested = berry_row[start:end]
    s_count = harvested.count('S')
    b_count = harvested.count('B')
    r_count = harvested.count('R')

    result = []
    if s_count > 0:
        result.append(f"{s_count} Strawberr{'y' if s_count == 1 else 'ies'}")
    if b_count > 0:
        result.append(f"{b_count} Blueberr{'y' if b_count == 1 else 'ies'}")
    if r_count > 0:
        result.append(f"{r_count} Raspberr{'y' if r_count == 1 else 'ies'}")

    return "Harvest results: " + ", ".join(result) if result else "No berries harvested."


if __name__ == "__main__":
    print("---------- Berry Harvest Analyzer ----------")
    print("Analisa uma fileira de frutas e mostra quantas de cada tipo foram colhidas.")
    print("Use 'S' para morangos, 'B' para mirtilos e 'R' para framboesas.")
    print("Formato: <fileira> <início> <fim>")
    print("Exemplo: SBRSBBRSBR 0 3")
    print("Escreva 'sair' para encerrar ou 'help' para ajuda.\n")

    while True:
        entrada = input("> ").strip()

        if entrada.lower() == "sair":
            print("\nEncerrando...\n")
            break
        elif entrada.lower() == "help":
            print(berry_harvest.__doc__)
            continue

        try:
            parts = entrada.split()
            if len(parts) != 3:
                print("❌ Use o formato: <fileira> <início> <fim>\nExemplo: SBRSBBRSBR 0 3\n")
                continue

            berry_row = parts[0].strip().upper()
            start = int(parts[1])
            end = int(parts[2])

            if start < 0 or end > len(berry_row) or start >= end:
                print("❌ Intervalo inválido. Certifique-se de que 0 ≤ início < fim ≤ tamanho da fileira.\n")
                continue

            resultado = berry_harvest(berry_row, start, end)
            print(f"Resultado: {resultado}\n")

        except ValueError:
            print("❌ Digite números válidos para o início e o fim.\n")
