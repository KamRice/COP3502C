import p1_random as p1

rng = p1.P1Random()

# Game State Variables
games_Won = 0
games_Lost = 0
games_Tie = 0
games_Played = 0
exit_Game = False
active_Game = False

# Player Variables
current_card = None
current_hand_value = 0

# Dealer Variables
dealer_hand_value = 0


def start_game():
    global games_Played
    global current_card
    global current_hand_value

    print("START GAME #", games_Played + 1, sep="", end="\n")

    give_new_card(rng.next_int(13) + 1)

    display_hand_information(current_card, current_hand_value)

    return True


def end_game():
    global games_Played
    global current_card
    global current_hand_value

    games_Played += 1
    current_card = None
    current_hand_value = 0

    return False


def determine_card(rng_val):
    if rng_val == 1:
        return "ACE"
    elif rng_val == 2:
        return "2"
    elif rng_val == 3:
        return "3"
    elif rng_val == 4:
        return "4"
    elif rng_val == 5:
        return "5"
    elif rng_val == 6:
        return "6"
    elif rng_val == 7:
        return "7"
    elif rng_val == 8:
        return "8"
    elif rng_val == 9:
        return "9"
    elif rng_val == 10:
        return "10"
    elif rng_val == 11:
        return "JACK"
    elif rng_val == 12:
        return "QUEEN"
    else:
        return "KING"


def determine_card_value(rng_val):
    if rng_val == 1:
        return 1
    elif rng_val == 2:
        return 2
    elif rng_val == 3:
        return 3
    elif rng_val == 4:
        return 4
    elif rng_val == 5:
        return 5
    elif rng_val == 6:
        return 6
    elif rng_val == 7:
        return 7
    elif rng_val == 8:
        return 8
    elif rng_val == 9:
        return 9
    elif rng_val == 10:
        return 10
    elif rng_val == 11:
        return 10
    elif rng_val == 12:
        return 10
    else:
        return 10


def display_hand_information(card, hand_value):
    print(f"\nYour card is a {card}!")
    print(f"Your hand is {hand_value}!", end="\n")


def hold_hand(player_hand_value):
    global games_Won
    global games_Lost
    global games_Tie
    global active_Game
    global dealer_hand_value

    dealer_hand_value = rng.next_int(11) + 16

    if player_hand_value > dealer_hand_value or dealer_hand_value > 21:
        games_Won += 1
        print("\nDealer's hand:", dealer_hand_value)
        print("Your hand:", player_hand_value)
        print("\nYou win!\n")
        active_Game = end_game()
    elif player_hand_value < dealer_hand_value:
        games_Lost += 1
        print("\nDealer's hand:", dealer_hand_value)
        print("Your hand:", player_hand_value)
        print("\nDealer wins!\n")
        active_Game = end_game()
    else:
        games_Tie += 1
        print("\nDealer's hand:", dealer_hand_value)
        print("Your hand:", player_hand_value)
        print("\nIt's a tie! No one wins!\n")
        active_Game = end_game()


def give_new_card(rng_val):
    global current_card
    global current_hand_value

    current_card = determine_card(rng_val)
    current_hand_value += determine_card_value(rng_val)


def display_game_statistics():
    global games_Played
    global games_Won
    global games_Lost
    global games_Tie

    print("\nNumber of Player wins:", games_Won)
    print("Number of Dealer wins:", games_Lost)
    print("Number of tie games:", games_Tie)
    print("Total # of games played is:", games_Played)

    if games_Played > 0:
        win_percentage = round((games_Won / games_Played) * 100, 1)
    else:
        win_percentage = 0

    print("Percentage of Player wins: ", win_percentage, "%", sep='')


"""
MAIN LOOP
"""

while not exit_Game:

    if not active_Game:
        active_Game = start_game()

    # Gather player input for next action.
    print("\n1. Get another card", "2. Hold hand", "3. Print statistics", "4. Exit", sep="\n", end="\n\n")

    player_input_choice = int(input("Choose an option: "))

    if player_input_choice < 1 or player_input_choice >= 5:
        print("Invalid input!\n")
        print("Please enter an integer value between 1 and 4.")

    # Route based off of player input.
    if player_input_choice == 1:

        # Generate new card.
        give_new_card(rng.next_int(13) + 1)

        # Display new card information
        display_hand_information(current_card, current_hand_value)

        # Check for win/lose conditions with new hand value.
        if current_hand_value == 21:
            games_Won += 1
            active_Game = end_game()
            print("\nBLACKJACK! You win!", end="\n\n")
        elif current_hand_value >= 22:
            games_Lost += 1
            active_Game = end_game()
            print("\nYou exceeded 21! You lose.", end="\n\n")

    elif player_input_choice == 2:
        hold_hand(current_hand_value)
    elif player_input_choice == 3:
        display_game_statistics()
    elif player_input_choice == 4:
        exit_Game = True
