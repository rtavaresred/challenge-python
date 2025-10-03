"""
Create a function named simulate_reaction that receives elements and quantities as its parameters.

You are a curious scientist exploring chemical reactions in a brightly lit laboratory. Your task is to simulate a simple chemical reaction experiment using the given elements and their quantities.

The function should perform the following operations in order:

1. Combine the first two elements in the list if their quantities allow it. This means adding their quantities and keeping only the first element's name.
2. Double the quantity of the third element (if it exists).
3. Reverse the order of the remaining elements and their quantities.
4. Remove any elements with zero quantity.
5. After performing these operations, create a new list where each element is represented as a string in the format "ElementQuantity" (e.g., "H2", "O1", "C3").

Parameters:

elements (list of str): A list of strings representing chemical elements (e.g., ["H", "O", "C", "N"]).
quantities (list of int): A list of integers representing the quantity of each element (e.g., [2, 1, 3, 1]).
The function returns a list of strings representing the final state of the elements after the reaction.
"""

# Hoje fiz o exercício quase todo certo, mas travei no final. Eu já sabia usar zip, mas não pensei em aplicá-lo aqui.
# Também não pensei em usar f-string para juntar elemento e quantidade em "N2", "C3", "H3".
# No fim, percebi que essas duas coisas eram justamente o que faltava. Acabei aprendendo +2 no mesmo exercício:
# como usar zip na prática e como aproveitar f-strings de forma simples. 🚀

def simulate_reaction(elements: list[str], quantities: list[int]) -> list[str]:
    """
    DOCSTRING:
    Simula uma reação química simplificada a partir de listas de elementos
    e suas respectivas quantidades.

    - Se houver 2 ou mais elementos: soma a quantidade do primeiro com o segundo
      e remove o segundo.
    - Se houver 3 ou mais elementos: dobra a quantidade do terceiro.
    - Inverte a ordem das listas.
    - Remove os itens cuja quantidade seja zero.
    - Retorna a lista formatada no padrão "ElementoQuantidade".

    EXEMPLO:
    >>> simulate_reaction(["H", "O", "C"], [2, 1, 3])
    ['C6', 'O1', 'H3']
    """
    # 1. Combine the first two elements in the list if their quantities allow it. This means adding their quantities and keeping only the first element's name.
    if len(elements) >= 2 and quantities[0] > 0:
        quantities[0] += quantities[1]
        del elements[1]
        del quantities[1]

    # 2. Double the quantity of the third element (if it exists).
    if len(elements) >= 3:
        quantities[2] *= 2

    # 3. Reverse the order of the remaining elements and their quantities.
    elements.reverse()
    quantities.reverse()

    # 4. Remove any elements with zero quantity.
    new_elements = []
    new_quantities = []
    for e, q in zip(elements, quantities):
        if q != 0:
            new_elements.append(e)
            new_quantities.append(q)

    # 5. After performing these operations, create a new list where each element is represented as a string in the format "ElementQuantity" (e.g., "H2", "O1", "C3").
    return [f"{e}{q}" for e, q in zip(new_elements, new_quantities)]

if __name__ == "__main__":
    print("---------- Simulate Reaction ----------")
    print("Digite elementos e quantidades separados por vírgula.")
    print("Exemplo: H,O,C 2,1,3")
    print("Escreva 'sair' para encerrar ou 'help' para ajuda.\n")

    while True:
        texto = input("> ").strip()

        if texto.lower() == "sair":
            print("\nEncerrando...\n")
            break
        elif texto.lower() == "help":
            print(simulate_reaction.__doc__)
            continue

        # Verificar entrada válida
        try:
            partes = texto.split()
            if len(partes) != 2:
                print("❌ Digite elementos e quantidades no formato: H,O,C 2,1,3\n")
                continue

            elements = [e.strip() for e in partes[0].split(",")]
            quantities = [int(q.strip()) for q in partes[1].split(",")]

            if len(elements) != len(quantities):
                print("❌ O número de elementos deve ser igual ao número de quantidades.\n")
                continue

        except ValueError:
            print("❌ Digite apenas números inteiros nas quantidades.\n")
            continue

        # Chamar a função
        resultado = simulate_reaction(elements, quantities)
        print("Resultado:", resultado, "\n")