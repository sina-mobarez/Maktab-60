# we wat to write a game 
import random
print(" rock ")
print(" paper ")
print(" cutter ")

randomNumber = random.randint(0, 2)
cumputerMove = "rock"

if randomNumber == 0 :
    computerMove = "rock"
elif randomNumber == 1 :
    computerMove = "paper"
elif randomNumber == 2 :
    computerMove = "cutter"

player1 = input("player1 enter yr name :")
# player2 = input("palyer2 enter yr name ")

player_2 = computerMove

winpPlayer1 = 0
winPlayer2 = 0
wining = 4

while winpPlayer1 < wining and winPlayer2 < wining :
    print(f"consequense of game untill now :win player1 is {winpPlayer1} and win palyer2 is {winPlayer2}")
    player_1 = input(f" {player1} choose yr turn :")
    print(f"computermove is : {player_2}")
    
    if player_1 == "rock" and player_2 == "paper" :
        print("player_2 winner ")
        winPlayer2 += 1
    elif player_1 == "rock" and player_2 == "cutter" :
        print("player_1 winner")
        winpPlayer1 += 1
    elif player_1 == "paper" and player_2 == "rock" :
        print("player_1 winner")
        winpPlayer1 += 1             
    elif player_1 == "paper" and player_2 == "cutter" :
        print("player_2 winner")
        winPlayer2 += 1
    elif player_1 == "cutter" and player_2 == "rock" :
        print("player_2 winner")
        winPlayer2 += 1
    elif player_1 == "cutter" and player_2 == "paper" :
        print("player_1 winner")
        winpPlayer1 += 1    
    elif player_1 == player_2 :
        print(" draw choose again")
    else :
        print("you enter wrong words")

