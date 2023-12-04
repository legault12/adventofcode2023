def parse_scratchcards(data):
    scratchcards = []

    for line in data:
        parts = line.strip().split('|')
        winning_numbers = list(map(int, parts[0].split(':')[1].split()))
        your_numbers = list(map(int, parts[1].split()))
        scratchcards.append({"winning_numbers": winning_numbers, "your_numbers": your_numbers})

    return scratchcards

def calculate_points(scratchcards):
    total_points = 0

    for card in scratchcards:
        matches = set(card["winning_numbers"]) & set(card["your_numbers"])
        if matches:
            points = 1 << (len(matches) - 1)
            total_points += points

    return total_points

file_path = 'input.txt'
with open(file_path, 'r') as file:
    scratchcard_data = file.readlines()

parsed_scratchcards = parse_scratchcards(scratchcard_data)
total_points = calculate_points(parsed_scratchcards)
print(f"Total points: {total_points}")
