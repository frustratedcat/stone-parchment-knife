def greet_player():
  print('Welcome to Stone, Parchment, Knife!')

  player_name = input('What should I call you?\n> ')

  print(f'Hello, {player_name.title()}! The rules of the game are simple, Stone beats Knife, Knife beats Parchment, Parchment beats Stone!')

def get_player_choice():
  player_choice = input('Choose Stone, Parchment, of Knife\n> ')