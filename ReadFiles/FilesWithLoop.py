'''
    Author: @XXXKaos (GitHub)
    Francisco Ramirez
    Twitter: @DeNyJaviier
'''

#Reading data from file

textfile = open("employees.txt" , "r")

#Getting data in array, and loop the information

for textfile in textfile.readlines():
    print(textfile)

#Close file reader
