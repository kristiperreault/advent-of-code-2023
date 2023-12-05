# part 1
sum = 0
digits = ""

with open("input1.txt", "r", encoding="UTF-8") as file:
    while line := file.readline():
        for c in line:
            if c.isdigit():
                digits = digits + c
        value = int(digits[0] + digits[-1])
        sum = sum + value
        digits = ""

# part 2
ans = 0
with open("input1.txt", "r", encoding="UTF-8") as file:
    while line := file.readline():
        digits = []
        for i, c in enumerate(line):
            if c.isdigit():
                digits.append(c)
            for d, val in enumerate(
                ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
            ):
                if line[i:].startswith(val):
                    digits.append(str(d + 1))
        ans += int(digits[0] + digits[-1])

print(ans)
