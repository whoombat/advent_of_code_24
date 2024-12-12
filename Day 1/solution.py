# Day 1 solution
#

import pandas as pd

df = pd.read_csv('input.txt', sep=r'\s+', header=None)


sum = 0
similarity_score = 0

first_array = []
second_array = []

for i, row in enumerate(df.itertuples(), 1):
    #print("i:" + str(i) + " row:" + str(row))
    first_array.append(row[1])
    second_array.append(row[2])

first_array.sort()
second_array.sort()

for (first, second) in zip(first_array, second_array):
    abs_result = abs(first - second)
    #print("first:" + str(first) + " second:" + str(second) + " abs:" + str(abs_result))
    sum += abs_result

for first in first_array:
    for second in second_array:
        if first == second:
            similarity_score += first

print("Part 1 sum:" + str(sum))
print("Part 2 similarity score:" + str(similarity_score))