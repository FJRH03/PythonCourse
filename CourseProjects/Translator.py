'''
    Author: @XXXKaos (GitHub)
    Francisco Ramirez
    Twitter: @DeNyJavier
'''

#Buiilding translator method
def translate(phrase):
    tranlation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                tranlation = tranlation + "G"
            tranlation = tranlation + "g"
        else:
            tranlation = tranlation + letter
    return tranlation
print(
    translate(input("Enter a phrase:"))
)

