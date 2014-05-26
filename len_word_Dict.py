words ={}
for line in open("sowpods.txt"):
    line = line.strip()
    if len(line) not in words:
        words[len(line)] = []
    words[len(line)].append(line)
print(words)
  
