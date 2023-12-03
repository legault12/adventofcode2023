def sum_part_numbers(schematic):
    symbols = {'$', '*', '+', '-', '/', '@', '&', '#', '%', '='}
    grid = [list(line.strip()) for line in schematic]
    rows, cols = len(grid), len(grid[0])

    def is_adjacent_to_symbol(r, c, num_length):
        for i in range(num_length):
            for dr in range(-1, 2):
                for dc in range(-1, 2):
                    if dr == 0 and dc == 0:
                        continue
                    nr, nc = r + dr, c + i + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] in symbols:
                        return True
        return False

    def extract_numbers():
        for r in range(rows):
            c = 0
            while c < cols:
                if grid[r][c].isdigit():
                    num = ''
                    start_col = c
                    while c < cols and grid[r][c].isdigit():
                        num += grid[r][c]
                        c += 1
                    yield r, start_col, int(num), len(num)
                else:
                    c += 1

    sum_of_parts = 0
    for r, c, num, num_length in extract_numbers():
        if is_adjacent_to_symbol(r, c, num_length):
            sum_of_parts += num

    return sum_of_parts

with open('input.txt', 'r') as file:
    schematic = file.readlines()

sum_of_part_numbers = sum_part_numbers(schematic)
print("Sum of part numbers:", sum_of_part_numbers)
