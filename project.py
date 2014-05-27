def patternmatch(string, length, words):
    l1 = words[length]
    for i in l1:
        string = i
    return string

def patternmatch2(string, length, words):
    k = 0
    a = {}
    for i in range(0,len(string)):
        if string[i] == " ":
            i += 1
        else:
            a[i] = string[i]
    return insertM(string, words, a, length)

def presence_of_characters(length,string):
    k = 0
    h ={}
    for j in range(0,len(string)):
        if string[j] !=" ":
            k += 1
    if k == 0:
        string = patternmatch(string,length,words)
    else:
        string = patternmatch2(string,length,words)
    return string

def insertM(string, words, a, length):
    for i in words[length]:
        for j in a:
            if a[j] == i[j]:
                string = i
    return string

#string = "h p  "
#length = len(string)
#Test Data
#words = {2: ['hi', 'to', 'as'], 3: ['how', 'are', 'you', 'for', 'the'], 4: ['find', 'hear', 'from', 'hare'], 5: ['happy', 'could', 'cloud'], 7: ['concern'], 8: ['thankyou']}

words ={}
def addToDict(filename):
    for line in open(filename):
        line = line.strip()
        if len(line) not in words:
            words[len(line)] = []
        words[len(line)].append(line)
    return words
   
def test_func(filename):
    words = addToDict("files/sampledict.txt")
    #s = ""
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

length = 0
s = ""
for i in open("input.txt"):
    i = i.strip("\n")
    inp = i.split('!')
    length = len(inp[0])
    print(inp)
    print(inp[1])
    resstr = presence_of_characters(length,inp)
    print(resstr[1])
    if resstr[1] == inp[1]:
        print("Test passed for input " + inp[1])
    else:
        print("Test failed for input " + inp[1])
    

