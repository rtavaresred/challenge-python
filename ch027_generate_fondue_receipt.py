def generate_fondue_receipt(customer_name, party_size, fondue_type):
    
    # Calculate the base cost: $25 per person for cheese fondue, $30 for chocolate, and $35 for oil.
    prices = {
        'cheese': 25,
        'chocolate': 30,
        'oil': 35
    }

    price = prices[fondue_type]
    
    discount = 0.1 if party_size >= 4 else 0
    discount_str = 'Discount Applied: 10%' if discount else 'No Discount Applied'

    total = (price * party_size) * (1 - discount)

    # Calculate a "lucky number" by summing the ASCII values of the customer's name and dividing by the name's length, rounded to the nearest integer.
    # Asked chatGPT about lucky number to solve it for me
    name = customer_name.strip()
    total_ascii = sum(ord(char) for char in name)
    lucky_number = round(total_ascii / len(name))
    # End of chatGPT

    # Format the receipt using string formatting techniques.

    print(f"Fondue Receipt for {customer_name}")
    print(f"Party Size: {party_size}")
    print(f"Fondue Type: {fondue_type.title()}")
    print(f"Base Cost: ${price:.2f} per person")
    print(discount_str)
    print(f"Total Cost: ${total:.2f}")
    print(f"Lucky Number: {lucky_number}")
    print("Thank you for dining with us!")


if __name__ == "__main__":
    print("---------- Cozy Fondue Receipt Generator ----------")
    print("Gera um recibo de fondue com total, desconto e número da sorte.")
    print("Digite 'sair' a qualquer momento para encerrar.\n")

    prices = {
        'cheese': 25,
        'chocolate': 30,
        'oil': 35
    }

    while True:
        nome = input("Qual é seu nome? ").strip()
        nome = nome.title()
        if nome.lower() == "sair":
            print("\nEncerrando...\n")
            break

        try:
            tamanho_str = input("\nTamanho do grupo? ").strip()
            if tamanho_str.lower() == "sair":
                print("\nEncerrando...\n")
                break
            tamanho = int(tamanho_str)
        except ValueError:
            print("❌ Digite um número válido para o tamanho do grupo.\n")
            continue

        print("\nTipos de fondue disponíveis:")
        for indice, (tipo, preco) in enumerate(prices.items(), 1):
            print(f"{indice} - {tipo} (${preco:.2f})")

        while True:
            escolha = input("\nEscolha seu fondue (1 a 3): ").strip().lower()
            if escolha == "sair":
                print("\nEncerrando...\n")
                exit()

            if escolha in ["1", "2", "3"]:
                tipo = list(prices.keys())[int(escolha) - 1]
                break
            else:
                print("❌ Opção inválida! Digite 1, 2 ou 3.")

        print(f"\n{'-' * 10}[ RECEIPT ]{'-' * 10}")
        generate_fondue_receipt(nome, tamanho, tipo)
        break
