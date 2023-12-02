import re

def find_minimum_cubes(game_line):
    rounds = game_line.strip().split(':')[1].split(';')
    min_red, min_green, min_blue = 0, 0, 0
    for round in rounds:
        cubes = re.findall(r'(\d+) (red|green|blue)', round)
        red, green, blue = 0, 0, 0
        for cube_count, cube_color in cubes:
            if cube_color == 'red':
                red = max(red, int(cube_count))
            elif cube_color == 'green':
                green = max(green, int(cube_count))
            elif cube_color == 'blue':
                blue = max(blue, int(cube_count))
        min_red = max(min_red, red)
        min_green = max(min_green, green)
        min_blue = max(min_blue, blue)
    return min_red, min_green, min_blue

file_path = 'input.txt'
with open(file_path, 'r') as file:
    data = file.readlines()

powers = []
for line in data:
    min_red, min_green, min_blue = find_minimum_cubes(line)
    power = min_red * min_green * min_blue
    powers.append(power)

sum_of_powers = sum(powers)
print("Sum of powers:", sum_of_powers)
