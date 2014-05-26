def hor_fill ( i, j):
    while l[i][j] != 'X' :
        s.append(l[i][j])
        j += 1
    insert(s)
    ver_fill(i,j)

def ver_fill( i, j):
    while l[i][j] != 'X' :
        s.append(l[i][j])
        i += 1
    insert(s)

