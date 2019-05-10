'''
    Author: @XXXKaos (GitHub)
    Francisco Ramirez
    Twitter: @DeNyJaviier
'''

#If Statement

#boolean variable | True or False |
#boolean operators: or, and
#elif == else if
is_Male = False
is_Tall = False

if is_Male and is_Tall:
    print("You are a tall male")
elif is_Male and not (is_Tall):
    print("You are a short male")
elif not is_Male and is_Tall:
    print("You are not a male but are tall")
else:
    print("You are not male and not tall")





