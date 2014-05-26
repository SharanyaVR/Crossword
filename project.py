def patternmatch(string, length, words):
    l1 = words[length]
    for i in l1:
        string = i
    print(string)

def patternmatch2(string, length, words):
    k = 0
    a = {}
    for i in range(0,len(string)):
        if string[i] == " ":
            i += 1
        else:
            a[i] = string[i]
    print(a)
    insertM(string, words, a, length)

def presence_of_characters(string):
    k = 0
    h ={}
    for j in range(0,len(string)):
        if string[j] !=" ":
            k += 1
    print(k)
    if k == 0:
        patternmatch(string,length,words)
    else:
        patternmatch2(string,length,words)

def insertM(string, words, a, length):
    for i in words[length]:
        for j in a:
            if a[j] == i[j]:
                string = i
                print(string)


string = " ou  "
length = len(string)
words = {2: ['hi', 'to'], 3: ['how', 'are', 'you', 'for', 'the', 'you'], 4: ['find', 'hear', 'from', 'hare'], 5: ['happy', 'could', 'cloud'], 7: ['concern'], 8: ['thankyou']}

presence_of_characters(string)
