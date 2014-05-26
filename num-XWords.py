NOT_FOUND = -1
NUMBER_AT = "X  "
def loadGrid(gridfile):
    grid = []
    for line in open(gridfile):
        grid.append(line.strip())
    return len(grid), ''.join(grid)

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

import sys
size, grid = loadGrid(sys.argv[1])
h_num_locations = get_h_triads(grid, size)
v_num_locations = get_v_triads(grid, size)
numbers = assign_numbers(h_num_locations + v_num_locations)
for loc in numbers.keys():
    li.append(loc) 
l = 0    
while l < len(li) :
    hor_fill(li[l][0], li[l][1])
