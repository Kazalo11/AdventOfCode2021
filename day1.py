count = 0
curr = 0
i = 0
values = []
with open('day1input.txt') as f:
    for line in f:
        line = line.strip()
        if i == 0:
            curr = int(line)
            i+=1
        else:
            if int(line) > curr:
                count+=1
            curr = int(line)
        values.append(int(line))

count2 = 0

for j in range(len(values)-2):
    if j == 0:
        curr = values[j]+values[j+1]+values[j+2]
    else:
        if values[j]+values[j+1]+values[j+2] > curr:
            count2+=1
        curr = values[j]+values[j+1]+values[j+2]
print(count2)
