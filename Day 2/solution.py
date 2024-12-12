"""Day 2 solution"""

import pandas as pd

# header=None is needed because the data doesn't have headers
# without this, the first row is skipped
df = pd.read_csv('input.txt', sep=r'\s+', header=None, names=range(8))

# each report is safe if all increasing/decreasing and adjacent levels differ by 1-3
SAFE_COUNT_1 = 0

# part 2 allows one level to be ignored
SAFE_COUNT_2 = 0

for i, row in enumerate(df.itertuples(index=False)):
    #print("i:" + str(i) + " row:" + str(row))
    if row.count == 1:
        SAFE_COUNT_1+=1
        continue
    # we have 2 entries
    increasing = row[0] < row[1]
    LAST_VALUE = 0
    IS_SAFE = True
    for i, level in enumerate(row):
        if i != 0:
            #fail if not following increasing or the same or greater than 3
            if (increasing and level <= LAST_VALUE) or \
                (not increasing and level >= LAST_VALUE) or \
                    (abs(level - LAST_VALUE) > 3):
                IS_SAFE = False
        LAST_VALUE = level
    if IS_SAFE:
        SAFE_COUNT_1+=1


    # part 2
    for j in range(len(row)):
        # j represents what we'll ignore in each pass
        FIRST = True
        IS_SAFE = True
        for i, level in enumerate(row):
            if i == j:
                if i == 0:
                    LAST_VALUE = level
                    increasing = row[1] < row[2]
                elif i == 1:
                    increasing = row[0] < row[2]
                continue
            #print(" i:"+str(i) + " level:"+str(level) + " LAST_VALUE:" + str(LAST_VALUE) + " IS_SAFE:" + str(IS_SAFE))
            #fail if not following increasing or the same or greater than 3
            if FIRST:
                FIRST = False
            elif (increasing and level <= LAST_VALUE) or \
                (not increasing and level >= LAST_VALUE) or \
                    (abs(level - LAST_VALUE) > 3):
                IS_SAFE = False
            LAST_VALUE = level

        if IS_SAFE:
            SAFE_COUNT_2+=1
            break
        #print("bad row:" + str(row))


print("Part 1 result:" + str(SAFE_COUNT_1))
print("Part 2 result:" + str(SAFE_COUNT_2))
