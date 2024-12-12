# Day 1 solution
#

import pandas as pd

# header=None is needed because the data doesn't have headers
# without this, the first row is skipped
df = pd.read_csv('input.txt', sep=r'\s+', header=None)

first_list = []
second_list = []

for i, row in enumerate(df.itertuples(), 1):
    # print("i:" + str(i) + " row:" + str(row))
    first_list.append(row[1])
    second_list.append(row[2])

# only part 1 needs a sort, but doesn't hurt part 2
first_list.sort()
second_list.sort()

# part 1
sum = 0
for (first, second) in zip(first_list, second_list):
    abs_result = abs(first - second)
    # print("first:" + str(first) + " second:" + str(second) + " abs:" + str(abs_result))
    sum += abs_result


# part 2
similarity_score = 0
for first in first_list:
    for second in second_list:
        if first == second:
            # instead of counting the instances and multiplying, just add each time
            similarity_score += first


print("Part 1 sum:" + str(sum))
print("Part 2 similarity score:" + str(similarity_score))