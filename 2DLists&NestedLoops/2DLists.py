'''
    Author: @XXXKaos (GitHub)
    Francisco Ramirez
    Twitter: @DeNyJaviier
'''

# 2D Lists and nested loops

# Create basic list

number_grid = [

    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

#Printing number 1, | First need to aim the row, and then the column:
print(number_grid[2][2])
print("")

#Nested for loops

for row in number_grid:
    for col in row:
        print(col)
