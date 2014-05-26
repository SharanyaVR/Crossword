words ={}
def addToDict():
    for line in open("sowpods.txt"):
        line = line.strip()
        if len(line) not in words:
            words[len(line)] = []
        words[len(line)].append(line)
    return words

def test_func(filename):
    words = addToDict()
    s = ""
    for test_line in open(filename):
        word, length, exp_output= test_line.split()
        #print(word)
        if word.upper() in words[int(length)]:
            s = "True"
        else:
            s = "False"
        if s == exp_output:
            print("test suceeded for " + word)
        else:
            print("test failed for " + word)

test_func("testdata.txt")


