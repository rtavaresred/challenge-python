"""
ch036_count_consonants.py  
Conta quantas consoantes existem em uma string.

Exemplo:
    count_consonants("Crowex") → 4
"""

def count_consonants(text: str) -> int:
    """
    Conta o número de consoantes em uma string.
    
    Args:
        text (str): Texto de entrada.
        
    Returns:
        int: Quantidade de consoantes encontradas.
    """
    consonants = "bcdfghjklmnpqrstvwxyz"
    return sum(1 for c in text.lower() if c in consonants)

if __name__ == "__main__":
    palavra = "Crowex"
    resultado = count_consonants(palavra)
    print(f"'{palavra}' possui {resultado} consoantes.\n")

    print("Digite qualquer palavra ou frase para calcular quantas consoantes ela possui.")
    print("(Digite 'sair' para encerrar ou 'help' para ver a explicação da função.)\n")

    while True:
        entrada = input("> ").strip()

        if entrada.lower() == "sair":
            print("\nEncerrando...\n")
            break
        elif entrada.lower() == "help":
            print(count_consonants.__doc__)
            continue

        resultado = count_consonants(entrada)
        print(f"'{entrada}' possui {resultado} consoantes.\n")
