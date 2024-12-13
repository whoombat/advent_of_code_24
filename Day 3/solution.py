"""Day 3 solution"""

import re

number_pattern = re.compile(r"\d{1,3}")
pattern_1 = re.compile(r"mul\(\d{1,3},\d{1,3}\)")
pattern_2 = re.compile(r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)")

TOTAL_1 = 0
TOTAL_2 = 0
ENABLED = True

for line in open('input.txt'):
    for match in re.finditer(pattern_1, line):
        # print('Found:'+ match.group())
        numbers = re.findall(number_pattern, match.group())
        # print ("1: Number 1:" + numbers[0] + " 2:" + numbers[1])
        TOTAL_1 += (int(numbers[0]) * int(numbers[1]))
    for match in re.finditer(pattern_2, line):
        print('Found:'+ match.group())
        MATCH_STR = match.group()
        if MATCH_STR == "do()":
            ENABLED = True
        elif MATCH_STR == "don't()":
            ENABLED = False
        elif ENABLED:
            numbers = re.findall(number_pattern, match.group())
            # print ("2: Number 1:" + numbers[0] + " 2:" + numbers[1])
            TOTAL_2 += (int(numbers[0]) * int(numbers[1]))

print('Part 1 result:' + str(TOTAL_1))
print('Part 2 result:' + str(TOTAL_2))
