def detectar_spam(email: str) -> str:
    """
    DOCSTRING:
    Verifica se um endereço de e-mail é considerado spam.
    Critério: termina com "@xyz.com".

    EXEMPLOS:
    >>> detectar_spam("usuario1@empresa.com")
    'O email de usuario1@empresa.com não é spam.'
    >>> detectar_spam("usuario2@xyz.com")
    'O email de usuario2@xyz.com é spam.'
    """
    if email.endswith("@xyz.com"):
        return f"O email de {email} é spam."
    else:
        return f"O email de {email} não é spam."


if __name__ == "__main__":
    print("---------- Detecção de Spam ----------")
    print("Digite um endereço de e-mail para verificar se é spam (termina com '@xyz.com').")
    print("Exemplo: usuario@empresa.com")
    print("Escreva 'sair' para encerrar ou 'help' para ajuda.\n")

    while True:
        texto = input("> ").strip()

        if texto.lower() == "sair":
            print("\nEncerrando...\n")
            break
        elif texto.lower() == "help":
            print(detectar_spam.__doc__)
            continue

        if "@" not in texto or "." not in texto:
            print("❌ Digite um e-mail válido no formato nome@dominio.com\n")
            continue

        resultado = detectar_spam(texto)
        print(f"{resultado}\n")
