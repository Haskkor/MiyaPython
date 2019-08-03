def check_guess(guess, answer, nbr_attempts):
    global score
    still_guessing = True
    attempt = 0
    while still_guessing and attempt < nbr_attempts:
        if guess.lower() == answer.lower():
            print('Correct answer')
            score = score + 3 - attempt 
            still_guessing = False
        else:
            if attempt < nbr_attempts - 1:
                guess = input('Sorry wrong answer. Try again. ')
            attempt = attempt + 1
    if attempt == nbr_attempts:
        print('The correct answer is ' + answer )

score = 0
print('Guess the Animal!')

guess1 = input('Which bear lives at the North Pole? ')
check_guess(guess1, 'polar bear', 3)

guess2 = input('Which is the fastest land animal? ')
check_guess(guess2, 'cheetah', 3)

guess3 = input('Which is the largest animal? ')
check_guess(guess3, 'blue whale', 3)

guess = input('Which one of these is a fish?\n \
A) Whale\n B) Dolphin\n C) Shark\n D) Squid\n \
Type A, B, C, or D ')
check_guess(guess, 'C', 2)

guess = input('Mice are mammals. True or False? ')
check_guess(guess, 'True', 1)

print('Your score is ' + str(score))

