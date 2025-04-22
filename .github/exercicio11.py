import random

cura = random.randint(1, 50)

# jogador
vida_jogador = random.randint(200, 1000)
ataque_jogador = random.randint(1, 50)
defesa_jogador = random.randint(1, 50)

# robô
vida_robo = random.randint(200, 1000)
ataque_robo = random.randint(1, 50)
defesa_robo = random.randint(1, 50)

while True:
    print("=== DUELO DE HERÓIS ===")
    print("[1] - Começar a jogar")
    print("[2] - Sair")

    op = int(input(""))

    print("=== DUELO DE HERÓIS ===")
    print("=== VOCÊ ===")
    print(f"HP: {vida_jogador}")
    print(f"ATQ: {ataque_jogador}           DEF: {defesa_jogador}\n")

    print("=== INIMIGO ===")
    print(f"HP: {vida_robo}")
    print(f"ATQ: {ataque_robo}           DEF: {defesa_robo}")

    if op == 1:
        print("\n== Escolha! ==="
              "[1] - Atacar"
              "[2] - Curar")

        opcao_batalha = int(input(""))

        if opcao_batalha == 1:
            dano = ataque_jogador - vida_robo
            vida_robo -= dano
            print(f"Você ataca! Inimigo perde {vida_robo} HP.")
        else:
            if opcao_batalha == 2:
                cura += vida_jogador

                print(f"Você se cura em {cura} HP!")
            else:
                print("Opção invalida")

        escolha_robo = random.choices(['atacar','curar'])

        if escolha_robo == 'atacar':
            dano = ataque_robo - defesa_jogador
            vida_jogador -= dano

            print(f"Inimigo atacar! Você perde {vida_jogador} HP.")
        else:
            if escolha_robo == 'curar':
                cura += vida_robo

                print(f"Inimigo se cura em {cura} HP!")
            else:
                print("Opção invalida")

    else:
        if op == 2:
            print("Você saiu do jogo!")
            break




