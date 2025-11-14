import random

def sortear_quartas():
    """
    Pergunta o time do usuário, adiciona à lista de times participantes
    e sorteia automaticamente um grupo de 4 times para as quartas-de-final.

    Grupos possíveis: A, B, C, D
    Cada grupo tem 4 times.
    """
    
    # Pergunta o time do usuário
    time_usuario = input("Qual é o seu time atual? ").strip()

    # Lista com 16 times (exemplo)
    times = [
        "Corinthians", "Palmeiras", "Santos", "Flamengo",
        "Fluminense", "Vasco", "Botafogo", "Grêmio",
        "Internacional", "Cruzeiro", "Atlético-MG", "Bahia",
        "Sport", "Athletico-PR", "Fortaleza", "Ceará"
    ]

    # Se o time do usuário já estiver na lista, não repete
    if time_usuario not in times:
        times.append(time_usuario)

    # Embaralha todos os times
    random.shuffle(times)

    # Cria os grupos de 4 times
    grupos = {
        "Grupo A": times[0:4],
        "Grupo B": times[4:8],
        "Grupo C": times[8:12],
        "Grupo D": times[12:16]
    }

    # Descobrir em qual grupo o time do usuário caiu
    grupo_do_usuario = None
    for nome_grupo, lista in grupos.items():
        if time_usuario in lista:
            grupo_do_usuario = nome_grupo
            break

    # Mostrar resultado
    print("\n--- RESULTADO DO SORTEIO ---")
    for nome_grupo, lista in grupos.items():
        print(f"{nome_grupo}: {', '.join(lista)}")

    print(f"\nSeu time **{time_usuario}** caiu no **{grupo_do_usuario}**!")
    print("----------------------------------")


if __name__ == "__main__":
    sortear_quartas()
