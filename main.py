import string
import random
import time

difficulty = 0

def pick_a_difficulty():
    global difficulty
    choice = int(input("PICK A DIFFICULTY\n\n [1] EASY\n\n [2] NORMAL\n\n [3] IMPOSSIBLE\n\n"))
    if(choice == 1):
        difficulty = 1
    elif(choice == 2):
        difficulty = 2
    elif(choice == 3):
        difficulty = 3

def pick_option():
    choice = int(input("TIME TO CHOOSE AGAINST YOUR OPPONENT!\n\n [1] ROCK\n\n [2] PAPER\n\n [3] SCISSORS\n\n"))
    if(choice == 1):
        return "ROCK"
    elif(choice == 2):
        return "PAPER"
    elif(choice == 3):
        return "SCISSORS"

def computer_option(player_option:string):
    global difficulty
    if(difficulty != 0):

        if(difficulty == 1):
            if(player_option == "ROCK"):
                return "SCISSORS"
            elif(player_option == "PAPER"):
                return "ROCK"
            else:
                return "PAPER"
            
        elif(difficulty == 2):
            let_player_win = random.randint(1, 3)
            if(let_player_win == 1):
                difficulty = 1
                computer_option(player_option)
            elif(let_player_win == 2):
                if(player_option == "ROCK"):
                    return "PAPER"
                elif(player_option == "PAPER"):
                    return "SCISSORS"
                else:
                    return "ROCK"
            else:
                return player_option
                
        else:
            if(player_option == "ROCK"):
                return "PAPER"
            elif(player_option == "PAPER"):
                return "SCISSORS"
            else:
                return "ROCK"

def compute_winner(player_option:string, computer_option:string):
    if(computer_option == player_option):
        return "DRAW"

    if player_option == "PAPER":
        if computer_option == "ROCK":
            return "PLAYER"
        else:
            return "COMPUTER"
        
    elif player_option == "ROCK":
        if computer_option == "SCISSORS":
            return "PLAYER"
        else:
            return "COMPUTER"
    else:
        if computer_option == "PAPER":
            return "PLAYER"
        else:
            return "COMPUTER"
    

if __name__ == "__main__":
    pick_a_difficulty()
    player_option = pick_option()
    computer_option = computer_option(player_option)

    if computer_option == "ROCK":
        print("The computer has picked Rock.")
    elif computer_option == "PAPER":
        print("The computer has picked Paper.")
    elif computer_option == "SCISSORS":
        print("The computer has picked Scissors.")

    time.sleep(3)
    final_result = compute_winner(player_option, computer_option)

    if final_result == "PLAYER":
        print("The winner is... You, actually! Well done!")
    elif final_result == "COMPUTER":
        print("The winner is... The computer. Tough luck!")
    elif final_result == "DRAW":
        print("The winner is... Oh? It appers to be a draw. Tough luck or good luck?")