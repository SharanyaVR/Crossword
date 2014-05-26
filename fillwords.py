def hor_fill ( i, j):
    while grid[i][j] != 'X' :
        s.append(grid[i][j])
        j += 1
    presence_of_characters(s)
    ver_fill(i,j)

def ver_fill( i, j):
    while grid[i][j] != 'X' :
        s.append(l[i][j])
        i += 1
    presence_of_characters(s)



