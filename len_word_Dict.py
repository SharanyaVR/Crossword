words ={}
LineNum = 0
#test_data = ["", "123"," @#"]

#test_data = ["", "123"," @#"]
def test_case(line):
    test_data = ["", "123"," @#"]
    if line not in test_data:
        return "valid"
    else:
        return "invalid"


for line in open("sowpods.txt"):
    line = line.strip()
    if test_case(line) == "invalid":
        print("invalid")
        print(line)
        break
    if len(line) not in words:
        words[len(line)] = []
    words[len(line)].append(line)
print(words)

