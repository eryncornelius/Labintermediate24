import random

def update_text(word, guessed):
    return " ".join([guess if guess in guessed else "_" for guess in word])

def hangman(word):
    guessed = set()
    wrong = 0
    print("Welcome to Hangman Game! Try to guess the word!")
    
    while wrong < 6:
        guess = input("Give me ONE letter: ").lower()
        if len(guess) != 1 or not guess.isalpha() or guess in guessed:
            print("Invalid or you already guessed that!")
            continue
        
        guessed.add(guess)
        if guess not in word:
            wrong += 1
            print("Wrong!", 6 - wrong, "guesses left.")
        
        display = update_text(word, guessed)
        print("Current Progress:", display)
        
        if "_" not in display:
            print("You win!")
            return
    
    print("Game Over! The word was:", word)

word = ["singapore", "france", "indonesia"]
secret_word = random.choice(word)
hangman(secret_word)