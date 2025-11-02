def find_digits_chars_symbols(sample_str: str) -> str:
    """
    DOCSTRING:
    Conta quantas letras, dígitos e símbolos existem em uma string.
    Letras são reconhecidas por `isalpha()`, dígitos por `isdigit()` e o restante como símbolo.

    EXEMPLOS:
    >>> find_digits_chars_symbols("P@yn2at&#i5ve")
    'Chars = 8, Digits = 2, Symbols = 3'
    """
    char_count = 0
    digit_count = 0
    symbol_count = 0

    for char in sample_str:
        if char.isalpha():
            char_count += 1
        elif char.isdigit():
            digit_count += 1
        else:
            symbol_count += 1

    return f"Chars = {char_count}, Digits = {digit_count}, Symbols = {symbol_count}"


if __name__ == "__main__":
    print("---------- Character, Digit & Symbol Counter ----------")
    print("Conta letras, números e símbolos especiais em uma string.")
    print("Exemplo: P@yn2at&#i5ve")
    print("Escreva 'sair' para encerrar ou 'help' para ajuda.\n")

    while True:
        texto = input("> ").strip()

        if texto.lower() == "sair":
            print("\nEncerrando...\n")
            break
        elif texto.lower() == "help":
            print(find_digits_chars_symbols.__doc__)
            continue

        if not texto:
            print("❌ Digite algum texto para análise.\n")
            continue

        resultado = find_digits_chars_symbols(texto)
        print(f"Resultado: {resultado}\n")
