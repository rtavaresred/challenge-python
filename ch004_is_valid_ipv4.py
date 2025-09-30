"""
Write a function is_valid_ipv4(ip_str) that takes a string ip_str as input and returns True
if the string represents a valid IPv4 address and False otherwise. A valid IPv4 address is in
the form of four decimal numbers separated by periods, where each number is between 0 and 255 inclusive.
"""

# Eu aprendi um novo método de string 'isdigit()' que retorna um valor booleano.

def is_valid_ipv4(ip_str: str) -> bool:
    """
    DOCSTRING:
    Verifica se uma string representa um endereço IPv4 válido.

    EXEMPLO:
    >>> is_valid_ipv4("192.168.0.1")
    True
    >>> is_valid_ipv4("999.10.10.20")
    False
    >>> is_valid_ipv4("abc.def.gha.bcd")
    False
    """
    parts = ip_str.split(".")

    if len(parts) != 4:
        return False

    for part in parts:
        if not part.isdigit():
            return False

        num = int(part)
        if num < 0 or num > 255:
            return False

    return True


if __name__ == "__main__":
    print("---------- IPv4 Validator ----------")
    print("Digite um endereço IPv4 para validar (ex: 192.168.0.1).")
    print("Escreva 'sair' para encerrar ou 'help' para ajuda.\n")

    while True:
        texto = input("> ").strip().lower()

        if texto == "sair":
            print("\nEncerrando...\n")
            break
        elif texto == "help":
            print(is_valid_ipv4.__doc__)
            continue

        # Verificar se entrada parece com IPv4
        if not any(c.isdigit() for c in texto):
            print("❌ Digite apenas um endereço IPv4 válido (ex: 192.168.0.1).\n")
            continue

        # Chamar a função
        resultado = is_valid_ipv4(texto)
        print("Resultado:", resultado, "\n")
