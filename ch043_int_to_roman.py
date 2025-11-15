def int_to_roman(num: int) -> str:
    """
    Converte um número inteiro (1 a 3999) para algarismos romanos.

    Args:
        num (int): Número inteiro entre 1 e 3999.

    Returns:
        str: Representação em algarismos romanos.

    Exemplos:
        >>> int_to_roman(4)
        'IV'
        >>> int_to_roman(2024)
        'MMXXIV'
    """

    if not 1 <= num <= 3999:
        raise ValueError("O número deve estar entre 1 e 3999.")

    valores = [
        (1000, "M"),
        (900,  "CM"),
        (500,  "D"),
        (400,  "CD"),
        (100,  "C"),
        (90,   "XC"),
        (50,   "L"),
        (40,   "XL"),
        (10,   "X"),
        (9,    "IX"),
        (5,    "V"),
        (4,    "IV"),
        (1,    "I")
    ]

    resultado = ""
    for valor, romano in valores:
        while num >= valor:
            resultado += romano
            num -= valor
    return resultado


if __name__ == "__main__":
    print("Conversor de números para romanos (1 a 3999)")
    print("Digite 'sair' para encerrar.\n")

    while True:
        entrada = input("Digite um número: ").strip()

        if entrada.lower() in ["sair", ""]:
            print("Encerrando...")
            break

        if not entrada.isdigit():
            print("Por favor, digite apenas números!")
            continue

        numero = int(entrada)

        try:
            romano = int_to_roman(numero)
            print(f"{numero} → {romano}\n")
        except ValueError as e:
            print(f"Erro: {e}\n")
