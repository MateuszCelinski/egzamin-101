import random
from enum import IntEnum

game_type_option = IntEnum("Game_Type", ("player_vs_player", "player_vs_computer"))
game_options = IntEnum("Game_Options", ("paper", "rock", "scissors"))


def choose_game_type():
    try:
        print("Choose game type:")
        for option in list(game_type_option):
            print(f'{option.value} for {option.name.replace("_", " ")}')
        choosen_game_type = int(input("You choose: "))
        if choosen_game_type == game_type_option.player_vs_player:
            return game_type_option.player_vs_player
        elif choosen_game_type == game_type_option.player_vs_computer:
            return game_type_option.player_vs_computer
        else:
            print("unknown game type")
            choose_game_type()
    except ValueError:
        choose_game_type()


def choice_option():
    try:
        print("Choose option: ")
        for option in list(game_options):
            print(f'{option.value} for {option.name}')
        choice = int(input("You choose: "))
        if choice == game_options.paper:
            return game_options.paper
        elif choice == game_options.rock:
            return game_options.rock
        elif choice == game_options.scissors:
            return game_options.scissors
        else:
            print("unknown choice")
            choice_option()
    except ValueError:
        choice_option()


def check_score(player1, player2):
    if player1 == player2:
        print("--- Game is draw ---")
    elif player1 == game_options.paper:
        if player2 == game_options.rock:
            print("--- Player 1 win! ---")
        elif player2 == game_options.scissors:
            print("--- Player 2 win! ---")
    elif player1 == game_options.rock:
        if player2 == game_options.scissors:
            print("--- Player 1 win! ---")
        elif player2 == game_options.paper:
            print("--- Player 2 win! ---")
    elif player1 == game_options.scissors:
        if player2 == game_options.paper:
            print("--- Player 1 win! ---")
        elif player2 == game_options.rock:
            print("--- Player 2 win! ---")


def game():
    game_type = choose_game_type()
    print()
    print()
    print(f'*** Your game type is {game_type.name.replace("_", " ")} ***')
    print()

    if game_type == game_type_option.player_vs_player:
        print("---Player 1 choose:---")
        player1 = choice_option()
        print("---Player 2 choose:---")
        player2 = choice_option()
    elif game_type == game_type_option.player_vs_computer:
        print("---Player 1 choose:---")
        player1 = choice_option()
        player2 = random.choice(list(game_options))
    print()
    print(f'-- Player 1 choose: {player1.name}')
    print(f'-- Player 2 choose: {player2.name}')
    print()
    check_score(player1, player2)


game()
