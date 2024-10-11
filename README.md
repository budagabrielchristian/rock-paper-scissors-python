# README: Rock, Paper, Scissors Game

## Overview
This is a Python implementation of the classic game **Rock, Paper, Scissors**, with three difficulty levels: **Easy**, **Normal**, and **Impossible**. The game pits the player against the computer, with different outcomes depending on the chosen difficulty. 

- **Easy Mode**: The player always wins.
- **Normal Mode**: The game simulates a 50/50 chance, giving the player a fair shot.
- **Impossible Mode**: The computer almost always wins.

## Table of Contents
- [Installation](#installation)
- [How to Run](#how-to-run)
- [Game Description](#game-description)
  - [Difficulty Levels](#difficulty-levels)
  - [Game Logic](#game-logic)
- [Customization](#customization)
- [Contributing](#contributing)

---

## Installation

### Requirements
- Python 3.x
- No external libraries are needed as the game uses the standard Python library.

### Steps:
1. Clone the repository or download the Python files to your local machine.
   ```bash
   git clone https://github.com/yourusername/rock-paper-scissors-python.git
   ```
2. Navigate to the directory where the Python files are stored.
   ```bash
   cd rock-paper-scissors-python
   ```

---

## How to Run

You can run the Python script in your terminal or using any Python IDE:

```bash
python rock_paper_scissors.py
```

Once the game starts, follow the on-screen prompts to pick a difficulty and your option (rock, paper, or scissors).

---

## Game Description

### Difficulty Levels
The game allows the player to choose from three different difficulty levels:

1. **Easy** - The computer intentionally loses every round. This is the easiest difficulty, where the player will always win.
   
2. **Normal** - The computer plays fairly, with a 50/50 chance of winning. The computer may randomly decide to let the player win, choose the same option for a draw, or beat the player.

3. **Impossible** - The computer almost always chooses the option that beats the player. It rarely draws or loses, making it extremely difficult to win in this mode.

### Game Logic

1. **Player's Choice**:
   - The player selects their option (rock, paper, or scissors).
   
2. **Computer's Choice**:
   - The computer makes a choice based on the difficulty selected:
     - In **Easy Mode**, the computer picks the option that guarantees a win for the player.
     - In **Normal Mode**, the computer makes its choice randomly or lets the player win occasionally.
     - In **Impossible Mode**, the computer picks the option that beats the player's choice almost every time.
   
3. **Determine Winner**:
   - The game compares the player's option and the computer's option to determine the winner based on the following rules:
     - **Rock** beats **Scissors**
     - **Scissors** beats **Paper**
     - **Paper** beats **Rock**
   - If both the player and computer choose the same option, the result is a **draw**.

4. **Results**:
   - The game prints out the winner of the round and the computer’s choice after a short pause for suspense.

---

## Customization

### Changing Options
You can modify the options for the game by adjusting the choices in the `pick_option()` and `computer_option()` functions. For example, you can add options like "Lizard" or "Spock" from the expanded version of the game.

### Adjusting Difficulty Logic
To adjust how the computer chooses its options based on the difficulty level, modify the `computer_option()` function.

---

## Contributing

Contributions are welcome! If you'd like to improve the project or add new features, please:
1. Fork the repository.
2. Make your changes in a new branch.
3. Submit a pull request explaining the changes.

---

Enjoy the game, and may luck (or skill) be with you!
