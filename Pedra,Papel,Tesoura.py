import random

opcoes = {
    "pedra": "🪨",
    "papel": "📃",
    "tesoura": "✂️"
}

jogadas = list(opcoes.keys())

print("Bem-vindo ao jogo!🎮")
print("Escolha: pedra🪨, papel📃, tesoura✂️")

jogador = input("Sua jogada: ").lower()

if jogador not in jogadas:
    print("Jogada inválida!")
else:
    computador = random.choice(jogadas)
    print(f"Você jogou {opcoes[jogador]} vs {opcoes[computador]} Computador")

    if jogador == computador:
        print("Empate")
    elif (jogador == "pedra" and computador == "tesoura") or \
         (jogador == "papel" and computador == "pedra") or \
         (jogador == "tesoura" and computador == "papel"):
        print("Você venceu!")
    else:
        print("Você perdeu!")