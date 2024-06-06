import random

def greet_player():
  print('Welcome to Stone, Parchment, Knife!')

  player_name = input('What should I call you?\n> ')

  print(f'Hello, {player_name.title()}! The rules of the game are simple, Stone beats Knife, Knife beats Parchment, Parchment beats Stone!')

def get_player_choice():
  make_choice = True
  while make_choice == True:
    player_choice = input('Choose Stone, Parchment, of Knife\n> ')

    if player_choice.lower() == 'stone' or player_choice.lower() == 'parchment' or player_choice.lower() == 'knife':
      make_choice = False
    else:
      print(f'{player_choice.title()} is not a valid choice. Please choose again.')

  return player_choice

def get_computer_choice():
  computer_choice = random.randint(1, 3)

  if computer_choice == 1:
    computer_choice = 'Stone'
  elif computer_choice == 2:
    computer_choice = 'Parchment'
  else:
    computer_choice = 'Knife'

  return computer_choice

print(get_player_choice(), get_computer_choice())
