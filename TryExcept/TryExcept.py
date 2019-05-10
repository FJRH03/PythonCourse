'''
    Author: @XXXKaos (GitHub)
    Francisco Ramirez
    Twitter: @DeNyJaviier
'''

#Try and catch in Python
from builtins import print

#value = 10/0 no util syntax
try:
    num = int(input("Enter a number:"))
    print(num)
except ZeroDivisionError as err: #If you divide in zero catch this error.
    print(err)
except ValueError:
    print("Invalid input error!")


