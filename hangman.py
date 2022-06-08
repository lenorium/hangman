from random import choice


def uncover(word, hidden_word, letter):
    for i in range(len(word)):
        if word[i] == letter:
            hidden_word[i] = letter
    return hidden_word


def play():
    is_won = False
    attempts = 8
    words = ['python', 'java', 'swift', 'javascript']
    correct_word = list(choice(words))
    hint = ['-'] * len(correct_word)
    guessed_letters = set()

    while True:
        if attempts == 0:
            print('You lost!')
            break

        print()
        print(''.join(hint))
        guess = input(f'Input a letter:')
        guess = guess.strip()

        if guess in guessed_letters:
            print("You've already guessed this letter.")
            continue

        if len(guess) != 1:
            print('Please, input a single letter.')
            continue

        if not guess.islower() or not guess.isalpha():
            print('Please, enter a lowercase letter from the English alphabet.')
            continue

        guessed_letters.add(guess)

        if guess not in correct_word:
            print(f"That letter doesn't appear in the word.")
            attempts -= 1
            continue

        hint = uncover(correct_word, hint, guess)
        if hint == correct_word:
            print(f"You guessed the word {''.join(hint)}!\nYou survived!")
            is_won = True
            break

    return is_won


def print_result(won, lost):
    print(f'You won: {won} times')
    print(f'You lost: {lost} times')


def game():
    won_count = 0
    lost_count = 0
    print('H A N G M A N ')

    while True:
        action = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:')
        match action:
            case 'play':
                is_won = play()
                if is_won:
                    won_count += 1
                else:
                    lost_count += 1
                continue
            case 'results':
                print_result(won_count, lost_count)
                continue
            case 'exit':
                break


if __name__ == '__main__':
    game()




