import random
word_bank = ['sigma','pokemon','deez','smut','trials','love','hate','party','zebra']
word = random.choice(word_bank)
guessWord = ['_'] * len(word)
attempts = 10

while attempts > 0:

    print('\nCurrent Word: ' + ' '.join(guessWord))

    guess = input('Guess the letter: ').lower()

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessWord[i] = guess
        print('Great guess!')
    else:
        attempts -= 1
        print('Wrong guess! Attempts left: ' + str(attempts))
    if '_' not in guessWord:
        print('\nCongrats! You guessed correctly: ' + word)
        break

    else:
        print('\nYou\'ve run out of attempts the word was: ' + word)