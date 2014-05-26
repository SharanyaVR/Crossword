pattern = [['X','X','X','X','X','X','X'],
           ['X',' ',' ',' ','X','X','X'],
           ['X','X','X',' ','X','X','X'],
           ['X','X','X',' ','X','X','X'],
           ['X','X','X',' ',' ',' ','X'],
           ['X','X','X','X','X','X','X'],
           ['X','X','X','X','X','X','X']]
def num(pattern):
    l = len(pattern[0])
    pr = [' ']
    for i in range(1,l):
        for j in range(1,l):
            if pattern[i][j] == ' ' and pattern[i][j-1] == 'X' and pattern[i][j+1] == ' ':
                pattern[i][j] = 'x'
            if pattern[i][j] == ' ' and pattern[i-1][j] == 'X' and pattern[i+1][j] == ' ':
                pattern[i][j] = 'x'
    ct = 1
    for i in range(0,l):
        for j in range(0,l):
            if pattern[i][j] == 'x' :
                pattern[i][j] = ct
                ct += 1
            else:
                pattern[i][j] = 0
            if pattern[i][j] !=0:
                pr = pr + [(i,j)]
    return pr
        
x = []
x = num(pattern)
print(x)
