import random
import os

def main():
  clear_screen()
  play_game = True

  greeting_name = greet_player()
  clear_screen()
  print(f'Hello, {greeting_name.title()}!\nThe rules of the game are simple, Stone beats Knife, Knife beats Parchment, Parchment beats Stone!\n')

  while play_game == True:

    result = compare_player_computer_choices()
    print(result)

    play_again = input('\nWould you like to play again? Type "Yes" or "No"\n> ')
    clear_screen()
    if play_again.title() == 'Yes':
      play_game = True
    elif play_again.title() == 'No':
      play_game = False
      print('See you next time!')

def clear_screen():
  os.system('cls' if os.name == 'nt' else 'clear')

def greet_player():
  player_name = input('Welcome to Stone, Parchment, Knife!\nWhat should I call you?\n> ')
  return player_name

def get_player_choice():
  make_choice = True

  while make_choice == True:
    player_choice = input('Choose Stone, Parchment, of Knife\n> ')

    if player_choice.lower() == 'stone' or player_choice.lower() == 'parchment' or player_choice.lower() == 'knife':
      make_choice = False
    else:
      print(f'{player_choice.title()} is not a valid choice. Please choose again.')

  return player_choice.title()

def get_computer_choice():
  computer_choice = random.randint(1, 3)

  if computer_choice == 1:
    computer_choice = 'Stone'
  elif computer_choice == 2:
    computer_choice = 'Parchment'
  else:
    computer_choice = 'Knife'

  return computer_choice

def compare_player_computer_choices():
  result = ''
  player_choice = get_player_choice()
  computer_choice = get_computer_choice()
  clear_screen()
  print(f'You chose {player_choice}\n\nComputer chose {computer_choice}\n')

  if player_choice == 'Stone' and computer_choice == 'Stone':
    result = 'Draw!'
  elif player_choice == 'Stone' and computer_choice == 'Parchment':
    result = 'Computer Wins!'
  elif player_choice == 'Stone' and computer_choice == 'Knife':
    result = 'You win!'
  elif player_choice == 'Parchment' and computer_choice == 'Stone':
    result = 'You win!'
  elif player_choice == 'Parchment' and computer_choice == 'Parchment':
    result = 'Draw!'
  elif player_choice == 'Parchment' and computer_choice== 'Knife':
    result = 'Computer Wins!'
  elif player_choice == 'Knife' and computer_choice == 'Stone':
    result = 'Computer Wins!'
  elif player_choice == 'Knife' and computer_choice == 'Parchment':
    result = 'You win!'
  elif player_choice == 'Knife' and computer_choice == 'Knife':
    result = 'Draw!'

  return result

if __name__ == '__main__':
  main()
