import random
word_list = ["lion", "baboon", "elephant", "duck"]
word = random.choice(word_list)
#print(word)
X = ""
for n in range(0, len(word)):
    X += "_"

print(X)
Chances = 0
print("You have 3 chances to guess!")
while Chances <= 3:
    Guess_word = input("ENTER THE GUESSED WORD: ")
    Guess_word = Guess_word.lower()
    Chances += 1
    if Guess_word == word:
        print("You win.")
        break
    elif Chances == 3 and Guess_word != word:
        print("Out of lives. Game Over")
        break
    else:
        print("Incorrect.")
