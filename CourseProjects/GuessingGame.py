'''
    Author: @XXXKaos (GitHub)
    Francisco Ramriez
    Twitter: @DeNyJaviier
'''

#Let's make a guess game using while loop
secretWord = "Kaos"
guess = ""
guessCount = 0
guessLimit = 3
outOfGuess = False

while guess != secretWord and not (outOfGuess):
    if guessCount < guessLimit:
        guess = input("Enter guess: ")
        guessCount += 1
    else:
        outOfGuess = True

if outOfGuess:
        print("Out of Guesses, YOU LOSE!")
else:
        print("YOU WIN!")
