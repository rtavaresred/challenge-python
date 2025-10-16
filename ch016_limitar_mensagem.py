def limitar_mensagem(texto: str, max_len: int = 20) -> str:
    """
    DOCSTRING:
    Limita o tamanho de uma mensagem sem cortar palavras no meio.
    Se a mensagem ultrapassar o limite, adiciona " ..." ao final.

    EXEMPLO:
    >>> limitar_mensagem("Olá, mundo maravilhoso!", 15)
    'Olá, mundo ...'
    >>> limitar_mensagem("Mensagem curta", 20)
    'Mensagem curta'
    """
    sufixo = " ..."
    texto = texto.strip()

    if len(texto) <= max_len:
        return texto

    temp = texto
    while len(temp) + len(sufixo) > max_len:
        new = temp.rsplit(" ", 1)[0]
        if new == temp:
            cut_len = max_len - len(sufixo)
            temp = temp[:cut_len].rstrip()
            break
        temp = new

    return temp + sufixo

if __name__ == "__main__":
    print("---------- Limit Message ----------")
    print("Digite uma mensagem e o limite de caracteres (opcional).")
    print("Exemplo: 'Olá mundo, tudo bem? / 10'")
    print("Escreva 'sair' para encerrar ou 'help' para ajuda.\n")

    while True:
        texto = input("> ").strip()

        if texto.lower() == "sair":
            print("\nEncerrando...\n")
            break
        elif texto.lower() == "help":
            print(limitar_mensagem.__doc__)
            continue

        if "/" in texto:
            partes = [p.strip() for p in texto.split("/", 1)]
            mensagem = partes[0]
            try:
                limite = int(partes[1])
            except ValueError:
                print("❌ O limite deve ser um número inteiro.\n")
                continue
        else:
            mensagem = texto
            limite = 20

        if not mensagem:
            print("❌ Digite uma mensagem válida.\n")
            continue

        resultado = limitar_mensagem(mensagem, limite)
        print(f"Resultado: {resultado}\n")