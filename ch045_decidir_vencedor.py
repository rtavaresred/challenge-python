# ch045_torneio_futebol.py
# Programa: Torneio de futebol com semifinal, final e decisão por pênaltis

import random

first_time = True

def decidir_vencedor(time1: str, time2: str) -> str:
    """
    Recebe dois times, pergunta o placar, trata empate, pênaltis
    e retorna o time vencedor.

    Args:
        time1 (str): Nome do primeiro time.
        time2 (str): Nome do segundo time.

    Returns:
        str: Nome do time vencedor.

    Exemplos:
        (Supondo entrada do usuário)
        >>> decidir_vencedor("A", "B")
        Digite o placar (ex: 2x0): 1x1
        Pênaltis (ex: 5x3): 4x5
        'B'
    """
    global first_time

    print(f"\nJogo: {time1} x {time2}")
    placar = input(f"Digite o placar{' (ex: 2x0)' if first_time else ':'} ").strip().lower()
    first_time = False

    # Separar placar
    g1, g2 = placar.split("x")
    g1, g2 = int(g1), int(g2)

    if g1 > g2:
        return time1
    elif g2 > g1:
        return time2

    # EMPATE
    print("Empatou! Vamos para os pênaltis!")
    pen = input("Pênaltis (ex: 5x3): ").strip().lower()
    p1, p2 = pen.split("x")
    p1, p2 = int(p1), int(p2)

    if p1 > p2:
        return time1
    else:
        return time2


def torneio_semifinal_e_final():
    """
    Sorteia 4 times entre 12 disponíveis,
    monta a semifinal, pergunta os placares,
    define os vencedores e descobre o campeão do torneio.

    Retorna:
        None — apenas exibe o andamento e resultado final.
    """

    times = [
        "São Paulo", "Corinthians", "Palmeiras", "Santos",
        "Flamengo", "Fluminense", "Vasco", "Grêmio",
        "Inter", "Cruzeiro", "Atlético-MG", "Athletico-PR"
    ]

    # Sorteio dos semifinalistas
    semifinalistas = random.sample(times, 4)

    print("\n=== TIMES SORTEADOS PARA SEMIFINAL ===")
    for t in semifinalistas:
        print("-", t)

    # Confrontos
    jogo1_t1, jogo1_t2 = semifinalistas[0], semifinalistas[1]
    jogo2_t1, jogo2_t2 = semifinalistas[2], semifinalistas[3]

    print("\n=== SEMIFINAL ===")
    print(f"Jogo 1: {jogo1_t1} x {jogo1_t2}")
    print(f"Jogo 2: {jogo2_t1} x {jogo2_t2}")

    # Decidir vencedores
    finalista1 = decidir_vencedor(jogo1_t1, jogo1_t2)
    finalista2 = decidir_vencedor(jogo2_t1, jogo2_t2)

    # FINAL
    print("\n=== FINAL ===")
    print(f"{finalista1} x {finalista2}")

    campeao = decidir_vencedor(finalista1, finalista2)

    print("\n=== CAMPEÃO DO TORNEIO ===")
    print("🏆", campeao, "🏆")
    print('')


if __name__ == "__main__":
    torneio_semifinal_e_final()
