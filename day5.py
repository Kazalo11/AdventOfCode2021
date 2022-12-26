grid = [[0 for _ in range(1000)] for _ in range(1000)]
with open('day5input.txt') as f:
    for line in f:
        line = line.strip()
        start,end = line.split('->')
        start = start.strip()
        end = end.strip()
        start = start.split(',')
        end = end.split(',')
        xstart,ystart = int(start[0]),int(start[1])
        xend,yend = int(end[0]),int(end[1])
        if xstart == xend:
            ymin = min(ystart,yend)
            diff = abs(ystart-yend)
            for i in range(diff+1):
                grid[ymin+i][xstart]+=1
        if ystart == yend:
            xmin = min(xstart,xend)
            diff = abs(xstart-xend)
            for i in range(diff+1):
                grid[ystart][xmin+i]+=1

        if xstart == ystart and xend == yend:
            minimum = min(xstart,xend)
            diff = abs(xend-xstart)
            for i in range(diff+1):
                grid[minimum+i][minimum+i]+=1
        elif abs(xstart - xend) == abs(ystart - yend):
            diff = abs(xstart-xend)
            if xstart < xend and ystart > yend:
                for i in range(diff+1):
                    grid[ystart-i][xstart+i]+=1
            elif xstart > xend and ystart < yend:
                for i in range(diff+1):
                    grid[ystart+i][xstart-i]+=1
            else:
                xmin = min(xstart,xend)
                ymin = min(ystart,yend)
                for i in range(diff+1):
                    grid[ymin+i][xmin+i]+=1


print(grid)

count = 0
for row in grid:
    for column in row:
        if column > 1:
            count+=1
print(count)
# elif abs(xstart - xend) == abs(ystart - yend):
# diff = abs(xend - xstart)
# if xstart > xend:
#     for i in range(diff + 1):
#         grid[ystart + i][xstart - i] += 1
# else:
#     for i in range(diff + 1):
#         grid[yend + i][xend - i] += 1