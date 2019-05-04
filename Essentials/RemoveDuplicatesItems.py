'''
Removes duplicate values from lists
so we must define a funcition will return new list
with n duplicate elements
'''

def removeDupl(inputList):
    #we need an empty list before the loop
    secondList = []

    for element in inputList:
        if element not in secondList:
            secondList.append(element)
            #so if there is not such element - add it to list
    return secondList

#Let's check

myL = ['hello','everybody','hello','everybody','this is python']
myL = removeDupl(myL)

print(myL)