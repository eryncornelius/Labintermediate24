guess_word = "apel"
correct_word = set(guess_word)
guessed = set()
wrong = 0

print("Welcome to Hangman 2.0!")
print("Try to guess the word!")

while wrong < 6:
    guess = input("Give me ONE letter").lower()
    
    if len(guess) !=1:
        print("Invalid input! Give me ONE letter!")
        continue
    
    if guess in guessed:
        print("You already guessed that letter! Give me another letter!")
        continue
    
    guessed.add(guess)
    
    if guess in correct_word:
        print("Correct!", guess, " is in the word")
    else:
        wrong += 1
        remaining = 6 - wrong
        print("Wrong answer! You only have", remaining, "guesses left")
    
    current = "". join([letter if letter in guessed else "_" for letter in guess_word])
    print("Guessed Word:", current)
    
    if set(current) == correct_word:
        print("Congrats! You guessed the word")
        break
else:
        print("Game Over! Correct answer:", guess_word)
