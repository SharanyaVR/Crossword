def addToDict(filename, words):
    for line in open(filename):
        line = line.strip()
        if len(line) not in words:
            words[len(line)] = []
        words[len(line)].append(line)
    return words

def test_func(filename):
    for test_line in open(filename):
        sampdict, exp_output= test_line.split('!')
        words = {}
        words = addToDict(sampdict,words)
        print(words)
        exp_output = exp_output.strip("\n")
        if str(words) == exp_output:
            print("test suceeded for " + sampdict)
        else:
            print("test failed for " + sampdict)

test_func("testdict")


