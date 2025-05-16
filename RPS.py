#RPS.py
#Name: Caden Cerny
#Date: Feb. 9, 2025
#Assignment: Lab 3
import random

def get_computer_choice():
  return random.choice(['R', 'P', 'S'])

def determine_winner(player_choice, computer_choice):
  if player_choice == computer_choice:
    return "Tie"
  elif (player_choice == 'R' and computer_choice == 'S') or (player_choice == 'P' and computer_choice == 'R') or (player_choice == 'S' and computer_choice == 'P'):
    return "You win!"
  else:
    return "You lose."

def main():
  wins = 0
  ties = 0
  losses = 0

  while True:
    player_choice = input("Select Rock, Paper, or Scissors (R, P, S): ").upper()
    if player_choice not in ['R', 'P', 'S']:
            print("Invalid choice, please try again.")
            continue
        

    computer_choice = get_computer_choice()
        
    print(f"Player chose: {player_choice}")
    print(f"Computer chose: {computer_choice}")
        
    result = determine_winner(player_choice, computer_choice)
    print(result)
        
      
    if result == "You win!":
            wins += 1
    elif result == "Tie":
            ties += 1
    else:
            losses += 1
        
        
    play_again = input("Would you like to play again? (Y/N): ").upper()
    if play_again != 'Y':
            break
  #Create a loop that continues as long as the user wants to play.
  #User can play as many games as they wish.

  #Randomly choose the computer between 'R', 'P', or 'S'
  #Prompt the user for their RPS selection
  #Determine winner and state what happened to the user
  #Ask the user if they would like to play again.

  #In the end, print the stats
  print("Wins \t Ties \t Losses")
  print("---- \t ---- \t ------")
  print(wins, "\t", ties , "\t", losses)

if __name__ == '__main__':
  main()
