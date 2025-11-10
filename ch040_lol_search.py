# ch040_lol_search.py
# Programa: Busca campeões de LoL por nome parcial

def buscar_campeoes(parte: str, campeoes: list[str]) -> list[str]:
    """
    Retorna todos os campeões cujo nome contém a parte digitada (sem diferenciar maiúsculas/minúsculas).

    Args:
        parte (str): Parte do nome digitada pelo usuário.
        campeoes (list[str]): Lista de nomes de campeões.

    Returns:
        list[str]: Lista com os campeões que combinam.

    Exemplos:
        >>> buscar_campeoes("lux", ["Lux", "Lulu", "Leona"])
        ['Lux']
        >>> buscar_campeoes("ka", ["Katarina", "Kayle", "Yasuo"])
        ['Katarina', 'Kayle']
    """
    parte = parte.lower()
    return [c for c in campeoes if parte in c.lower()]


def main():
    campeoes = [
        "Ahri", "Akali", "Annie", "Ashe", "Aurelion Sol", "Braum", "Caitlyn",
        "Camille", "Cassiopeia", "Cho'Gath", "Darius", "Diana", "Draven",
        "Ekko", "Ezreal", "Fiora", "Fizz", "Galio", "Garen", "Gwen", "Jinx",
        "Kai'Sa", "Katarina", "Kayle", "Kayn", "LeBlanc", "Lee Sin", "Leona",
        "Lissandra", "Lulu", "Lux", "Malphite", "Master Yi", "Miss Fortune",
        "Morgana", "Nasus", "Nautilus", "Neeko", "Nidalee", "Ornn", "Pantheon",
        "Pyke", "Qiyana", "Riven", "Samira", "Senna", "Seraphine", "Sett",
        "Sona", "Soraka", "Swain", "Sylas", "Syndra", "Talon", "Teemo",
        "Thresh", "Tristana", "Tryndamere", "Twisted Fate", "Vayne", "Veigar",
        "Vel'Koz", "Vi", "Viego", "Viktor", "Vladimir", "Warwick", "Wukong",
        "Xayah", "Yasuo", "Yone", "Yuumi", "Zed", "Zeri", "Ziggs", "Zyra"
    ]

    print("---------- LoL Champion Search ----------")
    print("Digite parte do nome de um campeão para pesquisar (sem diferenciar maiúsculas/minúsculas).")
    print("Exemplo: 'lux' → Lux\n")

    while True:
        parte = input("Parte do nome (ou pressione Enter para 'sair'): ").strip()
        if not parte or parte == 'sair':
            print("\nEncerrando...\n")
            break

        resultados = buscar_campeoes(parte, campeoes)
        
        if resultados:
            print(f"\n✅ Campeões encontrados ({len(resultados)}):")
            for nome in resultados:
                print(" -", nome)
        else:
            print("❌ Nenhum campeão encontrado.\n")
        print()


if __name__ == "__main__":
    main()
