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

def insertIntoCrossword(grid, s, locationofWord, acrossorDown, size):
    if s != None:
        col = int(locationofWord[1])
        row = int(locationofWord[0])       
        if acrossorDown == 'a':
            grid = insertWordHorizontal(grid, s, row, col, size)
        else:
            grid = insertWordVertical(grid, s, row, col, size)
    return grid


def patternmatch_empty(string, length, words):
    l1 = words[length]
    for i in l1:
        string = i
        
    return string

def patternmatch_nonempty(string, length, words):
    k = 0
    a = {}
    for i in range(0,length):
        if string[i] == " ":
            i += 1
        else:
            a[i] = string[i]
    return insertM(string, words, a, length)

def presence_of_characters(length,string, words):
    k = 0
    h ={}
    print(length)
    for j in range(0,length):
        if string[j] !=" ":
            k += 1
    if k == 0:
        string = patternmatch_empty(string,length,words)
    else:
        string = patternmatch_nonempty(string,length,words)
    return string

def insertM(string, words, a, length):
    print(length)
    for i in words[length]:
        for j in a:
            if a[j] == i[j]:
                string = i
    return string

def addToDict(filename):
    for line in open(filename):
        line = line.strip()
        if len(line) not in words:
            words[len(line)] = []
        words[len(line)].append(line)
    return words
   
def hor_fill ( i, j,grid, words):
    tup = (i,j)
    s = []
    while grid[i][j] != 'X' :
        s.append(grid[i][j])
        j += 1
        print(len(str(s)))
        st = presence_of_characters(len(str(s)), str(s), words)
        grid = insertIntoCrossword(grid, st, tup, 'a', len(grid)) 
        grid = ver_fill(i,j,grid,words)
    return grid
        
def ver_fill( i, j,grid, words):
    tup = (i, j)
    s = []
    while grid[i][j] != 'X' :
        s.append(l[i][j])
        i += 1
        st = presence_of_characters(len(s), str(s), words)
        grid = insertIntoCrossword(grid, st, tup, 'd', len(grid))
        return grid


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
h_num_locations = get_h_triads(gridstring, size)
v_num_locations = get_v_triads(gridstring, size)
numbers = assign_numbers(h_num_locations + v_num_locations)
li = []
for loc in numbers.keys():
    li.append(loc) 
print(li)
l = 0 
words = {}
words = addToDict("files/sowpods.txt")
while l < len(li) :
    grid = hor_fill(li[l][0], li[l][1],grid, words)
for row in grid:
    print(row)
#testInsertion("files/testinsertionintocrossword")
