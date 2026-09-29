import random

words = ["python","computer","program","coding","database","keyboard","internet","software","hardware","developer","algorithm","function","variable","network","website","machine","science","student","project","technology"]
word = random.choice(words)
guessed_word = ["_"] * len(word)
guessed_letters = []

max_attempts = 6
wrong_guesses = 0

print("HANGMAN GAME")
print("Guess the word!")
print("You have 6 incorrect guesses.")

while wrong_guesses < max_attempts and "_" in guessed_word:
    print("\nWord:", " ".join(guessed_word))
    print("Guessed letters:", guessed_letters)
    print("Wrong guesses left:", max_attempts - wrong_guesses)

    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.")
        continue
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Correct guess!")
        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess

    else:
        wrong_guesses += 1
        print("Wrong guess!")
if "_" not in guessed_word:
    print("\n🎉 Congratulations! You won!")
    print("The word was:", word)
else:
    print("\n💀 Game Over!")
    print("The word was:", word)