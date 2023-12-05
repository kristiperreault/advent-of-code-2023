import re

grid = []
sum = 0

with open("input3.txt", "r", encoding="UTF-8") as file:
    while line := file.readline():
        grid.append([line])


# find number
for i in re.finditer("([0-9]|[1-9][0-9]|[1-9][0-9][0-9])", grid):
# if num 1 digit, 2 digit, 3 digit...
    if len(i) == 1:

    if len(i) == 2:

    if len(i) == 3:
# check number surrounded by '.' or does not exist
# if number near symbol, add to sum
sum += num
