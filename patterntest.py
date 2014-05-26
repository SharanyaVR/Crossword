grid = [ "XXXXX","Xs tX","XX XX "]
i = 1
s = ""
j = 1
while grid[i][j] != 'X' :
    s = s + grid[i][j]
    j += 1
print(s)
