"""Day 5 solution"""
import math
import functools

rules = []

for line in open('rules.txt'):
    line = line.strip()
    pair = line.split("|")
    rules.append(pair)

#print("rules:" + str(rules))

def mycmp(a, b):
    #print("comparing ", a, " and ", b)
    if [a,b] in rules:
        #print(" found in rules")
        return -1
    #print(" not found")
    return 0


RESULT_1 = 0
RESULT_2 = 0
for line in open('input.txt'):
    line = line.strip()
    page_numbers = line.split(",")
    count = len(page_numbers)
    half_index = math.floor(count / 2)
    ALLOWED = True
    for i, page_number in enumerate(page_numbers, 1):
        #print("checking:" + str(page_number))
        # need to compare number to all the subsequent numbers
        while i < count:
            for rule in rules:
                #print(" comparing:" + str(rule))
                if rule[0] == page_numbers[i] and rule[1] == page_number:
                    ALLOWED = False
                    break
            i += 1
    #print("line:" + line + " allowed:" + str(ALLOWED))
    if ALLOWED:
        RESULT_1 += int(page_numbers[half_index])
    else:
        sorted_page_numbers = sorted(page_numbers, key=functools.cmp_to_key(mycmp))
        #print(" sorted to:" + str(page_numbers))
        RESULT_2 += int(sorted_page_numbers[half_index])


print("Result 1:" + str(RESULT_1))
print("Result 2:" + str(RESULT_2))
