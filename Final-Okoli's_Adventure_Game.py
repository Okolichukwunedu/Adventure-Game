import random
import time
import string


combat = ["troll", "wicked witch", "pirate", "dragon"]
item = []


def get_random_combat():
    combat_agent = random.choice(combat)
    return combat_agent


combat_agent = get_random_combat()


def print_stop(message, delay=0):
    for char in message:
        print(char, end='')
        if char in string.punctuation:
            time.sleep(.5)
        time.sleep(.03)


def valid_input(prompt, options):
    while True:
        option = input(prompt).lower()
        if option in options:
            return option
        print_stop(f"\nSorry, the option {option} is invalid. Try again")


def intro():
    print_stop("\nYou find yourself standing in an open field, "
               "filled with grass and yellow wild flowers.", 2)
    print_stop(f"\nRumour has it that a {combat_agent} is somewhere around "
               "here, and has been terrifying the nearby village.", 2)
    print_stop("\nIn front of you is a house.", 2)
    print_stop("\nTo your right is a dark cave.", 2)
    print_stop("\nIn your hand you hold your trusty (but not very"
               " effective) dagger.", 2)


def go_to_cave():
    if "Sword" in item:
        print_stop("\nYou peer cautiously into the cave.", 2)
        print_stop("\nYou've been here before, and gotten all"
                   " the good stuff. It's just an empty cave now.", 2)
        print_stop("\nYou walk back to the field.\n", 2)

    elif "Sword" not in item:
        print_stop("\nYou peer cautiously into the cave.", 2)
        print_stop("\nIt turns out to be only a very small cave.", 2)
        print_stop("\nYour eye catches a glint of metal behind a rock.", 2)
        print_stop("\nYou have found the magical Sword of Ogoroth!", 2)
        print_stop("\nYou discard your silly old dagger and take"
                   " the sword with you.", 2)
        print_stop("\nYou walk back out to the field\n", 2)
        item.append("Sword")
    location()


def go_to_house():
    print_stop(f"\nYou approach the door of the house.", 2)
    print_stop(f"\nYou are about to knock when the door opens and"
               f" out steps a {combat_agent}.", 2)
    print_stop(f"\nEep! This is the {combat_agent}'s house!", 2)
    print_stop(f"\nThe {combat_agent} attacks you!", 2)
    print_stop(f"\nYou feel a bit under-prepared for this, what "
               f"with only having a tiny dragger.", 2)
    run_or_fight()


def run_or_fight():
    response1 = valid_input("\nWould you like to (1) fight or (2) "
                            "run away? \n", ['1', '2']).lower()
    if "2" == response1:
        print_stop("\nYou run back into the field. "
                   "Luckily, you don't seem to have been "
                   "followed.\n", 2)
        location()

    if "1" == response1:
        if "Sword" in item:
            print_stop(f"\nAs the {combat_agent} moves to attack,"
                       f" you unsheath your new sword.", 2)
            print_stop("\nThe Sword of Ogoroth shines brightly in"
                       " your hand as you brace yourself for the"
                       " attack.", 2)
            print_stop(f"\nBut the {combat_agent} takes one look at"
                       f" your shiny new toy and runs away!", 2)
            print_stop(f"\nYou have rid the town of the {combat_agent}."
                       " You are victorious!\n", 2)
        if "Sword" not in item:
            print_stop("\nYou do your best...", 2)
            print_stop(f"\nbut your dagger is no match for the "
                       f"{combat_agent}.", 2)
            print_stop("\nYou have been defeated!\n", 2)

    play_again()


def location():
    print_stop("\nEnter 1 to knock on the door of the house.")
    print_stop("\nEnter 2 to peer into the cave.")
    print_stop("\nWhat would you like to do?")
    while True:
        response = valid_input("\n(Please enter 1 or 2.)\n", ['1', '2'])
        if "1" in response:
            go_to_house()
            break
        elif "2" in response:
            go_to_cave()
            break


def play_again():
    choice = valid_input("\nWould you like to play again?"
                         " [y|n]", ['y', 'n']).lower()
    if choice == 'n':
        print_stop("\nThanks for playing! See you next time.\n")
        exit(0)
    if choice == "y":
        print_stop("\nExcellent! Restarting the game ...\n", 2)
        start_game()


def start_game():
    while True:
        global combat_agent
        combat_agent = get_random_combat()
        intro()
        location()


def game():
    while True:
        start_game()
        play_again()


if __name__ == '__main__':
    game()
