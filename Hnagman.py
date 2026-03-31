import random

# Word list (can be extended)
words = ["apple", "banana", "grapes", "orange", "mango"]

word = random.choice(words)
guessed = ["_"] * len(word)
attempts = 6
used_letters = []

print("Welcome to AI Hangman Game!")

while attempts > 0 and "_" in guessed:
    print("\nWord:", " ".join(guessed))
    print("Attempts left:", attempts)
    
    guess = input("Enter a letter: ").lower()
    
    if guess in used_letters:
        print("Already used!")
        continue
    
    used_letters.append(guess)
    
    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessed[i] = guess
        print("Correct guess!")
    else:
        attempts -= 1
        print("Wrong guess!")

# Result
if "_" not in guessed:
    print("\n🎉 You guessed the word:", word)
else:
    print("\n💀 Game Over! Word was:", word)
