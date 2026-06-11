import random

# Predefined list of 5 simple words
words = ["python", "coding", "intern", "smart", "device"]
secret_word = random.choice(words)
guessed_letters = []
attempts_left = 6

print("--- Welcome to Hangman! ---")

while attempts_left > 0:
    # Display the word with underscores for unguessed letters
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    
    print("\nWord: " + display_word.strip())
    print(f"Attempts remaining: {attempts_left}")
    
    # Check if the player won
    if "_" not in display_word:
        print("🎉 Congratulations! You guessed the word correctly!")
        break
        
    guess = input("Guess a letter: ").lower().strip()
    
    # Validation
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single valid letter.")
        continue
        
    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue
        
    guessed_letters.append(guess)
    
    # Check if letter is in the word
    if guess in secret_word:
        print("Good guess!")
    else:
        print("Wrong guess!")
        attempts_left -= 1

if attempts_left == 0:
    print(f"\n❌ Game over! The correct word was: {secret_word}")
