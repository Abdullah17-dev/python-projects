import random
class Hangman:
    def __init__(self,words):
        self.words = words
        self.word = random.choice(self.words)
        self.word_display = ["_" if letter.isalpha() else letter for letter in self.word]
        self.guessed_letters = set()
        self.attempts = 10
    def display(self):
        print("\nWord",",".join(self.word_display))
        print(f"Attempts left: {self.attempts}")
        if self.guessed_letters:
            print(f"Guessed letters: {', '.join(self.guessed_letters)}")
    def guess(self,letter):
        letter = letter.upper()
        if letter in self.guessed_letters:
            print("you already guessed that letter!")
            return
        self.guessed_letters.add(letter)
        if letter in self.word:
            for idx, char in self.word:
                if char == letter:
                    self.word_display[idx] = letter
        else:
            self.attempts -= 1
            print("Wrong guess!")

    def is_won(self):
        return "_" not in self.word_display
    
    def is_lost(self):
        return self.attempts == 0

    def play(self):
        print("Welcome to Hangman Game!")
        while not self.is_won() and not self.is_lost():
            self.display()
            letter = input("Guess a letter: ")
            if len(letter) == 1 and letter.isalpha():
                self.guess(letter)
            else:
                print("Invalid input. PLease enter a single letter")
        if self.is_won():
            print(f"Congratulations! You guessed the word: {self.word}")

        else:
            print(f"Game over! The word was: {self.word}")