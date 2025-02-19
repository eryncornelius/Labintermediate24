import random

def choose_word(words):
    return random.choice(words)

def display_word(word, guessed):
    return ' '.join(letter if letter in guessed else '_' for letter in word)

def play():
    global wins, losses
    words = ["indonesia", "pancake", "computer", "orange", "keyboard", "noodles"]
    
    while words:
        word = choose_word(words)
        words.remove(word)
        guessed = set()
        attempts = 6
        
        print("Welcome to the Hangman Game! Guess the word.")
        
        while attempts > 0:
            print(display_word(word, guessed))
            guess = input("Enter a letter: ").lower()
            
            if guess in guessed:
                print("You already guessed that letter.")
                continue
            
            guessed.add(guess)
            
            if guess not in word:
                attempts -= 1
                print("Incorrect! " + str(attempts) + " attempts left.")
            
            if all(letter in guessed for letter in word):
                print("Congratulations! You guessed the word: " + word)
                wins += 1
                break
        else:
            print("Game Over! The word was: " + word)
            losses += 1
        
        print("Score: Wins - " + str(wins) + ", Losses - " + str(losses))
        
        choice = input("Play again? (yes/no): ").lower()
        if choice != 'yes':
            break
    
    print("Final Score: Wins - " + str(wins) + ", Losses - " + str(losses))
    print("Thanks for playing!")

wins = 0
losses = 0

play()
