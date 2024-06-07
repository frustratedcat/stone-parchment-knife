import random

def main():
  greeting_name = greet_player()
  print(f'Hello, {greeting_name.title()}!\nThe rules of the game are simple, Stone beats Knife, Knife beats Parchment, Parchment beats Stone!'
)

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

if __name__ == '__main__':
  main()
