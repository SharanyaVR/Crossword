l = []
l1 = []
line = ""
for line in open('crossworddata.txt'):
    l.append(line)   
for i in open('patterndata.txt'):
    s = ""
    st = i.strip("\n")
    l1 = st.split(",")
    row = int(l1[0])
    col = int(l1[1])
    c = col
    while l[row][col] != 'X':
        s = s + l[row][col]
        col += 1

    if s == l1[2]:
        print("string returned" + " " + s)
        print("test passed for" + " " + str(row) +"  " + str(c))
    else:
        print("test failed for" + " " + str(row) + " " + str(c))
