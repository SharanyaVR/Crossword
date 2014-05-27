words ={}
def addToDict(filename):
    for line in open(filename):
        line = line.strip()
        if len(line) not in words:
            words[len(line)] = []
        words[len(line)].append(line)
    return words

def test_func(filename):
    for test_line in open(filename):
        sampdict, exp_output= test_line.split('!')
        words = addToDict(sampdict)
        print(words)
        print(exp_output)
        if str(words) != exp_output:
            print("test suceeded for " + sampdict)
        else:
            print("test failed for " + sampdict)

test_func("testdict")


