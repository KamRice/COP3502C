import p1_random as p1

"""
THINGS TO FIX:
1. When player busts, add a loss for player. and a win for dealer.
"""

rng = p1.P1Random()

"""
Global Variables
"""

games_Won = 0
games_Lost = 0
games_Tie = 0
games_Played = 0
game_Count = 0

card_Map = {
    1: {"name": "ACE", "value": 1},
    2: {"name": "2", "value": 2},
    3: {"name": "3", "value": 3},
    4: {"name": "4", "value": 4},
    5: {"name": "5", "value": 5},
    6: {"name": "6", "value": 6},
    7: {"name": "7", "value": 7},
    8: {"name": "8", "value": 8},
    9: {"name": "9", "value": 9},
    10: {"name": "10", "value": 10},
    11: {"name": "JACK", "value": 10},
    12: {"name": "QUEEN", "value": 10},
    13: {"name": "KING", "value": 10},

}


def main():
    # General Variables

    # Update Global Game Count
    global game_Count
    game_Count += 1

    # Initial Player Hand
    player_current_card = card_Map[rng.next_int(13) + 1]
    player_score = player_current_card["value"]
    print("START GAME #", game_Count, end="\n\n")

    # Display game information.
    print(f"Your card is a {player_current_card['name']}!")
    print(f"Your hand is {player_score}!", end="\n\n")

    player_input_choice = validate_player_input()

    if player_input_choice == 1:
        blackjack(player_score)
    elif player_input_choice == 2:
        hold_hand(player_score)
    elif player_input_choice == 3:
        get_statistics(player_score)
    else:
        print("Option: ", player_input_choice)


def blackjack(score):
    global games_Won
    global games_Lost
    global games_Played

    # Deal new player card.
    player_new_card = card_Map[rng.next_int(13) + 1]
    score += player_new_card["value"]

    # Display game information.
    print(f"\nYour card is a {player_new_card['name']}!")
    print(f"Your hand is {score}!", end="\n\n")

    # Validate player hand.

    if score == 21:
        print("BLACKJACK! You win!\n")
        games_Won += 1
        games_Played += 1
        main()
    elif score >= 22:
        print("You exceeded 21! You lose.\n")
        main()

    player_input_choice = validate_player_input()

    if player_input_choice == 1:
        blackjack(score)
    elif player_input_choice == 2:
        hold_hand(score)
    elif player_input_choice == 3:
        get_statistics(score)
    else:
        return


def validate_player_input():
    # Gather player input for next action
    print("1. Get another card", "2. Hold hand", "3. Print statistics", "4. Exit", sep="\n", end="\n\n")
    player_input_choice = int(input("Choose an option: "))

    if player_input_choice <= 0 or player_input_choice >= 5:
        print("Invalid input!", end="\n\n")
        print("Please enter and integer value between 1 and 4.")
        return validate_player_input()
    else:
        return player_input_choice


def get_statistics(score):
    global games_Won
    global games_Played

    print("\nNumber of Player Wins:", games_Won)
    print("Number of Dealer Wins:", games_Lost)
    print("Number of tie games:", games_Tie)
    print("Total # of games played is:", games_Played)

    if games_Played > 0:
        win_percentage = (games_Won / games_Played) * 100
    else:
        win_percentage = 0

    print("\nPercentage of Player wins:", round(win_percentage, 1), "\n")

    player_input_choice = validate_player_input()

    if player_input_choice == 1:
        blackjack(score)
    elif player_input_choice == 2:
        hold_hand(score)
    elif player_input_choice == 3:
        get_statistics(score)
    else:
        return


def hold_hand(score):
    global games_Won
    global games_Lost
    global games_Tie
    global games_Played

    # Create dealer score.
    dealer_score = rng.next_int(11) + 16

    print("\nDealer's hand:", dealer_score)
    print("Your hand is:", score)

    if score > dealer_score:
        print("\nYou win!")
        games_Won += 1
        games_Played += 1
        main()
    elif score < dealer_score:
        print("\nDealer wins!\n")
        games_Lost += 1
        games_Played += 1
        main()
    else:
        print("\nIt's a tie! No one wins!\n")
        games_Tie += 1
        games_Played += 1
        main()


"""
Main Loop
"""

main()
