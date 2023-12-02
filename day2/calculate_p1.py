import re

def is_game_possible(game_line, red_cubes, green_cubes, blue_cubes):
    game_number = int(re.search(r'Game (\d+):', game_line).group(1))
    rounds = game_line.strip().split(':')[1].split(';')
    for round in rounds:
        cubes = re.findall(r'(\d+) (red|green|blue)', round)
        for cube_count, cube_color in cubes:
            if cube_color == 'red' and int(cube_count) > red_cubes:
                return False, game_number
            elif cube_color == 'green' and int(cube_count) > green_cubes:
                return False, game_number
            elif cube_color == 'blue' and int(cube_count) > blue_cubes:
                return False, game_number
    return True, game_number

file_path = 'input.txt'
with open(file_path, 'r') as file:
    data = file.readlines()

red_limit, green_limit, blue_limit = 12, 13, 14

possible_games = []
for line in data:
    possible, game_id = is_game_possible(line, red_limit, green_limit, blue_limit)
    if possible:
        possible_games.append(game_id)

sum_of_possible_game_ids = sum(possible_games)
print("Sum of possible game IDs:", sum_of_possible_game_ids)
print("Possible games:", possible_games)
