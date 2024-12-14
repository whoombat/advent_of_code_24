"""Day 4 solution"""

# This function searches for the given word
# in all 8 directions from the coordinate.
def search2D_1(grid, row, col, word):
    m = len(grid)
    n = len(grid[0])

    # return if the given coordinate
    # does not match with first index char.
    if grid[row][col] != word[0]:
        return 0

    lenWord = len(word)

    count = 0

    # x and y are used to set the direction in which
    # word needs to be searched.
    x = [-1, -1, -1, 0, 0, 1, 1, 1]
    y = [-1, 0, 1, -1, 1, -1, 0, 1]

    # This loop will search in all the 8 directions
    # one by one. It will return true if one of the
    # directions contain the word.
    for dir in range(8):

        # Initialize starting point for current direction
        currX, currY = row + x[dir], col + y[dir]
        k = 1

        while k < lenWord:

            # break if out of bounds
            if currX >= m or currX < 0 or currY >= n or currY < 0:
                break

            # break if characters dont match
            if grid[currX][currY] != word[k]:
                break

            # Moving in particular direction
            currX += x[dir]
            currY += y[dir]
            k += 1

        # If all character matched, then value of must
        # be equal to length of word
        if k == lenWord:
            count+= 1

    return count

def search2D_2(grid, row, col, word):
    m = len(grid)
    n = len(grid[0])

    # return false if the given coordinate
    # does not match with 2nd index char.
    if grid[row][col] != word[1]:
        return False

    lenWord = len(word)

    count = 0

    #print("A at:" + str(row) + str(col))
    # x and y are used to set the direction in which
    # word needs to be searched.
    x = [-1, -1, 1, 1]
    y = [-1, 1, -1, 1]

    for dir in range(4):

        # Initialize starting point for current direction
        currX, currY = row + (-1 * x[dir]), col + (-1 * y[dir])
        #print(" checking from point:" + str(currX) + str(currY))
        k = 0

        while k < lenWord:

            # break if out of bounds
            if currX >= m or currX < 0 or currY >= n or currY < 0:
                #print("  out of bounds")
                break

            # break if characters dont match
            if grid[currX][currY] != word[k]:
                #print("  grid letter:" + grid[currX][currY] + " doesn't match:" + word[k])
                break
            #print("  grid letter:" + grid[currX][currY] + " does match")

            # Moving in particular direction
            currX += x[dir]
            currY += y[dir]
            #print("  now checking:" + str(currX) + str(currY))
            k += 1

        # If all character matched, then value of must
        # be equal to length of word
        if k == lenWord:
            #print("  match")
            count+= 1
        # else:
        #     print("  no match")

    return count


def searchWord(grid, word):
    m = len(grid)
    n = len(grid[0])

    ans = []

    for i in range(m):
        for j in range(n):

            count_part1 = search2D_1(grid, i, j, word)
            count_part2 = search2D_2(grid, i, j, "MAS")
            ans.append((i, j, count_part1, count_part2))

    return ans


def printResult(ans):
    total_1 = 0
    total_2 = 0
    for coord in ans:
        #print(f"{{{coord[0]},{coord[1]},{coord[2]},{coord[3]}}}", end="\n")
        total_1+=coord[2]
        if coord[3] == 2:
            total_2+=1
    print("part 1:" + str(total_1))
    print("part 2:" + str(total_2))


if __name__ == "__main__":
    grid = []
    with open("input.txt", "r") as file:
        for line in file:
            line = line.strip()
            row = list(line)
            grid.append(row)
    WORD = "XMAS"

    ans = searchWord(grid, WORD)

    printResult(ans)
