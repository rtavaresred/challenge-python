"""
A valid email address:

Contains a username part, followed by an @ symbol, and a domain name part, separated by a single dot.
The username part can include letters, digits, dashes, and underscores, but it cannot start or end with a dash or underscore.
The domain name part can include letters, digits, and dashes, but it must contain at least one letter after the dot.
"""
import re

def is_valid_email(email: str) -> bool:
    """
    DOCSTRING:
    Verifica se uma string representa um endereço de e-mail válido.
    O formato deve incluir um nome de usuário, o símbolo '@' e um domínio válido.

    EXEMPLO:
    >>> is_valid_email("usuario@gmail.com")
    True
    >>> is_valid_email("teste@dominio")
    False
    >>> is_valid_email("invalido@@gmail.com")
    False
    """
    pattern = r'^[a-zA-Z0-9._-]+@[a-zA-Z0-9-]+\.[a-zA-Z]+$'
    return bool(re.match(pattern, email))


if __name__ == "__main__":
    print("---------- Email Validator ----------")
    print("Digite um endereço de e-mail para validar (ex: usuario@gmail.com).")
    print("Escreva 'sair' para encerrar ou 'help' para ajuda.\n")

    while True:
        texto = input("> ").strip()

        if texto.lower() == "sair":
            print("\nEncerrando...\n")
            break
        elif texto.lower() == "help":
            print(is_valid_email.__doc__)
            continue

        # Verificar se entrada parece um e-mail
        if "@" not in texto or "." not in texto:
            print("❌ Digite um e-mail válido no formato nome@dominio.com\n")
            continue

        resultado = is_valid_email(texto)
        print("Resultado:", resultado, "\n")