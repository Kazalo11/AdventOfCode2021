count = 0
frequency = {}
t1 = ""
t2 = ""
values = []
p1 = []
p2 = []

with open('day3input.txt') as f:
    for line in f:
        line = line.strip()
        values.append(line)
        line = [int(i) for i in line]
        for j in range(len(line)):
            if line[j] == 1:
                frequency[j] = frequency.get(j, 0) + 1
        count += 1

for i in range(len(frequency.values())):
    if frequency[i] >= count // 2:
        t1 += '1'
        t2 += '0'
    else:
        t1 += '0'
        t2 += '1'

print(int(t1, 2) * int(t2, 2))

values2 = values.copy()

index = 0
while len(values) != 1:
    count = 0
    for value in values:
        if value[index] == '1':
            count+=1
    if count >= len(values)/2:
        values = [i for i in values if i[index] == '1']
    else:
        values = [i for i in values if i[index] == '0']
    index+=1

index = 0
while len(values2) != 1:
    count = 0
    for value in values2:
        if value[index] == '1':
            count+=1
    if count >= len(values2)/2:
        values2 = [i for i in values2 if i[index] == '0']
    else:
        values2 = [i for i in values2 if i[index] == '1']
    index+=1

print(int(values[0],2)*int(values2[0],2))

