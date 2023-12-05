import re

# part 1
red = 12
green = 13
blue = 14
sum = 0
game_count = 0
red_high = 0
green_high = 0
blue_high = 0

with open("input2.txt", "r", encoding="UTF-8") as file:
    while line := file.readline():
        game_count += 1
        for i in re.finditer("red", line):
            index = int(i.start())
            red_game_str = line[index - 3 : index]
            red_game = int(red_game_str)
            if red_game > red_high:
                red_high = red_game
        for i in re.finditer("green", line):
            index = int(i.start())
            green_game_str = line[index - 3 : index]
            green_game = int(green_game_str)
            if green_game > green_high:
                green_high = green_game
        for i in re.finditer("blue", line):
            index = int(i.start())
            blue_game_str = line[index - 3 : index]
            blue_game = int(blue_game_str)
            if blue_game > blue_high:
                blue_high = blue_game
        if red_high <= red and blue_high <= blue and green_high <= green:
            sum += game_count
        red_high = 0
        green_high = 0
        blue_high = 0
    print(sum)


# part 2
sum = 0
game_count = 0
red_high = 0
green_high = 0
blue_high = 0

with open("input2.txt", "r", encoding="UTF-8") as file:
    while line := file.readline():
        for i in re.finditer("red", line):
            index = int(i.start())
            red_game_str = line[index - 3 : index]
            red_game = int(red_game_str)
            if red_game > red_high:
                red_high = red_game
        for i in re.finditer("green", line):
            index = int(i.start())
            green_game_str = line[index - 3 : index]
            green_game = int(green_game_str)
            if green_game > green_high:
                green_high = green_game
        for i in re.finditer("blue", line):
            index = int(i.start())
            blue_game_str = line[index - 3 : index]
            blue_game = int(blue_game_str)
            if blue_game > blue_high:
                blue_high = blue_game
        power = red_high * green_high * blue_high
        sum += power
        red_high = 0
        green_high = 0
        blue_high = 0
    print(sum)
