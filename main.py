from art import logo,vs
import random 
from game_data import data
import os


# function to clear the console
def clear_console():
  if os.name == 'nt':
    _ = os.system('cls')
  else:
    _ = os.system('clear')

# let's create the function that selects a random person
def select_person(data):
    last_index = len(data)-1
    first_index = 0
    random_index = random.randint(first_index,last_index)
    selected_person = data[random_index]
    return selected_person

def find_the_highest(person_1,person_2):
    if person_1['follower_count'] > person_2['follower_count']:
        return 'A'
    else:
        return 'B'

def play_higher_lower_game():
    # let's clear the console
    clear_console()
    current_score = 0
    is_game_over = False

    print(logo)
    person_A = select_person(data)
    # to make sure that we don't select the same person twice
    data_reduced = data.copy()
    data_reduced.remove(person_A)
    # we select from the list but this time with the person already selected removed
    person_B = select_person(data_reduced) 
    while not is_game_over:
        #let's clear the console
        # clear_console()
        print(f"compare A : {person_A['name']}, {person_A['description']}, from {person_A['country']}")
        print(vs)
        print(f"Against B : {person_B['name']}, {person_B['description']}, from {person_B['country']}")

        user_choice = input('Who has more followers? Type "A" or "B": ')
        correct_letter = find_the_highest(person_A,person_B)
        if user_choice == correct_letter:
            current_score += 1
            print(f"You are right! Current score : {current_score}")
            person_A = person_B
            data_reduced = data.copy()
            # to make sure that we don't select the same person 
            data_reduced.remove(person_A)
            person_B = select_person(data_reduced)
        else:
            is_game_over = True
    # when the game is over 
    print(logo)
    print(f"Sorry,that's wrong. Final score: {current_score}")
    print(f"{person_A['name']}, {person_A['description']}, from {person_A['country']} has {person_A['follower_count']}M followers")
    print(f"{person_B['name']}, {person_B['description']}, from {person_B['country']} has {person_B['follower_count']}M followers")

    # ask the user if he want's to play higher 
    play_again = input("Do you want to play higher and lower again? Type 'y' or 'n': ")
    if play_again == 'y':
       play_higher_lower_game()

play_higher_lower_game()
    



