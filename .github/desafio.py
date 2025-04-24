import random

# Atributos iniciais aleatórios
hp = random.randint(200, 1000)
ataque_jogador1 = random.randint(1, 50)
ataque_jogador2 = random.randint(1, 50)
defesa_jogador1 = random.randint(1, ataque_jogador2)
defesa_jogador2 = random.randint(1, ataque_jogador1)

# Itens especiais
efeitos = {
    "1": {"nome": "Poção de Força", "efeito": "ataque +20", "turno": 2},
    "2": {"nome": "Poção de Regeneração", "efeito": "cura +50", "turno": 3},
    "3": {"nome": "Poção de Fraqueza", "efeito": "inimigo ataque -20", "turno": 2},
    "4": {"nome": "Parede de Fogo", "efeito": "defesa +50", "turno": 2}
}

# Jogadores
jogador1 = {"hp": hp, "ataque": ataque_jogador1, "defesa": defesa_jogador1}
jogador2 = {"hp": hp, "ataque": ataque_jogador2, "defesa": defesa_jogador2}

# Efeitos ativos
efeito_jogador1 = {"efeito": "", "duracao": 0}
efeito_jogador2 = {"efeito": "", "duracao": 0}

turno = 1  # Alterna os turnos entre 1 e 2

print("=== DUELO DE HERÓIS ===")
print("Jogador 1 e Jogador 2 se enfrentam!")

print("--- JOGADOR 1 ---")
print(f"HP: {jogador1['hp']}\n"
      f"ATQ: {jogador1['ataque']} | DEF: {jogador1['defesa']}\n")

print("--- JOGADOR 2 ---")
print(f"HP: {jogador2['hp']}\n"
      f"ATQ: {jogador2['ataque']} | DEF: {jogador2['defesa']}")

while jogador1["hp"] > 0 and jogador2["hp"] > 0:
    if turno == 1:
        # Aplica efeitos do jogador 1
        if efeito_jogador1["efeito"] == "1" and efeito_jogador1["duracao"] == 0:
            jogador1["ataque"] -= 20
            efeito_jogador1["efeito"] = ""
        elif efeito_jogador1["efeito"] == "3" and efeito_jogador1["duracao"] == 0:
            jogador2["ataque"] += 20
            efeito_jogador1["efeito"] = ""
        elif efeito_jogador1["duracao"] > 0:
            efeito_jogador1["duracao"] -= 1

        print("\n--- VEZ DO JOGADOR 1 ---")
        print("[1] - Atacar\n[2] - Curar\n[3] - Usar item")
        acao = input("Escolha sua ação: ")

        if acao == "1":
            dano = jogador1["ataque"] - jogador2["defesa"]
            if random.random() < 0.1:
                dano *= 2
                print("CRÍTICO!")
            jogador2["hp"] -= max(dano, 0)
            print(f"Você causou {dano} de dano! HP do jogador 2: {jogador2['hp']}")

        elif acao == "2":
            jogador1["hp"] = min(hp, jogador1["hp"] + 20)
            print(f"Você se curou. HP atual: {jogador1['hp']}")

        elif acao == "3":
            for k, v in efeitos.items():
                print(f"[{k}] {v['nome']} - {v['efeito']}")
            escolha = input("Escolha o item: ")

            if escolha == "1":
                jogador1["ataque"] += 20
                efeito_jogador1 = {"efeito": "1", "duracao": 2}
            elif escolha == "2":
                jogador1["hp"] = min(hp, jogador1["hp"] + 50)
            elif escolha == "3":
                jogador2["ataque"] -= 20
                efeito_jogador1 = {"efeito": "3", "duracao": 2}

        turno = 2

    else:
        # Aplica efeitos do jogador 2
        if efeito_jogador2["efeito"] == "1" and efeito_jogador2["duracao"] == 0:
            jogador2["ataque"] -= 20
            efeito_jogador2["efeito"] = ""
        elif efeito_jogador2["efeito"] == "3" and efeito_jogador2["duracao"] == 0:
            jogador1["ataque"] += 20
            efeito_jogador2["efeito"] = ""
        elif efeito_jogador2["duracao"] > 0:
            efeito_jogador2["duracao"] -= 1

        print("\n--- VEZ DO JOGADOR 2 ---")
        print("[1] Atacar\n[2] Curar\n[3] Usar item")
        acao = input("Escolha sua ação: ")

        if acao == "1":
            dano = jogador2["ataque"] - jogador1["defesa"]
            if random.random() < 0.1:
                dano *= 2
                print("CRÍTICO!")
            jogador1["hp"] -= max(dano, 0)
            print(f"Você causou {dano} de dano! HP inimigo: {jogador1['hp']}")

        elif acao == "2":
            jogador2["hp"] = min(hp, jogador2["hp"] + 20)
            print(f"Você se curou. HP atual: {jogador2['hp']}")

        elif acao == "3":
            for k, v in efeitos.items():
                print(f"[{k}] {v['nome']} - {v['efeito']}")
            escolha = input("Escolha o item: ")

            if escolha == "1":
                jogador2["ataque"] += 20
                efeito_jogador2 = {"efeito": "1", "duracao": 2}
            elif escolha == "2":
                jogador2["hp"] = min(hp, jogador2["hp"] + 50)
            elif escolha == "3":
                jogador1["ataque"] -= 20
                efeito_jogador2 = {"efeito": "3", "duracao": 2}

        turno = 1

# Fim de jogo
if jogador1["hp"] <= 0:
    print("\nJogador 2 venceu!")
elif jogador2["hp"] <= 0:
    print("\nJogador 1 venceu!")
