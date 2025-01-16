secret_word = "banana"

print("Welcome to the Secret Word Game!")

while True:
    guess = input("Enter your guess: ")

    if guess == secret_word: 
        print("Congratulations! You guessed the secret word!")
        break
    else:
        print("Wrong! Try again.")