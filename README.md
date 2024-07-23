### README

# Turn-Based Card Game with Tiers

## Introduction

This repository contains a simple implementation of a turn-based card game, inspired by the traditional card game "Truco". The game is designed for 2 to 6 players and includes a ranking system for the cards. The game logic is written in Python and utilizes the `colorama` library for colored terminal output.

## Game Rules

1. **Players**: The game supports 2 to 6 players.
2. **Cards**: The deck consists of 40 cards (1-7, 10-12) from four suits: Oros, Copas, Bastos, and Espadas. The cards 8 and 9 are not used.
3. **Card Hierarchy**:
   - 1 de Espadas (Highest)
   - 1 de Bastos
   - 7 de Espadas
   - 7 de Oros
   - 3 of any suit
   - 2 of any suit
   - 1 de Copas and 1 de Oros
   - 12 of any suit
   - 11 of any suit
   - 10 of any suit
   - 7 de Copas and 7 de Bastos
   - 6 of any suit
   - 5 of any suit
   - 4 of any suit
4. **Rounds**: The game is played in rounds. Each player gets 3 cards per round. The player with the highest-ranking card wins the round.
5. **Winning the Game**:
   - A player who wins 2 rounds is declared the winner.
   - If different players win the first two rounds, a third round is played to determine the winner.
   - If there is a tie in the number of rounds won after the third round, the game is declared a tie between those players.

## How to Play

1. **Setup**: Run the Python script. The program will prompt you to enter the number of players (2 to 6).
2. **Card Distribution**: The program randomly distributes 3 cards to each player.
3. **Playing a Round**: 
   - Players take turns to choose and play a card from their hand.
   - The player with the highest-ranking card wins the round.
   - In case of a tie, the tied players play another card until a winner is determined for that round.
4. **Winning**:
   - The first player to win 2 rounds is the winner.
   - If no player wins 2 rounds in the first 2 rounds, a third round is played.
   - If there is a tie after the third round, the game is declared a tie.

## Code Overview

- **Card Hierarchy**: Defined using a dictionary `jerarquia` with cards as keys and their ranks as values.
- **Card Distribution**: The function `distribuircartas` handles the random distribution of cards to players.
- **Display Cards**: The function `mostrar_cartas` prints each player's hand.
- **Player Choice**: The function `elegir_carta` allows players to choose a card to play.
- **Play Rounds**: 
  - The function `jugar_ronda` manages the logic for playing a single round and determining the winner.
  - The function `jugar_desempate` handles tie-breaker rounds.
- **Game Loop**: The main loop runs through the rounds, checks for winners, and handles the game flow.

## Running the Game

To run the game, ensure you have Python installed. Additionally, install the `colorama` library if you haven't already:

```sh
pip install colorama
```

Run the script:

```sh
python card_game.py
```

Follow the prompts to enter the number of players and play the game.

## Example Output

```
=============================
Bienvenido al Juego de Cartas
=============================

Cantidad de jugadores (2 a 6): 3

Jugador 1:  3 de Oros         5 de Espadas      1 de Bastos     
Jugador 2:  7 de Espadas      12 de Copas       10 de Bastos    
Jugador 3:  2 de Copas        4 de Bastos       1 de Oros       

========
Ronda 1
========

Jugador 1
Tus cartas son: 3 de Oros, 5 de Espadas, 1 de Bastos
Elige una carta para tirar: 1 de Bastos

< Jugador 1 tira 1 de Bastos >

Jugador 2
Tus cartas son: 7 de Espadas, 12 de Copas, 10 de Bastos
Elige una carta para tirar: 7 de Espadas

< Jugador 2 tira 7 de Espadas >

Jugador 3
Tus cartas son: 2 de Copas, 4 de Bastos, 1 de Oros
Elige una carta para tirar: 1 de Oros

< Jugador 3 tira 1 de Oros >

El ganador de la ronda 1 es el: Jugador 2
...
¡El ganador final es el Jugador 2 con 2 rondas ganadas!
```

Enjoy the game!

---

Feel free to modify and extend the code as needed. Contributions are welcome!
