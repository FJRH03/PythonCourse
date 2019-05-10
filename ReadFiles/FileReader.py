'''
    Author: @XXXKaos (GitHub)
    Francisco Ramirez
    Twitter: @DeNyJaviier
'''

# Python program to read files.

#opening files:

#namefile, mode that file will be open (Read,Write,Appendd,r+ > read and write)

#save file content into a variable
employee_file = open("employees.txt", "r")

#print information
print(employee_file.read())

#closing file opened
employee_file.close()
