def parse_line(line):
    return [int(x) for x in line.split()]

def process_ranges(ranges, number):
    for start, source, length in ranges:
        if source <= number < source + length:
            return start + number - source
    return number  # Default case: no change

def process_through_maps(number, maps):
    for mapping in maps:
        number = process_ranges(mapping, number)
    return number

def find_lowest_location(seeds, mappings):
    lowest_location = float('inf')
    for start, length in seeds:
        print(f"Processing seed range: {start} to {start + length - 1}")
        for i in range(length):
            seed_number = start + i
            location_number = process_through_maps(seed_number, mappings)
            lowest_location = min(lowest_location, location_number)
            if i % 1000 == 0:  # Update every 1000 iterations
                print(f"  - Processing seed number: {seed_number}")
    return lowest_location

# Read the almanac data
with open('puzzle-input.txt', 'r') as file:
    lines = file.readlines()

# Parse the seeds
seed_line = lines[0].strip().split(':')[1].strip()
seeds = [(int(x.split()[0]), int(x.split()[1])) for x in seed_line.split(', ')]

# Parse the mappings
mappings = []
current_map = []
for line in lines[2:]:  # Start reading from the line after the seeds
    if 'map:' in line:
        if current_map:
            mappings.append(current_map)
            current_map = []
    else:
        parsed_line = parse_line(line)
        if parsed_line:  # Only add non-empty lines
            current_map.append(parsed_line)

if current_map:  # Add the last map
    mappings.append(current_map)

# Find the lowest location
lowest_location = find_lowest_location(seeds, mappings)
print("Lowest location number:", lowest_location)
