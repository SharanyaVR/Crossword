words ={}
def addToDict(test_line):
    for line in open("sowpods.txt"):
        line = line.strip()
        if line == test_line:
            return "valid"
        else:
            return "invalid"
        if len(line) not in words:
            words[len(line)] = []
        words[len(line)].append(line)
     #print(words)


for line in open("testdata.txt"):
    line = line.split()
    if addToDict(line[0]) == line[1]:
        print("True")
    else:
        print("False")


