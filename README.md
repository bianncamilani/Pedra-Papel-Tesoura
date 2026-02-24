# Pedra, Papel e Tesoura

Este é um jogo simples de Pedra, Papel e Tesoura, desenvolvido em Python para a disciplina de LCI (Laboratório de Computação I). O jogo utiliza entrada do usuário e escolha aleatória do computador para simular uma partida clássica, com emojis divertidos para deixar a experiência mais visual.

Como o jogo funciona

O usuário escolhe entre:

- pedra 🪨

- papel 📃

- tesoura ✂️

O computador escolhe uma jogada aleatória.

O programa compara as escolhas e determina:

- Empate

- Vitória do jogador

- Vitória do computador

Funcionalidades

 Emojis para representar as jogadas

- Validação da entrada do usuário

- Escolha aleatória do computador

- Lógica completa das regras do jogo

- Feedback imediato do resultado

Tecnologias Utilizadas

- Python 3

- Biblioteca padrão random

Código Principal (resumo)
opcoes = {
    "pedra": "🪨",
    "papel": "📃",
    "tesoura": "✂️"
}

jogador = input("Sua jogada: ").lower()
computador = random.choice(list(opcoes.keys()))

Autor(a)

- Bianca Milani
