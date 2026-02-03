import p1_random as p1

rng = p1.P1Random()

# Game Variables
games_Won = 0
games_Lost = 0
games_Tie = 0
games_Played = 0
current_card = None
current_hand_value = 0
exitGame = False
activeGame = False


def start_game():
    print("START GAME #", games_Played + 1, end="\n")
    return True
def end_game():
    pass


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


"""
MAIN LOOP
"""
while not exitGame:

    if not activeGame:
        start_game()

    # Gather player input for next action.
    print("\n1. Get another card", "2. Hold hand", "3. Print statistics", "4. Exit", sep="\n", end="\n\n")

    player_input_choice = int(input("Choose an option: "))

    # Route based off of player input.
    if player_input_choice == 1:

        # Generate new rng value for new card.
        rng_value = rng.next_int(13) + 1

        # Validate new rng
        current_card = determine_card(rng_value)
        current_hand_value += determine_card_value(rng_value)

        # Display new card information
        print(f"\nYour card is a {current_card}!")
        print(f"Your hand is {current_hand_value}!", end="\n\n")

        # Check for win/lose conditions
        if current_hand_value >= 22:
            games_Lost += 1
            games_Played += 1
            print("You exceeded 21! You lose!", end="\n\n")

    elif player_input_choice == 2:
        pass
    elif player_input_choice == 3:
        pass
    elif player_input_choice == 4:
        exitGame = True
