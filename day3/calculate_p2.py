def calculate_gear_ratios(schematic):
    grid = [list(line.strip()) for line in schematic]
    rows, cols = len(grid), len(grid[0])

    def get_full_number(r, c):
        if not grid[r][c].isdigit():
            return None
        num = ''
        lc = c - 1
        while lc >= 0 and grid[r][lc].isdigit():
            num = grid[r][lc] + num
            lc -= 1
        rc = c
        while rc < cols and grid[r][rc].isdigit():
            num += grid[r][rc]
            rc += 1
        return int(num)

    def find_adjacent_part_numbers(r, c):
        part_numbers = set()
        for dr in range(-1, 2):
            for dc in range(-1, 2):
                if dr == 0 and dc == 0:
                    continue
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    part_num = get_full_number(nr, nc)
                    if part_num is not None:
                        part_numbers.add(part_num)
        return list(part_numbers)

    total_gear_ratio = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '*':
                adjacent_part_numbers = find_adjacent_part_numbers(r, c)
                if len(adjacent_part_numbers) == 2:
                    total_gear_ratio += adjacent_part_numbers[0] * adjacent_part_numbers[1]

    return total_gear_ratio

with open('input.txt', 'r') as file:
    schematic = file.readlines()

total_gear_ratio = calculate_gear_ratios(schematic)
print("Total gear ratio:", total_gear_ratio)
