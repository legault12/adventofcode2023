def find_mapped_value(source, mappings):
    for dest_start, src_start, length in mappings:
        if src_start <= source < src_start + length:
            offset = source - src_start
            return dest_start + offset
    return source

def parse_mapping_section_to_tuples(section):
    lines = section.split('\n')[1:]
    mappings = []
    for line in lines:
        if line.strip():
            mappings.append(tuple(map(int, line.split())))
    return mappings

with open('puzzle-input.txt', 'r') as file:
    puzzle_input = file.read()

sections = puzzle_input.split('\n\n')

seeds = list(map(int, sections[0].split(':')[1].strip().split()))

seed_to_soil_tuples = parse_mapping_section_to_tuples(sections[1])
soil_to_fertilizer_tuples = parse_mapping_section_to_tuples(sections[2])
fertilizer_to_water_tuples = parse_mapping_section_to_tuples(sections[3])
water_to_light_tuples = parse_mapping_section_to_tuples(sections[4])
light_to_temperature_tuples = parse_mapping_section_to_tuples(sections[5])
temperature_to_humidity_tuples = parse_mapping_section_to_tuples(sections[6])
humidity_to_location_tuples = parse_mapping_section_to_tuples(sections[7])

lowest_location = float('inf')
for seed in seeds:
    soil = find_mapped_value(seed, seed_to_soil_tuples)
    fertilizer = find_mapped_value(soil, soil_to_fertilizer_tuples)
    water = find_mapped_value(fertilizer, fertilizer_to_water_tuples)
    light = find_mapped_value(water, water_to_light_tuples)
    temperature = find_mapped_value(light, light_to_temperature_tuples)
    humidity = find_mapped_value(temperature, temperature_to_humidity_tuples)
    location = find_mapped_value(humidity, humidity_to_location_tuples)
    lowest_location = min(lowest_location, location)

print(lowest_location)
