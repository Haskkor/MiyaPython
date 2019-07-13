def check_guess(guess, answer):
    global score
    if guess == answer:
        print('Correct answer')
        score = score + 1

score = 0
print('Guess the Animal!')
guess1 = input('Which bear lives at the north pole? ')
check_guess(guess1, 'polar bear')
