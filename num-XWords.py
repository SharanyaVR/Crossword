NOT_FOUND = -1
NUMBER_AT = "X  "
def loadGrid(gridfile):
    grid = []
    for line in open(gridfile):
        grid.append(line.strip())
    return len(grid), ''.join(grid), grid

def get_h_triads(grid, size):
    start = 0
    h_triads = []
    while True:
        location = grid.find(NUMBER_AT, start)
        if location == NOT_FOUND:
            break
        h_triads.append(divmod((location + 1), size))
        start = location + 1
    return h_triads

def get_v_triads(grid, size):
    v_triads = []
    for row in range(size - 3):
        for col in range(size):
            if NUMBER_AT == grid[row * size + col] +  grid[row * size + size + col]  + grid[row * size + size + size + col]:
                v_triads.append((row + 1, col + 1))
    return v_triads

def assign_numbers(locations):
    number = 0
    numbers = {}
    for location in locations:
        if location not in numbers:
            number += 1
            numbers[location] = number
    return numbers

     
def insertWordHorizontal(grid, s, row, col, size):
    newstr = list(grid[row])
    for ch in s:
        newstr[col] = ch
        col += 1
    grid[row] = ''.join(newstr)
    return grid

def insertWordVertical(grid, s, row, col, size):
    for ch in s:
        newstr = list(grid[row])
        newstr[col] = ch
        grid[row] = ''.join(newstr)
        row += 1
    return grid

def insertIntoCrossword(grid, s, indexofWord, locationofWord, acrossorDown, size):
    if s != None:
        col = int(locationofWord[1])
        row = int(locationofWord[0])       
        if acrossorDown == 'a':
            grid = insertWordHorizontal(grid, s, row, col, size)
        else:
            grid = insertWordVertical(grid, s, row, col, size)
    return grid

def hor_fill ( i, j):
    while grid[i][j] != 'X' :
        s.append(grid[i][j])
        j += 1
        presence_of_characters(str(s))
        ver_fill(i,j)
        
def ver_fill( i, j):
    while grid[i][j] != 'X' :
        s.append(l[i][j])
        i += 1
        presence_of_characters(str(s))


#TESTS
def testInsertion(filename):
    grid = []
    for line in open(filename):
        gridfile, s, row, col, acrossorDown, resgridfile = line.split()
        for line in open(gridfile):
            grid.append(line.strip())
        size = len(grid)
        locationofWord = (row, col)
        grid = insertIntoCrossword(grid, s, 2, locationofWord, acrossorDown, size)
        i = 0
        for line in open(resgridfile):
            st = (line.strip("\n"))
            if str(st) == grid[i]:
                i += 1
            else:
                break
        if i == size:
            print("test passed for crossword" + gridfile)
        else:
            print("test failed for crossword" + gridfile)
        grid = []

import sys
size, gridstring,grid = loadGrid(sys.argv[1])
h_num_locations = get_h_triads(grid, size)
v_num_locations = get_v_triads(grid, size)
numbers = assign_numbers(h_num_locations + v_num_locations)
for loc in numbers.keys():
    li.append(loc) 
l = 0    
while l < len(li) :
    hor_fill(li[l][0], li[l][1])

testInsertion("files/testinsertionintocrossword")
