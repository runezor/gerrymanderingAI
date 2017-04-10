import random
N = 40 #height
M = 40 #width

lines = []

for i in range(N):
    lines.append("")
    for j in range(M):
        x = round(random.random()-0.05)
        lines[i] += str(x) #-0.05 makes 0 more likely than 1

for line in lines:
    print(line)
