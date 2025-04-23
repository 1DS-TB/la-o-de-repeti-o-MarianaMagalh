import random

# jogador
hp = random.randint(200, 1000)
ataque_jogador = random.randint(1, 50)
ataque_robo = random.randint(1, 50)
defesa_jogador = random.randint(1, ataque_robo)
defesa_robo = random.randint(1, ataque_jogador)

contador = 0

itens = {
    "1": {"nome": "Poção de Força", "efeito": "ataque + 20", "turno": 2},
    "2": {"nome": "Poção de regeneração", "efeito": "vida + 50", "turno": 3},
    "3": {"nome": "Poção de Fraqueza", "efeito": "ataque robo - 20", "turno": 2}
}

efeito_jogador = {
    "efeito": "",
    "duracao": 0
}

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

            if efeito_jogador['efeito'] == '1':
                if efeito_jogador['duracao'] > 0:
                    efeito_jogador['duracao'] -= 1
                else:
                    jogador['ataque'] -= 20
                    efeito_jogador['efeito'] = ''
            if efeito_jogador['efeito'] == '2':
                if efeito_jogador['duracao'] > 0:
                    efeito_jogador['duracao'] -= 1
                    jogador += 50
                else:
                    jogador['ataque'] -= 20
            if efeito_jogador['efeito'] == '3':
                if efeito_jogador['duracao'] > 0:
                    efeito_jogador['duracao'] -= 1
                else:
                    jogador['ataque'] += 20
                    efeito_jogador['efeito'] = ''

            print("\n== Escolha! ===\n"
                  "[1] - Atacar\n"
                  "[2] - Curar\n"
                  "[3] - Itens Especiais")

            opcao_batalha = int(input(""))

            if opcao_batalha == 1:
                dano = jogador['ataque'] - robo['defesa']
                if random.random() < 0.1:
                    dano *= 2
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

            elif opcao_batalha == 3:

                print("Itens disponiveis:")
                for chave,valor in itens.items():
                    print(f"[{chave} {valor['nome']} - {valor['efeito']}")
                escolha_item = input("Escolha um item: ")

                if escolha_item == "1":
                    jogador['ataque'] += 20
                    efeito_jogador['efeito'] = '1'
                    efeito_jogador['duracao'] = 2
                    print("ataque aumentado por 2 turnos!")
                elif escolha_item == "2":
                    jogador['hp'] += 50
                    efeito_jogador['efeito'] = '2'
                    efeito_jogador['duracao'] = 3
                    print("Cura aumentada em 50 por 3 turnos!")
                elif escolha_item == "3":
                    robo['ataque'] -= 20
                    efeito_jogador['efeito'] = '3'
                    efeito_jogador['duracao'] = 2
                    print("Ataque inimigo diminuido em 20 por 2 turno!!")

            else:
                print("opção invalida")

            if robo['hp'] <= 0:
                print("Voce venceu!")
                break

            opcao_batalha_robo = random.choice(['1', '2'])

            if opcao_batalha_robo == '1':
                dano = robo['ataque'] - jogador['defesa']
                if random.random() < 0.1:
                    dano *= 2
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




