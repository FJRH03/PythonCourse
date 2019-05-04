#Working with functions with lists on Python

lucky_number = [4,8,15,16,23,42]
friends = ["Kevin","Martha","Jim","Javier"]

print(friends)

#Extends functions allows you to apend other list
friends.extend(lucky_number)
print(friends)

#Append functions allows you to append another item into a list
friends.append("Oscar")
print(friends)

#Insert function append items through index and push the other items contained into a list
friends.insert(1,"Kelly") # index,value
print(friends)

#Remove functions remove items from lists
friends.remove("Oscar")
print(friends)

#Clear fuction clears all items from list
friends.clear()
print(friends)

friends = ["Juan", "Antonio", "Alberto"]

#Pop functions remove the last item from list
friends.pop()
print(friends)

#Tell index of items contained into a list
print("Index: ")
print(friends.index("Antonio"))

friends.append("Karla")
friends.append("Christina")
friends.append("Juan")

#Count function oounts how many times values exists into a lists
print("")
print(friends.count("Juan"))

#Sort function sort the items of the list
print(friends.sort()) #order in alphabetical order or ascending order

#Reverse method
lucky_number.reverse()
print(lucky_number)

friends2 = friends.copy()
friends2.remove("Juan")
print(friends2)



