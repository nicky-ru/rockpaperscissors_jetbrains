from random import choice

default_options = 'rock,paper,scissors'
options = []
name = ''

def restore_game():
    global name, score
    name = input("Enter your name: ")
    print(f"Hello, {name}")
    rating = open('rating.txt', 'r')
    for record in rating:
        if record.split()[0] == name:
            score = int(record.split()[1])
    rating.close()


def set_options():
    global options
    user_options = input()
    if not user_options:
        options = default_options.split(',')
    else:
        options = user_options.split(',')


def user_wins(computer, user):
    half_index = options.index(user) + 1
    half_len = len(options) // 2
    if len(options[:half_index]) < len(options[half_index:]):
        defeaters = options[half_index:half_index + half_len]
    else:
        defeaters = options[half_index:]
        defeaters.extend(options[:half_len - len(defeaters)])
    return computer not in defeaters


restore_game()
set_options()
print("\nOkay, let's start")

while True:
    user_input = input()
    if user_input == '!exit':
        print('Bye!')
        break
    if user_input == '!rating':
        print(f'Your rating: {score}')
        continue
    elif user_input not in options:
        print('Invalid input')
        continue

    computer_choice = choice(options)
    if user_input == computer_choice:
        print(f"There is a draw ({computer_choice})")
        score += 50
    elif user_wins(computer_choice, user_input):
        print(f"Well done. Computer chose {computer_choice} and failed")
        score += 100
    else:
        print(f"Sorry, but computer chose {computer_choice}")
