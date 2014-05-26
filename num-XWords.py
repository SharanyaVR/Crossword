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

#def backtrackLastInsertion(indexofLastWordInserted):
#    location = getLocationofWordIndex(indexofLastWordInserted)
     
def insertWordHorizontal(grid, s, row, col, size):
    newstr = list(grid[row])
    for ch in s:
        newstr[col] = ch
        col += 1
    print(newstr)
    grid[row] = ''.join(newstr)
    print(grid)
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
        print(s)
        col = locationofWord[1]    
        row = locationofWord[0]       
        if acrossorDown == 'a':
            grid = insertWordHorizontal(grid, s, row, col, size)
            print("if")
        else:
            print("else")
            grid = insertWordVertical(grid, s, locationofWord, size)
    return grid


import sys
size, gridstring, grid  = loadGrid(sys.argv[1])
h_num_locations = get_h_triads(gridstring, size)
v_num_locations = get_v_triads(gridstring, size)
numbers = assign_numbers(h_num_locations + v_num_locations)
for loc in numbers.keys():
    print(loc, numbers[loc])
grid = insertIntoCrossword(grid, "abc", 2, (2,1), 'a',size)
print(grid)


 
