"""Day 6 solution"""

data = []

with open("input.txt") as myfile:
    for line in myfile:
        line = line.strip()
        line = list(line)
        tuples = []
        for entry in line:
            tuples.append([entry, False])        
        data.append(tuples)

current_point = []
direction = '^'
for i in range(len(data)):
    #  Columns
    for j in range(len(data[i])):
        #  If keyString is found
        if data[i][j][0] in ['^', '<', '>', 'v']:
            current_point.append(i)
            current_point.append(j)
            direction = data[i][j][0]
            break

#print(current_point)

#print(data[current_point[0]][current_point[1]])
#print(direction)

points_visited = 1
data[current_point[0]][current_point[1]][1] = True

while True:
    # need to traverse to next point, if valid increase points_visited, if invalid, set valid False
    if direction == '^':
        #go up
        current_point = [current_point[0]-1, current_point[1]]
        #print('up to:' + str(current_point))
        if current_point[0] < 0:
            #print(" invalid")
            break
        try:
            data[current_point[0]][current_point[1]]
        except (ValueError, IndexError):
            #print(" invalid")
            break
        else:
            #print(" vaild")
            #found
            #if value is false, then set to true and increment the points_visited
            if data[current_point[0]][current_point[1]][1] is False:
                data[current_point[0]][current_point[1]][1] = True
                points_visited += 1
                #print(" points_visited++")
            if current_point[0] > 0 and data[current_point[0]-1][current_point[1]][0] == '#':
                #turn
                #print(" turn to > right")
                direction = '>'
    elif direction == '>':
        #go right
        current_point = [current_point[0], current_point[1]+1]
        #print('right to:' + str(current_point))
        if current_point[1] > 129:
            #print(" invalid")
            break
        try:
            data[current_point[0]][current_point[1]]
        except (ValueError, IndexError):
            #print(" invalid")
            break
        else:
            #print(" vaild")
            #found
            #if value is false, then set to true and increment the points_visited
            if data[current_point[0]][current_point[1]][1] is False:
                data[current_point[0]][current_point[1]][1] = True
                points_visited += 1
                #print(" points_visited++")
            if current_point[1] < 129 and data[current_point[0]][current_point[1]+1][0] == '#':
                #turn
                direction = 'v'
                #print(" turn to v down")
    elif direction == 'v':
        #go down
        current_point = [current_point[0]+1, current_point[1]]
        #print('down to:' + str(current_point))
        if current_point[0] > 129:
            #print(" invalid")
            break
        try:
            data[current_point[0]][current_point[1]]
        except (ValueError, IndexError):
            #print(" invalid")
            break
        else:
            #print(" vaild")
            #found
            #if value is false, then set to true and increment the points_visited
            if data[current_point[0]][current_point[1]][1] is False:
                data[current_point[0]][current_point[1]][1] = True
                points_visited += 1
                #print(" points_visited++")
            if current_point[0] < 129 and data[current_point[0]+1][current_point[1]][0] == '#':
                #turn
                direction = '<'
                #print(" turn to < left")
    else: # direction == '<':
        #go left
        current_point = [current_point[0], current_point[1]-1]
        #print('left to:' + str(current_point))
        if current_point[1] < 0:
            #print(" invalid")
            break
        try:
            data[current_point[0]][current_point[1]]
        except (ValueError, IndexError):
            #print(" invalid")
            break
        else:
            #print(" vaild")
            #found
            #if value is false, then set to true and increment the points_visited
            if data[current_point[0]][current_point[1]][1] is False:
                data[current_point[0]][current_point[1]][1] = True
                points_visited += 1
                #print(" points_visited++")
            if current_point[1] > 0 and data[current_point[0]][current_point[1]-1][0] == '#':
                #turn
                direction = '^'
                #print(" turn to ^ up")

print(points_visited)

#print(data)
