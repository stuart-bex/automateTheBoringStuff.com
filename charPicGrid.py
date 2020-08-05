# Character Picture Grid 1-4C
# Training project from automateTheBoringStuff.com

#Say you have a list of lists where each value in 
# the inner lists is a one-character string, like 
# this:

# grid = [['.', '.', '.', '.', '.', '.'],
#        ['.', 'O', 'O', '.', '.', '.'],
#        ['O', 'O', 'O', 'O', '.', '.'],
#        ['O', 'O', 'O', 'O', 'O', '.'],
#        ['.', 'O', 'O', 'O', 'O', 'O'],
#        ['O', 'O', 'O', 'O', 'O', '.'],
#        ['O', 'O', 'O', 'O', '.', '.'],
#        ['.', 'O', 'O', '.', '.', '.'],
#        ['.', '.', '.', '.', '.', '.']]

# Think of grid[x][y] as being the character at the 
# x- and y-coordinates of a “picture” drawn with 
# text characters. The (0, 0) origin is in the 
# upper-left corner, the x-coordinates increase 
# going right, and the y-coordinates increase going 
# down.

# Copy the previous grid value, and write code that 
# uses it to print the image.

# ..OO.OO..
# .OOOOOOO.
# .OOOOOOO.
# ..OOOOO..
# ...OOO...
# ....O....

def rotateClockwise(myGrid) :
    # takes a Charature Picture Grid and rotates 90deg clockwise

    # build a new grid, transposing items from myGrid
    newGrid = [] # new grid to build into to avoid changing the original

    for y in range(len(myGrid[0])) : # take each row for new grid in turn (old cols)
 
        newRow = [] # blank row to build into

        for x in range(len(myGrid)) : #  then each item in turn (old rows)

            #transposes the corresponding item from myGrid
            newRow.append(myGrid[len(myGrid) -x -1][y])
            
        #add the new row to the new grid
        newGrid.append(newRow)
    
    return(newGrid)

def printGrid(myGrid) :
    # print a grid to StdOut

    for x in range(len(myGrid)) : 
        for y in range(len(myGrid[x])) :
            print(myGrid[x][y] + " ", end ='')
        print() # add new line chr to end of each row



# Main Code block

#load starting condition
grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

print("Starting grid")
printGrid(grid) # display starting condition

grid = rotateClockwise(grid)

print("\nEnd grid")
printGrid(grid) # display final grid

