import random

cura = random.randint(1, 50)

# jogador
vida_jogador = random.randint(200, 1000)
ataque_jogador = random.randint(1, 50)

# robô
vida_robo = random.randint(200, 1000)
ataque_robo = random.randint(1, 50)

while True:
    print("=== DUELO DE HERÓIS ==="
          "[1] - Começar a jogar"
          "[2] - Sair\n")
    op = int(input(""))

    if op == 1:
        print("=== Escolha! ==="
              "[1] - Atacar"
              "[2] - Curar")

        opcao_batalha = int(input(""))

        if opcao_batalha == 1:
            ataque_jogador -= vida_robo
        else:
            if opcao_batalha == 2:
                cura += vida_jogador
            else:
                print("Opção invalida")

        escolha_robo = random.randint(['atacar','curar'])

        if escolha_robo == 'atacar':
            ataque_robo -= vida_jogador
        else:
            if escolha_robo == 'curar':
                cura += vida_robo
            else:
                print("Opção invalida")




"""

se robo escolheu atacar:
   dano = ataque_robo - defesa_jogador
   vida_jogador -= dano

"""