i = 1
s = ""
l = []
f =  open("test.txt")
st = f.readline()
l = st.split(",")
while l[0][i] != 'X':
    s = s + l[0][i]
    i += 1 
expected = l[1].strip('\n')    
print(s)
print(expected)
if str(s) == str(expected):
    print("passed")
else:
    print("failed")
