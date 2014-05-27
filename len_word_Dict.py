def addToDict(wordfile, words):
    for line in open(wordfile):
        line = line.strip()
        if len(line) not in words:
            words[len(line)] = []
        words[len(line)].append(line)
    return words

def test_func(testfile):
    for test_line in open(testfile):
        sampdict, exp_output= test_line.split('!')
        words = {}
        words = addToDict(sampdict, words)
        #print(words)
        #print(exp_output)
        if str(words) in exp_output:
            print("test suceeded for " + sampdict)
        else:
            print("test failed for " + sampdict)

test_func("testdict")
#words = {}
#addToDict("sowpods.txt", words)

