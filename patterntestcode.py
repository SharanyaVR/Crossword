l = []
s = ""
l1 = []
line = ""
for line in open('crossworddata.txt'):
    l.append(line)   
row = int(input())
col = int(input())
c = col
while l[row][col] != 'X':
    s = s + l[row][col]
    col += 1
for i in open('patterndata.txt'):
    st = i.strip("\n")
    l1.append(st.split(","))
k = 0

while int(l1[k][0]) != row and int(l1[k][1]) != col :
    k += 1
if s == l1[k][2]:
    print("string returned" + " " + s)
    print("test passed for" + str(row) +"  " + str(c))
else:
    print("test failed for" + str(row) + " " + str(c))
