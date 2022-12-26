pos = [0,0]
aim = 0
with open('day2input.txt') as f:
    for line in f:
         line = line.strip()
         line = line.split(" ")
         if line[0] == 'forward':
             pos[0]+= int(line[1])
             pos[1]+= int(line[1])*aim
         elif line[0] == 'down':
             aim+=int(line[1])
         elif line[0] == 'up':
             aim-=int(line[1])

print(pos[0]*pos[1])