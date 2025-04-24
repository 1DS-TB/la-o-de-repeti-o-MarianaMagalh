import random

# jogador
hp = random.randint(200, 1000)
ataque_jogador = random.randint(1, 50)
ataque_robo = random.randint(1, 50)
defesa_jogador = random.randint(1, ataque_robo)
defesa_robo = random.randint(1, ataque_jogador)


while True:
    print("=== DUELO DE HERÓIS ===")
    print("[1] - Começar a jogar")
    print("[2] - Sair")

    op = int(input(""))

    if op == 2:
        print("Ate breve!!")
        break
    elif op == 1:

        jogador = {
            "hp": hp,
            "ataque": ataque_jogador,
            "defesa": defesa_jogador
        }

        robo = {
            "hp": hp,
            "ataque": ataque_robo,
            "defesa": defesa_robo
        }

        while jogador['hp'] > 0 and robo['hp'] > 0:
            print("\n=== VOCÊ ===")
            print(f"HP: {jogador['hp']}")
            print(f"ATQ: {jogador['ataque']}           DEF: {jogador['defesa']}\n")

            print("=== INIMIGO ===")
            print(f"HP: {robo['hp']}")
            print(f"ATQ: {robo['ataque']}           DEF: {robo['defesa']}")

            print("\n== Escolha! ===\n"
                  "[1] - Atacar\n"
                  "[2] - Curar")

            opcao_batalha = int(input(""))

            if opcao_batalha == 1:
                dano = jogador['ataque'] - robo['defesa']
                robo['hp'] -= dano

                print(f"Vc casou {dano} de dano!")
                print(f"O inimigo ficou com {robo['hp']} de vida")
            elif opcao_batalha == 2:
                cura = 20
                if jogador['hp'] + cura > hp:
                    jogador['hp'] = hp
                else:
                    jogador['hp'] += cura
                print(f"voce ficou com {jogador['hp']} de vida")
            else:
                print("opção invalida")

            if robo['hp'] <= 0:
                print("Voce venceu!")
                break

            opcao_batalha_robo = random.choice(['1', '2'])

            if opcao_batalha_robo == '1':
                dano = robo['ataque'] - jogador['defesa']
                jogador['hp'] -= dano

                print(f"O inimigo casou {dano} de dano em vc!")
                print(f"Vc ficou com {jogador['hp']} de vida!")
            elif opcao_batalha_robo == '2':
                cura = 20
                if robo['hp'] + cura > hp:
                    robo['hp']
                else:
                    robo['hp'] += cura
                print(f"o inimigo ficou com {robo['hp']} de vida")

            if jogador['hp'] <= 0:
                print("Voce perdeu!")
                break
